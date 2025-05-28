---
icon: earth-africa
---

# ST\_NUMPOINTS

## Syntax

```sql
ST_NumPoints(ls)
NumPoints(ls)
```

## Description

Returns the number of [Point](../../../sql-statements/geometry-constructors/geometry-constructors/point.md) objects in the [LineString](../../../sql-statements/geometry-constructors/geometry-constructors/linestring.md)\
value `ls`.

`ST_NumPoints()` and `NumPoints()` are synonyms.

## Examples

```sql
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT NumPoints(GeomFromText(@ls));
+------------------------------+
| NumPoints(GeomFromText(@ls)) |
+------------------------------+
|                            3 |
+------------------------------+
```

GPLv2 fill\_help\_tables.sql
