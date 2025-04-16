
# ST_LineFromWKB

## Syntax


```
ST_LineFromWKB(wkb[,srid])
LineFromWKB(wkb[,srid])
ST_LineStringFromWKB(wkb[,srid])
LineStringFromWKB(wkb[,srid])
```

## Description


Constructs a LINESTRING value using its [WKB](well-known-binary-wkb-format.md) representation and SRID.


`ST_LineFromWKB()`, `LineFromWKB()`, `ST_LineStringFromWKB()`, and `LineStringFromWKB()` are synonyms.


## Examples


```
SET @g = ST_AsBinary(ST_LineFromText('LineString(0 4,4 6)'));

SELECT ST_AsText(ST_LineFromWKB(@g)) AS l;
+---------------------+
| l                   |
+---------------------+
| LINESTRING(0 4,4 6) |
+---------------------+
```
