
# Performance Schema events_statements_summary_by_digest Table

The [Performance Schema digest](../performance-schema-digests.md) is a hashed, normalized form of a statement with the specific data values removed. It allows statistics to be gathered for similar kinds of statements.


The [Performance Schema](../README.md) `events_statements_summary_by_digest` table records statement events summarized by schema and digest. It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| SCHEMA NAME | Database name. Records are summarised together with DIGEST. |
| DIGEST | [Performance Schema digest](../performance-schema-digests.md). Records are summarised together with SCHEMA NAME. |
| DIGEST TEXT | The unhashed form of the digest. |
| COUNT_STAR | Number of summarized events |
| SUM_TIMER_WAIT | Total wait time of the summarized events that are timed. |
| MIN_TIMER_WAIT | Minimum wait time of the summarized events that are timed. |
| AVG_TIMER_WAIT | Average wait time of the summarized events that are timed. |
| MAX_TIMER_WAIT | Maximum wait time of the summarized events that are timed. |
| SUM_LOCK_TIME | Sum of the LOCK_TIME column in the events_statements_current table. |
| SUM_ERRORS | Sum of the ERRORS column in the events_statements_current table. |
| SUM_WARNINGS | Sum of the WARNINGS column in the events_statements_current table. |
| SUM_ROWS_AFFECTED | Sum of the ROWS_AFFECTED column in the events_statements_current table. |
| SUM_ROWS_SENT | Sum of the ROWS_SENT column in the events_statements_current table. |
| SUM_ROWS_EXAMINED | Sum of the ROWS_EXAMINED column in the events_statements_current table. |
| SUM_CREATED_TMP_DISK_TABLES | Sum of the CREATED_TMP_DISK_TABLES column in the events_statements_current table. |
| SUM_CREATED_TMP_TABLES | Sum of the CREATED_TMP_TABLES column in the events_statements_current table. |
| SUM_SELECT_FULL_JOIN | Sum of the SELECT_FULL_JOIN column in the events_statements_current table. |
| SUM_SELECT_FULL_RANGE_JOIN | Sum of the SELECT_FULL_RANGE_JOIN column in the events_statements_current table. |
| SUM_SELECT_RANGE | Sum of the SELECT_RANGE column in the events_statements_current table. |
| SUM_SELECT_RANGE_CHECK | Sum of the SELECT_RANGE_CHECK column in the events_statements_current table. |
| SUM_SELECT_SCAN | Sum of the SELECT_SCAN column in the events_statements_current table. |
| SUM_SORT_MERGE_PASSES | Sum of the SORT_MERGE_PASSES column in the events_statements_current table. |
| SUM_SORT_RANGE | Sum of the SORT_RANGE column in the events_statements_current table. |
| SUM_SORT_ROWS | Sum of the SORT_ROWS column in the events_statements_current table. |
| SUM_SORT_SCAN | Sum of the SORT_SCAN column in the events_statements_current table. |
| SUM_NO_INDEX_USED | Sum of the NO_INDEX_USED column in the events_statements_current table. |
| SUM_NO_GOOD_INDEX_USED | Sum of the NO_GOOD_INDEX_USED column in the events_statements_current table. |
| FIRST_SEEN | Time at which the digest was first seen. |
| LAST_SEEN | Time at which the digest was most recently seen. |



The `*_TIMER_WAIT` columns only calculate results for timed events, as non-timed events have a `NULL` wait time.


The `events_statements_summary_by_digest` table is limited in size by the [performance_schema_digests_size](../performance-schema-system-variables.md#performance_schema_digests_size) system variable. Once the limit has been reached and the table is full, all entries are aggregated in a row with a `NULL` digest. The `COUNT_STAR` value of this `NULL` row indicates how many digests are recorded in the row and therefore gives an indication of whether `performance_schema_digests_size` should be increased to provide more accurate statistics.

