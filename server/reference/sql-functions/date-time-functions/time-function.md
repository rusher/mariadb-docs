# TIME Function

## Syntax

```
TIME(expr)
```

## Description

Extracts the time part of the time or datetime expression `expr` and\
returns it as a string.

## Examples

```
SELECT TIME('2003-12-31 01:02:03');
+-----------------------------+
| TIME('2003-12-31 01:02:03') |
+-----------------------------+
| 01:02:03                    |
+-----------------------------+

SELECT TIME('2003-12-31 01:02:03.000123');
+------------------------------------+
| TIME('2003-12-31 01:02:03.000123') |
+------------------------------------+
| 01:02:03.000123                    |
+------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
