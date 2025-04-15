
# ST_GeomCollFromText

## Syntax


```
ST_GeomCollFromText(wkt[,srid])
ST_GeometryCollectionFromText(wkt[,srid])
GeomCollFromText(wkt[,srid])
GeometryCollectionFromText(wkt[,srid])
```

## Description


Constructs a [GEOMETRYCOLLECTION](../geometry-constructors/geometrycollection.md) value using its [WKT](wkt-definition.md) 
representation and [SRID](../geometry-properties/st_srid.md).


`<code>ST_GeomCollFromText()</code>`, `<code>ST_GeometryCollectionFromText()</code>`, `<code>GeomCollFromText()</code>` and `<code>GeometryCollectionFromText()</code>` are all synonyms.


## Example


```
CREATE TABLE gis_geometrycollection  (g GEOMETRYCOLLECTION);
SHOW FIELDS FROM gis_geometrycollection;
INSERT INTO gis_geometrycollection VALUES
    (GeomCollFromText('GEOMETRYCOLLECTION(POINT(0 0), LINESTRING(0 0,10 10))')),
    (GeometryFromWKB(AsWKB(GeometryCollection(Point(44, 6), LineString(Point(3, 6), Point(7, 9)))))),
    (GeomFromText('GeometryCollection()')),
    (GeomFromText('GeometryCollection EMPTY'));
```
