
# FLUSH

## Syntax


```
FLUSH [NO_WRITE_TO_BINLOG | LOCAL]
    flush_option [, flush_option] ...
```

or when flushing tables:


```
FLUSH [NO_WRITE_TO_BINLOG | LOCAL] TABLES [table_list]  [table_flush_option]
```

where `table_list` is a list of tables separated by `,` (comma).


## Description


The `FLUSH` statement clears or reloads various internal caches used by
MariaDB. To execute `FLUSH`, you must have the `RELOAD`
privilege. See [GRANT](../../account-management-sql-commands/grant.md).


The `RESET` statement is similar to `FLUSH`. See
[RESET](../replication-statements/reset-master.md).


You cannot issue a FLUSH statement from within a [stored function](../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) or a [trigger](../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/triggers-and-implicit-locks.md). Doing so within a stored procedure is permitted, as long as it is not called by a stored function or trigger. See [Stored Routine Limitations](../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-routine-limitations.md), [Stored Function Limitations](../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/stored-function-limitations.md) and [Trigger Limitations](../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/trigger-limitations.md).


If a listed table is a view, an error like the following will be produced:


```
ERROR 1347 (HY000): 'test.v' is not BASE TABLE
```

By default, `FLUSH` statements are written to the [binary log](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) and will be [replicated](../replication-statements/README.md). The `NO_WRITE_TO_BINLOG` keyword (`LOCAL` is an alias) will ensure the statement is not written to the binary log.


The different flush options are:



