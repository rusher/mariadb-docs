
# ST_PolyFromWKB

## Syntax


```
ST_PolyFromWKB(wkb[,srid])
ST_PolygonFromWKB(wkb[,srid])
PolyFromWKB(wkb[,srid])
PolygonFromWKB(wkb[,srid])
```

## Description


Constructs a [POLYGON](../geometry-constructors/polygon.md) value using its [WKB](well-known-binary-wkb-format.md) representation and [SRID](../geometry-properties/st_srid.md).


`<code>ST_PolyFromWKB()</code>`, `<code>ST_PolygonFromWKB()</code>`, `<code>PolyFromWKB()</code>` and `<code>PolygonFromWKB()</code>` are synonyms.


## Examples


```
SET @g = ST_AsBinary(ST_PolyFromText('POLYGON((1 1,1 5,4 9,6 9,9 3,7 2,1 1))'));

SELECT ST_AsText(ST_PolyFromWKB(@g)) AS p;
+----------------------------------------+
| p                                      |
+----------------------------------------+
| POLYGON((1 1,1 5,4 9,6 9,9 3,7 2,1 1)) |
+----------------------------------------+
```
