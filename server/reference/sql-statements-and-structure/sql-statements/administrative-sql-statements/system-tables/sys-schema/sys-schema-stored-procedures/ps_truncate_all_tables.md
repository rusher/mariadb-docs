
# ps_truncate_all_tables

## Syntax


```
ps_truncate_all_tables(bool display)
```

## Description


`<code>ps_truncate_all_tables</code>` is a [stored procedure](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md) available with the [Sys Schema](../sys-schema-views/sys-schema-views-host_summary_by_statement_latency-and-xhost_summary_by_sta.md).


The procedure resets all aggregated instrumentation as a snapshot, producing a result set indicating the number of truncated tables. The boolean parameter *display* specifies whether to display each [TRUNCATE TABLE](../../../../table-statements/truncate-table.md) statement before execution.


## Examples


```
CALL sys.ps_truncate_all_tables(false);
+---------------------+
| summary             |
+---------------------+
| Truncated 44 tables |
+---------------------+
```

```
CALL sys.ps_truncate_all_tables(true);
+------------------------------------------------------------------+
| status                                                           |
+------------------------------------------------------------------+
| Running: TRUNCATE TABLE performance_schema.events_stages_history |
+------------------------------------------------------------------+

...

+------------------------------------------------------------------------------+
| status                                                                       |
+------------------------------------------------------------------------------+
| Running: TRUNCATE TABLE performance_schema.table_lock_waits_summary_by_table |
+------------------------------------------------------------------------------+

+---------------------+
| summary             |
+---------------------+
| Truncated 44 tables |
+---------------------+
```
