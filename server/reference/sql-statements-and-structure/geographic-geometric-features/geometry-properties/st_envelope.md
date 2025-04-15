
# ST_ENVELOPE

## Syntax


```
ST_ENVELOPE(g)
ENVELOPE(g)
```

## Description


Returns the Minimum Bounding Rectangle (MBR) for the geometry value `<code>g</code>`. The result is returned as a Polygon value.


The polygon is defined by the corner points of the bounding box:


```
POLYGON((MINX MINY, MAXX MINY, MAXX MAXY, MINX MAXY, MINX MINY))
```

`<code>ST_ENVELOPE()</code>` and `<code>ENVELOPE()</code>` are synonyms.


## Examples


```
SELECT AsText(ST_ENVELOPE(GeomFromText('LineString(1 1,4 4)')));
+----------------------------------------------------------+
| AsText(ST_ENVELOPE(GeomFromText('LineString(1 1,4 4)'))) |
+----------------------------------------------------------+
| POLYGON((1 1,4 1,4 4,1 4,1 1))                           |
+----------------------------------------------------------+
```
