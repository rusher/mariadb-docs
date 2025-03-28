# ST_NUMPOINTS

#

# Syntax

```
ST_NumPoints(ls)
NumPoints(ls)
```

#

# Description

Returns the number of [Point](../point-properties/point-properties-y.md) objects in the [LineString](../wkb/linestringfromwkb.md)
value `ls`.

`ST_NumPoints()` and `NumPoints()` are synonyms.

#

# Examples

```
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT NumPoints(GeomFromText(@ls));
+------------------------------+
| NumPoints(GeomFromText(@ls)) |
+------------------------------+
| 3 |
+------------------------------+
```