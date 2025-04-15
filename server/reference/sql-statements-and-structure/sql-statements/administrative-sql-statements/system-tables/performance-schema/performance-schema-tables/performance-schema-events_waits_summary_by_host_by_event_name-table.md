
# Performance Schema events_waits_summary_by_host_by_event_name Table

The [Performance Schema](performance-schema-table_handles-table.md) `<code>events_waits_summary_by_host_by_event_name</code>` table contains wait events summarized by host and event name. It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| HOST | Host. Used together with EVENT_NAME for grouping events. |
| EVENT_NAME | Event name. Used together with USER and HOST for grouping events. |
| COUNT_STAR | Number of summarized events |
| SUM_TIMER_WAIT | Total wait time of the summarized events that are timed. |
| MIN_TIMER_WAIT | Minimum wait time of the summarized events that are timed. |
| AVG_TIMER_WAIT | Average wait time of the summarized events that are timed. |
| MAX_TIMER_WAIT | Maximum wait time of the summarized events that are timed. |



The `<code>*_TIMER_WAIT</code>` columns only calculate results for timed events, as non-timed events have a `<code>NULL</code>` wait time.


## Example


```
SELECT * FROM events_waits_summary_by_host_by_event_name\G
...
*************************** 610. row ***************************
          HOST: NULL
    EVENT_NAME: wait/io/socket/sql/server_unix_socket
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
*************************** 611. row ***************************
          HOST: NULL
    EVENT_NAME: wait/io/socket/sql/client_connection
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
*************************** 612. row ***************************
          HOST: NULL
    EVENT_NAME: idle
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
```
