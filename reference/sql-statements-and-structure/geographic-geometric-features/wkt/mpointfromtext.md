# MPointFromText

#

# Syntax

```
MPointFromText(wkt[,srid])
MultiPointFromText(wkt[,srid])
```

#

# Description

Constructs a [MULTIPOINT](../wkb/multipointfromwkb.md) value using its [WKT](wkt-definition.md) representation and [SRID](/en/srid/).

`MPointFromText()` and `MultiPointFromText()` are synonyms.

#

# Examples

```
CREATE TABLE gis_multi_point (g MULTIPOINT);
SHOW FIELDS FROM gis_multi_point;
INSERT INTO gis_multi_point VALUES
 (MultiPointFromText('MULTIPOINT(0 0,10 10,10 20,20 20)')),
 (MPointFromText('MULTIPOINT(1 1,11 11,11 21,21 21)')),
 (MPointFromWKB(AsWKB(MultiPoint(Point(3, 6), Point(4, 10)))));
```