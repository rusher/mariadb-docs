
# ST_CONTAINS

## Syntax


```
ST_CONTAINS(g1,g2)
```

## Description


Returns `1` or `0` to indicate whether a geometry `g1` completely contains geometry `g2`.


ST_CONTAINS() uses object shapes, while [CONTAINS()](contains.md), based on the original MySQL implementation, uses object bounding rectangles.


ST_CONTAINS tests the opposite relationship to [ST_WITHIN()](st-within.md).


## Examples


```
SET @g1 = ST_GEOMFROMTEXT('POLYGON((175 150, 20 40, 50 60, 125 100, 175 150))');

SET @g2 = ST_GEOMFROMTEXT('POINT(174 149)');

SELECT ST_CONTAINS(@g1,@g2);
+----------------------+
| ST_CONTAINS(@g1,@g2) |
+----------------------+
|                    1 |
+----------------------+

SET @g2 = ST_GEOMFROMTEXT('POINT(175 151)');

SELECT ST_CONTAINS(@g1,@g2);
+----------------------+
| ST_CONTAINS(@g1,@g2) |
+----------------------+
|                    0 |
+----------------------+
```


CC BY-SA / Gnu FDL

