# Addition Operator (+)

## Syntax

```
+
```

## Description

Addition.

If both operands are integers, the result is calculated with [BIGINT](../../../data-types/data-types-numeric-data-types/bigint.md) precision. If either integer is unsigned, the result is also an unsigned integer.

For real or string operands, the operand with the highest precision determines the result precision.

## Examples

```
SELECT 3+5;
+-----+
| 3+5 |
+-----+
|   8 |
+-----+
```

## See Also

* [Type Conversion](../string-functions/type-conversion.md)
* [Subtraction Operator (-)](../../../sql-statements-and-structure/operators/arithmetic-operators/subtraction-operator-.md)
* [Multiplication Operator (\*)](multiplication-operator.md)
* [Division Operator (/)](division-operator.md)
* [Operator Precedence](../../../sql-statements-and-structure/operators/operator-precedence.md)

GPLv2 fill\_help\_tables.sql
