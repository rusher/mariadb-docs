
# ST_X

## Syntax


```
ST_X(p)
X(p)
```

## Description


Returns the X-coordinate value for the point `<code>p</code>` as a double-precision number.


`<code>ST_X()</code>` and `<code>X()</code>` are synonyms.


## Examples


```
SET @pt = 'Point(56.7 53.34)';

SELECT X(GeomFromText(@pt));
+----------------------+
| X(GeomFromText(@pt)) |
+----------------------+
|                 56.7 |
+----------------------+
```
