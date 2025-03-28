# ST_LineFromText

#

# Syntax

```
ST_LineFromText(wkt[,srid])
ST_LineStringFromText(wkt[,srid])
LineFromText(wkt[,srid])
LineStringFromText(wkt[,srid])
```

#

# Description

Constructs a [LINESTRING](../wkb/linestringfromwkb.md) value using its [WKT](wkt-definition.md) representation and [SRID](/en/srid/).

`ST_LineFromText()`, `ST_LineStringFromText()`, `ST_LineFromText()` and `ST_LineStringFromText()` are all synonyms.

#

# Examples

```
CREATE TABLE gis_line (g LINESTRING);
SHOW FIELDS FROM gis_line;
INSERT INTO gis_line VALUES
 (LineFromText('LINESTRING(0 0,0 10,10 0)')),
 (LineStringFromText('LINESTRING(10 10,20 10,20 20,10 20,10 10)')),
 (LineStringFromWKB(AsWKB(LineString(Point(10, 10), Point(40, 10)))));
```