
# GLENGTH

## Syntax


```
GLength(ls)
```

## Description


Returns as a double-precision number the length of the
[LineString](../geometry-constructors/linestring.md) value *`ls`* in its associated spatial reference.


## Examples


```
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT GLength(GeomFromText(@ls));
+----------------------------+
| GLength(GeomFromText(@ls)) |
+----------------------------+
|           2.82842712474619 |
+----------------------------+
```

## See Also


* [ST_LENGTH()](../geometry-relations/st_length.md) is the OpenGIS equivalent.


GPLv2 fill_help_tables.sql

