# &

## Syntax

```
&
```

## Description

Bitwise AND. Converts the values to binary and compares bits. Only if both the corresponding bits are 1 is the resulting bit also 1.

See also [bitwise OR](bitwise-or.md).

## Examples

```
SELECT 2&1;
+-----+
| 2&1 |
+-----+
|   0 |
+-----+

SELECT 3&1;
+-----+
| 3&1 |
+-----+
|   1 |
+-----+

SELECT 29 & 15;
+---------+
| 29 & 15 |
+---------+
|      13 |
+---------+
```

## See Also

* [Operator Precedence](../../../../sql-statements-and-structure/operators/operator-precedence.md)

GPLv2 fill\_help\_tables.sql
