
# Performance Schema events_statements_summary_by_program Table


##### MariaDB starting with [10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
The `<code>events_statements_summary_by_program</code>` table, along with many other new [Performance Schema tables](list-of-performance-schema-tables.md), was added in [MariaDB 10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md).


Each row in the the [Performance Schema](performance-schema-table_handles-table.md) events_statements_summary_by_program table summarizes events for a particular stored program (stored procedure, stored function, trigger or event).


It contains the following fields.



| Column | Type | Null | Description |
| --- | --- | --- | --- |
| Column | Type | Null | Description |
| OBJECT_TYPE | enum('EVENT', 'FUNCTION', 'PROCEDURE', 'TABLE', 'TRIGGER') | YES | Object type for which the summary is generated. |
| OBJECT_SCHEMA | varchar(64) | NO | The schema of the object for which the summary is generated. |
| OBJECT_NAME | varchar(64) | NO | The name of the object for which the summary is generated. |
| COUNT_STAR | bigint(20) unsigned | NO | The number of summarized events (from events_statements_current). This value includes all events, whether timed or nontimed. |
| SUM_TIMER_WAIT | bigint(20) unsigned | NO | The number of summarized events (from events_statements_current). This value includes all events, whether timed or nontimed. |
| MIN_TIMER_WAIT | bigint(20) unsigned | NO | The minimum wait time of the summarized timed events. |
| AVG_TIMER_WAIT | bigint(20) unsigned | NO | The average wait time of the summarized timed events. |
| MAX_TIMER_WAIT | bigint(20) unsigned | NO | The maximum wait time of the summarized timed events. |
| COUNT_STATEMENTS | bigint(20) unsigned | NO | Total number of nested statements invoked during stored program execution. |
| SUM_STATEMENTS_WAIT | bigint(20) unsigned | NO | The total wait time of the summarized timed statements. This value is calculated only for timed statements because nontimed statements have a wait time of NULL. The same is true for the other xxx_STATEMENT_WAIT values. |
| MIN_STATEMENTS_WAIT | bigint(20) unsigned | NO | The minimum wait time of the summarized timed statements. |
| AVG_STATEMENTS_WAIT | bigint(20) unsigned | NO | The average wait time of the summarized timed statements. |
| MAX_STATEMENTS_WAIT | bigint(20) unsigned | NO | The maximum wait time of the summarized timed statements. |
| SUM_LOCK_TIME | bigint(20) unsigned | NO | The total time spent (in picoseconds) waiting for table locks for the summarized statements. |
| SUM_ERRORS | bigint(20) unsigned | NO | The total number of errors that occurend for the summarized statements. |
| SUM_WARNINGS | bigint(20) unsigned | NO | The total number of warnings that occurend for the summarized statements. |
| SUM_ROWS_AFFECTED | bigint(20) unsigned | NO | The total number of affected rows by the summarized statements. |
| SUM_ROWS_SENT | bigint(20) unsigned | NO | The total number of rows returned by the summarized statements. |
| SUM_ROWS_EXAMINED | bigint(20) unsigned | NO | The total number of rows examined by the summarized statements.The total number of affected rows by the summarized statements. |
| SUM_CREATED_TMP_DISK_TABLES | bigint(20) unsigned | NO | The total number of on-disk temporary tables created by the summarized statements. |
| SUM_CREATED_TMP_TABLES | bigint(20) unsigned | NO | The total number of in-memory temporary tables created by the summarized statements. |
| SUM_SELECT_FULL_JOIN | bigint(20) unsigned | NO | The total number of full joins executed by the summarized statements. |
| SUM_SELECT_FULL_RANGE_JOIN | bigint(20) unsigned | NO | The total number of range search joins executed by the summarized statements. |
| SUM_SELECT_RANGE | bigint(20) unsigned | NO | The total number of joins that used ranges on the first table executed by the summarized statements. |
| SUM_SELECT_RANGE_CHECK | bigint(20) unsigned | NO | The total number of joins that check for key usage after each row executed by the summarized statements. |
| SUM_SELECT_SCAN | bigint(20) unsigned | NO | The total number of joins that did a full scan of the first table executed by the summarized statements. |
| SUM_SORT_MERGE_PASSES | bigint(20) unsigned | NO | The total number of merge passes that the sort algorithm has had to do for the summarized statements. |
| SUM_SORT_RANGE | bigint(20) unsigned | NO | The total number of sorts that were done using ranges for the summarized statements. |
| SUM_SORT_ROWS | bigint(20) unsigned | NO | The total number of sorted rows that were sorted by the summarized statements. |
| SUM_SORT_SCAN | bigint(20) unsigned | NO | The total number of sorts that were done by scanning the table by the summarized statements. |
| SUM_NO_INDEX_USED | bigint(20) unsigned | NO | The total number of statements that performed a table scan without using an index. |
| SUM_NO_GOOD_INDEX_USED | bigint(20) unsigned | NO | The total number of statements where no good index was found. |


