# ST_STARTPOINT

#

# Syntax

```
ST_StartPoint(ls)
StartPoint(ls)
```

#

# Description

Returns the [Point](../point-properties/point-properties-y.md) that is the start point of the
[LineString](../wkb/linestringfromwkb.md) value `ls`.

`ST_StartPoint()` and `StartPoint()` are synonyms.

#

# Examples

```
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT AsText(StartPoint(GeomFromText(@ls)));
+---------------------------------------+
| AsText(StartPoint(GeomFromText(@ls))) |
+---------------------------------------+
| POINT(1 1) |
+---------------------------------------+
```