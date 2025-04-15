
# list_add

## Syntax


```
sys.list_add(list,value)
```

## Description


`<code>list_add</code>` is a [stored function](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) available with the [Sys Schema](../sys-schema-views/sys-schema-views-host_summary_by_statement_latency-and-xhost_summary_by_sta.md).


It takes a *list* to be be modified and a *value* to be added to the list, returning the resulting value. This can be used, for example, to add a value to a system variable taking a comma-delimited list of options, such as [sql_mode](../../../../../../../server-management/variables-and-modes/sql-mode.md).


The related function [list_drop](list_drop.md) can be used to drop a value from a list.


## Examples


```
SELECT @@sql_mode;
+-----------------------------------------------------------------------+
| @@sql_mode                                                            |
+-----------------------------------------------------------------------+
| STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,
NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+-----------------------------------------------------------------------+

SET @@sql_mode = sys.list_add(@@sql_mode, 'NO_ZERO_DATE');

SELECT @@sql_mode;
+-----------------------------------------------------------------------+
| @@sql_mode                                                            |
+-----------------------------------------------------------------------+
| STRICT_TRANS_TABLES,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,
NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+-----------------------------------------------------------------------+
```

## See Also


* [list_drop](list_drop.md)

