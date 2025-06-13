
# Performance Schema objects_summary_global_by_type Table

It aggregates object wait events, and contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| OBJECT_TYPE | Groups records together with OBJECT_SCHEMA and OBJECT_NAME. |
| OBJECT_SCHEMA | Groups records together with OBJECT_TYPE and OBJECT_NAME. |
| OBJECT_NAME | Groups records together with OBJECT_SCHEMA and OBJECT_TYPE. |
| COUNT_STAR | Number of summarized events |
| SUM_TIMER_WAIT | Total wait time of the summarized events that are timed. |
| MIN_TIMER_WAIT | Minimum wait time of the summarized events that are timed. |
| AVG_TIMER_WAIT | Average wait time of the summarized events that are timed. |
| MAX_TIMER_WAIT | Maximum wait time of the summarized events that are timed. |



You can [TRUNCATE](../../../../table-statements/truncate-table.md) the table, which will reset all counters to zero.


## Example


```
SELECT * FROM objects_summary_global_by_type\G
...
*************************** 101. row ***************************
   OBJECT_TYPE: TABLE
 OBJECT_SCHEMA: test
   OBJECT_NAME: v
    COUNT_STAR: 0
SUM_TIMER_WAIT: 0
MIN_TIMER_WAIT: 0
AVG_TIMER_WAIT: 0
MAX_TIMER_WAIT: 0
*************************** 102. row ***************************
   OBJECT_TYPE: TABLE
 OBJECT_SCHEMA: test
   OBJECT_NAME: xx2
    COUNT_STAR: 2
SUM_TIMER_WAIT: 1621920
MIN_TIMER_WAIT: 481344
AVG_TIMER_WAIT: 810960
MAX_TIMER_WAIT: 1140576
```


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
