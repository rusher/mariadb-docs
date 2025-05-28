---
icon: earth-africa
---

# ST\_AsText

## Syntax

```sql
ST_AsText(g)
AsText(g)
ST_AsWKT(g)
AsWKT(g)
```

## Description

Converts a value in internal geometry format to its [WKT](wkt-definition.md) representation and returns the string result.

`ST_AsText()`, `AsText()`, `ST_AsWKT()` and `AsWKT()` are all synonyms.

## Examples

```sql
SET @g = 'LineString(1 1,4 4,6 6)';

SELECT ST_AsText(ST_GeomFromText(@g));
+--------------------------------+
| ST_AsText(ST_GeomFromText(@g)) |
+--------------------------------+
| LINESTRING(1 1,4 4,6 6)        |
+--------------------------------+
```

GPLv2 fill\_help\_tables.sql
