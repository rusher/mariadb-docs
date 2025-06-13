# UTC\_DATE

## Syntax

```
UTC_DATE, UTC_DATE()
```

## Description

Returns the current [UTC date](../../data-types/string-data-types/character-sets/internationalization-and-localization/coordinated-universal-time.md) as a value in 'YYYY-MM-DD' or YYYYMMDD\
format, depending on whether the function is used in a string or numeric context.

## Examples

```
SELECT UTC_DATE(), UTC_DATE() + 0;
+------------+----------------+
| UTC_DATE() | UTC_DATE() + 0 |
+------------+----------------+
| 2010-03-27 |       20100327 |
+------------+----------------+
```

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
