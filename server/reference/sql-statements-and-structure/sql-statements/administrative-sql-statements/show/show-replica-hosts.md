
# SHOW REPLICA HOSTS


## Syntax


```
SHOW SLAVE HOSTS
SHOW REPLICA HOSTS -- from MariaDB 10.5.1
```

## Description


This command is run on the primary and displays a list of replicas that are currently registered with it. The output looks like this:


```
SHOW SLAVE HOSTS;
+------------+-----------+------+-----------+
| Server_id  | Host      | Port | Master_id |
+------------+-----------+------+-----------+
|  192168010 | iconnect2 | 3306 | 192168011 |
| 1921680101 | athena    | 3306 | 192168011 |
+------------+-----------+------+-----------+
```

* `Server_id`: The unique server ID of the replica server, as configured in the server's option file, or on the command line with [--server-id=value](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md).
* `Host`: The host name of the replica server, as configured in the server's option file, or on the command line with `--report-host=host_name` (note that this can differ from the machine name as configured in the operating system). Starting in [MariaDB 10.5.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md), if a replica doesn't configure `--report-host` explicitly, the value for the `Host` column is automatically extracted using the network connection's host name or IP address. Prior to 10.5, the Host value is left blank if a replica's `--report-host` parameter is not configured.
* `Port`: The port the replica server is listening on.
* `Master_id`: The unique server ID of the primary server that the replica server is replicating from.


Some MariaDB and MySQL versions report another variable, [rpl_recovery_rank](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#rpl_recovery_rank). This
variable was never used, and was eventually removed in [MariaDB 10.1.2](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-2-release-notes.md) .


Requires the [REPLICATION MASTER ADMIN](../../account-management-sql-commands/grant.md#replication-master-admin) privilege (>= [MariaDB 10.5.2](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)) or the [REPLICATION SLAVE](../../account-management-sql-commands/grant.md#replication-slave) privilege (<= [MariaDB 10.5.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md)).


#### SHOW REPLICA HOSTS



##### MariaDB starting with [10.5.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md)
`SHOW REPLICA HOSTS` is an alias for `SHOW SLAVE HOSTS` from [MariaDB 10.5.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md). 


## See Also


* [MariaDB replication](../../../../../server-usage/replication-cluster-multi-master/standard-replication/README.md)
* [Replication threads](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md)
* [SHOW PROCESSLIST](show-processlist.md). In `[SHOW PROCESSLIST](show-processlist.md)` output, replica threads are identified by `Binlog Dump`

