
# MaxScale 24.08 Beta Binlogrouter

# Binlogrouter


The binlogrouter is a router that acts as a replication proxy for MariaDB
primary-replica replication. The router connects to a primary, retrieves the binary
logs and stores them locally. Replica servers can connect to MaxScale like they
would connect to a normal primary server. If the primary server goes down,
replication between MaxScale and the replicas can still continue up to the latest
point to which the binlogrouter replicated to. The primary can be changed without
disconnecting the replicas and without them noticing that the primary server has
changed. This allows for a more highly available replication setup.


In addition to the high availability benefits, the binlogrouter creates only one
connection to the primary whereas with normal replication each individual replica
will create a separate connection. This reduces the amount of work the primary
database has to do which can be significant if there are a large number of
replicating replicas.




* [Binlogrouter](#binlogrouter)

  * [Binlog purge, archive and compress](#binlog-purge-archive-and-compress)
  * [Modifying binlog files manually](#modifying-binlog-files-manually)
  * [Supported SQL Commands](#supported-sql-commands)
  * [Semi-sync replication](#semi-sync-replication)
  * [Configuration Parameters](#configuration-parameters)

    * [datadir](#datadir)
    * [archivedir](#archivedir)
    * [server_id](#server_id)
    * [net_timeout](#net_timeout)
    * [select_master](#select_master)
    * [expiration_mode](#expiration_mode)
    * [expire_log_duration](#expire_log_duration)
    * [expire_log_minimum_files](#expire_log_minimum_files)
    * [compression_algorithm](#compression_algorithm)
    * [number_of_noncompressed_files](#number_of_noncompressed_files)
    * [ddl_only](#ddl_only)
    * [encryption_key_id](#encryption_key_id)
    * [encryption_cipher](#encryption_cipher)
    * [rpl_semi_sync_slave_enabled](#rpl_semi_sync_slave_enabled)
  * [New installation](#new-installation)
  * [Upgrading from legacy versions](#upgrading-from-legacy-versions)

    * [Before you start](#before-you-start)
    * [Deployment](#deployment)
    * [Bootstrap binlogrouter](#bootstrap-binlogrouter)
  * [Galera cluster](#galera-cluster)
  * [Example](#example)
  * [Limitations](#limitations)




## Binlog purge, archive and compress


File purge and archive are mutually exclusive. Archiving simply means that
a binlog is moved to another directory. That directory can be mounted to another
file system for backups or, for example, a locally mounted S3 bucket.


If archiving is started from a primary that still has all its history intact, a
full copy of the primary can be archived.


File compression preserves disk space and makes archiving faster. All
binlogs except the very last one, which is the one being logged to, can be
compressed. The overhead of reading from a compressed binlog is small, and
is typically only needed when a replica goes down, reconnects and is far
enough behind the current GTID that an older file needs to be opened.


There is no automated way as of yet for the binlogrouter to use archived files,
but should the need arise files can be copied from the archive to the binlog
directory. See ['Modifying binlog files manually'](#modifying-binlog-files-manually).


The related configuration options, which are explained in more detail in the
configuration section are:
*[expiration_mode](#expiration_mode) Select purge or archive.* [datadir](#datadir) Directory where binlog files are stored (the default is usually fine).
*[archivedir](#archivedir) Directory to which files are archived. This directory
 must exist when MaxScale is started.* [expire_log_minimum_files](#expire_log_minimum_files) The minimum number of
 binlogs to keep before purge or archive is allowed.
*[expire_log_duration](#expire_log_duration) Duration from the last file
 modification until the binlog is eligible for purge or archive.* [compression_algorithm](#compression_algorithm) Select a compression algorithm
 or `<code>none</code>` for no compression. Currently only zstandard is supported.
* [number_of_noncompressed_files](#number_of_noncompressed_files) The minimum number of
 binlogs not to compress.


Following are example settings where it is expected that a
replica is down for no more than 24 hours.



```
expiration_mode=archive
archivedir = /mnt/binlog-s3
expire_log_minimum_files=3
expire_log_duration=24h
compression_algorithm=zstandard
number_of_noncompressed_files=2
```



## Modifying binlog files manually


There is usually no reason to modify the contents of the binlog directory.
Changing the contents can cause **failures** if not done correctly. Never make
any changes if running a version prior to 23.08, except when a
[bootstrap](#bootstrap-binlogrouter) is needed.


A binlog file has the name <basename>.<sequence_number>. The basename is decided
by the primary server. The sequence number increases by one for each file and is six
digits long. The first file has the name <basename>.000001


The file `<code>binlog.index</code>` contains the view of the current state of the binlogs
as a list of file names ordered by the file sequence number. `<code>binlog.index</code>` is
automatically generated any time the contents of `<code>datadir</code>` changes.


Older files can be manually deleted and should be deleted in the order they
were created, lowest to highest sequence number. Prefer to use purge configuration.


Archived files can be copied back to `<code>datadir</code>`, but care should be taken to copy
them back in the reverse order they were created, highest to lowest sequence number.
The copied over files will be re-archived once `<code>expire_log_duration</code>` time has
passed.


Never leave a gap in the sequence numbers, and always preserve the name of a
binlog file if copied. Do not copy binlog files on top of existing binlog files.


As of version 24.02 any binlog except the latest one can be manually compressed, .e.g:



```
zstd --rm -z binlog.001234
```



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
 ones listed by the original primary where the binlogrouter is replicating
 from.
* `<code>PURGE { BINARY | MASTER } LOGS TO <filename></code>`
* Purges binary logs up to but not including the given file. The file name
 must be one of the names shown in `<code>SHOW BINARY LOGS</code>`. The version of this
 command which accepts a timestamp is not currently supported.
 Automatic purging is supported using the configuration
 parameter [expire_log_duration](#expire_log_duration).
The files are purged in the order they were created. If a file to be purged
 is detected to be in use, the purge stops. This means that the purge will
 stop at the oldest file that a replica is still reading.
NOTE: You should still take precaution not to purge files that a potential
 replica will need in the future. MaxScale can only detect that a file is
 in active use when a replica is connected, and requesting events from it.
* `<code>SHOW MASTER STATUS</code>`
* Shows the name and position of the file to which the binlogrouter will write
 the next replicated data. The name and position do not correspond to the
 name and position in the primary.
* `<code>SHOW SLAVE STATUS</code>`
* Shows the replica status information similar to what a normal MariaDB replica
 server shows. Some of the values are replaced with constants values that
 never change. The following values are not constant:


  * `<code>Slave_IO_State</code>`: Set to `<code>Waiting for primary to send event</code>` when
 replication is ongoing.
  * `<code>Master_Host</code>`: Address of the current primary.
  * `<code>Master_User</code>`: The user used to replicate.
  * `<code>Master_Port</code>`: The port the primary is listening on.
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
 it is mainly used by the replicating replicas to query various parameters. If
 a field queried by a client is not known to the binlogrouter, the value
 will be returned back as-is. The following list of functions and variables
 are understood by the binlogrouter and are replaced with actual values:


  * `<code>@@gtid_slave_pos</code>`, `<code>@@gtid_current_pos</code>` or `<code>@@gtid_binlog_pos</code>`: All of
 these return the latest GTID replicated from the primary.
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


## Semi-sync replication


If the server from which the binlogrouter replicates from is using semi-sync
replication, the binlogrouter will acknowledge the replicated events.


## Configuration Parameters


The binlogrouter is configured similarly to how normal routers are configured in
MaxScale. It requires at least one listener where clients can connect to and one
server from which the database user information can be retrieved. An example
configuration can be found in the [example](#example) section of this document.


### `<code>datadir</code>`


* Type: string
* Mandatory: No
* Default: `<code>/var/lib/maxscale/binlogs</code>`
* Dynamic: No


Directory where binary log files are stored. By default the files are stored in
`<code>/var/lib/maxscale/binlogs</code>`. **NOTE:** If you are upgrading from a version prior
to 2.5, make sure this directory is different from what it was before, or
move the old data.


### `<code>archivedir</code>`


* Type: string
* Mandatory: Yes if `expiration_mode=archive"
* Default: No
* Dynamic: No


The directory to where files are archived. This is presumably a directory
mounted to a remote file system or an S3 bucket. Ensure that the user running
MaxScale (typically "maxscale") has sufficient privileges on the archive directory.
S3 buckets mounted with s3fs may require setting permissions manually:



```
s3fs my-bucket /home/joe/S3_bucket_mount/ -o umask=0077
```



The directory must exist when MaxScale starts.


### `<code>server_id</code>`


* Type: count
* Mandatory: No
* Dynamic: No
* Default: `<code>1234</code>`


The server ID that MaxScale uses when connecting to the primary and when serving
binary logs to the replicas.


### `<code>net_timeout</code>`


* Type: [duration](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>10s</code>`


Network connection and read timeout for the connection to the primary.


### `<code>select_master</code>`


* Type: boolean
* Mandatory: No
* Dynamic: No
* Default: `<code>false</code>`


Automatically select the primary server to replicate from.


When this feature is enabled, the primary which binlogrouter will replicate
from will be selected from the servers defined by a monitor `<code>cluster=TheMonitor</code>`.
Alternatively servers can be listed in `<code>servers</code>`. The servers should be monitored
by a monitor. Only servers with the `<code>Master</code>` status are used. If multiple primary
servers are available, the first available primary server will be used.


If a `<code>CHANGE MASTER TO</code>` command is received while `<code>select_master</code>` is on, the
command will be honored and `<code>select_master</code>` turned off until the next reboot.
This allows the Monitor to perform failover, and more importantly, switchover.
It also allows the user to manually redirect the Binlogrouter. The current
primary is "sticky", meaning that the same primary will be chosen on reboot.


**NOTE:** Do not use the `<code>mariadbmon</code>` parameter
[auto_rejoin](https://mariadb.com/kb/Monitor/MariaDB-Monitor#auto_rejoin) if the monitor is
monitoring a binlogrouter. The binlogrouter does not support all the SQL
commands that the monitor will send and the rejoin will fail. This restriction
will be lifted in a future version.


The GTID the replication will start from, will be based on the latest replicated
GTID. If no GTID has been replicated, the router will start replication from the
start. Manual configuration of the GTID can be done by first configuring the
replication manually with `<code>CHANGE MASTER TO</code>`.


### `<code>expiration_mode</code>`


* Type: [enum](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
* Dynamic: No
* Values: `<code>purge</code>`, `<code>archive</code>`
* Default: `<code>purge</code>`


Choose whether expired logs should be purged or archived.


### `<code>expire_log_duration</code>`


* Type: [duration](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>0s</code>` (off)


Duration after which a binary log file expires, i.e. becomes eligible for purge or archive.
This is similar to the server system variable
[expire_log_days](../../../server/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#expire_logs_days).


The duration is measured from the last modification of the log file. Files are
purged in the order they were created. The automatic purge works in a similar
manner to `<code>PURGE BINARY LOGS TO <filename></code>` in that it will stop the purge if
an eligible file is in active use, i.e. being read by a replica.


### `<code>expire_log_minimum_files</code>`


* Type: count
* Mandatory: No
* Dynamic: No
* Default: `<code>2</code>`


The minimum number of log files the automatic purge keeps. At least one file
is always kept.


### `<code>compression_algorithm</code>`


* Type: [enum](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>none</code>`, `<code>zstandard</code>`
* Default: `<code>none</code>`


### `<code>number_of_noncompressed_files</code>`


* Type: count
* Mandatory: No
* Dynamic: No
* Default: `<code>2</code>`


The minimum number of log files that are not compressed. At least one file
is not compressed.


### `<code>ddl_only</code>`


* Type: boolean
* Mandatory: No
* Dynamic: No
* Default: false


When enabled, only DDL events are written to the binary logs. This means that
`<code>CREATE</code>`, `<code>ALTER</code>` and `<code>DROP</code>` events are written but `<code>INSERT</code>`, `<code>UPDATE</code>` and
`<code>DELETE</code>` events are not.


This mode can be used to keep a record of all the schema changes that occur on a
database. As only the DDL events are stored, it becomes very easy to set up an
empty server with no data in it by simply pointing it at a binlogrouter instance
that has `<code>ddl_only</code>` enabled.


### `<code>encryption_key_id</code>`


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


Encryption key ID used to encrypt the binary logs. If configured, an [Encryption
Key Manager](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
must also be configured and it must contain the key with the given ID. If the
encryption key manager supports versioning, new binary logs will be encrypted
using the latest encryption key. Old binlogs will remain encrypted with older
key versions and remain readable as long as the key versions used to encrypt
them are available.


Once binary log encryption has been enabled, the encryption key ID cannot be
changed and the key must remain available to MaxScale in order for replication
to work. If an encryption key is not available or the key manager fails to
retrieve it, the replication from the currently selected primary server will
stop. If the replication is restarted manually, the encryption key retrieval is
attempted again.


Re-encryption of binlogs using another encryption key is not possible. However,
this is possible if the data is replicated to a second MaxScale server that uses
a different encryption key. The same approach can also be used to decrypt
binlogs.


### `<code>encryption_cipher</code>`


* Type: [enum](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>AES_CBC</code>`, `<code>AES_CTR</code>`, `<code>AES_GCM</code>`
* Default: `<code>AES_GCM</code>`


The encryption cipher to use. The encryption key size also affects which mode is
used: only 128, 192 and 256 bit encryption keys are currently supported.


Possible values are:


* `<code>AES_GCM</code>` (default)
* [AES in Galois/Counter Mode](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Galois/counter_(GCM)).
* `<code>AES_CBC</code>`
* [AES in Cipher Block Chaining Mode](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_(CBC)).
* `<code>AES_CTR</code>`
* [AES in Counter Mode](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_(CTR)).


### `<code>rpl_semi_sync_slave_enabled</code>`


* Type: [boolean](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: false
* Dynamic: Yes


Enable
[semi-synchronous](../../../server/server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md)
replication when replicating from a MariaDB server. If enabled, the binlogrouter
will send acknowledgment for each received event. Note that the
[rpl_semi_sync_master_enabled](../../../server/server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_enabled)
parameter must be enabled in the MariaDB server where the replication is done
from for the semi-synchronous replication to take place.


## New installation


1. Configure and start MaxScale.
1. If you have not configured `<code>select_master=true</code>` (automatic
 primary selection), issue a `<code>CHANGE MASTER TO</code>` command to binlogrouter.



```
mariadb -u USER -pPASSWORD -h maxscale-IP -P binlog-PORT
CHANGE MASTER TO master_host="primary-IP", master_port=primary-PORT, master_user=USER, master_password="PASSWORD", master_use_gtid=slave_pos;
START SLAVE;
```



1. Redirect each replica to replicate from Binlogrouter



```
mariadb -u USER -pPASSWORD -h replica-IP -P replica-PORT
STOP SLAVE;
CHANGE MASTER TO master_host="maxscale-IP", master_port=binlog-PORT,
master_user="USER", master_password="PASSWORD", master_use_gtid=slave_pos;
START SLAVE;
SHOW SLAVE STATUS \G
```



## Upgrading from legacy versions


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
* If the primary contains binlogs from the blank state, and there
 is a large amount of data, consider purging old binlogs.
 See [Using and Maintaining the Binary Log](../../../server/server-management/server-monitoring-logs/binary-log/using-and-maintaining-the-binary-log.md).


### Deployment


The method described here inflicts the least downtime. Assuming you have
configured MaxScale version 2.5 or newer, and it is ready to go:


1. Redirect each replica that replicates from Binlogrouter to replicate from the
 primary.



```
mariadb -u USER -pPASSWORD -h replica-IP -P replica-PORT
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
mariadb -u USER -pPASSWORD -h maxscale-IP -P binlog-PORT
CHANGE MASTER TO master_host="primary-IP", master_port=primary-PORT,
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
if any binlog files have been purged on the primary. The server will only stream
from the start of time if the first binlog file is present.
See [select_master](#select_master).


1. Redirect each replica to replicate from Binlogrouter.



```
mariadb -u USER -pPASSWORD -h replica-IP -P replica-PORT
STOP SLAVE;
CHANGE MASTER TO master_host="maxscale-IP", master_port=binlog-PORT,
master_user="USER", master_password="PASSWORD",
master_use_gtid=slave_pos;
START SLAVE;
SHOW SLAVE STATUS \G
```



### Bootstrap binlogrouter


If for any reason you need to "bootstrap" the binlogrouter you can change
the `<code>datadir</code>` or delete the entire binglog directory (`<code>datadir</code>`) when
MaxScale is NOT running. This could be necessary if files are accidentally
deleted or the file system becomes corrupt.


No changes are required to the attached replicas.


if [select_master](#select_master) is set to `<code>true</code>` and the primary contains
the entire binlog history, a simple restart of MaxScale sufficies.


In the normal case, the primary does not have the entire history and
you will need to set the GTID position to a starting value, usually the
earliest gtid state of all replicas. Once MaxScale has been restarted
connect to the binlogrouter from the command line.


If [select_master](#select_master) is set to true issue:



```
mariadb -u USER -pPASSWORD -h maxscale-IP -P binlog-PORT
STOP SLAVE;
SET @@global.gtid_slave_pos = "gtid_state";
START SLAVE;
```



else



```
mariadb -u USER -pPASSWORD -h maxscale-IP -P binlog-PORT
CHANGE MASTER TO master_host="primary-IP", master_port=primary-PORT, master_user=USER, master_password="PASSWORD", master_use_gtid=slave_pos;
SET @@global.gtid_slave_pos = "gtid_state";
START SLAVE;
```



## Galera cluster


When replicating from a Galera cluster, [select_master](#select_master) must be
set to true, and the servers must be monitored by the
[Galera Monitor](../../mariadb-maxscale-25/maxscale-25-rest-api/mariadb-maxscale-25-monitor-resource.md).
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


The following is a small configuration file with automatic primary selection.
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
expiration_mode=archive
archivedir=/mnt/somedir
expire_log_minimum_files=3
expire_log_duration=24h
compression_algorithm=zstandard
number_of_noncompressed_files=2
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
* Old encrypted binary logs are not re-encrypted with newer key versions ([MXS-4140](https://jira.mariadb.org/browse/MXS-4140))
* The MariaDB server where the replication is done from must be configured with
 `<code>binlog_checksum=CRC32</code>`.
