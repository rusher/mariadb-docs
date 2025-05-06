
# innodb_lock_waits and x$innodb_lock_waits Sys Schema Views


##### MariaDB starting with [10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106)
These [Sys Schema](../README.md) views were introduced in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106).


## Description


The `innodb_lock_waits` and `x$innodb_lock_waits` views summarize InnoDB locks that transactions are waiting upon, by default sorted in descending buffer size.


The `innodb_lock_waits` view is intended to be easier for human reading, while the `x$innodb_lock_waits` view provides the data in raw form, intended for tools that process the data.


They contain the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| wait_started | Time that lock wait began. |
| wait_age | TIME value for the length of the lock wait. |
| wait_age_secs | Seconds value for the length of the lock wait. |
| locked_table_schema | Schema containing the locked table. |
| locked_table_name | Name of the locked table. |
| locked_table_partition | Name of the locked partition, or NULL if none. |
| locked_table_subpartition | Name of the locked subpartition, or NULL if none. |
| locked_index | Name of the locked index. |
| locked_type | Type of the waiting lock. |
| waiting_trx_id | ID of the waiting transaction. |
| waiting_trx_started | Time that the waiting transaction started. |
| waiting_trx_age | TIME value for the length of time that the transaction has been waiting. |
| waiting_trx_rows_locked | Number of rows locked by the waiting transaction. |
| waiting_trx_rows_modified | Number of rows modified by the waiting transaction. |
| waiting_pid | Processlist ID of the waiting transaction. |
| waiting_query | Statement waiting for the lock. |
| waiting_lock_id | ID of the waiting lock. |
| waiting_lock_mode | Mode of the waiting lock. |
| blocking_trx_id | ID of the transaction blocking the waiting lock. |
| blocking_pid | Processlist ID of the blocking transaction. |
| blocking_query | Statement the blocking transaction is executing, or NULL if the session that issued the blocking query has become idle. |
| blocking_lock_id | ID of the lock blocking the waiting lock. |
| blocking_lock_mode | Mode of the lock blocking the waiting lock. |
| blocking_trx_started | Time the blocking transaction started. |
| blocking_trx_age | TIME value for how long the blocking transaction has been executing. |
| blocking_trx_rows_locked | Number of rows locked by the blocking transaction. |
| blocking_trx_rows_modified | Number of rows modified by the blocking transaction. |
| sql_kill_blocking_query | KILL statement that could be used to kill the blocking statement. |
| sql_kill_blocking_connection | KILL statement that could be used to kill the blocking statement session. |




CC BY-SA / Gnu FDL

