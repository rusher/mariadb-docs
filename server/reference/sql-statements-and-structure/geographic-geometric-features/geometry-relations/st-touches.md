
# ST_TOUCHES

## Syntax


```
ST_TOUCHES(g1,g2)
```

## Description


Returns `1` or `0` to indicate whether geometry *`g1`* spatially touches geometry *`g2`*. Two geometries spatially touch if the interiors of the geometries do not intersect,
but the boundary of one of the geometries intersects either the boundary or the
interior of the other.


ST_TOUCHES() uses object shapes, while [TOUCHES()](touches.md), based on the original MySQL implementation, uses object bounding rectangles.


## Examples


```
SET @g1 = ST_GEOMFROMTEXT('POINT(2 0)');

SET @g2 = ST_GEOMFROMTEXT('LINESTRING(2 0, 0 2)');

SELECT ST_TOUCHES(@g1,@g2);
+---------------------+
| ST_TOUCHES(@g1,@g2) |
+---------------------+
|                   1 |
+---------------------+

SET @g1 = ST_GEOMFROMTEXT('POINT(2 1)');

SELECT ST_TOUCHES(@g1,@g2);
+---------------------+
| ST_TOUCHES(@g1,@g2) |
+---------------------+
|                   0 |
+---------------------+
```


CC BY-SA / Gnu FDL

