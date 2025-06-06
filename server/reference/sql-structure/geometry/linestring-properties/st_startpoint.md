# ST\_STARTPOINT

## Syntax

```sql
ST_StartPoint(ls)
StartPoint(ls)
```

## Description

Returns the [Point](../../../sql-statements/geometry-constructors/geometry-constructors/point.md) that is the start point of the[LineString](../../../sql-statements/geometry-constructors/geometry-constructors/linestring.md) value `ls`.

`ST_StartPoint()` and `StartPoint()` are synonyms.

## Examples

```sql
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT AsText(StartPoint(GeomFromText(@ls)));
+---------------------------------------+
| AsText(StartPoint(GeomFromText(@ls))) |
+---------------------------------------+
| POINT(1 1)                            |
+---------------------------------------+
```

GPLv2 fill\_help\_tables.sql
