
# ST_INTERSECTION

## Syntax


```
ST_INTERSECTION(g1,g2)
```

## Description


Returns a geometry that is the intersection, or shared portion, of geometry *`<code>g1</code>`* and geometry *`<code>g2</code>`*.


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
