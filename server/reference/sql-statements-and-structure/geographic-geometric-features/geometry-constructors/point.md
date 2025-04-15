# POINT

#

# Syntax

```
Point(x,y)
```

#

# Description

Constructs a [WKB](../wkb/wkb-polyfromwkb.md) Point using the given coordinates.

#

# Examples

```
SET @g = ST_GEOMFROMTEXT('Point(1 1)');

CREATE TABLE gis_point (g POINT);
INSERT INTO gis_point VALUES
 (PointFromText('POINT(10 10)')),
 (PointFromText('POINT(20 10)')),
 (PointFromText('POINT(20 20)')),
 (PointFromWKB(AsWKB(PointFromText('POINT(10 20)'))));
```