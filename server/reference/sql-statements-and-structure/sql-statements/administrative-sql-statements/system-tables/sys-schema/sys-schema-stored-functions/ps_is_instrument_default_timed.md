
# ps_is_instrument_default_timed

## Syntax


```
sys.ps_is_instrument_default_timed(instrument)
```

## Description


`ps_is_instrument_default_timed` is a [stored function](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) available with the [Sys Schema](../README.md).


It returns `YES` if the given Performance Schema *instrument* is timed by default, and `NO` if it is not, does not exist, or is a NULL value.


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
