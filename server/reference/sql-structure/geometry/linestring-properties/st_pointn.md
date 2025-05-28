---
icon: earth-africa
---

# ST\_POINTN

## Syntax

```sql
ST_PointN(ls,N)
PointN(ls,N)
```

## Description

Returns the N-th [Point](../../../sql-statements/geometry-constructors/geometry-constructors/point.md) in the [LineString](../../../sql-statements/geometry-constructors/geometry-constructors/linestring.md) value `ls`.\
Points are numbered beginning with `1`.

`ST_PointN()` and `PointN()` are synonyms.

## Examples

```sql
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT AsText(PointN(GeomFromText(@ls),2));
+-------------------------------------+
| AsText(PointN(GeomFromText(@ls),2)) |
+-------------------------------------+
| POINT(2 2)                          |
+-------------------------------------+
```

GPLv2 fill\_help\_tables.sql
