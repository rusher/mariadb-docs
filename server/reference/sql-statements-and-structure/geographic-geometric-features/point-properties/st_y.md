
# ST_Y

## Syntax


```
ST_Y(p)
Y(p)
```

## Description


Returns the Y-coordinate value for the point p as a double-precision number.


`ST_Y()` and `Y()` are synonyms.


## Examples


```
SET @pt = 'Point(56.7 53.34)';

SELECT Y(GeomFromText(@pt));
+----------------------+
| Y(GeomFromText(@pt)) |
+----------------------+
|                53.34 |
+----------------------+
```
