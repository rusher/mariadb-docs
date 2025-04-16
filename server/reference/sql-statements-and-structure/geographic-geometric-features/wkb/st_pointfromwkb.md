
# ST_PointFromWKB

## Syntax


```
ST_PointFromWKB(wkb[,srid])
PointFromWKB(wkb[,srid])
```

## Description


Constructs a [POINT](../geometry-constructors/point.md) value using its [WKB](well-known-binary-wkb-format.md) representation and [SRID](../geometry-properties/st_srid.md).


`ST_PointFromWKB()` and `PointFromWKB()` are synonyms.


## Examples


```
SET @g = ST_AsBinary(ST_PointFromText('POINT(0 4)'));

SELECT ST_AsText(ST_PointFromWKB(@g)) AS p;
+------------+
| p          |
+------------+
| POINT(0 4) |
+------------+
```
