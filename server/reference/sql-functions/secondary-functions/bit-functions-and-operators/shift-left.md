# <<

## Syntax

```
value1 << value2
```

## Description

Converts a longlong ([BIGINT](../../../data-types/numeric-data-types/bigint.md)) number (_value1_) to binary and shifts _value2_ units to the left.

## Examples

```
SELECT 1 << 2;
+--------+
| 1 << 2 |
+--------+
|      4 |
+--------+
```

## See Also

* [Operator Precedence](../../../sql-structure/operators/operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
