
# ST_NUMGEOMETRIES

## Syntax


```
ST_NumGeometries(gc)
NumGeometries(gc)
```

## Description


Returns the number of geometries in the GeometryCollection `<code>gc</code>`.


`<code>ST_NumGeometries()</code>` and `<code>NumGeometries()</code>` are synonyms.


## Example


```
SET @gc = 'GeometryCollection(Point(1 1),LineString(2 2, 3 3))';

SELECT NUMGEOMETRIES(GeomFromText(@gc));
+----------------------------------+
| NUMGEOMETRIES(GeomFromText(@gc)) |
+----------------------------------+
|                                2 |
+----------------------------------+
```
