
# ps_thread_trx_info

## Syntax


```
sys.ps_thread_trx_info(thread_id)
```


## Description


`<code>ps_thread_trx_info</code>` is a [stored function](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) available with the [Sys Schema](../sys-schema-views/sys-schema-views-host_summary_by_statement_latency-and-xhost_summary_by_sta.md).


It returns a JSON object with information about the thread specified by the given *thread_id*. This information includes:


* the current transaction
* executed statements (derived from the [Performance Schema events_transactions_current Table](../../performance-schema/performance-schema-tables/performance-schema-events_transactions_current-table.md) and the [Performance Schema events_statements_history Table](../../performance-schema/performance-schema-tables/performance-schema-events_statements_history-table.md) (full data will only returned if the consumers for those tables are enabled).


The maximum length of the returned JSON object is determined by the value of the [ps_thread_trx_info.max_length sys_config option](../sys-schema-sys_config-table.md) (by default 65535). If the returned value exceeds this length, a JSON object error is returned.


## Examples


```

```

## See Also


* [Sys Schema sys_config Table](../sys-schema-sys_config-table.md)

