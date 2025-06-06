# ST\_INTERSECTION

## Syntax

```sql
ST_INTERSECTION(g1,g2)
```

## Description

Returns a geometry that is the intersection, or shared portion, of geometry _`g1`_ and geometry _`g2`_.

## Examples

```sql
SET @g1 = ST_GEOMFROMTEXT('POINT(2 1)');

SET @g2 = ST_GEOMFROMTEXT('LINESTRING(2 1, 0 2)');

SELECT ASTEXT(ST_INTERSECTION(@g1,@g2));
+----------------------------------+
| ASTEXT(ST_INTERSECTION(@g1,@g2)) |
+----------------------------------+
| POINT(2 1)                       |
+----------------------------------+
```

CC BY-SA / Gnu FDL
