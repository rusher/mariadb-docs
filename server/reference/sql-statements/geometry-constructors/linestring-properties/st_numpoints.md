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

Returns the number of [Point](../point.md) objects in the [LineString](../linestring.md)\
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
