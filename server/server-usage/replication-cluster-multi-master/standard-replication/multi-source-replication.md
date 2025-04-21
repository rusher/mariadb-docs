
# Multi-Source Replication

The terms *master* and *slave* have historically been used in replication, and MariaDB has begun the process of adding *primary* and *replica* synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.



Multi-source replication means that one server has many primaries from which it
replicates.


![multi_source_replication_small](../../../.gitbook/assets/multi-source-replication/+image/multi_source_replication_small.png "multi_source_replication_small")


## New Syntax


You specify which primary connection you want to work with by either specifying
the connection name in the command or setting
[default_master_connection](replication-and-binary-log-system-variables.md) to the connection you want to work with.


The connection name may include any characters and should be less than 64
characters. Connection names are compared without regard to case (case
insensitive). You should preferably keep the connection name short as it will
be used as a suffix for relay logs and primary info index files.


The new syntax introduced to handle many connections:


* `[CHANGE MASTER ['connection_name'] TO ...](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md)`. This creates or modifies a connection to a primary.
* `FLUSH RELAY LOGS ['connection_name']`
* `[MASTER_POS_WAIT(....,['connection_name'])](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/miscellaneous-functions/master_pos_wait.md)`
* `[RESET SLAVE ['connection_name'] [ALL](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/reset-replica.md)]`. This is used to reset a replica's replication position or to remove a replica permanently.
* `[SHOW RELAYLOG ['connection_name'] EVENTS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-relaylog-events.md)`
* `[SHOW SLAVE ['connection_name'] STATUS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-replica-status.md)`
* `[SHOW ALL SLAVES STATUS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-replica-status.md)`
* `[START SLAVE ['connection_name'](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/start-replica.md)...]]`
* `[START ALL SLAVES ...](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/start-replica.md)`
* `[STOP SLAVE ['connection_name'] ...](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/stop-replica.md)`
* `[STOP ALL SLAVES ...](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/stop-replica.md)`


The original old-style connection is an empty string `''`.
You don't have to use this connection if you don't want to.


You create new primary connections with [CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md).
You delete the connection permanently with [RESET SLAVE 'connection_name' ALL](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/reset-replica.md).


## Replication Variables for Multi-Source


The new replication variable [default_master_connection](replication-and-binary-log-system-variables.md)
specifies which connection will be used for commands and variables if you don't
specify a connection. By default this is `''` (the default
connection name).


The following replication variables are local for the connection. (In other
words, they show the value for the
`@@default_master_connection` connection). We are working on
making all the important ones local for the connection.



