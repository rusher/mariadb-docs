
# ST_POINTN

## Syntax


```
ST_PointN(ls,N)
PointN(ls,N)
```

## Description


Returns the N-th [Point](../geometry-constructors/point.md) in the [LineString](../geometry-constructors/linestring.md) value `ls`.
Points are numbered beginning with `1`.


`ST_PointN()` and `PointN()` are synonyms.


## Examples


```
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT AsText(PointN(GeomFromText(@ls),2));
+-------------------------------------+
| AsText(PointN(GeomFromText(@ls),2)) |
+-------------------------------------+
| POINT(2 2)                          |
+-------------------------------------+
```


GPLv2 fill_help_tables.sql

