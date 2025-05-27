# NULLIF

## Syntax

```
NULLIF(expr1,expr2)
```

## Description

Returns NULL if expr1 = expr2 is true, otherwise returns expr1. This is\
the same as [CASE](case-operator.md) WHEN expr1 = expr2 THEN NULL ELSE expr1 END.

## Examples

```
SELECT NULLIF(1,1);
+-------------+
| NULLIF(1,1) |
+-------------+
|        NULL |
+-------------+

SELECT NULLIF(1,2);
+-------------+
| NULLIF(1,2) |
+-------------+
|           1 |
+-------------+
```

## See Also

* [NULL values](../../../data-types/null-values.md)
* [IS NULL operator](../../../sql-statements-and-structure/operators/comparison-operators/is-null.md)
* [IS NOT NULL operator](../../../sql-statements-and-structure/operators/comparison-operators/is-not-null.md)
* [COALESCE function](../../../sql-statements-and-structure/operators/comparison-operators/coalesce.md)
* [IFNULL function](ifnull.md)
* [CONNECT data types](../../../storage-engines/connect/connect-data-types.md#null-handling)

GPLv2 fill\_help\_tables.sql
