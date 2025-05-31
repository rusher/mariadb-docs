# >>

## Syntax

```
value1 >> value2
```

## Description

Converts a longlong ([BIGINT](../../../data-types/numeric-data-types/bigint.md)) number (_value1_) to binary and shifts _value2_ units to the right.

## Examples

```
SELECT 4 >> 2;
+--------+
| 4 >> 2 |
+--------+
|      1 |
+--------+
```

## See Also

* [Operator Precedence](../../../sql-structure/operators/operator-precedence.md)

GPLv2 fill\_help\_tables.sql
