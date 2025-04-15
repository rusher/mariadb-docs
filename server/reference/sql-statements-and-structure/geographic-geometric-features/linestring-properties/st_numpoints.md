
# ST_NUMPOINTS

## Syntax


```
ST_NumPoints(ls)
NumPoints(ls)
```

## Description


Returns the number of [Point](../geometry-constructors/point.md) objects in the [LineString](../geometry-constructors/linestring.md)
value `<code>ls</code>`.


`<code>ST_NumPoints()</code>` and `<code>NumPoints()</code>` are synonyms.


## Examples


```
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT NumPoints(GeomFromText(@ls));
+------------------------------+
| NumPoints(GeomFromText(@ls)) |
+------------------------------+
|                            3 |
+------------------------------+
```
