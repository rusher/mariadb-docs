
# Performance Schema setup_timers Table

## Description


The `setup_timers` table shows the currently selected event timers. Deprecated since 10.5, removed in 12.0


It contains the following columns:



| Column | Description |
| --- | --- |
| NAME | Type of instrument the timer is used for. |
| TIMER_NAME | Timer applying to the instrument type. Can be modified. |



The `TIMER_NAME` value can be changed to choose a different timer, and can be any non-NULL value in the [performance_timers.TIMER_NAME](performance-schema-performance_timers-table.md) column.


If you modify the table, monitoring is immediately affected, and currently monitored events would use a combination of old and new timers, which is probably undesirable. It is best to reset the Performance Schema statistics if you make changes to this table.


## Example


```
SELECT * FROM setup_timers;
+-----------+-------------+
| NAME      | TIMER_NAME  |
+-----------+-------------+
| idle      | MICROSECOND |
| wait      | CYCLE       |
| stage     | NANOSECOND  |
| statement | NANOSECOND  |
+-----------+-------------+
```


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
