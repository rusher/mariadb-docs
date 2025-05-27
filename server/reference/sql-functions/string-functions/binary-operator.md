# BINARY Operator

This page describes the BINARY operator. For details about the data type, see [Binary Data Type](../../data-types/string-data-types/binary.md).

## Syntax

```
BINARY
```

## Description

The `BINARY` operator casts the string following it to a binary string. This is an easy way to force a column comparison to be done byte by byte rather than character by character. This causes the comparison to be case sensitive even if the column isn't defined as `[BINARY](../../../../data-types/string-data-types/binary.md)` or `[BLOB](../../../../data-types/string-data-types/blob-and-text-data-types.md)`.

`BINARY` also causes trailing spaces to be significant.

## Examples

```
SELECT 'a' = 'A';
+-----------+
| 'a' = 'A' |
+-----------+
|         1 |
+-----------+

SELECT BINARY 'a' = 'A';
+------------------+
| BINARY 'a' = 'A' |
+------------------+
|                0 |
+------------------+

SELECT 'a' = 'a ';
+------------+
| 'a' = 'a ' |
+------------+
|          1 |
+------------+

SELECT BINARY 'a' = 'a ';
+-------------------+
| BINARY 'a' = 'a ' |
+-------------------+
|                 0 |
+-------------------+
```

## See Also

* [Operator Precedence](../../sql-structure/operators/operator-precedence.md)

GPLv2 fill\_help\_tables.sql
