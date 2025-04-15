
# ST_GEOMETRYTYPE

## Syntax


```
ST_GeometryType(g)
GeometryType(g)
```

## Description


Returns as a string the name of the geometry type of which the
geometry instance `<code>g</code>` is a member. The name corresponds to one of the
instantiable Geometry subclasses.


`<code>ST_GeometryType()</code>` and `<code>GeometryType()</code>` are synonyms.


## Examples


```
SELECT GeometryType(GeomFromText('POINT(1 1)'));
+------------------------------------------+
| GeometryType(GeomFromText('POINT(1 1)')) |
+------------------------------------------+
| POINT                                    |
+------------------------------------------+
```
