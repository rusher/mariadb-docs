
# CROSSES

## Syntax


```
Crosses(g1,g2)
```

## Description


Returns `<code>1</code>` if `<code>g1</code>` spatially crosses `<code>g2</code>`. Returns `<code>NULL</code>` if `<code>g1</code>` is
a [Polygon](../geometry-constructors/polygon.md) or a [MultiPolygon](../geometry-constructors/multipolygon.md), or if `<code>g2</code>` is a
[Point](../geometry-constructors/point.md) or a [MultiPoint](../geometry-constructors/multipoint.md). Otherwise, returns `<code>0</code>`.


The term spatially crosses denotes a spatial relation between two
given geometries that has the following properties:


* The two geometries intersect
* Their intersection results in a geometry that has a dimension that is one
 less than the maximum dimension of the two given geometries
* Their intersection is not equal to either of the two given geometries


CROSSES() is based on the original MySQL implementation, and uses object bounding rectangles, while [ST_CROSSES()](st-crosses.md) uses object shapes.

