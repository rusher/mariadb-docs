
# MariaDB Monitor

# MariaDB Monitor


Up until MariaDB MaxScale 2.2.0, this monitor was called *MySQL Monitor*.


## Overview


The MariaDB Monitor is a monitoring module for MaxScale that monitors a Master-Slave
replication cluster. It assigns master and slave roles inside MaxScale according to
the actual replication tree in the cluster.


## Configuration


A minimal configuration for a monitor requires a set of servers for monitoring
and a username and a password to connect to these servers.



```
[MyMonitor]
type=monitor
module=mariadbmon
servers=server1,server2,server3
user=myuser
passwd=mypwd
```



Note that from MaxScale 2.2.1 onwards, the module name is `<code>mariadbmon</code>`; up until
MaxScale 2.2.0 it was `<code>mysqlmon</code>`. The name `<code>mysqlmon</code>` has been deprecated but can
still be used, although it will cause a warning to be logged.


The user requires the REPLICATION CLIENT privilege to successfully monitor the
state of the servers.



```
MariaDB [(none)]> grant replication client on *.* to 'maxscale'@'maxscalehost';
Query OK, 0 rows affected (0.00 sec)
```



## Common Monitor Parameters


For a list of optional parameters that all monitors support, read the
[Monitor Common](../../mariadb-maxscale-21-06/README.md) document.


## MariaDB Monitor optional parameters


These are optional parameters specific to the MariaDB Monitor.


### `<code>detect_replication_lag</code>`


A boolean value which controls if replication lag between the master and the
slaves is monitored. This allows the routers to route read queries to only
slaves that are up to date. Default value for this parameter is *false*.


To detect the replication lag, MaxScale uses the *maxscale_schema.replication_heartbeat*
table. This table is created on the master server and it is updated at every heartbeat
with the current timestamp. The updates are then replicated to the slave servers
and when the replicated timestamp is read from the slave servers, the lag between
the slave and the master can be calculated.


The monitor user requires INSERT, UPDATE, DELETE and SELECT permissions on the
maxscale_schema.replication_heartbeat table and CREATE permissions on the
maxscale_schema database. The monitor user will always try to create the database
and the table if they do not exist.


### `<code>detect_stale_master</code>`


Allow previous master to be available even in case of stopped or misconfigured
replication.


Starting from MaxScale 2.0.0 this feature is enabled by default. It is disabled
by default in MaxScale 1.4.3 and below.


This allows services that depend on master and slave roles to continue
functioning as long as the master server is available. This is a situation
which can happen if all slave servers are unreachable or the replication
breaks for some reason.



```
detect_stale_master=true
```



### `<code>detect_stale_slave</code>`


Treat running slaves servers without a master server as valid slave servers.


This feature is enabled by default.


If a slave server loses its master server, the replication is considered broken.
With this parameter, slaves that have lost their master but have been slaves of
a master server can retain their slave status even without a master. This means
that when a slave loses its master, it can still be used for reads.


If this feature is disabled, a server is considered a valid slave if and only if
it has a running master server monitored by this monitor.



```
detect_stale_slave=true
```



### `<code>mysql51_replication</code>`


Enable support for MySQL 5.1 replication monitoring. This is needed if a MySQL
server older than 5.5 is used as a slave in replication.



```
mysql51_replication=true
```



### `<code>multimaster</code>`


Detect multi-master replication topologies. This feature is disabled by default.


When enabled, the multi-master detection looks for the root master servers in
the replication clusters. These masters can be found by detecting cycles in the
graph created by the servers. When a cycle is detected, it is assigned a master
group ID. Every master in a master group will receive the Master status. The
special group ID 0 is assigned to all servers which are not a part of a
multi-master replication cycle.


If one or more masters in a group has the `<code>@@read_only</code>` system variable set to
`<code>ON</code>`, those servers will receive the Slave status even though they are in the
multi-master group. Slave servers with `<code>@@read_only</code>` disabled will never receive
the master status.


By setting the servers into read-only mode, the user can control which
server receive the master status. To do this:


* Enable `<code>@@read_only</code>` on all servers (preferably through the configuration file)
* Manually disable `<code>@@read_only</code>` on the server which should be the master


This functionality is similar to the [Multi-Master Monitor](mariadb-maxscale-22-multi-master-monitor.md)
functionality. The only difference is that the MariaDB monitor will also detect
traditional Master-Slave topologies.


### `<code>ignore_external_masters</code>`


