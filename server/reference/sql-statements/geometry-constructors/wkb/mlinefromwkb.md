---
icon: earth-africa
---

# MLineFromWKB

## Syntax

```sql
MLineFromWKB(wkb[,srid])
MultiLineStringFromWKB(wkb[,srid])
```

## Description

Constructs a [MULTILINESTRING](../multilinestring.md) value using its [WKB](well-known-binary-wkb-format.md) representation and [SRID](../geometry-properties/st_srid.md).

`MLineFromWKB()` and `MultiLineStringFromWKB()` are synonyms.

## Examples

```sql
SET @g = ST_AsBinary(MLineFromText('MULTILINESTRING((10 48,10 21,10 0),(16 0,16 23,16 48))'));

SELECT ST_AsText(MLineFromWKB(@g));
+--------------------------------------------------------+
| ST_AsText(MLineFromWKB(@g))                            |
+--------------------------------------------------------+
| MULTILINESTRING((10 48,10 21,10 0),(16 0,16 23,16 48)) |
+--------------------------------------------------------+
```

GPLv2 fill\_help\_tables.sql
