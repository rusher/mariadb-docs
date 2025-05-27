# DATE FUNCTION

## Syntax

```
DATE(expr)
```

## Description

Extracts the date part of the [date](../../../data-types/date-and-time-data-types/date.md) or [datetime](../../../data-types/date-and-time-data-types/datetime.md) expression _expr_. Returns NULL and throws a warning when passed an invalid date.

## Examples

```
SELECT DATE('2013-07-18 12:21:32');
+-----------------------------+
| DATE('2013-07-18 12:21:32') |
+-----------------------------+
| 2013-07-18                  |
+-----------------------------+
```

GPLv2 fill\_help\_tables.sql
