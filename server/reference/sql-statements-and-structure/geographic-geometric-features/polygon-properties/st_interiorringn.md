
# ST_InteriorRingN

## Syntax


```
ST_InteriorRingN(poly,N)
InteriorRingN(poly,N)
```

## Description


Returns the N-th interior ring for the Polygon value `<code>poly</code>` as a LineString. Rings are numbered beginning with 1.


`<code>ST_InteriorRingN()</code>` and `<code>InteriorRingN()</code>` are synonyms.


## Examples


```
SET @poly = 'Polygon((0 0,0 3,3 3,3 0,0 0),(1 1,1 2,2 2,2 1,1 1))';

SELECT AsText(InteriorRingN(GeomFromText(@poly),1));
+----------------------------------------------+
| AsText(InteriorRingN(GeomFromText(@poly),1)) |
+----------------------------------------------+
| LINESTRING(1 1,1 2,2 2,2 1,1 1)              |
+----------------------------------------------+
```
