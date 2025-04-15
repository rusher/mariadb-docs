
# sys_get_config

## Syntax


```
sys.sys_get_config(name,default)
```


## Description


`<code>sys_get_config</code>` is a [stored function](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) available with the [Sys Schema](../sys-schema-views/sys-schema-views-host_summary_by_statement_latency-and-xhost_summary_by_sta.md).


The function returns a configuration option value from the [sys_config table](../sys-schema-sys_config-table.md). It takes two arguments; *name*, a configuration option name, and *default*, which is returned if the given option does not exist in the table.


Both arguments are VARCHAR(128) and can be NULL. Returns NULL if *name* is NULL, or if the given option is not found and *default* is NULL.


## Examples


```
SELECT sys.sys_get_config('ps_thread_trx_info.max_length',NULL);
+----------------------------------------------------------+
| sys.sys_get_config('ps_thread_trx_info.max_length',NULL) |
+----------------------------------------------------------+
| 65535                                                    |
+----------------------------------------------------------+
```

## See Also


* [Sys Schema sys_config Table](../sys-schema-sys_config-table.md)

