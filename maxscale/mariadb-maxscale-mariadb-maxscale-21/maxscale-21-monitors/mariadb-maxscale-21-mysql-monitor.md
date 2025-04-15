
# MySQL Monitor

# MySQL Monitor


## Overview


The MySQL Monitor is a monitoring module for MaxScale that monitors a Master-Slave replication cluster. It assigns master and slave roles inside MaxScale according to the actual replication tree in the cluster.


## Configuration


A minimal configuration for a monitor requires a set of servers for monitoring and a username and a password to connect to these servers.



```
[MySQL Monitor]
type=monitor
module=mysqlmon
servers=server1,server2,server3
user=myuser
passwd=mypwd
```



The user requires the REPLICATION CLIENT privilege to successfully monitor the state of the servers.



```
MariaDB [(none)]> grant replication client on *.* to 'maxscale'@'maxscalehost';
Query OK, 0 rows affected (0.00 sec)
```



## Common Monitor Parameters


For a list of optional parameters that all monitors support, read the [Monitor Common](../../mariadb-maxscale-21-06/README.md) document.


## MySQL Monitor optional parameters


These are optional parameters specific to the MySQL Monitor.


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


This functionality is similar to the [Multi-Master Monitor](mariadb-maxscale-21-multi-master-monitor.md)
functionality. The only difference is that the MySQL monitor will also detect
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


Detect standalone master servers. This feature takes a boolean parameter and is
disabled by default. In MaxScale 2.1.0, this parameter was called `<code>failover</code>`.


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


This mode in mysqlmon is completely passive in the sense that it does not modify
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


## Example 1 - Monitor script


Here is an example shell script which sends an email to an [admin@my.org](https://mariadb.com/kb/en/mailto:admin@my.org)
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


Here is a monitor configuration that only triggers the script when a master or a slave server goes down.



```
[Database Monitor]
type=monitor
module=mysqlmon
servers=server1,server2
script=mail_to_admin.sh
events=master_down,slave_down
```



When a master or a slave server goes down, the script is executed, a mail is sent and the administrator will be immediately notified of any possible problems.
This is just a simple example showing what you can do with MaxScale and monitor scripts.
