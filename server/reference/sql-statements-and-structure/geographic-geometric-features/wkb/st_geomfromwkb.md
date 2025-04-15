
# ST_GeomFromWKB

## Syntax


```
ST_GeomFromWKB(wkb[,srid])
ST_GeometryFromWKB(wkb[,srid])
GeomFromWKB(wkb[,srid])
GeometryFromWKB(wkb[,srid])
```

## Description


Constructs a geometry value of any type using its [WKB](well-known-binary-wkb-format.md) representation and SRID.


`<code>ST_GeomFromWKB()</code>`, `<code>ST_GeometryFromWKB()</code>`, `<code>GeomFromWKB()</code>` and `<code>GeometryFromWKB()</code>` are synonyms.


## Examples


```
SET @g = ST_AsBinary(ST_LineFromText('LINESTRING(0 4, 4 6)'));

SELECT ST_AsText(ST_GeomFromWKB(@g));
+-------------------------------+
| ST_AsText(ST_GeomFromWKB(@g)) |
+-------------------------------+
| LINESTRING(0 4,4 6)           |
+-------------------------------+
```
