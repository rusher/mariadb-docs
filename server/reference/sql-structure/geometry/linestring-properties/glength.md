---
icon: earth-africa
---

# GLENGTH

## Syntax

```sql
GLength(ls)
```

## Description

Returns as a double-precision number the length of the[LineString](../../../sql-statements/geometry-constructors/geometry-constructors/linestring.md) value _`ls`_ in its associated spatial reference.

## Examples

```sql
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT GLength(GeomFromText(@ls));
+----------------------------+
| GLength(GeomFromText(@ls)) |
+----------------------------+
|           2.82842712474619 |
+----------------------------+
```

## See Also

* [ST\_LENGTH()](../geometry-relations/st_length.md) is the OpenGIS equivalent.

GPLv2 fill\_help\_tables.sql
