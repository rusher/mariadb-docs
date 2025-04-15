# ST_ENDPOINT

#

# Syntax

```
ST_EndPoint(ls)
EndPoint(ls)
```

#

# Description

Returns the [Point](../point-properties/point-properties-y.md) that is the endpoint of the
[LineString](../wkb/linestringfromwkb.md) value `ls`.

`ST_EndPoint()` and `EndPoint()` are synonyms.

#

# Examples

```
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT AsText(EndPoint(GeomFromText(@ls)));
+-------------------------------------+
| AsText(EndPoint(GeomFromText(@ls))) |
+-------------------------------------+
| POINT(3 3) |
+-------------------------------------+
```