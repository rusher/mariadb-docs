# Addition Operator (+)

## Syntax

```
+
```

## Description

Addition.

If both operands are integers, the result is calculated with [BIGINT](../../data-types/numeric-data-types/bigint.md) precision. If either integer is unsigned, the result is also an unsigned integer.

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
* [Subtraction Operator (-)](../../sql-structure/operators/arithmetic-operators/subtraction-operator.md)
* [Multiplication Operator (\*)](multiplication-operator.md)
* [Division Operator (/)](division-operator.md)
* [Operator Precedence](../../sql-structure/operators/operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
