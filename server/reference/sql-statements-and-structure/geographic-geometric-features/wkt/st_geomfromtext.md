
# ST_GeomFromText

## Syntax


```
ST_GeomFromText(wkt[,srid])
ST_GeometryFromText(wkt[,srid])
GeomFromText(wkt[,srid])
GeometryFromText(wkt[,srid])

ST_MultiLineStringFromText(wkt[,srid])
ST_MLineFromText(wkt[,srid])
ST_MPointFromText(wkt[,srid])
ST_MultiPointFromText(wkt[,srid])
```

## Description


Constructs a geometry value of any type using its [WKT](wkt-definition.md) representation and [SRID](../geometry-properties/st_srid.md).


`<code>GeomFromText()</code>`, `<code>GeometryFromText()</code>`, `<code>ST_GeomFromText()</code>`, `<code>ST_GeometryFromText()</code>`, `<code>ST_MultiLineStringFromText</code>`, `<code>ST_MLineFromText</code>`, `<code>ST_MultiPolyFromText</code>` and `<code>ST_MPolygonFromText</code>` are all synonyms.


## Example


```
SET @g = ST_GEOMFROMTEXT('POLYGON((1 1,1 5,4 9,6 9,9 3,7 2,1 1))');
```
