
# LINESTRING

## Syntax


```
LineString(pt1,pt2,...)
```

## Description


WKB LineString from WKB Point coordinate data.
Constructs a [WKB](../wkb/README.md) LineString value from a number of WKB [Point](point.md) arguments. If any argument is not a WKB Point, the return value is
`NULL`. If the number of [Point](point.md) arguments is less than two, the return value is `NULL`.


## Examples


```
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT AsText(EndPoint(GeomFromText(@ls)));
+-------------------------------------+
| AsText(EndPoint(GeomFromText(@ls))) |
+-------------------------------------+
| POINT(3 3)                          |
+-------------------------------------+

CREATE TABLE gis_line  (g LINESTRING);
INSERT INTO gis_line VALUES
    (LineFromText('LINESTRING(0 0,0 10,10 0)')),
    (LineStringFromText('LINESTRING(10 10,20 10,20 20,10 20,10 10)')),
    (LineStringFromWKB(AsWKB(LineString(Point(10, 10), Point(40, 10)))));
```

Linestring_Example:


```
CREATE TABLE linestring_example (
  g LINESTRING
);
```

```
INSERT INTO linestring_example VALUES
  (ST_LineFromText('LINESTRING(0 0, 1 1, 2 2)')),
  (ST_LineStringFromText('LINESTRING(10 10, 20 10, 20 20, 10 20, 10 10)')),
  (LineString(Point(10, 10), Point(40, 10)));
```

```
SELECT ST_AsWKT(g) FROM linestring_example;
<</code>>

<<sql>>
+-------------------------------------------+
| ST_AsWKT(g)                               |
+-------------------------------------------+
| LINESTRING(0 0,1 1,2 2)                   |
| LINESTRING(10 10,20 10,20 20,10 20,10 10) |
| LINESTRING(10 10,40 10)                   |
+-------------------------------------------+
```


GPLv2 fill_help_tables.sql