Ignore any servers that are not monitored by this monitor but are a part of the
replication topology. This option was added in MaxScale 2.1.12 and is disabled
by default.


MaxScale detects if a master server replicates from an external server. When
this is detected, the server is assigned the `<code>Slave</code>` and `<code>Slave of External
Server</code>` labels and will be treated as a slave server. Most of the time this
topology is used when MaxScale is used for read scale-out without master
servers, a Galera cluster with read replicas being a prime example of this
setup. Sometimes this is not the desired behavior and the external master server
should be ignored. Most of the time this is due to multi-source replication.


When this option is enabled, all servers that have the `<code>Master, Slave, Slave of
External Server, Running</code>` labels will instead get the `<code>Master, Running</code>` labels.


### `<code>detect_standalone_master</code>`


Detect standalone master servers. This feature takes a boolean parameter and
from MaxScale 2.2.1 onwards is enabled by default. Up until MaxScale 2.2.0 it
was disabled by default. In MaxScale 2.1.0, this parameter was called `<code>failover</code>`.


This parameter is intended to be used with simple, two node master-slave pairs
where the failure of the master can be resolved by "promoting" the slave as the
new master. Normally this is done by using an external agent of some sort
(possibly triggered by MaxScale's monitor scripts), like
[MariaDB Replication Manager](https://github.com/tanji/replication-manager)
or [MHA](https://code.google.com/p/mysql-master-ha/).


When the number of running servers in the cluster drops down to one, MaxScale
cannot be absolutely certain whether the last remaining server is a master or a
slave. At this point, MaxScale will try to deduce the type of the server by
looking at the system variables of the server in question.


By default, MaxScale will only attempt to deduce if the server can be used as a
slave server (controlled by the `<code>detect_stale_slave</code>` parameter). When the
`<code>detect_standalone_master</code>` mode is enabled, MaxScale will also attempt to deduce
whether the server can be used as a master server. This is done by checking that
the server is not in read-only mode and that it is not configured as a slave.


This mode in mariadbmon is completely passive in the sense that it does not modify
the cluster or any of the servers in it. It only labels the last remaining
server in a cluster as the master server.


Before a server is labelled as a standalone master, the following conditions must
have been met:


* Previous attempts to connect to other servers in the cluster have failed,
 controlled by the `<code>failcount</code>` parameter
* There is only one running server among the monitored servers
* The value of the `<code>@@read_only</code>` system variable is set to `<code>OFF</code>`


In 2.1.1, the following additional condition was added:


* The last running server is not configured as a slave


If the value of the `<code>allow_cluster_recovery</code>` parameter is set to false, the monitor
sets all other servers into maintenance mode. This is done to prevent accidental
use of the failed servers if they came back online. If the failed servers come
back up, the maintenance mode needs to be manually cleared once replication has
been set up.


**Note**: A failover will cause permanent changes in the data of the promoted
 server. Only use this feature if you know that the slave servers are capable
 of acting as master servers.


### `<code>failcount</code>`


Number of failures that must occur on all failed servers before a standalone
server is labelled as a master. The default value is 5 failures.


The monitor will attempt to contact all servers once per monitoring cycle. When
`<code>detect_standalone_master</code>` is enabled, all of the failed servers must fail
*failcount* number of connection attempts before the last server is labeled as
the master.


The formula for calculating the actual number of milliseconds before the server
is labelled as the master is `<code>monitor_interval * failcount</code>`.


If automatic failover is enabled (`<code>auto_failover=true</code>`), this setting also
controls how many times the master server must fail to respond before failover
begins.


### `<code>allow_cluster_recovery</code>`


Allow recovery after the cluster has dropped down to one server. This feature
takes a boolean parameter is enabled by default. This parameter requires that
`<code>detect_standalone_master</code>` is set to true. In MaxScale 2.1.0, this parameter was
called `<code>failover_recovery</code>`.


When this parameter is disabled, if the last remaining server is labelled as the
master, the monitor will set all of the failed servers into maintenance
mode. When this option is enabled, the failed servers are allowed to rejoin the
cluster.


This option should be enabled only when MaxScale is used in conjunction with an
external agent that automatically reintegrates failed servers into the
cluster. One of these agents is the *replication-manager* which automatically
configures the failed servers as new slaves of the current master.


### `<code>enforce_read_only_slaves</code>`


This feature is disabled by default. If set to ON, the monitor attempts to set
the server `<code>read_only</code>` flag to ON on any slave server with `<code>read_only</code>` OFF. The
flag is checked at every monitor iteration. The monitor user requires the
SUPER-privilege for this feature to work. While the `<code>read_only</code>`-flag is ON, only
users with the SUPER-privilege can write to the backend server. If temporary
write access is required, this feature should be disabled before attempting to
disable `<code>read_only</code>`. Otherwise the monitor would quickly re-enable it.


## Failover, switchover and auto-rejoin


Starting with MaxScale 2.2.1, MariaDB Monitor supports replication cluster
modification. The operations implemented are: *failover* (replacing a failed
master), *switchover* (swapping a slave with a running master) and *rejoin*
(joining a standalone server to the cluster). The features and the parameters
controlling them are presented in this section.


These features require that the monitor user (`<code>user</code>`) has the SUPER and RELOAD privileges.
In addition, the monitor needs to know which username and password a slave
should use when starting replication. These are given in `<code>replication_user</code>` and
`<code>replication_password</code>`.


All three operations can be activated manually through MaxAdmin/MaxCtrl. All
commands require the monitor instance name as first parameter. Failover selects
the new master server automatically and does not require additional parameters.
Switchover requires the new master server name. Additionally, the user may
designate the current master server in the switchover command. Rejoin requires
the name of the joining server. Example commands are below:



```
call command mariadbmon failover MyMonitor
call command mariadbmon switchover MyMonitor SlaveServ3
call command mariadbmon switchover MyMonitor SlaveServ3 MasterServ
call command mariadbmon rejoin MyMonitor NewServer2
```



The commands follow the standard module command syntax. All require the monitor
configuration name (MyMonitor) as the first parameter. For switchover, the
following parameters define the server to promote (SlaveServ3) and the server to
demote (MasterServ). For rejoin, the server to join (NewServer2) is required.


Failover can also activate automatically, if `<code>auto_failover</code>` is on. The
activation begins when the master has been down for a number of monitor
iterations defined in `<code>failcount</code>`.


Rejoin stands for starting replication on a standalone server or redirecting a
slave replicating from the wrong master (any server that is not the cluster
master). The rejoined servers are directed to replicate from the current cluster
master server, forcing the replication topology to a 1-master-N-slaves
configuration.


A server is categorized as standalone if the server has no slave connections,
not even stopped ones. A server is replicating from the wrong master if the
slave IO thread is connected but the master server id seen by the slave does not
match the cluster master id. Alternatively, the IO thread may be stopped or
connecting but the master server host or port information differs from the
cluster master info. These criteria mean that a STOP SLAVE does not yet set a
slave as standalone.


With `<code>auto_rejoin</code>` active, the monitor will try to rejoin any server matching
the above requirements. When activating rejoin manually, the user-designated
server must fulfill the same requirements.


The user can define files with SQL statements which are executed on any server
being demoted or promoted by cluster manipulation commands. See the sections on
`<code>promotion_sql_file</code>` and `<code>demotion_sql_file</code>` for more information.


### Limitations and requirements


Switchover and failover only understand simple topologies. They will not work if
the cluster has multiple masters, relay masters, or if the topology is circular.
The server cluster is assumed to be well-behaving with no significant
replication lag and all commands that modify the cluster complete in a few
seconds (faster than `<code>backend_read_timeout</code>` and `<code>backend_write_timeout</code>`).


The backends must all use GTID-based replication, and the domain id should not
change during a switchover or failover. Master and slaves must have
well-behaving GTIDs with no extra events on slave servers.


Switchover requires that the cluster is "frozen" for the duration of the
operation. This means that no data modifying statements such as INSERT or UPDATE
are executed and the GTID position of the master server is stable. When
switchover begins, the monitor sets the global *read_only* flag on the old
master backend to stop any updates. *read_only* does not affect users with the
SUPER-privilege so any such user can issue writes during a switchover. These
writes have a high chance to break replication, because the write may not be
replicated to all slaves before they switch to the new master. To prevent this,
any users who commonly do updates should not have the SUPER-privilege. For even
more security, the only SUPER-user session during a switchover should be the
MaxScale monitor user.


When mixing rejoin with failover/switchover, the backends should have
*log_slave_updates* on. The rejoining server is likely lagging behind the rest
of the cluster. If the current cluster master does not have binary logs from the
moment the rejoining server lost connection, the rejoining server cannot
continue replication. This is an issue if the master has changed and
the new master does not have *log_slave_updates* on.


If an automatic cluster operation such as auto-failover or auto-rejoin fails,
all cluster modifying operations are disabled for `<code>failcount</code>` monitor iterations,
after which the operation may be retried. Similar logic applies if the cluster is
unsuitable for such operations, e.g. replication is not using GTID.


### External master support


The monitor detects if a server in the cluster is replicating from an external
master (a server that is not monitored by the monitor). If the replicating
server is the cluster master server, then the cluster itself is considered to
have an external master.


If a failover/switchover happens, the new master server is set to replicate from
the cluster external master server. The usename and password for the replication
are defined in `<code>replication_user</code>` and `<code>replication_password</code>`. The address and
port used are the ones shown by `<code>SHOW ALL SLAVES STATUS</code>` on the old cluster
master server. In the case of switchover, the old master also stops replicating
from the external server to preserve the topology.


After failover the new master is replicating from the external master. If the
failed old master comes back online, it is also replicating from the external
server. To normalize the situation, either have *auto_rejoin* on or manually
execute a rejoin. This will redirect the old master to the current cluster
master.


### Configuration parameters


#### `<code>auto_failover</code>`


Enable automated master failover. This parameter expects a boolean value and the
default value is false.


When automatic failover is enabled, traditional MariaDB Master-Slave clusters
will automatically elect a new master if the old master goes down and stays down
a number of iterations given in `<code>failcount</code>`. Failover will not take place when
MaxScale is configured as a passive instance. For details on how MaxScale
behaves in passive mode, see the documentation on `<code>failover_timeout</code>` below.


The monitor user must have the SUPER and RELOAD privileges for failover to work.


#### `<code>auto_rejoin</code>`


Enable automatic joining of server to the cluster. This parameter expects a
boolean value and the default value is false.


When enabled, the monitor will attempt to direct standalone servers and servers
replicating from a relay master to the main cluster master server, enforcing a
1-master-N-slaves configuration.


For example, consider the following event series.


1. Slave A goes down
1. Master goes down and a failover is performed, promoting Slave B
1. Slave A comes back


Slave A is still trying to replicate from the downed master, since it wasn't
online during failover. If `<code>auto_rejoin</code>` is on, Slave A will quickly be
redirected to Slave B, the current master.


#### `<code>replication_user</code>` and `<code>replication_password</code>`


The username and password of the replication user. These are given as the values
for `<code>MASTER_USER</code>` and `<code>MASTER_PASSWORD</code>` whenever a `<code>CHANGE MASTER TO</code>` command is
executed.


Both `<code>replication_user</code>` and `<code>replication_password</code>` parameters must be defined if
a custom replication user is used. If neither of the parameters is defined, the
`<code>CHANGE MASTER TO</code>` command will use the monitor credentials for the replication
user.


The credentials used for replication must have the `<code>REPLICATION SLAVE</code>`
privilege.


`<code>replication_password</code>` uses the same encryption scheme as other password
parameters. If password encryption is in use, `<code>replication_password</code>` must be
encrypted with the same key to avoid erroneous decryption.


#### `<code>failover_timeout</code>` and `<code>switchover_timeout</code>`


Time limit for the cluster failover and switchover in seconds. The default values
are 90 seconds.


If no successful failover/switchover takes place within the configured time
period, a message is logged and automatic failover is disabled. This prevents
further automatic modifications to the misbehaving cluster.


`<code>failover_timeout</code>` also controls how long a MaxScale instance that has
transitioned from passive to active will wait for a failover to take place after
an apparent loss of a master server. If no new master server is detected within
the configured time period, failover will be initiated again.


#### `<code>verify_master_failure</code>` and `<code>master_failure_timeout</code>`


Enable additional master failure verification for automatic failover.
`<code>verify_master_failure</code>` is a boolean value (default: true) which enables this
feature and `<code>master_failure_timeout</code>` defines the timeout in seconds (default: 10).


The failure verification is performed by checking whether the slaves are still
connected to the master and receiving events. Effectively, if a slave has
received an event within `<code>master_failure_timeout</code>` seconds, the master is not
considered down when deciding whether to auto_failover.


If every slave loses its connection to the master (*Slave_IO_Running* is not
"Yes"), master failure is considered verified regardless of timeout. This allows
a faster failover when the master server crashes, as that causes immediate
disconnection.


For automatic failover to activate, the `<code>failcount</code>` requirement must also be
met.


#### `<code>servers_no_promotion</code>`


This is a comma-separated list of server names that will not be chosen for
master promotion during a failover. This does not affect switchover since in
that case the user selects the server. Using this list can disrupt new master
selection such that an unoptimal server is chosen. At worst, this will cause
replication to break.



```
servers_no_promotion=backup_dc_server1,backup_dc_server2
```



#### `<code>promotion_sql_file</code>` and `<code>demotion_sql_file</code>`


These optional settings are paths to text files with SQL statements in them.
During promotion or demotion, the contents are read line-by-line and executed on
the backend. Use these settings to execute custom statements on the servers to
complement the built-in operations.


Empty lines or lines starting with '#' are ignored. Any results returned by the
statements are ignored. All statements must succeed for the failover, switchover
or rejoin to continue. The monitor user may require additional privileges and
grants for the custom commands to succeed.


When promoting a slave to master during switchover or failover, the
`<code>promotion_sql_file</code>` is read and executed on the new master server after its
read-only flag is disabled. The commands are ran *before* starting replication
from an external master if any.


`<code>demotion_sql_file</code>` is ran on an old master during demotion to slave, before the
old master starts replicating from the new master. The file is also ran before
rejoining a standalone server to the cluster, as the standalone server is
typically a former master server. When redirecting a slave replicating from a
wrong master, the sql-file is not executed.


Since the queries in the files are ran during operations which modify
replication topology, care is required. If `<code>promotion_sql_file</code>` contains data
modification (DML) queries, the new master server may not be able to
successfully replicate from an external master. `<code>demotion_sql_file</code>` should never
contain DML queries, as these may not replicate to the slave servers before
slave threads are stopped, breaking replication.



```
promotion_sql_file=/home/root/scripts/promotion.sql
demotion_sql_file=/home/root/scripts/demotion.sql
```



### Manual switchover and failover


Both failover and switchover can be activated manually through the REST API or
MaxAdmin. The commands are only performed when MaxScale is in active mode.


It is safe to perform switchover or failover even with `<code>auto_failover</code>` on, since
the automatic operation cannot happen simultaneously with the manual one.


When switchover is iniated via the REST-API, the URL path is:



```
/v1/maxscale/mariadbmon/switchover?<monitor-instance>&<new-master>&<current-master>
```



where `<code><monitor-instance></code>` is the monitor section mame from the MaxScale
configuration file, `<code><new-master></code>` the name of the server that should be
made into the new master and `<code><current-master></code>` the server that currently
is the master. If there is no master currently, then `<code><current-master></code>`
need not be specified.


So, given a MaxScale configuration file like



```
[Cluster1]
type=monitor
module=mariadbmon
servers=server1, server2, server3, server 4
...
```



with the assumption that `<code>server2</code>` is the current master, then the URL
path for making `<code>server4</code>` the new master would be:



```
/v1/maxscale/mariadbmon/switchover?Cluster1&server4&server2
```



The REST-API path for manual failover is similar, although the `<code><new-master></code>`
and `<code><current-master></code>` fields are left out.



```
/v1/maxscale/mariadbmon/failover?Cluster1
```



## Using the MariaDB Monitor With Binlogrouter


Since MaxScale 2.2 it's possible to detect a replication setup
which includes Binlog Server: the required action is to add the
binlog server to the list of servers only if *master_id* identity is set.


For addition information read the
[Replication Proxy](../maxscale-22-tutorials/mariadb-maxscale-22-mariadb-maxscale-as-a-binlog-server.md)
tutorial.


## Example 1 - Monitor script


Here is an example shell script which sends an email to an [admin@my.org](mailto:admin@my.org)
when a server goes down.


|   |   |
| --- | --- |
| 1
2
3
4
5
6
7
8 | #!/usr/bin/env bash

#This script assumes that the local mail server is configured properly
#The second argument is the event type
event=${$2/.*=/}
server=${$3/.*=/}
message="A server has gone down at `date`."
echo $message|mail -s "The event was $event for server $server." admin@my.org |


Here is a monitor configuration that only triggers the script when a master
or a slave server goes down.



```
[Database Monitor]
type=monitor
module=mariadbmon
servers=server1,server2
script=mail_to_admin.sh
events=master_down,slave_down
```



When a master or a slave server goes down, the script is executed, a mail is
sent and the administrator will be immediately notified of any possible
problems. This is just a simple example showing what you can do with MaxScale
and monitor scripts.
