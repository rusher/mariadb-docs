
# ST_GEOMETRYN

## Syntax


```
ST_GeometryN(gc,N)
GeometryN(gc,N)
```

## Description


Returns the N-th geometry in the GeometryCollection *`<code>gc</code>`.* Geometries are numbered beginning with 1.


`<code>ST_GeometryN()</code>` and `<code>GeometryN()</code>` are synonyms.


## Example


```
SET @gc = 'GeometryCollection(Point(1 1),LineString(12 14, 9 11))';

SELECT AsText(GeometryN(GeomFromText(@gc),1));
+----------------------------------------+
| AsText(GeometryN(GeomFromText(@gc),1)) |
+----------------------------------------+
| POINT(1 1)                             |
+----------------------------------------+
```
