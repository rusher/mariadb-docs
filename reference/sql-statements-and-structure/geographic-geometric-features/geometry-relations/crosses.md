# CROSSES

#

# Syntax

```
Crosses(g1,g2)
```

#

# Description

Returns `1` if `g1` spatially crosses `g2`. Returns `NULL` if `g1` is
a [Polygon](../wkb/polygonfromwkb.md) or a [MultiPolygon](../wkb/multipolygonfromwkb.md), or if `g2` is a
[Point](../point-properties/point-properties-y.md) or a [MultiPoint](../wkb/multipointfromwkb.md). Otherwise, returns `0`.

The term spatially crosses denotes a spatial relation between two
given geometries that has the following properties:

* The two geometries intersect
* Their intersection results in a geometry that has a dimension that is one
 less than the maximum dimension of the two given geometries
* Their intersection is not equal to either of the two given geometries

CROSSES() is based on the original MySQL implementation, and uses object bounding rectangles, while [ST_CROSSES()](/en/st_crosses/) uses object shapes.