# ST_POINTN

#

# Syntax

```
ST_PointN(ls,N)
PointN(ls,N)
```

#

# Description

Returns the N-th [Point](../point-properties/point-properties-y.md) in the [LineString](../wkb/linestringfromwkb.md) value `ls`.
Points are numbered beginning with `1`.

`ST_PointN()` and `PointN()` are synonyms.

#

# Examples

```
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT AsText(PointN(GeomFromText(@ls),2));
+-------------------------------------+
| AsText(PointN(GeomFromText(@ls),2)) |
+-------------------------------------+
| POINT(2 2) |
+-------------------------------------+
```