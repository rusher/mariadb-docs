
# ps_is_instrument_default_timed

## Syntax


```
sys.ps_is_instrument_default_timed(instrument)
```

## Description


`<code>ps_is_instrument_default_timed</code>` is a [stored function](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) available with the [Sys Schema](../sys-schema-views/sys-schema-views-host_summary_by_statement_latency-and-xhost_summary_by_sta.md).


It returns `<code>YES</code>` if the given Performance Schema *instrument* is timed by default, and `<code>NO</code>` if it is not, does not exist, or is a NULL value.


## Examples


```
SELECT sys.ps_is_instrument_default_timed('statement/sql/select');
+------------------------------------------------------------+
| sys.ps_is_instrument_default_timed('statement/sql/select') |
+------------------------------------------------------------+
| YES                                                        |
+------------------------------------------------------------+

SELECT sys.ps_is_instrument_default_timed('memory/sql/udf_mem');
+----------------------------------------------------------+
| sys.ps_is_instrument_default_timed('memory/sql/udf_mem') |
+----------------------------------------------------------+
| NO                                                       |
+----------------------------------------------------------+

SELECT sys.ps_is_instrument_default_timed('memory/sql/nonexistent');
+-------------------------------------------------------------+
| sys.ps_is_instrument_default_timed('memory/sql/udf_memsds') |
+-------------------------------------------------------------+
| NO                                                          |
+-------------------------------------------------------------+

SELECT sys.ps_is_instrument_default_timed(NULL);
+------------------------------------------+
| sys.ps_is_instrument_default_timed(NULL) |
+------------------------------------------+
| NO                                       |
+------------------------------------------+
```
