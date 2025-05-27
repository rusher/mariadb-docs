
# ST_ENDPOINT

## Syntax


```
ST_EndPoint(ls)
EndPoint(ls)
```

## Description


Returns the [Point](../geometry-constructors/point.md) that is the endpoint of the
[LineString](../geometry-constructors/linestring.md) value `ls`.


`ST_EndPoint()` and `EndPoint()` are synonyms.


## Examples


```
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT AsText(EndPoint(GeomFromText(@ls)));
+-------------------------------------+
| AsText(EndPoint(GeomFromText(@ls))) |
+-------------------------------------+
| POINT(3 3)                          |
+-------------------------------------+
```


GPLv2 fill_help_tables.sql

