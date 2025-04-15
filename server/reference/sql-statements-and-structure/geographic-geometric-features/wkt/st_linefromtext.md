
# ST_LineFromText

## Syntax


```
ST_LineFromText(wkt[,srid])
ST_LineStringFromText(wkt[,srid])
LineFromText(wkt[,srid])
LineStringFromText(wkt[,srid])
```

## Description


Constructs a [LINESTRING](../geometry-constructors/linestring.md) value using its [WKT](wkt-definition.md) representation and [SRID](../geometry-properties/st_srid.md).


`<code>ST_LineFromText()</code>`, `<code>ST_LineStringFromText()</code>`, `<code>ST_LineFromText()</code>` and `<code>ST_LineStringFromText()</code>` are all synonyms.


## Examples


```
CREATE TABLE gis_line  (g LINESTRING);
SHOW FIELDS FROM gis_line;
INSERT INTO gis_line VALUES
    (LineFromText('LINESTRING(0 0,0 10,10 0)')),
    (LineStringFromText('LINESTRING(10 10,20 10,20 20,10 20,10 10)')),
    (LineStringFromWKB(AsWKB(LineString(Point(10, 10), Point(40, 10)))));
```
