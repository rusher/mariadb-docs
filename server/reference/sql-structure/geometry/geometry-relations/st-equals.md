
# ST_EQUALS

## Syntax


```
ST_EQUALS(g1,g2)
```

## Description


Returns `1` or `0` to indicate whether geometry *`g1`* is spatially equal to geometry *`g2`*.


ST_EQUALS() uses object shapes, while [EQUALS()](equals.md), based on the original MySQL implementation, uses object bounding rectangles.


## Examples


```
SET @g1 = ST_GEOMFROMTEXT('LINESTRING(174 149, 176 151)');

SET @g2 = ST_GEOMFROMTEXT('LINESTRING(176 151, 174 149)');

SELECT ST_EQUALS(@g1,@g2);
+--------------------+
| ST_EQUALS(@g1,@g2) |
+--------------------+
|                  1 |
+--------------------+
```

```
SET @g1 = ST_GEOMFROMTEXT('POINT(0 2)');

SET @g1 = ST_GEOMFROMTEXT('POINT(2 0)');

SELECT ST_EQUALS(@g1,@g2);
+--------------------+
| ST_EQUALS(@g1,@g2) |
+--------------------+
|                  0 |
+--------------------+
```


CC BY-SA / Gnu FDL

