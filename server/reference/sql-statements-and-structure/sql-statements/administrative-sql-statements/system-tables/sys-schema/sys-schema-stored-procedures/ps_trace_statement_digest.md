
# ps_trace_statement_digest

## Syntax


```
ps_trace_statement_digest(in_digest, in_runtime, in_interval, in_start_fresh, in_auto_enable)
```

## Description


`ps_trace_statement_digest` is a [stored procedure](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md) available with the [Sys Schema](../sys-schema-views/sys-schema-views-host_summary_by_statement_latency-and-xhost_summary_by_sta.md).


Parameters:


* in_digest VARCHAR(32): The statement digest identifier to analyze.
* in_runtime INT: Specifies the duration to run the analysis in seconds.
* in_interval DECIMAL(2,2): The analysis interval measured in seconds (including fraction values), at which snapshots are taken.
* in_start_fresh BOOLEAN: Determines whether to truncate the Performance Schema events_statements_history_long and events_stages_history_long tables before starting.
* in_auto_enable BOOLEAN: Determines whether to automatically enable required consumers.


## Examples


```
CALL sys.ps_trace_statement_digest('891ec6860f98ba46d89dd20b0c03652c', 5, 0.5, TRUE, TRUE);
```
