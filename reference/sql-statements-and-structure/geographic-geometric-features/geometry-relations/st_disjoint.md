# ST_DISJOINT

#

# Syntax

```
ST_DISJOINT(g1,g2)
```

#

# Description

Returns `1` or `0` to indicate whether geometry *`g1`* is spatially disjoint from
(does not intersect with) geometry *`g2`*.

ST_DISJOINT() uses object shapes, while [DISJOINT()](disjoint.md), based on the original MySQL implementation, uses object bounding rectangles.

ST_DISJOINT() tests the opposite relationship to [ST_INTERSECTS()](/en/st_intersects/).

#

# Examples

```
SET @g1 = ST_GEOMFROMTEXT('POINT(0 0)');

SET @g2 = ST_GEOMFROMTEXT('LINESTRING(2 0, 0 2)');

SELECT ST_DISJOINT(@g1,@g2);
+----------------------+
| ST_DISJOINT(@g1,@g2) |
+----------------------+
| 1 |
+----------------------+

SET @g2 = ST_GEOMFROMTEXT('LINESTRING(0 0, 0 2)');

SELECT ST_DISJOINT(@g1,@g2);
+----------------------+
| ST_DISJOINT(@g1,@g2) |
+----------------------+
| 0 |
+----------------------+
```