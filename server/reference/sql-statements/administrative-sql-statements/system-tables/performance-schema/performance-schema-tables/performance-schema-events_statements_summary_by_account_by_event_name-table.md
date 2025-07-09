
# Performance Schema events_statements_summary_by_account_by_event_name Table

The [Performance Schema](../README.md) events_statements_summary_by_account_by_event_name table contains statement events summarized by account and event name. It contains the following columns:



| Column | Description |
| --- | --- |
| USER | User. Used together with HOST and EVENT_NAME for grouping events. |
| HOST | Host. Used together with USER and EVENT_NAME for grouping events. |
| EVENT_NAME | Event name. Used together with USER and HOST for grouping events. |
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



The `*_TIMER_WAIT` columns only calculate results for timed events, as non-timed events have a `NULL` wait time.


## Example


```
SELECT * FROM events_statements_summary_by_account_by_event_name\G
...
*************************** 521. row ***************************
                       USER: NULL
                       HOST: NULL
                 EVENT_NAME: statement/com/Error
                 COUNT_STAR: 0
             SUM_TIMER_WAIT: 0
             MIN_TIMER_WAIT: 0
             AVG_TIMER_WAIT: 0
             MAX_TIMER_WAIT: 0
              SUM_LOCK_TIME: 0
                 SUM_ERRORS: 0
               SUM_WARNINGS: 0
          SUM_ROWS_AFFECTED: 0
              SUM_ROWS_SENT: 0
          SUM_ROWS_EXAMINED: 0
SUM_CREATED_TMP_DISK_TABLES: 0
     SUM_CREATED_TMP_TABLES: 0
       SUM_SELECT_FULL_JOIN: 0
 SUM_SELECT_FULL_RANGE_JOIN: 0
           SUM_SELECT_RANGE: 0
     SUM_SELECT_RANGE_CHECK: 0
            SUM_SELECT_SCAN: 0
      SUM_SORT_MERGE_PASSES: 0
             SUM_SORT_RANGE: 0
              SUM_SORT_ROWS: 0
              SUM_SORT_SCAN: 0
          SUM_NO_INDEX_USED: 0
     SUM_NO_GOOD_INDEX_USED: 0
*************************** 522. row ***************************
                       USER: NULL
                       HOST: NULL
                 EVENT_NAME: statement/com/
                 COUNT_STAR: 0
             SUM_TIMER_WAIT: 0
             MIN_TIMER_WAIT: 0
             AVG_TIMER_WAIT: 0
             MAX_TIMER_WAIT: 0
              SUM_LOCK_TIME: 0
                 SUM_ERRORS: 0
               SUM_WARNINGS: 0
          SUM_ROWS_AFFECTED: 0
              SUM_ROWS_SENT: 0
          SUM_ROWS_EXAMINED: 0
SUM_CREATED_TMP_DISK_TABLES: 0
     SUM_CREATED_TMP_TABLES: 0
       SUM_SELECT_FULL_JOIN: 0
 SUM_SELECT_FULL_RANGE_JOIN: 0
           SUM_SELECT_RANGE: 0
     SUM_SELECT_RANGE_CHECK: 0
            SUM_SELECT_SCAN: 0
      SUM_SORT_MERGE_PASSES: 0
             SUM_SORT_RANGE: 0
              SUM_SORT_ROWS: 0
              SUM_SORT_SCAN: 0
          SUM_NO_INDEX_USED: 0
     SUM_NO_GOOD_INDEX_USED: 0
```


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
