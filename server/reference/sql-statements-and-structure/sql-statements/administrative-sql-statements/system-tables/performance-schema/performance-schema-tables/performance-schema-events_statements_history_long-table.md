# Performance Schema events_statements_history_long Table

The `events_statements_history_long` table by default contains the ten thousand most recent completed statement events. This number can be adjusted by setting the [performance_schema_events_statements_history_long_size](../performance-schema-system-variables.md#performance_schema_events_statements_history_long_size) system variable when the server starts up.

The table structure is identical to the [events_statements_current](performance-schema-events_statements_current-table.md) table structure, and contains the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| THREAD_ID | Thread associated with the event. Together with EVENT_ID uniquely identifies the row. |
| EVENT_ID | Thread's current event number at the start of the event. Together with THREAD_ID uniquely identifies the row. |
| END_EVENT_ID | NULL when the event starts, set to the thread's current event number at the end of the event. |
| EVENT_NAME | Event instrument name and a NAME from the setup_instruments table |
| SOURCE | Name and line number of the source file containing the instrumented code that produced the event. |
| TIMER_START | Value in picoseconds when the event timing started or NULL if timing is not collected. Relative to the server start, not to the epoch, so cannot directly be converted to a timestamp. |
| TIMER_END | Value in picoseconds when the event timing ended, or NULL if timing is not collected. Relative to the server start, not to the epoch, so cannot directly be converted to a timestamp. |
| TIMER_WAIT | Value in picoseconds of the event's duration or NULL if timing is not collected. |
| LOCK_TIME | Time in picoseconds spent waiting for locks. The time is calculated in microseconds but stored in picoseconds for compatibility with other timings. |
| SQL_TEXT | The SQL statement, or NULL if the command is not associated with an SQL statement. |
| DIGEST | [Statement digest](../performance-schema-digests.md). |
| DIGEST_TEXT | [Statement digest](../performance-schema-digests.md) text. |
| CURRENT_SCHEMA | Statement's default database for the statement, or NULL if there was none. |
| OBJECT_SCHEMA | Reserved, currently NULL |
| OBJECT_NAME | Reserved, currently NULL |
| OBJECT_TYPE | Reserved, currently NULL |
| OBJECT_INSTANCE_BEGIN | Address in memory of the statement object. |
| MYSQL_ERRNO | Error code. See [MariaDB Error Codes](/kb/en/mariadb-error-codes/) for a full list. |
| RETURNED_SQLSTATE | The [SQLSTATE](../../../../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/programmatic-compound-statements-diagnostics/sqlstate.md) value. |
| MESSAGE_TEXT | Statement error message. See [MariaDB Error Codes](/kb/en/mariadb-error-codes/). |
| ERRORS | 0 if SQLSTATE signifies completion (starting with 00) or warning (01), otherwise 1. |
| WARNINGS | Number of warnings from the diagnostics area. |
| ROWS_AFFECTED | Number of rows affected the statement affected. |
| ROWS_SENT | Number of rows returned. |
| ROWS_EXAMINED | Number of rows read during the statement's execution. |
| CREATED_TMP_DISK_TABLES | Number of on-disk temp tables created by the statement. |
| CREATED_TMP_TABLES | Number of temp tables created by the statement. |
| SELECT_FULL_JOIN | Number of joins performed by the statement which did not use an index. |
| SELECT_FULL_RANGE_JOIN | Number of joins performed by the statement which used a range search of the first table. |
| SELECT_RANGE | Number of joins performed by the statement which used a range of the first table. |
| SELECT_RANGE_CHECK | Number of joins without keys performed by the statement that check for key usage after each row. |
| SELECT_SCAN | Number of joins performed by the statement which used a full scan of the first table. |
| SORT_MERGE_PASSES | Number of merge passes by the sort algorithm performed by the statement. If too high, you may need to increase the [sort_buffer_size](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sort_buffer_size). |
| SORT_RANGE | Number of sorts performed by the statement which used a range. |
| SORT_ROWS | Number of rows sorted by the statement. |
| SORT_SCAN | Number of sorts performed by the statement which used a full table scan. |
| NO_INDEX_USED | 0 if the statement performed a table scan with an index, 1 if without an index. |
| NO_GOOD_INDEX_USED | 0 if a good index was found for the statement, 1 if no good index was found. See the Range checked for each record description in the [EXPLAIN](../../../../../../../clients-and-utilities/explain-analyzer.md) article. |
| NESTING_EVENT_ID | Reserved, currently NULL. |
| NESTING_EVENT_TYPE | Reserved, currently NULL. |

It is possible to empty this table with a `TRUNCATE TABLE` statement.

[events_statements_current](performance-schema-events_statements_current-table.md) and [events_statements_history](performance-schema-events_statements_history-table.md) are related tables.