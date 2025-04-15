
# ST_ExteriorRing

## Syntax


```
ST_ExteriorRing(poly)
ExteriorRing(poly)
```

## Description


Returns the exterior ring of the Polygon value `<code>poly</code>` as a LineString.


`<code>ST_ExteriorRing()</code>` and `<code>ExteriorRing()</code>` are synonyms.


## Examples


```
SET @poly = 'Polygon((0 0,0 3,3 3,3 0,0 0),(1 1,1 2,2 2,2 1,1 1))';

SELECT AsText(ExteriorRing(GeomFromText(@poly)));
+-------------------------------------------+
| AsText(ExteriorRing(GeomFromText(@poly))) |
+-------------------------------------------+
| LINESTRING(0 0,0 3,3 3,3 0,0 0)           |
+-------------------------------------------+
```
