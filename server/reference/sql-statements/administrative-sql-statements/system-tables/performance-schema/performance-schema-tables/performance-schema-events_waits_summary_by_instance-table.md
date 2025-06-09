
# Performance Schema events_waits_summary_by_instance Table

The [Performance Schema](../README.md) `events_waits_summary_by_instance` table contains wait events summarized by instance. It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| EVENT_NAME | Event name. Used together with OBJECT_INSTANCE_BEGIN for grouping events. |
| OBJECT_INSTANCE_BEGIN | If an instrument creates multiple instances, each instance has a unique OBJECT_INSTANCE_BEGIN value to allow for grouping by instance. |
| COUNT_STAR | Number of summarized events |
| SUM_TIMER_WAIT | Total wait time of the summarized events that are timed. |
| MIN_TIMER_WAIT | Minimum wait time of the summarized events that are timed. |
| AVG_TIMER_WAIT | Average wait time of the summarized events that are timed. |
| MAX_TIMER_WAIT | Maximum wait time of the summarized events that are timed. |



The `*_TIMER_WAIT` columns only calculate results for timed events, as non-timed events have a `NULL` wait time.


## Example


```
SELECT * FROM events_waits_summary_by_instance\G
...
*************************** 202. row ***************************
           EVENT_NAME: wait/io/file/sql/binlog
OBJECT_INSTANCE_BEGIN: 140578961969856
           COUNT_STAR: 6
       SUM_TIMER_WAIT: 90478331960
       MIN_TIMER_WAIT: 263344
       AVG_TIMER_WAIT: 15079721848
       MAX_TIMER_WAIT: 67760576376
*************************** 203. row ***************************
           EVENT_NAME: wait/io/file/sql/dbopt
OBJECT_INSTANCE_BEGIN: 140578961970560
           COUNT_STAR: 6
       SUM_TIMER_WAIT: 39891428472
       MIN_TIMER_WAIT: 387168
       AVG_TIMER_WAIT: 6648571412
       MAX_TIMER_WAIT: 24503293304
*************************** 204. row ***************************
           EVENT_NAME: wait/io/file/sql/dbopt
OBJECT_INSTANCE_BEGIN: 140578961971264
           COUNT_STAR: 6
       SUM_TIMER_WAIT: 39902495024
       MIN_TIMER_WAIT: 177888
       AVG_TIMER_WAIT: 6650415692
       MAX_TIMER_WAIT: 21026400404
```


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
