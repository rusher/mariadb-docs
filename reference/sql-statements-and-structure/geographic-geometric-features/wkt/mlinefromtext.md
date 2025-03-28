# MLineFromText

#

# Syntax

```
MLineFromText(wkt[,srid])
MultiLineStringFromText(wkt[,srid])
```

#

# Description

Constructs a [MULTILINESTRING](../wkb/multilinestringfromwkb.md) value using its [WKT](wkt-definition.md) representation and [SRID](/en/srid/).

`MLineFromText()` and `MultiLineStringFromText()` are synonyms.

#

# Examples

```
CREATE TABLE gis_multi_line (g MULTILINESTRING);
SHOW FIELDS FROM gis_multi_line;
INSERT INTO gis_multi_line VALUES
 (MultiLineStringFromText('MULTILINESTRING((10 48,10 21,10 0),(16 0,16 23,16 48))')),
 (MLineFromText('MULTILINESTRING((10 48,10 21,10 0))')),
 (MLineFromWKB(AsWKB(MultiLineString(
 LineString(Point(1, 2), Point(3, 5)), 
 LineString(Point(2, 5), Point(5, 8), Point(21, 7))))));
```