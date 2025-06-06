# ST\_X

## Syntax

```sql
ST_X(p)
X(p)
```

## Description

Returns the X-coordinate value for the point `p` as a double-precision number.

`ST_X()` and `X()` are synonyms.

## Examples

```sql
SET @pt = 'Point(56.7 53.34)';

SELECT X(GeomFromText(@pt));
+----------------------+
| X(GeomFromText(@pt)) |
+----------------------+
|                 56.7 |
+----------------------+
```

GPLv2 fill\_help\_tables.sql
