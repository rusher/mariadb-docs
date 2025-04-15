
# ST_AsText

## Syntax


```
ST_AsText(g)
AsText(g)
ST_AsWKT(g)
AsWKT(g)
```

## Description


Converts a value in internal geometry format to its [WKT](wkt-definition.md) representation and returns the string result.


`<code>ST_AsText()</code>`, `<code>AsText()</code>`, `<code>ST_AsWKT()</code>` and `<code>AsWKT()</code>` are all synonyms.


## Examples


```
SET @g = 'LineString(1 1,4 4,6 6)';

SELECT ST_AsText(ST_GeomFromText(@g));
+--------------------------------+
| ST_AsText(ST_GeomFromText(@g)) |
+--------------------------------+
| LINESTRING(1 1,4 4,6 6)        |
+--------------------------------+
```
