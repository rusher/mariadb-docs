
# ps_is_instrument_default_enabled

## Syntax


```
sys.ps_is_instrument_default_enabled(instrument)
```

## Description


`ps_is_instrument_default_enabled` is a [stored function](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) available with the [Sys Schema](../sys-schema-views/sys-schema-views-host_summary_by_statement_latency-and-xhost_summary_by_sta.md).


It returns `YES` if the given Performance Schema *instrument* is enabled by default, and `NO` if it is not, does not exist, or is a NULL value.


## Examples


```
SELECT sys.ps_is_instrument_default_enabled('statement/sql/select');
+--------------------------------------------------------------+
| sys.ps_is_instrument_default_enabled('statement/sql/select') |
+--------------------------------------------------------------+
| YES                                                          |
+--------------------------------------------------------------+

SELECT sys.ps_is_instrument_default_enabled('memory/sql/udf_mem');
+------------------------------------------------------------+
| sys.ps_is_instrument_default_enabled('memory/sql/udf_mem') |
+------------------------------------------------------------+
| NO                                                         |
+------------------------------------------------------------+

SELECT sys.ps_is_instrument_default_enabled('memory/sql/nonexistent');
+----------------------------------------------------------------+
| sys.ps_is_instrument_default_enabled('memory/sql/nonexistent') |
+----------------------------------------------------------------+
| NO                                                             |
+----------------------------------------------------------------+

SELECT sys.ps_is_instrument_default_enabled(NULL);
+--------------------------------------------+
| sys.ps_is_instrument_default_enabled(NULL) |
+--------------------------------------------+
| NO                                         |
+--------------------------------------------+
```
