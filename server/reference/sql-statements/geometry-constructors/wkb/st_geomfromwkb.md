---
icon: earth-africa
---

# ST\_GeomFromWKB

## Syntax

```sql
ST_GeomFromWKB(wkb[,srid])
ST_GeometryFromWKB(wkb[,srid])
GeomFromWKB(wkb[,srid])
GeometryFromWKB(wkb[,srid])
```

## Description

Constructs a geometry value of any type using its [WKB](well-known-binary-wkb-format.md) representation and SRID.

`ST_GeomFromWKB()`, `ST_GeometryFromWKB()`, `GeomFromWKB()` and `GeometryFromWKB()` are synonyms.

## Examples

```sql
SET @g = ST_AsBinary(ST_LineFromText('LINESTRING(0 4, 4 6)'));

SELECT ST_AsText(ST_GeomFromWKB(@g));
+-------------------------------+
| ST_AsText(ST_GeomFromWKB(@g)) |
+-------------------------------+
| LINESTRING(0 4,4 6)           |
+-------------------------------+
```

GPLv2 fill\_help\_tables.sql
