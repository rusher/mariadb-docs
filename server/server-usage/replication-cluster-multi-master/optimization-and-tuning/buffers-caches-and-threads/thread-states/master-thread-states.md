
# Master Thread States

This article documents thread states that are related to [replication](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) master threads. These correspond to the `STATE` values listed by the [SHOW PROCESSLIST](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-processlist.md) statement or in the [Information Schema PROCESSLIST Table](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) as well as the `PROCESSLIST_STATE` value listed in the [Performance Schema threads Table](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-threads-table.md).



| Value | Description |
| --- | --- |
| Value | Description |
| Finished reading one binlog; switching to next binlog | After completing one [binary log](../../../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md), the next is being opened for sending to the slave. |
| Master has sent all binlog to slave; waiting for binlog to be updated | All events have been read from the binary logs and sent to the slave. Now waiting for the binary log to be updated with new events. |
| Sending binlog event to slave | An event has been read from the [binary log](../../../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md), and is now being sent to the slave. |
| Waiting to finalize termination | State that only occurs very briefly while the thread is terminating. |


