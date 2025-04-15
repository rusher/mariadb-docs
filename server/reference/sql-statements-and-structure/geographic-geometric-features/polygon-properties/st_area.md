
# ST_AREA

## Syntax


```
ST_Area(poly)
Area(poly)
```

## Description


Returns as a double-precision number the area of the Polygon value `<code>poly</code>`, as measured in its spatial reference system.


`<code>ST_Area()</code>` and `<code>Area()</code>` are synonyms.


## Examples


```
SET @poly = 'Polygon((0 0,0 3,3 0,0 0),(1 1,1 2,2 1,1 1))';

SELECT Area(GeomFromText(@poly));
+---------------------------+
| Area(GeomFromText(@poly)) |
+---------------------------+
|                         4 |
+---------------------------+
```
