
# ps_is_consumer_enabled

## Syntax


```
sys.ps_is_consumer_enabled(consumer)
```

## Description


`ps_is_consumer_enabled` is a [stored function](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) available with the [Sys Schema](../README.md).


It returns an ENUM('YES','NO') depending on whether Performance Schema instrumentation for the given consumer is enabled, and NULL if not given a valid consumer name.


## Examples


```
SELECT sys.ps_is_consumer_enabled('global_instrumentation');
+------------------------------------------------------+
| sys.ps_is_consumer_enabled('global_instrumentation') |
+------------------------------------------------------+
| YES                                                  |
+------------------------------------------------------+

SELECT sys.ps_is_consumer_enabled('events_stages_current');
+-----------------------------------------------------+
| sys.ps_is_consumer_enabled('events_stages_current') |
+-----------------------------------------------------+
| NO                                                  |
+-----------------------------------------------------+

SELECT sys.ps_is_consumer_enabled('nonexistent_consumer');
+----------------------------------------------------+
| sys.ps_is_consumer_enabled('nonexistent_consumer') |
+----------------------------------------------------+
| NULL                                               |
+----------------------------------------------------+
```

## See Also


* [Performance Schema setup_consumers Table](../../performance-schema/performance-schema-tables/performance-schema-setup_consumers-table.md)

