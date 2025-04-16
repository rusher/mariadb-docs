
# quote_identifier

## Syntax


```
sys.quote_identifier(str)
```

## Description


`quote_identifier` is a [stored function](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) available with the [Sys Schema](../sys-schema-views/sys-schema-views-host_summary_by_statement_latency-and-xhost_summary_by_sta.md).


It quotes a string to produce a result that can be used as an identifier in an
SQL statement. The string is returned enclosed by backticks ("```") and
with each instance of backtick ("```") doubled. If the argument
is `NULL`, the return value is the word "`NULL`" without enclosing
backticks.


## Examples


```
SELECT sys.quote_identifier("Identifier with spaces");
+------------------------------------------------+
| sys.quote_identifier("Identifier with spaces") |
+------------------------------------------------+
| `Identifier with spaces`                       |
+------------------------------------------------+

SELECT sys.quote_identifier("Identifier` containing `backticks");
+-----------------------------------------------------------+
| sys.quote_identifier("Identifier` containing `backticks") |
+-----------------------------------------------------------+
| `Identifier`` containing ``backticks`                     |
+-----------------------------------------------------------+
```
