# ST\_ENDPOINT

## Syntax

```sql
ST_EndPoint(ls)
EndPoint(ls)
```

## Description

Returns the [Point](../../../sql-statements/geometry-constructors/geometry-constructors/point.md) that is the endpoint of the[LineString](../../../sql-statements/geometry-constructors/geometry-constructors/linestring.md) value `ls`.

`ST_EndPoint()` and `EndPoint()` are synonyms.

## Examples

```sql
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT AsText(EndPoint(GeomFromText(@ls)));
+-------------------------------------+
| AsText(EndPoint(GeomFromText(@ls))) |
+-------------------------------------+
| POINT(3 3)                          |
+-------------------------------------+
```

GPLv2 fill\_help\_tables.sql

{% @marketo/form formId="4316" %}
