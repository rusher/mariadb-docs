
# ST_GeomCollFromWKB

## Syntax


```
ST_GeomCollFromWKB(wkb[,srid])
ST_GeometryCollectionFromWKB(wkb[,srid])
GeomCollFromWKB(wkb[,srid])
GeometryCollectionFromWKB(wkb[,srid])
```

## Description


Constructs a GEOMETRYCOLLECTION value using its [WKB](well-known-binary-wkb-format.md) representation and SRID.


`<code>ST_GeomCollFromWKB()</code>`, `<code>ST_GeometryCollectionFromWKB()</code>`, `<code>GeomCollFromWKB()</code>` and `<code>GeometryCollectionFromWKB()</code>` are synonyms.


## Examples


```
SET @g = ST_AsBinary(ST_GeomFromText('GEOMETRYCOLLECTION(
   POLYGON((5 5,10 5,10 10,5 5)),POINT(10 10))'));

SELECT ST_AsText(ST_GeomCollFromWKB(@g));
+----------------------------------------------------------------+
| ST_AsText(ST_GeomCollFromWKB(@g))                              |
+----------------------------------------------------------------+
| GEOMETRYCOLLECTION(POLYGON((5 5,10 5,10 10,5 5)),POINT(10 10)) |
+----------------------------------------------------------------+
```
