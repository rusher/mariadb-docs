# JSON\_UNQUOTE

## Syntax

```
JSON_UNQUOTE(val)
```

## Description

Unquotes a JSON value, returning a string, or NULL if the argument is null.

An error will occur if the given value begins and ends with double quotes and is an invalid JSON string literal.

If the given value is not a JSON string, value is passed through unmodified.

Certain character sequences have special meanings within a string. Usually, a backslash is ignored, but the escape sequences in the table below are recognised by MariaDB, unless the [SQL Mode](../../../../server-management/variables-and-modes/sql-mode.md) is set to NO\_BACKSLASH\_ESCAPES SQL.

| Escape sequence | Character                          |
| --------------- | ---------------------------------- |
| Escape sequence | Character                          |
| "               | Double quote (")                   |
| \b              | Backslash                          |
| \f              | Formfeed                           |
|                 | Newline (linefeed)                 |
|                 | Carriage return                    |
|                 | Tab                                |
| \\              | Backslash ()                       |
| \uXXXX          | UTF-8 bytes for Unicode value XXXX |

## Examples

```
SELECT JSON_UNQUOTE('"Monty"');
+-------------------------+
| JSON_UNQUOTE('"Monty"') |
+-------------------------+
| Monty                   |
+-------------------------+
```

With the default [SQL Mode](../../../../server-management/variables-and-modes/sql-mode.md):

```
SELECT JSON_UNQUOTE('Si\bng\ting');
+-----------------------------+
| JSON_UNQUOTE('Si\bng\ting') |
+-----------------------------+
| Sng	ing                   |
+-----------------------------+
```

Setting NO\_BACKSLASH\_ESCAPES:

```
SET @@sql_mode = 'NO_BACKSLASH_ESCAPES';

SELECT JSON_UNQUOTE('Si\bng\ting');
+-----------------------------+
| JSON_UNQUOTE('Si\bng\ting') |
+-----------------------------+
| Si\bng\ting                 |
+-----------------------------+
```

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
