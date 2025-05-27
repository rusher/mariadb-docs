
# ST_STARTPOINT

## Syntax


```
ST_StartPoint(ls)
StartPoint(ls)
```

## Description


Returns the [Point](../geometry-constructors/point.md) that is the start point of the
[LineString](../geometry-constructors/linestring.md) value `ls`.


`ST_StartPoint()` and `StartPoint()` are synonyms.


## Examples


```
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT AsText(StartPoint(GeomFromText(@ls)));
+---------------------------------------+
| AsText(StartPoint(GeomFromText(@ls))) |
+---------------------------------------+
| POINT(1 1)                            |
+---------------------------------------+
```


GPLv2 fill_help_tables.sql

