
# ST_INTERSECTS

## Syntax


```
ST_INTERSECTS(g1,g2)
```

## Description


Returns `<code>1</code>` or `<code>0</code>` to indicate whether geometry *`<code>g1</code>`* spatially intersects geometry *`<code>g2</code>`*.


ST_INTERSECTS() uses object shapes, while [INTERSECTS()](intersects.md), based on the original MySQL implementation, uses object bounding rectangles.


ST_INTERSECTS() tests the opposite relationship to [ST_DISJOINT()](st_disjoint.md).


## Examples


```
SET @g1 = ST_GEOMFROMTEXT('POINT(0 0)');

SET @g2 = ST_GEOMFROMTEXT('LINESTRING(0 0, 0 2)');

SELECT ST_INTERSECTS(@g1,@g2);
+------------------------+
| ST_INTERSECTS(@g1,@g2) |
+------------------------+
|                      1 |
+------------------------+
```

```
SET @g2 = ST_GEOMFROMTEXT('LINESTRING(2 0, 0 2)');

SELECT ST_INTERSECTS(@g1,@g2);
+------------------------+
| ST_INTERSECTS(@g1,@g2) |
+------------------------+
|                      0 |
+------------------------+
```
