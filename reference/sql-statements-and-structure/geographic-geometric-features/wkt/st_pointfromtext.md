# ST_PointFromText

#

# Syntax

```
ST_PointFromText(wkt[,srid])
PointFromText(wkt[,srid])
```

#

# Description

Constructs a [POINT](../point-properties/point-properties-y.md) value using its [WKT](wkt-definition.md) representation and [SRID](/en/srid/).

`ST_PointFromText()` and `PointFromText()` are synonyms.

#

# Examples

```
CREATE TABLE gis_point (g POINT);
SHOW FIELDS FROM gis_point;
INSERT INTO gis_point VALUES
 (PointFromText('POINT(10 10)')),
 (PointFromText('POINT(20 10)')),
 (PointFromText('POINT(20 20)')),
 (PointFromWKB(AsWKB(PointFromText('POINT(10 20)'))));
```