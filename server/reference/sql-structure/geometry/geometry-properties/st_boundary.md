# ST\_BOUNDARY

## Syntax

```sql
ST_BOUNDARY(g)
BOUNDARY(g)
```

## Description

Returns a geometry that is the closure of the combinatorial boundary of the geometry value _`g`_.

BOUNDARY() is a synonym.

## Examples

```sql
SELECT ST_AsText(ST_Boundary(ST_GeomFromText('LINESTRING(3 3,0 0, -3 3)')));
+----------------------------------------------------------------------+
| ST_AsText(ST_Boundary(ST_GeomFromText('LINESTRING(3 3,0 0, -3 3)'))) |
+----------------------------------------------------------------------+
| MULTIPOINT(3 3,-3 3)                                                 |
+----------------------------------------------------------------------+

SELECT ST_AsText(ST_Boundary(ST_GeomFromText('POLYGON((3 3,0 0, -3 3, 3 3))')));
+--------------------------------------------------------------------------+
| ST_AsText(ST_Boundary(ST_GeomFromText('POLYGON((3 3,0 0, -3 3, 3 3))'))) |
+--------------------------------------------------------------------------+
| LINESTRING(3 3,0 0,-3 3,3 3)                                             |
+--------------------------------------------------------------------------+
```

GPLv2 fill\_help\_tables.sql
