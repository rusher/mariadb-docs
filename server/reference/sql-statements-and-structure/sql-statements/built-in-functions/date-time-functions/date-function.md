
# DATE FUNCTION

## Syntax


```
DATE(expr)
```

## Description


Extracts the date part of the [date](../../../sql-language-structure/date-and-time-literals.md) or [datetime](../../../../data-types/date-and-time-data-types/datetime.md) expression *expr*. Returns NULL and throws a warning when passed an invalid date.


## Examples


```
SELECT DATE('2013-07-18 12:21:32');
+-----------------------------+
| DATE('2013-07-18 12:21:32') |
+-----------------------------+
| 2013-07-18                  |
+-----------------------------+
```
