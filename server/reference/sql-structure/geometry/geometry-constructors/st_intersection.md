
# ST_INTERSECTION

## Syntax


```
ST_INTERSECTION(g1,g2)
```

## Description


Returns a geometry that is the intersection, or shared portion, of geometry *`g1`* and geometry *`g2`*.


## Examples


```
SET @g1 = ST_GEOMFROMTEXT('POINT(2 1)');

SET @g2 = ST_GEOMFROMTEXT('LINESTRING(2 1, 0 2)');

SELECT ASTEXT(ST_INTERSECTION(@g1,@g2));
+----------------------------------+
| ASTEXT(ST_INTERSECTION(@g1,@g2)) |
+----------------------------------+
| POINT(2 1)                       |
+----------------------------------+
```


CC BY-SA / Gnu FDL