| Type | Name | Description |
| --- | --- | --- |
| Type | Name | Description |
| Variable | [max_relay_log_size](replication-and-binary-log-system-variables.md) | Max size of relay log. Is set at startup to max_binlog_size if 0 |
| Variable | [replicate_do_db](replication-and-binary-log-system-variables.md) | Tell the replica to restrict replication to updates of tables whose names appear in the comma-separated list. For statement-based replication, only the default database (that is, the one selected by USE) is considered, not any explicitly mentioned tables in the query. For row-based replication, the actual names of table(s) being updated are checked. |
| Variable | [replicate_do_table](replication-and-binary-log-system-variables.md) | Tells the replica to restrict replication to tables in the comma-separated list |
| Variable | [replicate_ignore_db](replication-and-binary-log-system-variables.md) | Tell the replica to restrict replication to updates of tables whose names do not appear in the comma-separated list. For statement-based replication, only the default database (that is, the one selected by USE) is considered, not any explicitly mentioned tables in the query. For row-based replication, the actual names of table(s) being updated are checked. |
| Variable | [replicate_ignore_table](replication-and-binary-log-system-variables.md) | Tells the replica thread to not replicate any statement that updates the specified table, even if any other tables might be updated by the same statement. |
| Variable | [replicate_rewrite_db](replication-and-binary-log-system-variables.md#replicate_rewrite_db) | From [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-11-series/what-is-mariadb-1011). Allows one to configure a replica to rewrite database names. It uses the format primary_database->replica_database. If a replica encounters a binary log event in which the default database (i.e. the one selected by the USE statement) is primary_database, then the replica will apply the event in replica_database instead. |
| Variable | [replicate_wild_do_table](replication-and-binary-log-system-variables.md) | Tells the replica thread to restrict replication to statements where any of the updated tables match the specified database and table name patterns. |
| Variable | [replicate_wild_ignore_table](replication-and-binary-log-system-variables.md) | Tells the replica thread to not replicate to the tables that match the given wildcard pattern. |
| Status | [Slave_heartbeat_period](replication-and-binary-log-status-variables.md#slave_heartbeat_period) | How often to request a heartbeat packet from the primary (in seconds). |
| Status | [Slave_received_heartbeats](replication-and-binary-log-status-variables.md#slave_received_heartbeats) | How many heartbeats we have got from the primary. |
| Status | [Slave_running](replication-and-binary-log-status-variables.md#slave_running) | Shows if the replica is running. YES means that the sql thread and the IO thread are active. No means either one is not running. '' means that @@default_master_connection doesn't exist. |
| Variable | [Sql_slave_skip_counter](replication-and-binary-log-system-variables.md) | How many entries in the replication log that should be skipped (mainly used in case of errors in the log). |



You can access all of the above variables with either
`SESSION` or `GLOBAL`.


Note that in contrast to MySQL, all variables always show the correct active
value!


Example:


```
set @@default_master_connection='';
show status like 'Slave_running';
set @@default_master_connection='other_connection';
show status like 'Slave_running';
```

If `@@default_master_connection` contains a non existing name,
you will get a warning.


All other primary-related variables are global and affect either only the ''
connections or all connections. For example,
[Slave_retried_transactions](replication-and-binary-log-status-variables.md#slave_retried_transactions) now shows the total number of retried transactions over all replicas.


If you need to set [gtid_slave_pos](gtid.md) you need to set this for all primaries at the same time.


New status variables:



| Name | Description |
| --- | --- |
| Name | Description |
| [Com_start_all_slaves](replication-and-binary-log-status-variables.md) | Number of executed START ALL SLAVES commands. |
| [Com_start_slave](replication-and-binary-log-status-variables.md) | Number of executed START SLAVE commands. This replaces Com_slave_start. |
| [Com_stop_slave](replication-and-binary-log-status-variables.md) | Number of executed STOP SLAVE commands. This replaces Com_slave_stop. |
| [Com_stop_all_slaves](replication-and-binary-log-status-variables.md) | Number of executed STOP ALL SLAVES commands. |



`[SHOW ALL SLAVES STATUS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-replica-status.md)` has the following new columns:



| Name | Description |
| --- | --- |
| Name | Description |
| Connection_name | Name of the primary connection. This is the first variable. |
| Slave_SQL_State | State of SQL thread. |
| Retried_transactions | Number of retried transactions for this connection. |
| Max_relay_log_size | Max relay log size for this connection. |
| Executed_log_entries | How many log entries the replica has executed. |
| Slave_received_heartbeats | How many heartbeats we have got from the primary. |
| Slave_heartbeat_period | How often to request a heartbeat packet from the primary (in seconds). |



## New Files


The basic principle of the new files used by multi source replication is that
they have the same name as the original relay log files suffixed with
`connection_name` before the extension. The main exception is
the file that holds all connection is named as the normal
`master-info-file` with a `multi-` prefix.


When you are using multi source, the following new files are created:



| Name | Description |
| --- | --- |
| Name | Description |
| multi-master-info-file | The master-info-file (normally master.info) with a multi- prefix. This contains all primary connections in use. |
| master-info-file-connection_name.extension | Contains the current primary position for what's applied to in the replica. Extension is normally .info |
| relay-log-connection_name.xxxxx | The relay-log name with a connection_name suffix. The xxxxx is the relay log number. This contains the replication data read from the primary. |
| relay-log-index-connection_name.extension | Contains the name of the active relay-log-connection_name.xxxxx files. Extension is normally .index |
| relay-log-info-file-connection_name.extension | Contains the current primary position for the relay log. Extension is normally .info |



When creating the file, the connection name is converted to lower case and all
special characters in the connection name are converted, the same way as MySQL
table names are converted. This is done to make the file name portable across
different systems.


Hint:


Instead of specifying names for `mysqld` with [--relay-log](replication-and-binary-log-system-variables.md#relay_log), [--relay-log-index](replication-and-binary-log-system-variables.md#relay_log_index), [--general-log-file](../optimization-and-tuning/system-variables/server-system-variables.md#general_log_file), [--slow-query-log-file](../optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log_file),
[--log-bin](replication-and-binary-log-system-variables.md#log_bin) and [--log-bin-index](replication-and-binary-log-system-variables.md#log_bin_index), you can just
specify [--log-basename](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) and all the other variables are set
with this as a prefix.


## Other Things


* All error messages from a replica with a connection name, that are written to the error log, are prefixed with `Master 'connection_name':`. This makes it easy to see from where an error originated.
* Errors `ER_MASTER_INFO` and `WARN_NO_MASTER_INFO` now includes connection_name.
* There is no conflict resolution. The assumption is that there are no conflicts in data between the different primaries.
* All executed commands are stored in the normal binary log (nothing new here).
* If the server variable `log_warnings` > 1 then you will get some information in the log about how the multi-master-info file is updated (mainly for debugging).
* The output of [SHOW ALL SLAVES STATUS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-replica-status.md) has one more column than `SHOW SLAVE STATUS`, since it includes the `connection_name` column.
* `[RESET SLAVE](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/reset-replica.md)` now deletes all relay-log files.


## replicate-... Variables


* One can set the values for the `replicate-...` variables from the command line or in `my.cnf` for a given connection by prefixing the variable with the connection name.
* If one doesn't use any connection name prefix for a `replicate..` variable, then the value will be used as the default value for all connections that don't have a value set for this variable.


Example:


```
mysqld --main_connection.replicate_do_db=main_database --replicate_do_db=other_database
```

The have sets the `replicate_do_db` variable to `main_database` for the connection named `main_connection`. All other connections will use the value `other_database`.


One can also use this syntax to set `replicate-rewrite-db` for a given connection.


## Typical Use Cases


* You are partitioning your data over many primaries and would like to get it all together on one machine to do analytical queries on all data.
* You have many databases spread over many MariaDB/MySQL servers and would like to have all of them on one machine as an extra backup.
* In a Galera cluster the default replication filter rules like `replicate-do-db` do not apply to replication connections, but also to Galera write set applier threads. By using a named multi-primary replication connection instead, even when replicating from just one primary into the cluster, the primary-replica replication rules can be kept separate from the Galera intra-node replication traffic.


## Limitations


* Each active connection will create 2 threads (as is normal for MariaDB replication).
* You should ensure that all primaries have different `server-id`'s. If you don't do this, you will get into trouble if you try to replicate from the multi-source replica back to your primaries.
* One can change [max_relay_log_size](replication-and-binary-log-system-variables.md) for any active connection, but new connections will always use the server startup value for `max_relay_log_size`, which can't be changed at runtime.
* Option [innodb-recovery-update-relay-log](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_recovery_update_relay_log) (xtradb feature to store and restore relay log position for replicas) only works for the default connection ''. As this option is not really safe and can easily cause loss of data if you use storage engines other than InnoDB, we don't recommend this option be used.
* [slave_net_timeout](replication-and-binary-log-system-variables.md) affects all connections. We don't check anymore if it's less than [Slave_heartbeat_period](replication-and-binary-log-status-variables.md), as this doesn't make sense in a multi-source setup.


## Incompatibilities with MariaDB/MySQL 5.5


* [max_relay_log_size](replication-and-binary-log-system-variables.md) is now (almost) a normal variable and not automatically changed if [max_binlog_size](replication-and-binary-log-system-variables.md) is changed. To keep things compatible with old config files, we set it to `max_binlog_size` at startup if its value is 0.
* You can now access replication variables that depend on the active connection with either `GLOBAL` or `SESSION`.
* We only write information about relay log positions for recovery if [innodb-recovery-update-relay-log](../../../reference/storage-engines/innodb/innodb-system-variables.md) is set.
* [Slave_retried_transactions](replication-and-binary-log-status-variables.md#slave_retried_transactions) now shows the total count of retried transactions over all replicas.
* The status variable `Com_slave_start` is replaced with [Com_start_slave](replication-and-binary-log-status-variables.md#com_start_slave).
* The status variable `Com_slave_stop` is replaced with [Com_stop_slave](replication-and-binary-log-status-variables.md#com_stop_slave).
* `FLUSH RELAY LOGS` are not replicated anymore. This is not safe as connection names may be different on the replica.


## See Also


* [Multi-master ring replication](multi-master-ring-replication.md)
* Using multi-source with [global transaction id](gtid.md)
* The work in MariaDB is based on the project description at [MDEV-253](https://jira.mariadb.org/browse/MDEV-253).
* The original code base comes from [Taobao, developed by Peng Lixun](https://mysql.taobao.org/index.php/Patch_source_code#Multi-master_replication). A big thanks to them for this important feature!

