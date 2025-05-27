
# ST_PolyFromText

## Syntax


```
ST_PolyFromText(wkt[,srid])
ST_PolygonFromText(wkt[,srid])
PolyFromText(wkt[,srid])
PolygonFromText(wkt[,srid])
```

## Description


Constructs a [POLYGON](../geometry-constructors/polygon.md) value using its [WKT](wkt-definition.md) representation and [SRID](../geometry-properties/st_srid.md).


`ST_PolyFromText()`, `ST_PolygonFromText()`, `PolyFromText()` and `ST_PolygonFromText()` are all synonyms.


## Examples


```
CREATE TABLE gis_polygon   (g POLYGON);
INSERT INTO gis_polygon VALUES
    (PolygonFromText('POLYGON((10 10,20 10,20 20,10 20,10 10))')),
    (PolyFromText('POLYGON((0 0,50 0,50 50,0 50,0 0), (10 10,20 10,20 20,10 20,10 10))'));
```


GPLv2 fill_help_tables.sql

