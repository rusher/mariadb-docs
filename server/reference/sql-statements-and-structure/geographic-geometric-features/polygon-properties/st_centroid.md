
# ST_CENTROID

## Syntax


```
ST_Centroid(mpoly)
Centroid(mpoly)
```

## Description


Returns a point reflecting the mathematical centroid (geometric center) for the [MultiPolygon](../geometry-constructors/multipolygon.md) *mpoly*. The resulting point will not necessarily be on the MultiPolygon.


`ST_Centroid()` and `Centroid()` are synonyms.


## Examples


```
SET @poly = ST_GeomFromText('POLYGON((0 0,20 0,20 20,0 20,0 0))');
SELECT ST_AsText(ST_Centroid(@poly)) AS center;
+--------------+
| center       |
+--------------+
| POINT(10 10) |
+--------------+
```


CC BY-SA / Gnu FDL

