---
icon: earth-africa
---

# ST\_PointFromText

## Syntax

```sql
ST_PointFromText(wkt[,srid])
PointFromText(wkt[,srid])
```

## Description

Constructs a [POINT](../point.md) value using its [WKT](wkt-definition.md) representation and [SRID](../geometry-properties/st_srid.md).

`ST_PointFromText()` and `PointFromText()` are synonyms.

## Examples

```sql
CREATE TABLE gis_point  (g POINT);
SHOW FIELDS FROM gis_point;
INSERT INTO gis_point VALUES
    (PointFromText('POINT(10 10)')),
    (PointFromText('POINT(20 10)')),
    (PointFromText('POINT(20 20)')),
    (PointFromWKB(AsWKB(PointFromText('POINT(10 20)'))));
```

GPLv2 fill\_help\_tables.sql
