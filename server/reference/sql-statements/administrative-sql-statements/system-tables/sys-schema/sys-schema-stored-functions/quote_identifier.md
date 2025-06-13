# quote\_identifier

## Syntax

```
sys.quote_identifier(str)
```

## Description

`quote_identifier` is a [stored function](../../../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../).

It quotes a string to produce a result that can be used as an identifier in an\
SQL statement. The string is returned enclosed by backticks ("`") and with each instance of backtick ("`") doubled. If the argument\
is `NULL`, the return value is the word "`NULL`" without enclosing\
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

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
