# DIV

## Syntax

```
DIV
```

## Description

Integer division. Similar to [FLOOR()](floor.md), but is safe with [BIGINT](../../data-types/numeric-data-types/bigint.md) values.\
Incorrect results may occur for non-integer operands that exceed BIGINT range.

If the `ERROR_ON_DIVISION_BY_ZERO` [SQL\_MODE](../../../server-management/variables-and-modes/sql-mode.md) is used, a division by zero produces an error. Otherwise, it returns NULL.

The remainder of a division can be obtained using the [MOD](mod.md) operator.

## Examples

```
SELECT 300 DIV 7;
+-----------+
| 300 DIV 7 |
+-----------+
|        42 |
+-----------+

SELECT 300 DIV 0;
+-----------+
| 300 DIV 0 |
+-----------+
|      NULL |
+-----------+
```

## See Also

* [Division operator](division-operator.md)
* [Operator Precedence](../../sql-structure/operators/operator-precedence.md)

GPLv2 fill\_help\_tables.sql
