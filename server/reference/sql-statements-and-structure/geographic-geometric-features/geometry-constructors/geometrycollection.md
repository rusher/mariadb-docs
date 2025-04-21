
# GEOMETRYCOLLECTION

## Syntax


```
GeometryCollection(g1,g2,...)
```

## Description


Constructs a [WKB](../wkb/README.md) GeometryCollection. If any argument is not a well-formed WKB representation of a geometry, the return value is `NULL`.


## Examples


```
CREATE TABLE gis_geometrycollection  (g GEOMETRYCOLLECTION);
SHOW FIELDS FROM gis_geometrycollection;
INSERT INTO gis_geometrycollection VALUES
    (GeomCollFromText('GEOMETRYCOLLECTION(POINT(0 0), LINESTRING(0 0,10 10))')),
    (GeometryFromWKB(AsWKB(GeometryCollection(Point(44, 6), LineString(Point(3, 6), Point(7, 9)))))),
    (GeomFromText('GeometryCollection()')),
    (GeomFromText('GeometryCollection EMPTY'));
```

```
CREATE TABLE geomcoll_example (
  g GEOMETRYCOLLECTION
);
```

```
INSERT INTO geomcoll_example VALUES
  (ST_GeomCollFromText(
    'GEOMETRYCOLLECTION(POINT(0 0), LINESTRING(0 1, 0 2),
    POINT(1 0))')),
  (GeometryCollection(
    Point(0, 0),
    LineString(Point(0, 1), Point(0, 2))));
```

```
SELECT ST_AsWKT(g) FROM geomcoll_example;

+---------------------------------------------------------------+
| ST_AsWKT(g)                                                   |
+---------------------------------------------------------------+
| GEOMETRYCOLLECTION(POINT(0 0),LINESTRING(0 1,0 2),POINT(1 0)) |
| GEOMETRYCOLLECTION(POINT(0 0),LINESTRING(0 1,0 2))            |
+---------------------------------------------------------------+
```
