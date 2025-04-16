
# ST_DIMENSION

## Syntax


```
ST_Dimension(g)
Dimension(g)
```

## Description


Returns the inherent dimension of the geometry value *`g`*. The result can
be



| Dimension | Definition |
| --- | --- |
| Dimension | Definition |
| -1 | empty geometry |
| 0 | geometry with no length or area |
| 1 | geometry with no area but nonzero length |
| 2 | geometry with nonzero area |



`ST_Dimension()` and `Dimension()` are synonyms.


## Examples


```
SELECT Dimension(GeomFromText('LineString(1 1,2 2)'));
+------------------------------------------------+
| Dimension(GeomFromText('LineString(1 1,2 2)')) |
+------------------------------------------------+
|                                              1 |
+------------------------------------------------+
```
