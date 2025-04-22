
# Information Schema INNODB_METRICS Table

The [Information Schema](../../README.md) `INNODB_METRICS` table contains a list of useful InnoDB performance metrics. Each row in the table represents an instrumented counter that can be stopped, started and reset, and which can be grouped together by module.


The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


It has the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| NAME | Unique counter name. |
| SUBSYSTEM | InnoDB subsystem. See below for the matching module to use to enable/disable monitoring this subsytem with the [innodb_monitor_enable](../../../../../../../storage-engines/innodb/innodb-system-variables.md#innodb_monitor_enable) and [innodb_monitor_disable](../../../../../../../storage-engines/innodb/innodb-system-variables.md#innodb_monitor_disable) system variables. |
| COUNT | Count since being enabled. |
| MAX_COUNT | Maximum value since being enabled. |
| MIN_COUNT | Minimum value since being enabled. |
| AVG_COUNT | Average value since being enabled. |
| COUNT_RESET | Count since last being reset. |
| MAX_COUNT_RESET | Maximum value since last being reset. |
| MIN_COUNT_RESET | Minimum value since last being reset. |
| AVG_COUNT_RESET | Average value since last being reset. |
| TIME_ENABLED | Time last enabled. |
| TIME_DISABLED | Time last disabled |
| TIME_ELAPSED | Time since enabled |
| TIME_RESET | Time last reset. |
| ENABLED | 1 if enabled, 0 otherwise |
| TYPE | Item type; one of counter, value, status_counter, set_owner, set_member. |
| COMMENT | Counter description. |



Note: In [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104) and earlier the `ENABLED` column was called `STATUS`.


## Enabling and Disabling Counters


Most of the counters are disabled by default. To enable them, use the [innodb_monitor_enable](../../../../../../../storage-engines/innodb/innodb-system-variables.md#innodb_monitor_enable) system variable. You can either enable a variable by its name, for example:


```
SET GLOBAL innodb_monitor_enable = icp_match;
```

or enable a number of counters grouped by module. The `SUBSYSTEM` field indicates which counters are grouped together, but the following module names need to be used:



| Module Name | Subsytem Field |
| --- | --- |
| Module Name | Subsytem Field |
| module_metadata | metadata |
| module_lock | lock |
| module_buffer | buffer |
| module_buf_page | buffer_page_io |
| module_os | os |
| module_trx | transaction |
| module_purge | purge |
| module_compress | compression |
| module_file | file_system |
| module_index | index |
| module_adaptive_hash | adaptive_hash_index From [MariaDB 10.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/mariadb-1062-release-notes), if [innodb_adaptive_hash_index](../../../../../../../storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index) is disabled (the default), adaptive_hash_index will not be updated. |
| module_ibuf_system | change_buffer |
| module_srv | server |
| module_ddl | ddl |
| module_dml | dml |
| module_log | recovery |
| module_icp | icp |



There are four counters in the `icp` subsystem:


```
SELECT NAME, SUBSYSTEM FROM INNODB_METRICS WHERE SUBSYSTEM='icp';
+------------------+-----------+
| NAME             | SUBSYSTEM |
+------------------+-----------+
| icp_attempts     | icp       |
| icp_no_match     | icp       |
| icp_out_of_range | icp       |
| icp_match        | icp       |
+------------------+-----------+
```

To enable them all, use the associated module name from the table above, `module_icp`.


```
SET GLOBAL innodb_monitor_enable = module_icp;
```

The `%` wildcard, used to represent any number of characters, can also be used when naming counters, for example:


```
SET GLOBAL innodb_monitor_enable = 'buffer%'
```

To disable counters, use the [innodb_monitor_disable](../../../../../../../storage-engines/innodb/innodb-system-variables.md#innodb_monitor_disable) system variable, using the same naming rules as described above for enabling.


Counter status is not persistent, and will be reset when the server restarts. It is possible to use the options on the command line, or the `innodb_monitor_enable` option only in a configuration file.


## Resetting Counters


Counters can also be reset. Resetting sets all the `*_COUNT_RESET` values to zero, while leaving the `*_COUNT` values, which perform counts since the counter was enabled, untouched. Resetting is performed with the [innodb_monitor_reset](../../../../../../../storage-engines/innodb/innodb-system-variables.md#innodb_monitor_reset) (for individual counters) and [innodb_monitor_reset_all](../../../../../../../storage-engines/innodb/innodb-system-variables.md#innodb_monitor_reset_all) (for all counters) system variables.


## Simplifying from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106)



##### MariaDB starting with [10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106)
From [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106), the interface was simplified by removing the following:

* buffer_LRU_batches_flush
* buffer_LRU_batch_flush_pages
* buffer_LRU_batches_evict
* buffer_LRU_batch_evict_pages

and by making the following reflect the status variables:

* buffer_LRU_batch_flush_total_pages: [innodb_buffer_pool_pages_LRU_flushed](../../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_buffer_pool_pages_lru_flushed)
* buffer_LRU_batch_evict_total_pages: [innodb_buffer_pool_pages_LRU_freed](../../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_buffer_pool_pages_lru_freed)

The intention is to eventually remove the interface entirely (see [MDEV-15706](https://jira.mariadb.org/browse/MDEV-15706)).


## Examples


[MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108):


```
SELECT name,subsystem,type,comment FROM INFORMATION_SCHEMA.INNODB_METRICS\G
*************************** 1. row ***************************
     name: metadata_table_handles_opened
subsystem: metadata
     type: counter
  comment: Number of table handles opened
*************************** 2. row ***************************
     name: lock_deadlocks
subsystem: lock
     type: value
  comment: Number of deadlocks
*************************** 3. row ***************************
     name: lock_timeouts
subsystem: lock
     type: value
  comment: Number of lock timeouts
*************************** 4. row ***************************
     name: lock_rec_lock_waits
subsystem: lock
     type: counter
  comment: Number of times enqueued into record lock wait queue
*************************** 5. row ***************************
     name: lock_table_lock_waits
subsystem: lock
     type: counter
  comment: Number of times enqueued into table lock wait queue
*************************** 6. row ***************************
     name: lock_rec_lock_requests
subsystem: lock
     type: counter
  comment: Number of record locks requested
*************************** 7. row ***************************
     name: lock_rec_lock_created
subsystem: lock
     type: counter
  comment: Number of record locks created
*************************** 8. row ***************************
     name: lock_rec_lock_removed
subsystem: lock
     type: counter
  comment: Number of record locks removed from the lock queue
*************************** 9. row ***************************
     name: lock_rec_locks
subsystem: lock
     type: counter
  comment: Current number of record locks on tables
*************************** 10. row ***************************
     name: lock_table_lock_created
subsystem: lock
     type: counter
  comment: Number of table locks created

...

*************************** 207. row ***************************
     name: icp_attempts
subsystem: icp
     type: counter
  comment: Number of attempts for index push-down condition checks
*************************** 208. row ***************************
     name: icp_no_match
subsystem: icp
     type: counter
  comment: Index push-down condition does not match
*************************** 209. row ***************************
     name: icp_out_of_range
subsystem: icp
     type: counter
  comment: Index push-down condition out of range
*************************** 210. row ***************************
     name: icp_match
subsystem: icp
     type: counter
  comment: Index push-down condition matches
```