| Option | Description |
| --- | --- |
| Option | Description |
| CHANGED_PAGE_BITMAPS | [XtraDB](../../../../storage-engines/innodb/innodb-unmaintained/about-xtradb.md) only. Internal command used for backup purposes. See the [Information Schema CHANGED_PAGE_BITMAPS Table](../system-tables/information-schema/information-schema-tables/information-schema-xtradb-tables/information-schema-changed_page_bitmaps-table.md). |
| CLIENT_STATISTICS | Reset client statistics (see [SHOW CLIENT_STATISTICS](../show/show-client-statistics.md)). |
| DES_KEY_FILE | Reloads the DES key file (Specified with the [--des-key-file startup option](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md)). |
| HOSTS | Flush the hostname cache (used for converting ip to host names and for unblocking blocked hosts. See [max_connect_errors](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_connect_errors) and [performance_schema.host_cache](../system-tables/performance-schema/performance-schema-tables/performance-schema-host_cache-table.md) |
| INDEX_STATISTICS | Reset index statistics (see [SHOW INDEX_STATISTICS](../show/show-index-statistics.md)). |
| [ERROR | ENGINE | GENERAL | SLOW | RELAY] LOGS | Close and reopen the specified log type, or all log types if none are specified. FLUSH RELAY LOGS [connection-name] can be used to flush the relay logs for a specific connection. Only one connection can be specified per FLUSH command. See [Multi-source replication](../../../../../server-usage/replication-cluster-multi-master/standard-replication/multi-source-replication.md). FLUSH ENGINE LOGS will delete all unneeded [Aria](../../../../storage-engines/s3-storage-engine/aria_s3_copy.md) redo logs. FLUSH BINARY LOGS DELETE_DOMAIN_ID=(list-of-domains) can be used to discard obsolete [GTID](../../../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) domains from the server's [binary log](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) state. In order for this to be successful, no event group from the listed [GTID](../../../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) domains can be present in existing [binary log](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) files. If some still exist, then they must be purged prior to executing this command. If the command completes successfully, then it also rotates the [binary log](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md). |
| BINARY LOGS | FLUSH BINARY LOGS rotates the current [binary log](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md). |
| BINARY LOGS DELETE_DOMAIN_ID=(list-of-domains) | FLUSH BINARY LOGS DELETE_DOMAIN_ID can be used to discard obsolete [GTID](../../../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) domains from the server's [binary log](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) state. In order for this to be successful, no event group from the listed [GTID](../../../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) domains can be present in existing [binary log](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) files. If some still exist, then they must be purged prior to executing this command. If the command completes successfully, then it also rotates the [binary log](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md). |
| MASTER | Deprecated option, use [RESET MASTER](../replication-statements/reset-master.md) instead. |
| PRIVILEGES | Reload all privileges from the privilege tables in the mysql database. If the server is started with --skip-grant-table option, this will activate the privilege tables again. |
| [QUERY CACHE](flush-query-cache.md) | Defragment the [query cache](../../../../plugins/other-plugins/query-cache-information-plugin.md) to better utilize its memory. If you want to reset the query cache, you can do it with [RESET QUERY CACHE](../replication-statements/reset-master.md). |
| QUERY_RESPONSE_TIME | See the [QUERY_RESPONSE_TIME](../../../../plugins/other-plugins/query-response-time-plugin.md) plugin. |
| QUERY_RESPONSE_TIME_READ | See the [QUERY_RESPONSE_TIME](../../../../plugins/other-plugins/query-response-time-plugin.md) plugin. From [MariaDB 11.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md). |
| QUERY_RESPONSE_TIME_READ_WRITE | See the [QUERY_RESPONSE_TIME](../../../../plugins/other-plugins/query-response-time-plugin.md) plugin. From [MariaDB 11.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md). |
| QUERY_RESPONSE_TIME_WRITE | See the [QUERY_RESPONSE_TIME](../../../../plugins/other-plugins/query-response-time-plugin.md) plugin. From [MariaDB 11.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md). |
| SLAVE | Deprecated option, use [RESET REPLICA or RESET SLAVE](../replication-statements/reset-replica.md) instead. |
| SSL | Used to dynamically reinitialize the server's [TLS](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/README.md) context by reloading the files defined by several [TLS system variables](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md). See [FLUSH SSL](#flush-ssl) for more information. |
| [ GLOBAL | SESSION ] STATUS | Resets all [server status variables](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md) that can be reset to 0. Not all global status variables support this, so not all global values are reset. From [MariaDB 11.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md), GLOBAL or SESSION can be specified. See [FLUSH STATUS](#flush-status) for more information. |
| TABLE[S] | Close tables given as options or all open tables if no table list was used. Using without any table list will only close tables not in use, and tables not locked by the FLUSH TABLES connection. If there are no locked tables, FLUSH TABLES will be instant and will not cause any waits, as it no longer waits for tables in use. When a table list is provided, the server will wait for the end of any transactions that are using the tables. Previously, FLUSH TABLES only waited for the statements to complete. |
| [TABLE[S] ... FOR EXPORT](flush-tables-for-export.md) | For InnoDB tables, flushes table changes to disk to permit binary table copies while the server is running. See [FLUSH TABLES ... FOR EXPORT](flush-tables-for-export.md) for more. |
| TABLE[S] WITH READ LOCK | Closes all open tables. New tables are only allowed to be opened with read locks until an [UNLOCK TABLES](../../transactions/transactions-unlock-tables.md) is given. |
| TABLE[S] WITH READ LOCK AND DISABLE CHECKPOINT | As TABLES WITH READ LOCK but also disable all checkpoint writes by transactional table engines. This is useful when doing a disk snapshot of all tables. |
| TABLE_STATISTICS | Reset table statistics (see [SHOW TABLE_STATISTICS](../show/show-table-statistics.md)). |
| USER_RESOURCES | Resets all per hour [user resources](../../account-management-sql-commands/grant.md#setting-per-account-resources-limits). This enables clients that have exhausted their resources to connect again. |
| USER_STATISTICS | Reset user statistics (see [SHOW USER_STATISTICS](../show/show-user-statistics.md)). |
| USER_VARIABLES | Reset user variables (see [User-defined variables](../../../sql-language-structure/user-defined-variables.md)). |



You can also use the [mariadb-admin](../../../../../clients-and-utilities/mariadb-admin.md) client to flush things. Use `mariadb-admin --help` to examine what flush commands it supports.


## `FLUSH RELAY LOGS`


```
FLUSH RELAY LOGS 'connection_name';
```

### Compatibility with MySQL



##### MariaDB starting with [10.7.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1070-release-notes.md)
The `FOR CHANNEL` keyword was added for MySQL compatibility. This is identical to
using the channel_name directly after the `FLUSH command`.
For example, one can now use:

```
FLUSH RELAY LOGS FOR CHANNEL 'connection_name';
```


## FLUSH STATUS


[Server status variables](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md) can be reset by executing the following:


```
FLUSH STATUS;
```

This requires the [RELOAD](../../account-management-sql-commands/grant.md#reload) privilege


Until [MariaDB 11.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md), the variables flushed are mainly session, but also some global. Not all session (or global) variables are flushed - the decision was made per variable.



##### MariaDB starting with [11.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md)
From [MariaDB 11.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md) it is possible to specify FLUSH GLOBAL or FLUSH SESSION. Flushing of global status variables has been moved to `FLUSH GLOBAL STATUS` (in [MariaDB 11.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md), this flushes only the global variables previously flushed by `FLUSH STATUS`. In a future release, it is intended for this to reset all global summary variables.) `FLUSH SESSION STATUS` is a synonym for `FLUSH STATUS`. 
One can use `old-mode=OLD_FLUSH_STATUS` to restore the old behavior of the `FLUSH STATUS`.


### Global Status Variables that Support `FLUSH STATUS`


Not all global status variables support being reset by `FLUSH STATUS`. Currently, the following is an incomplete list of status variables are reset by `FLUSH GLOBAL STATUS` in 11.5 or `FLUSH STATUS` in earlier versions:


* [Aborted_clients](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#aborted_clients)
* [Aborted_connects](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#aborted_connects)
* [Binlog_cache_disk_use](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-status-variables.md#binlog_cache_disk_use)
* [Binlog_cache_use](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-status-variables.md#binlog_cache_use)
* [Binlog_stmt_cache_disk_use](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-status-variables.md#binlog_stmt_cache_disk_use)
* [Binlog_stmt_cache_use](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-status-variables.md#binlog_stmt_cache_use)
* [Connection_errors_accept](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#connection_errors_accept)
* [Connection_errors_internal](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#connection_errors_internal)
* [Connection_errors_max_connections](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#connection_errors_max_connections)
* [Connection_errors_peer_address](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#connection_errors_peer_address)
* [Connection_errors_select](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#connection_errors_select)
* [Connection_errors_tcpwrap](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#connection_errors_tcpwrap)
* [Created_tmp_files](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#created_tmp_files)
* [Delayed_errors](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#delayed_errors)
* [Delayed_writes](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#delayed_writes)
* [Feature_check_constraint](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#feature_check_constraint)
* [Feature_delay_key_write](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#feature_delay_key_write)
* [Max_used_connection_time](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#max_used_connection_time)
* [Max_used_connections](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#max_used_connections)
* [Opened_plugin_libraries](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#opened_plugin_libraries)
* [Performance_schema_accounts_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_accounts_lost)
* [Performance_schema_cond_instances_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_cond_instances_lost)
* [Performance_schema_digest_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_digest_lost)
* [Performance_schema_file_handles_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_file_handles_lost)
* [Performance_schema_file_instances_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_file_instances_lost)
* [Performance_schema_hosts_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_hosts_lost)
* [Performance_schema_locker_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_locker_lost)
* [Performance_schema_mutex_instances_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_mutex_instances_lost)
* [Performance_schema_rwlock_instances_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_rwlock_instances_lost)
* [Performance_schema_session_connect_attrs_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_session_connect_attrs_lost)
* [Performance_schema_socket_instances_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_socket_instances_lost)
* [Performance_schema_stage_classes_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_stage_classes_lost)
* [Performance_schema_statement_classes_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_statement_classes_lost)
* [Performance_schema_table_handles_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_table_handles_lost)
* [Performance_schema_table_instances_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_table_instances_lost)
* [Performance_schema_thread_instances_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_thread_instances_lost)
* [Performance_schema_users_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_users_lost)
* [Qcache_hits](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#qcache_hits)
* [Qcache_inserts](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#qcache_inserts)
* [Qcache_lowmem_prunes](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#qcache_lowmem_prunes)
* [Qcache_not_cached](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#qcache_not_cached)
* [Rpl_semi_sync_master_no_times](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_no_times)
* [Rpl_semi_sync_master_no_tx](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_no_tx)
* [Rpl_semi_sync_master_timefunc_failures](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_timefunc_failures)
* [Rpl_semi_sync_master_wait_pos_backtraverse](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_wait_pos_backtraverse)
* [Rpl_semi_sync_master_yes_tx](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_yes_tx)
* [Rpl_transactions_multi_engine](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-status-variables.md#rpl_transactions_multi_engine)
* [Server_audit_writes_failed](../../../../plugins/mariadb-audit-plugin/mariadb-audit-plugin-status-variables.md#server_audit_writes_failed)
* [Slave_retried_transactions](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-status-variables.md#slave_retried_transactions)
* [Slow_launch_threads](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#slow_launch_threads)
* [Ssl_accept_renegotiates](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_accept_renegotiates)
* [Ssl_accepts](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_accepts)
* [Ssl_callback_cache_hits](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_callback_cache_hits)
* [Ssl_client_connects](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_client_connects)
* [Ssl_connect_renegotiates](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_connect_renegotiates)
* [Ssl_ctx_verify_depth](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_ctx_verify_depth)
* [Ssl_ctx_verify_mode](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_ctx_verify_mode)
* [Ssl_finished_accepts](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_finished_accepts)
* [Ssl_finished_connects](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_finished_connects)
* [Ssl_session_cache_hits](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_session_cache_hits)
* [Ssl_session_cache_misses](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_session_cache_misses)
* [Ssl_session_cache_overflows](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_session_cache_overflows)
* [Ssl_session_cache_size](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_session_cache_size)
* [Ssl_session_cache_timeouts](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_session_cache_timeouts)
* [Ssl_sessions_reused](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_sessions_reused)
* [Ssl_used_session_cache_entries](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_used_session_cache_entries)
* [Subquery_cache_hit](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#subquery_cache_hit)
* [Subquery_cache_miss](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#subquery_cache_miss)
* [Table_locks_immediate](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#table_locks_immediate)
* [Table_locks_waited](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#table_locks_waited)
* [Tc_log_max_pages_used](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#tc_log_max_pages_used)
* [Tc_log_page_waits](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#tc_log_page_waits)
* [Transactions_gtid_foreign_engine](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-status-variables.md#transactions_gtid_foreign_engine)
* [Transactions_multi_engine](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-status-variables.md#transactions_multi_engine)


## FLUSH TABLES



##### MariaDB starting with [10.11.12](/en/mariadb-101112-release-notes/)
Prior to [MariaDB 10.11.12](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-12-release-notes.md), [MariaDB 11.4.6](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-6-release-notes.md) and [MariaDB 11.8.2](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-8-series/mariadb-11-8-2-release-notes.md), FLUSH TABLES caused [InnoDB statistics](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md) to be reloaded or recalculated. From [MariaDB 10.11.12](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-12-release-notes.md), [MariaDB 11.4.6](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-6-release-notes.md) and [MariaDB 11.8.2](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-8-series/mariadb-11-8-2-release-notes.md), this is no longer the case. [RENAME TABLE](../../data-definition/rename-table.md) is unaffected, and will continue to trigger a reload of the statistics.


### Purpose of FLUSH TABLES


The purpose of `FLUSH TABLES` is to clean up the open table cache and
table definition cache of tables that are not in use. This frees up memory
and file descriptors. Normally this is not needed as the caches works
on a first-in, first-out basis, but can be useful if the server seems to use too
much memory for some reason.


### Purpose of FLUSH TABLES WITH READ LOCK


`FLUSH TABLES WITH READ LOCK` is useful if you want to take a backup
of some tables. When `FLUSH TABLES WITH READ LOCK` returns, all
write access to tables is blocked and all tables are marked as
'properly closed' on disk. The tables can still be used for read
operations.


### Purpose of FLUSH TABLES table_list


`FLUSH TABLES` table_list is useful if you want to copy a table
object or files to or from the server. This command puts a lock that
stops new users of the table and will wait until everyone has stopped
using the table. The table is then removed from the table definition
and table cache.


Note that it's up to the user to ensure that no one is accessing the
table between `FLUSH TABLES` and the table is copied to or from the
server. This can be secured by using [LOCK TABLES](../../transactions/lock-tables.md).


If there are any tables locked by the connection that is using `FLUSH TABLES` all the locked tables will be closed as part of the flush and
reopened and relocked before `FLUSH TABLES` returns. This allows one
to copy the table after `FLUSH TABLES` returns without having any
writes on the table. For now this works works with most tables,
except InnoDB as InnoDB may do background purges on the table even
while it's write locked.


### Purpose of FLUSH TABLES table_list WITH READ LOCK


`FLUSH TABLES table_list WITH READ LOCK` should work as `FLUSH TABLES WITH READ LOCK`, but only those tables that are listed will be
properly closed. However in practice this works exactly like `FLUSH TABLES WITH READ LOCK` as the `FLUSH` command has anyway to wait
for all WRITE operations to end because we are depending on a global
read lock for this code. In the future we should consider fixing this
to instead use meta data locks.


### Implementation of FLUSH TABLES


* Free memory and file descriptors not in use


### Implementation of FLUSH TABLES WITH READ LOCK


* Lock all tables read only for simple old style backup.
* All background writes are suspended and tables are marked as closed.
* No statement requiring table changes are allowed for any user until `UNLOCK TABLES`.


Instead of using `FLUSH TABLE WITH READ LOCK` one should in most cases instead use
[BACKUP STAGE BLOCK_COMMIT](../backup-commands/backup-stage.md).


### Implementation of FLUSH TABLES table_list


* Free memory and file descriptors for tables not in use from table list.
* Lock given tables as read only.
* Wait until all translations has ended that uses any of the given tables.
* Wait until all background writes are suspended and tables are marked as closed.


### Implementation of FLUSH TABLES table_list FOR EXPORT


* Free memory and file descriptors for tables not in use from table list
* Lock given tables as read.
* Wait until all background writes are suspended and tables are marked as closed.
* Check that all tables supports `FOR EXPORT`
* No changes to these tables allowed until `UNLOCK TABLES`


This is basically the same behavior as in old MariaDB version if one first lock the tables, then do
`FLUSH TABLES`. The tables will be copyable until `UNLOCK TABLES`.


## FLUSH SSL


The `FLUSH SSL` command can be used to dynamically reinitialize the server's [TLS](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/README.md) context. This is most useful if you need to replace a certificate that is about to expire without restarting the server.


This operation is performed by reloading the files defined by the following [TLS system variables](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md):


* [ssl_cert](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md#ssl_cert)
* [ssl_key](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md#ssl_key)
* [ssl_ca](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md#ssl_ca)
* [ssl_capath](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md#ssl_capath)
* [ssl_crl](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md#ssl_crl)
* [ssl_crlpath](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md#ssl_crlpath)


These [TLS system variables](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md) are not dynamic, so their values can **not** be changed without restarting the server.


If you want to dynamically reinitialize the server's [TLS](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/README.md) context, then you need to change the certificate and key files at the relevant paths defined by these [TLS system variables](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md), without actually changing the values of the variables. See [MDEV-19341](https://jira.mariadb.org/browse/MDEV-19341) for more information.


## Reducing Memory Usage


To flush some of the global caches that take up memory, you could execute the following command:


```
FLUSH LOCAL HOSTS,
   QUERY CACHE, 
   TABLE_STATISTICS, 
   INDEX_STATISTICS, 
   USER_STATISTICS;
```
