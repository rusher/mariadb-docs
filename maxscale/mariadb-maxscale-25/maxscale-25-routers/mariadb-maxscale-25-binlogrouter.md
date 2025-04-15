
# Binlogrouter

# Binlogrouter


**NOTE:** The binlog router delivered with 2.5 is completely new and is **not**
 100% backward compatible with the binlog router delivered with earlier
 versions of MaxScale.


The binlogrouter is a router that acts as a replication proxy for MariaDB
master-slave replication. The router connects to a master, retrieves the binary
logs and stores them locally. Slave servers can connect to MaxScale like they
would connect to a normal master server. If the master server goes down,
replication between MaxScale and the slaves can still continue up to the latest
point to which the binlogrouter replicated to. The master can be changed without
disconnecting the slaves and without them noticing that the master server has
changed. This allows for a more highly available replication setup.


In addition to the high availability benefits, the binlogrouter creates only one
connection to the master whereas with normal replication each individual slave
will create a separate connection. This reduces the amount of work the master
database has to do which can be significant if there are a large number of
replicating slaves.




* [Binlogrouter](#binlogrouter)

  * [Differences Between Old and New Binlogrouter Implementations](#differences-between-old-and-new-binlogrouter-implementations)
  * [Supported SQL Commands](#supported-sql-commands)
  * [Configuration Parameters](#configuration-parameters)

    * [datadir](#datadir)
    * [server_id](#server_id)
    * [net_timeout](#net_timeout)
    * [select_master](#select_master)
    * [expire_log_duration](#expire_log_duration)
    * [expire_log_minimum_files](#expire_log_minimum_files)
  * [New installation](#new-installation)
  * [Upgrading to version 2.5](#upgrading-to-version-25)

    * [Before you start](#before-you-start)
    * [Deployment](#deployment)
  * [Galera cluster](#galera-cluster)
  * [Example](#example)
  * [Limitations](#limitations)




## Differences Between Old and New Binlogrouter Implementations


The binlogrouter in MaxScale 2.5.0 is a new and improved version of the original
binlogrouter found in older MaxScale versions. The new implementation contains
most of the features that were in the original binlogrouter but some of them
were removed as they were either redundant or not useful.


The major differences between the new and old binlog router are:


* The list of servers where the database users for authentication are loaded
 must be explicitly configured with the `<code>cluster</code>`, `<code>servers</code>` or
 `<code>targets</code>` parameter.
* The old binlog router had both `<code>server_id</code>` and `<code>master_id</code>`, the new only
 `<code>server_id</code>`.
* No need to configure heartbeat and burst interval anymore as they are
 now automatically configured.
* Traditional replication that uses the binary log name and file offset to
 start the replication process is not supported.
* Semi-sync support is not implemented.
* Binlog encryption is not implemented.
* Secondary masters are not supported, but the functionality provided by
 `<code>select_master</code>` is roughly equivalent.
* The new binlogrouter will write its own binlog files to prevent problems that
 could happen when the master changes. This causes the binlog names to be
 different in the binlogrouter when compared to the ones on the master.


The documentation for the binlogrouter in MaxScale 2.4 is provided for reference
[here](mariadb-maxscale-25-binlogrouter-24.md).


## Supported SQL Commands


The binlogrouter supports a subset of the SQL constructs that the MariaDB server
supports. The following commands are supported:


* `<code>CHANGE MASTER TO</code>`
* The binlogrouter supports the same syntax as the MariaDB server but only the
 following values are allowed:


  * `<code>MASTER_HOST</code>`
  * `<code>MASTER_PORT</code>`
  * `<code>MASTER_USER</code>`
  * `<code>MASTER_PASSWORD</code>`
  * `<code>MASTER_USE_GTID</code>`
  * `<code>MASTER_SSL</code>`
  * `<code>MASTER_SSL_CA</code>`
  * `<code>MASTER_SSL_CAPATH</code>`
  * `<code>MASTER_SSL_CERT</code>`
  * `<code>MASTER_SSL_CRL</code>`
  * `<code>MASTER_SSL_CRLPATH</code>`
  * `<code>MASTER_SSL_KEY</code>`
  * `<code>MASTER_SSL_CIPHER</code>`
  * `<code>MASTER_SSL_VERIFY_SERVER_CERT</code>`

NOTE: `<code>MASTER_LOG_FILE</code>` and `<code>MASTER_LOG_POS</code>` are not supported
 as binlogrouter only supports GTID based replication.
* `<code>STOP SLAVE</code>`
* Stops replication, same as MariaDB.
* `<code>START SLAVE</code>`
* Starts replication, same as MariaDB.
* `<code>RESET SLAVE</code>`
* Resets replication. Note that the `<code>RESET SLAVE ALL</code>` form that is supported
 by MariaDB isn't supported by the binlogrouter.
* `<code>SHOW BINARY LOGS</code>`
* Lists the current files and their sizes. These will be different from the
 ones listed by the original master where the binlogrouter is replicating
 from.
* `<code>PURGE { BINARY | MASTER } LOGS TO <filename></code>`
* Purges binary logs up to but not including the given file. The file name
 must be one of the names shown in `<code>SHOW BINARY LOGS</code>`. The version of this
 command which accepts a timestamp is not currently supported.
 Automatic purging is supported using the configuration
 parameter [expire_log_duration](#expire_log_duration).
The files are purged in the order they were created. If a file to be purged
 is detected to be in use, the purge stops. This means that the purge will
 stop at the oldest file that a slave is still reading.
NOTE: You should still take precaution not to purge files that a potential
 slave will need in the future. MaxScale can only detect that a file is
 in active use when a slave is connected, and requesting events from it.
* `<code>SHOW MASTER STATUS</code>`
* Shows the name and position of the file to which the binlogrouter will write
 the next replicated data. The name and position do not correspond to the
 name and position in the master.
* `<code>SHOW SLAVE STATUS</code>`
* Shows the slave status information similar to what a normal MariaDB slave
 server shows. Some of the values are replaced with constants values that
 never change. The following values are not constant:


  * `<code>Slave_IO_State</code>`: Set to `<code>Waiting for master to send event</code>` when
 replication is ongoing.
  * `<code>Master_Host</code>`: Address of the current master.
  * `<code>Master_User</code>`: The user used to replicate.
  * `<code>Master_Port</code>`: The port the master is listening on.
  * `<code>Master_Log_File</code>`: The name of the latest file that the binlogrouter is
 writing to.
  * `<code>Read_Master_Log_Pos</code>`: The current position where the last event was
 written in the latest binlog.
  * `<code>Slave_IO_Running</code>`: Set to `<code>Yes</code>` if replication running and `<code>No</code>` if it's
 not.
  * `<code>Slave_SQL_Running</code>` Set to `<code>Yes</code>` if replication running and `<code>No</code>` if it's
 not.
  * `<code>Exec_Master_Log_Pos</code>`: Same as `<code>Read_Master_Log_Pos</code>`.
  * `<code>Gtid_IO_Pos</code>`: The latest replicated GTID.
* `<code>SELECT { Field } ...</code>`
* The binlogrouter implements a small subset of the MariaDB SELECT syntax as
 it is mainly used by the replicating slaves to query various parameters. If
 a field queried by a client is not known to the binlogrouter, the value
 will be returned back as-is. The following list of functions and variables
 are understood by the binlogrouter and are replaced with actual values:


  * `<code>@@gtid_slave_pos</code>`, `<code>@@gtid_current_pos</code>` or `<code>@@gtid_binlog_pos</code>`: All of
 these return the latest GTID replicated from the master.
  * `<code>version()</code>` or `<code>@@version</code>`: The version string returned by MaxScale when
 a client connects to it.
  * `<code>UNIX_TIMESTAMP()</code>`: The current timestamp.
  * `<code>@@version_comment</code>`: Always `<code>pinloki</code>`.
  * `<code>@@global.gtid_domain_id</code>`: Always `<code>0</code>`.
  * `<code>@master_binlog_checksum</code>`: Always `<code>CRC32</code>`.
  * `<code>@@session.auto_increment_increment</code>`: Always `<code>1</code>`
  * `<code>@@character_set_client</code>`: Always `<code>utf8</code>`
  * `<code>@@character_set_connection</code>`: Always `<code>utf8</code>`
  * `<code>@@character_set_results</code>`: Always `<code>utf8</code>`
  * `<code>@@character_set_server</code>`: Always `<code>utf8mb4</code>`
  * `<code>@@collation_server</code>`: Always `<code>utf8mb4_general_ci</code>`
  * `<code>@@collation_connection</code>`: Always `<code>utf8_general_ci</code>`
  * `<code>@@init_connect</code>`: Always an empty string
  * `<code>@@interactive_timeout</code>`: Always `<code>28800</code>`
  * `<code>@@license</code>`: Always `<code>BSL</code>`
  * `<code>@@lower_case_table_names</code>`: Always `<code>0</code>`
  * `<code>@@max_allowed_packet</code>`: Always `<code>16777216</code>`
  * `<code>@@net_write_timeout</code>`: Always `<code>60</code>`
  * `<code>@@performance_schema</code>`: Always `<code>0</code>`
  * `<code>@@query_cache_size</code>`: Always `<code>1048576</code>`
  * `<code>@@query_cache_type</code>`: Always `<code>OFF</code>`
  * `<code>@@sql_mode</code>`: Always an empty string
  * `<code>@@system_time_zone</code>`: Always `<code>UTC</code>`
  * `<code>@@time_zone</code>`: Always `<code>SYSTEM</code>`
  * `<code>@@tx_isolation</code>`: Always `<code>REPEATABLE-READ</code>`
  * `<code>@@wait_timeout</code>`: Always `<code>28800</code>`
* `<code>SET</code>`
* `<code>@@global.gtid_slave_pos</code>`: Set the position from which binlogrouter should
 start replicating. E.g. `<code>SET @@global.gtid_slave_pos="0-1000-1234,1-1001-5678"</code>`
* `<code>SHOW VARIABLES LIKE '...'</code>`
* Shows variables matching a string. The `<code>LIKE</code>` operator in `<code>SHOW VARIABLES</code>`
 is mandatory for the binlogrouter. This means that a plain `<code>SHOW VARIABLES</code>`
 is not currently supported. In addition, the `<code>LIKE</code>` operator in
 binlogrouter only supports exact matches.
Currently the only variables that are returned are `<code>gtid_slave_pos</code>`,
 `<code>gtid_current_pos</code>` and `<code>gtid_binlog_pos</code>` which return the current GTID
 coordinates of the binlogrouter. In addition to these, the `<code>server_id</code>`
 variable will return the configured server ID of the binlogrouter.


## Configuration Parameters


The binlogrouter is configured similarly to how normal routers are configured in
MaxScale. It requires at least one listener where clients can connect to and one
server from which the database user information can be retrieved. An example
configuration can be found in the [example](#example) section of this document.


### `<code>datadir</code>`


Directory where binary log files are stored. By default the files are stored in
`<code>/var/lib/maxscale/binlogs</code>`. **NOTE:** If you are upgrading from a version prior
to 2.5, make sure this directory is different from what it was before, or
move the old data.


### `<code>server_id</code>`


The server ID that MaxScale uses when connecting to the master and when serving
binary logs to the slaves. Default value is 1234.


### `<code>net_timeout</code>`


Network connection and read timeout for the connection to the master. The value
is specified as documented
[here](../maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-configuration-guide.md#durations). Default value is 10
seconds.


### `<code>select_master</code>`


Automatically select the master server to replicate from. The default value is
false.


When this feature is enabled, the master which binlogrouter will replicate
from will be selected from the servers defined by a monitor `<code>cluster=TheMonitor</code>`.
Alternatively servers can be listed in `<code>servers</code>`. The servers should be monitored
by a monitor. Only servers with the `<code>Master</code>` status are used. If multiple master
servers are available, the first available master server will be used.


If a `<code>CHANGE MASTER TO</code>` command is received while `<code>select_master</code>` is on, the
command will be honored and `<code>select_master</code>` turned off until the next reboot.
This allows the Monitor to perform failover, and more importantly, switchover.
It also allows the user to manually redirect the Binlogrouter. The current
master is "sticky", meaning that the same master will be chosen on reboot.


**NOTE:** Do not use the `<code>mariadbmon</code>` parameter
[auto_rejoin](https://mariadb.com/kb/Monitor/MariaDB-Monitor#auto_rejoin) if the monitor is
monitoring a binlogrouter. The binlogrouter does not support all the SQL
commands that the monitor will send and the rejoin will fail. This restriction
will be lifted in a future version.


The GTID the replication will start from, will be based on the latest replicated
GTID. If no GTID has been replicated, the router will start replication from the
start. Manual configuration of the GTID can be done by first configuring the
replication manually with `<code>CHANGE MASTER TO</code>`.


### `<code>expire_log_duration</code>`


Duration after which a binary log file can be automatically removed. The default is 0,
or no automatic removal. This is similar to the server system variable
[expire_log_days](../../../server/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#expire_logs_days).


The duration is measured from the last modification of the log file. Files are
purged in the order they were created. The automatic purge works in a similar
manner to `<code>PURGE BINARY LOGS TO <filename></code>` in that it will stop the purge if
an eligible file is in active use, i.e. being read by a slave.


The duration can be specified as explained
[here](../maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-configuration-guide.md#durations).


### `<code>expire_log_minimum_files</code>`


The minimum number of log files the automatic purge keeps. At least one file
is always kept. The default setting is 2.


## New installation


1. Configure and start MaxScale.
1. If you have not configured `<code>select_master=true</code>` (automatic
 master selection), issue a `<code>CHANGE MASTER TO</code>` command to binlogrouter.



```
mysql -u USER -pPASSWORD -h maxscale-IP -P binlog-PORT
CHANGE MASTER TO master_host="master-IP", master_port=master-PORT, master_user=USER, master_password="PASSWORD", master_use_gtid=slave_pos;
START SLAVE;
```



1. Redirect each slave to replicate from Binlogrouter



```
mysql -u USER -pPASSWORD -h slave-IP -P slave-PORT
STOP SLAVE;
CHANGE MASTER TO master_host="maxscale-IP", master_port=binlog-PORT,
master_user="USER", master_password="PASSWORD", master_use_gtid=slave_pos;
START SLAVE;
SHOW SLAVE STATUS \G
```



## Upgrading to version 2.5


Binlogrouter does not read any of the data that a version prior to 2.5
has saved. By default binlogrouter will request the replication stream
from the blank state (from the start of time), which is basically meant
for new systems. If a system is live, the entire replication data probably
does not exist, and if it does, it is not necessary for binlogrouter to read
and store all the data.


### Before you start


* Note that binlogrouter only supports GTID based replication.
* Make sure that the configured data directory for the new binlogrouter
 is different from the old one, or move old data away.
 See [datadir](#datadir).
* If the master contains binlogs from the blank state, and there
 is a large amount of data, consider purging old binlogs.
 See [Using and Maintaining the Binary Log](../../../server/server-management/server-monitoring-logs/binary-log/using-and-maintaining-the-binary-log.md).


### Deployment


The method described here inflicts the least downtime. Assuming you have
configured version 2.5, and it is ready to go:


1. Redirect each slave that replicates from Binlogrouter to replicate from the
 master.



```
mysql -u USER -pPASSWORD -h slave-IP -P slave-PORT
STOP SLAVE;
CHANGE MASTER TO master_host="master-IP", master_port=master-PORT,
master_user="USER", master_password="PASSWORD", master_use_gtid=slave_pos;
START SLAVE;
SHOW SLAVE STATUS \G
```



1. Stop the old version of MaxScale, and start the new one.
 Verify routing functionality.
1. Issue a `<code>CHANGE MASTER TO</code>` command, or use [select_master](#select_master).



```
mysql -u USER -pPASSWORD -h maxscale-IP -P binlog-PORT
CHANGE MASTER TO master_host="master-IP", master_port=master-PORT,
master_user=USER,master_password="PASSWORD", master_use_gtid=slave_pos;
```



1. Run `<code>maxctrl list servers</code>`. Make sure all your servers are accounted for.
 Pick the lowest gtid state (e.g. 0-1000-1234,1-1001-5678) on display and
 issue this command to Binlogrouter:



```
STOP SLAVE
SET @@global.gtid_slave_pos = "0-1000-1234,1-1001-5678";
START SLAVE
```



**NOTE:** Even with `<code>select_master=true</code>` you have to set @@global.gtid_slave_pos
if any binlog files have been purged on the master. The server will only stream
from the start of time if the first binlog file is present.
See [select_master](#select_master).


1. Redirect each slave to replicate from Binlogrouter.



```
mysql -u USER -pPASSWORD -h slave-IP -P slave-PORT
STOP SLAVE;
CHANGE MASTER TO master_host="maxscale-IP", master_port=binlog-PORT,
master_user="USER", master_password="PASSWORD",
master_use_gtid=slave_pos;
START SLAVE;
SHOW SLAVE STATUS \G
```



## Galera cluster


When replicating from a Galera cluster, [select_master](#select_master) must be
set to true, and the servers must be monitored by the
[Galera Monitor](../maxscale-25-rest-api/mariadb-maxscale-25-monitor-resource.md).
Configuring binlogrouter is the same as described above.


The Galera cluster must be configured to use [Wsrep GTID Mode](../../../server/server-usage/replication-cluster-multi-master/galera-cluster/using-mariadb-replication-with-mariadb-galera-cluster/using-mariadb-gtids-with-mariadb-galera-cluster.md).


The MariaDB version must be 10.5.1 or higher.
The required GTID related server settings for MariaDB/Galera to work with
Binlogrouter are listed here:



```
[mariadb]
log_slave_updates = ON
log_bin = pinloki       # binlog file base name. Must be the same on all servers
gtid_domain_id = 1001   # Must be different for each galera server
binlog_format = ROW

[galera]
wsrep_on = ON
wsrep_gtid_mode = ON
wsrep_gtid_domain_id = 42  # Must be the same for all servers
```



## Example


The following is a small configuration file with automatic master selection.
With it, the service will accept connections on port 3306.



```
[server1]
type=server
address=192.168.0.1
port=3306

[server2]
type=server
address=192.168.0.2
port=3306

[MariaDB-Monitor]
type=monitor
module=mariadbmon
servers=server1, server2
user=maxuser
password=maxpwd
monitor_interval=10s

[Replication-Proxy]
type=service
router=binlogrouter
cluster=MariaDB-Monitor
select_master=true
expire_log_duration=5h
expire_log_minimum_files=3
user=maxuser
password=maxpwd

[Replication-Listener]
type=listener
service=Replication-Proxy
protocol=MariaDBClient
port=3306
```



## Limitations


* Old-style replication with binlog name and file offset is not supported
 and the replication must be started by setting up the GTID to replicate
 from.
* Only replication from MariaDB servers (including Galera) is supported.
* The MariaDB server where the replication is done from must be configured with
 `<code>binlog_checksum=CRC32</code>`.
