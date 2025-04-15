# Geometry Types

#

# Description

MariaDB provides a standard way of creating spatial columns for geometry types,
for example, with [CREATE TABLE](../sql-statements/data-definition/create/create-tablespace.md) or [ALTER TABLE](../sql-statements/data-definition/alter/alter-table.md).
Currently, spatial columns are supported for [MyISAM](../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk-table-information.md), [InnoDB](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) and [ARCHIVE](/en/archive/)
tables. See also [SPATIAL INDEX](spatial-index.md).

The basic geometry type is `GEOMETRY`. But the type can be more specific. The following types are supported:

| Geometry Types |
| --- |
| Geometry Types |
| [POINT](point-properties/point-properties-y.md) |
| [LINESTRING](wkb/linestringfromwkb.md) |
| [POLYGON](wkb/polygonfromwkb.md) |
| [MULTIPOINT](wkb/multipointfromwkb.md) |
| [MULTILINESTRING](wkb/multilinestringfromwkb.md) |
| [MULTIPOLYGON](wkb/multipolygonfromwkb.md) |
| [GEOMETRYCOLLECTION](wkb/geometrycollectionfromwkb.md) |
| GEOMETRY |

#

# Examples

**Note:** For clarity, only one type is listed per table in the examples below, but a table
row can contain multiple types. For example:

```
CREATE TABLE object (shapeA POLYGON, shapeB LINESTRING);
```

#

## [POINT](point-properties/point-properties-y.md)

```
CREATE TABLE gis_point (g POINT);
SHOW FIELDS FROM gis_point;
INSERT INTO gis_point VALUES
 (PointFromText('POINT(10 10)')),
 (PointFromText('POINT(20 10)')),
 (PointFromText('POINT(20 20)')),
 (PointFromWKB(AsWKB(PointFromText('POINT(10 20)'))));
```

#

## [LINESTRING](wkb/linestringfromwkb.md)

```
CREATE TABLE gis_line (g LINESTRING);
SHOW FIELDS FROM gis_line;
INSERT INTO gis_line VALUES
 (LineFromText('LINESTRING(0 0,0 10,10 0)')),
 (LineStringFromText('LINESTRING(10 10,20 10,20 20,10 20,10 10)')),
 (LineStringFromWKB(AsWKB(LineString(Point(10, 10), Point(40, 10)))));
```

#

## [POLYGON](wkb/polygonfromwkb.md)

```
CREATE TABLE gis_polygon (g POLYGON);
SHOW FIELDS FROM gis_polygon;
INSERT INTO gis_polygon VALUES
 (PolygonFromText('POLYGON((10 10,20 10,20 20,10 20,10 10))')),
 (PolyFromText('POLYGON((0 0,50 0,50 50,0 50,0 0), (10 10,20 10,20 20,10 20,10 10))')),
 (PolyFromWKB(AsWKB(Polygon(LineString(Point(0, 0), Point(30, 0), Point(30, 30), Point(0, 0))))));
```

#

## [MULTIPOINT](wkb/multipointfromwkb.md)

```
CREATE TABLE gis_multi_point (g MULTIPOINT);
SHOW FIELDS FROM gis_multi_point;
INSERT INTO gis_multi_point VALUES
 (MultiPointFromText('MULTIPOINT(0 0,10 10,10 20,20 20)')),
 (MPointFromText('MULTIPOINT(1 1,11 11,11 21,21 21)')),
 (MPointFromWKB(AsWKB(MultiPoint(Point(3, 6), Point(4, 10)))));
```

#

## [MULTILINESTRING](wkb/multilinestringfromwkb.md)

```
CREATE TABLE gis_multi_line (g MULTILINESTRING);
SHOW FIELDS FROM gis_multi_line;
INSERT INTO gis_multi_line VALUES
 (MultiLineStringFromText('MULTILINESTRING((10 48,10 21,10 0),(16 0,16 23,16 48))')),
 (MLineFromText('MULTILINESTRING((10 48,10 21,10 0))')),
 (MLineFromWKB(AsWKB(MultiLineString(LineString(Point(1, 2), Point(3, 5)), LineString(Point(2, 5), Point(5, 8), Point(21, 7))))));
```

#

## [MULTIPOLYGON](wkb/multipolygonfromwkb.md)

```
CREATE TABLE gis_multi_polygon (g MULTIPOLYGON);
SHOW FIELDS FROM gis_multi_polygon;
INSERT INTO gis_multi_polygon VALUES
 (MultiPolygonFromText('MULTIPOLYGON(((28 26,28 0,84 0,84 42,28 26),(52 18,66 23,73 9,48 6,52 18)),((59 18,67 18,67 13,59 13,59 18)))')),
 (MPolyFromText('MULTIPOLYGON(((28 26,28 0,84 0,84 42,28 26),(52 18,66 23,73 9,48 6,52 18)),((59 18,67 18,67 13,59 13,59 18)))')),
 (MPolyFromWKB(AsWKB(MultiPolygon(Polygon(LineString(Point(0, 3), Point(3, 3), Point(3, 0), Point(0, 3)))))));
```

#

## [GEOMETRYCOLLECTION](wkb/geometrycollectionfromwkb.md)

```
CREATE TABLE gis_geometrycollection (g GEOMETRYCOLLECTION);
SHOW FIELDS FROM gis_geometrycollection;
INSERT INTO gis_geometrycollection VALUES
 (GeomCollFromText('GEOMETRYCOLLECTION(POINT(0 0), LINESTRING(0 0,10 10))')),
 (GeometryFromWKB(AsWKB(GeometryCollection(Point(44, 6), LineString(Point(3, 6), Point(7, 9)))))),
 (GeomFromText('GeometryCollection()')),
 (GeomFromText('GeometryCollection EMPTY'));
```

#

## [GEOMETRY](geometry-types.md)

```
CREATE TABLE gis_geometry (g GEOMETRY);
SHOW FIELDS FROM gis_geometry;
INSERT into gis_geometry SELECT * FROM gis_point;
INSERT into gis_geometry SELECT * FROM gis_line;
INSERT into gis_geometry SELECT * FROM gis_polygon;
INSERT into gis_geometry SELECT * FROM gis_multi_point;
INSERT into gis_geometry SELECT * FROM gis_multi_line;
INSERT into gis_geometry SELECT * FROM gis_multi_polygon;
INSERT into gis_geometry SELECT * FROM gis_geometrycollection;
```