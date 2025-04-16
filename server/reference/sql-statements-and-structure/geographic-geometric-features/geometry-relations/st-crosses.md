
# ST_CROSSES

## Syntax


```
ST_CROSSES(g1,g2)
```

## Description


Returns `1` if geometry *`g1`* spatially crosses geometry *`g2`*. Returns `NULL` if `g1` is a [Polygon](../geometry-constructors/polygon.md) or a [MultiPolygon](../geometry-constructors/multipolygon.md), or if `g2` is a
[Point](../geometry-constructors/point.md) or a [MultiPoint](../geometry-constructors/multipoint.md). Otherwise, returns `0`.


The term spatially crosses denotes a spatial relation between two
given geometries that has the following properties:


* The two geometries intersect
* Their intersection results in a geometry that has a dimension that is one
 less than the maximum dimension of the two given geometries
* Their intersection is not equal to either of the two given geometries


ST_CROSSES() uses object shapes, while [CROSSES()](crosses.md), based on the original MySQL implementation, uses object bounding rectangles.


## Examples


```
SET @g1 = ST_GEOMFROMTEXT('LINESTRING(174 149, 176 151)');

SET @g2 = ST_GEOMFROMTEXT('POLYGON((175 150, 20 40, 50 60, 125 100, 175 150))');

SELECT ST_CROSSES(@g1,@g2);
+---------------------+
| ST_CROSSES(@g1,@g2) |
+---------------------+
|                   1 |
+---------------------+

SET @g1 = ST_GEOMFROMTEXT('LINESTRING(176 149, 176 151)');

SELECT ST_CROSSES(@g1,@g2);
+---------------------+
| ST_CROSSES(@g1,@g2) |
+---------------------+
|                   0 |
+---------------------+
```
