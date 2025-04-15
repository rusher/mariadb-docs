# ps_is_thread_instrumented

#

# Syntax

```
sys.ps_is_thread_instrumented(connection_id)
```

#

# Description

`ps_is_thread_instrumented` is a [stored function](/en/stored-functions/) available with the [Sys Schema](../sys-schema-sys_config-table.md) that returns whether or not Performance Schema instrumentation for the given *connection_id* is enabled.

* `YES` - instrumentation is enabled
* `NO` - instrumentation is not enabled
* `UNKNOWN` - the connection ID is unknown
* `NULL` - NULL value

#

# Examples

```
SELECT sys.ps_is_thread_instrumented(CONNECTION_ID());
+------------------------------------------------+
| sys.ps_is_thread_instrumented(CONNECTION_ID()) |
+------------------------------------------------+
| YES |
+------------------------------------------------+

SELECT sys.ps_is_thread_instrumented(2042);
+-------------------------------------+
| sys.ps_is_thread_instrumented(2042) |
+-------------------------------------+
| UNKNOWN |
+-------------------------------------+

SELECT sys.ps_is_thread_instrumented(NULL);
+-------------------------------------+
| sys.ps_is_thread_instrumented(NULL) |
+-------------------------------------+
| NULL |
+-------------------------------------+
```