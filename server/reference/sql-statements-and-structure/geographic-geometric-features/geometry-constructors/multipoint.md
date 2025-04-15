# MULTIPOINT

#

# Syntax

```
MultiPoint(pt1,pt2,...)
```

#

# Description

Constructs a [WKB](../wkb/wkb-polyfromwkb.md) MultiPoint value using WKB [Point](../point-properties/point-properties-y.md) arguments. If any argument is not a WKB Point, the return value is `NULL`.

#

# Examples

```
SET @g = ST_GEOMFROMTEXT('MultiPoint( 1 1, 2 2, 5 3, 7 2, 9 3, 8 4, 6 6, 6 9, 4 9, 1 5 )');

CREATE TABLE gis_multi_point (g MULTIPOINT);
INSERT INTO gis_multi_point VALUES
 (MultiPointFromText('MULTIPOINT(0 0,10 10,10 20,20 20)')),
 (MPointFromText('MULTIPOINT(1 1,11 11,11 21,21 21)')),
 (MPointFromWKB(AsWKB(MultiPoint(Point(3, 6), Point(4, 10)))));
```