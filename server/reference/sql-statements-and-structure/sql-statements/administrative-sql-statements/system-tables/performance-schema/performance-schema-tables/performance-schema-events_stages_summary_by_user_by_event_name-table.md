
# Performance Schema events_stages_summary_by_user_by_event_name Table

The table lists stage events, summarized by user and event name.


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| USER | User. Used together with EVENT_NAME for grouping events. |
| EVENT_NAME | Event name. Used together with USER for grouping events. |
| COUNT_STAR | Number of summarized events, which includes all timed and untimed events. |
| SUM_TIMER_WAIT | Total wait time of the timed summarized events. |
| MIN_TIMER_WAIT | Minimum wait time of the timed summarized events. |
| AVG_TIMER_WAIT | Average wait time of the timed summarized events. |
| MAX_TIMER_WAIT | Maximum wait time of the timed summarized events. |



## Example


```
SELECT * FROM events_stages_summary_by_user_by_event_name\G
...
*************************** 325. row ***************************
          USER: NULL
    EVENT_NAME: stage/sql/Waiting for event metadata lock
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
*************************** 326. row ***************************
          USER: NULL
    EVENT_NAME: stage/sql/Waiting for commit lock
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
*************************** 327. row ***************************
          USER: NULL
    EVENT_NAME: stage/aria/Waiting for a resource
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
```
