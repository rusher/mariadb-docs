# LINESTRING

#

# Syntax

```
LineString(pt1,pt2,...)
```

#

# Description

Constructs a [WKB](../wkb/wkb-polyfromwkb.md) LineString value from a number of WKB [Point](../point-properties/point-properties-y.md) arguments. If any argument is not a WKB Point, the return value is
`NULL`. If the number of [Point](../point-properties/point-properties-y.md) arguments is less than two, the return value is `NULL`.

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

CREATE TABLE gis_line (g LINESTRING);
INSERT INTO gis_line VALUES
 (LineFromText('LINESTRING(0 0,0 10,10 0)')),
 (LineStringFromText('LINESTRING(10 10,20 10,20 20,10 20,10 10)')),
 (LineStringFromWKB(AsWKB(LineString(Point(10, 10), Point(40, 10)))));
```