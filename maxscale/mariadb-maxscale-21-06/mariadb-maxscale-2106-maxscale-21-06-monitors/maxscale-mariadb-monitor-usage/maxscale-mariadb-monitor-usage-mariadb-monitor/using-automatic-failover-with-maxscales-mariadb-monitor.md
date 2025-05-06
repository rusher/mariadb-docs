
# Using Automatic Failover with MaxScale's MariaDB Monitor


# Overview


MaxScale's [MariaDB Monitor (mariadbmon)](../../../../mariadb-maxscale-23-02/mariadb-maxscale-23-02-monitors/mariadb-maxscale-2302-mariadb-monitor.md) monitors [MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/) deployments.


When the primary server fails, MariaDB Monitor can promote a replica server to be the new primary server automatically.


# How MariaDB Monitor uses Cooperative Locks


When automatic failover is enabled for MariaDB Monitor, it does the following:


1. It selects the replica server with the latest GTID position to be the new primary server.


2. If the new primary server has unprocessed relay logs, then it cancels and restarts the failover process after a short wait.


3. It prepares the new primary server:


* It stops its replica threads by executing [STOP REPLICA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/stop-replica) and [RESET REPLICA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/reset-replica).
* It configures it to allow writes by setting [read_only](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables#read_only) to OFF.
* If the handle_events parameter is true, then it enable events that were previously enabled on the old primary server.
* If the promotion_sql_file parameter is set, then the script referred to by the parameter is executed.
* If there is an external master, then it configures that replication by executing [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to) and [START REPLICA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/start-replica).


4. It redirects all replica servers to replicate to the new primary server:


* It stops its replica threads by executing [STOP REPLICA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/stop-replica) and [RESET REPLICA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/reset-replica).
* It configures that replication by executing [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to) and [START REPLICA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/start-replica).


5. It checks that all slaves are replicating properly by executing [SHOW REPLICA STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-replica-status).


# Configuring Automatic Failover


1. Configure automatic failover by configuring several parameter for the MariaDB Monitor in `maxscale.cnf`.



| Parameter | Description |
| --- | --- |
| Parameter | Description |
| failcount | • This parameter defines the number of monitoring checks that must pass before a primary server is considered to be down. • The default value is 5. • The total wait time can be calculated as: (monitor_interval + backend_connect_timeout) * failcount |
| auto_failover | • When this parameter is enabled, the monitor will automatically failover to a new primary server if the primary server fails. • When this parameter is disabled, the monitor will not automatic failover to a new primary server if the primary server fails, so failover must be performed manually. • This parameter is disabled by default. |
| auto_rejoin | • When this parameter is enabled, the monitor will attempt to automatically configure new replica servers to replicate from the primary server when they come online. • When this parameter is disabled, the monitor will not attempt to automatically configure new replica servers to replicate from the primary server when they come online, so they must be configured manually. • TThis parameter is disabled by default. |
| switchover_on_low_disk_space | • When this parameter is enabled, the monitor will automatically switchover to a new primary server if the primary server is low on disk space. • When this parameter is disabled, the monitor will automatically switchover to a new primary server if the primary server is low on disk space, so switchover must be performed manually. • This parameter requires the disk_space_threshold parameter to be set for the server or the monitor. • This parameter requires the disk_space_check_interval parameter to be set for the monitor. • This parameter is disabled by default. |
| enforce_simple_topology | • When this parameter is enabled, the monitor assumes that the topology of the cluster only consists of a single primary server, which has multiple replica servers. • When this parameter is disabled, the monitor does not make assumptions about the topology of the cluster. • This parameter implicitly sets the assume_unique_hostnames, auto_failover, and auto_rejoin parameters. |
| replication_user | • This parameter is used by the monitor to set the MASTER_USER option when executing the [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to) statement. • If this parameter is not set, then the monitor uses the monitor user. |
| replication_password | • This parameter is used by the monitor to set the MASTER_PASSWORD option when executing the [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to) statement. • If this parameter is not set, then the monitor uses the monitor user's password. |
| replication_master_ssl | • This parameter is used by the monitor to set the MASTER_SSL option when executing the [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to) statement. • If this parameter is not set, then the monitor does not enable TLS.t |
| failover_timeout | • This parameter defines the maximum amount of time allowed to perform a failover. • If failover times out, then a message is logged to the MaxScale log, and automatic failover is disabled. |
| switchover_timeout | • This parameter defines the maximum amount of time allowed to perform a switchover. • If switchover times out, then a message is logged to the MaxScale log, and automatic failover is disabled. |
| verify_master_failure | • When this parameter is enabled, if the monitor detects that the primary server failed, it will execute [SHOW REPLICA STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-replica-status) to verify that the replica servers have also detected the failure. • If a replica has received an event within master_failure_timeout duration, the primary is not considered down when deciding whether to failover, even if the monitor cannot connect to the primary. |
| master_failure_timeout | • This parameter defines the timeout for verify_master_failure. • The default value is 10 seconds. |
| servers_no_promotion | • This parameter defines a comma-separated list of servers that should not be chosen to be primary server. |
| promotion_sql_file | • This parameter defines an SQL script that should be executed on the new primary server during failover or switchover. |
| demotion_sql_file | • This parameter defines an SQL script that should be executed on the old primary server during failover or switchover when it is demoted to be a replica server. • The script is also executed when a server is automatically added to the cluster due to the auto_rejoin parameter. |
| handle_events | • When this parameter is enabled, the monitor enables events on the new primary server that were previously enabled on the old primary server. • The monitor also disables the events on the old primary server. |



For example:


```
[repl-cluster]
type                     = monitor
module                   = mariadbmon
...
auto_failover            = true
auto_rejoin              = true
replication_user         = repl
replication_password     = passwd
replication_master_ssl   = true
```

2. Restart the MaxScale instance.


```
$ sudo systemctl restart maxscale
```


Copyright © 2025 MariaDB

