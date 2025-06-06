# INTERSECTS

## Syntax

```sql
INTERSECTS(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether geometry _`g1`_ spatially intersects geometry _`g2`_.

INTERSECTS() is based on the original MySQL implementation and uses object bounding rectangles, while [ST\_INTERSECTS()](st-intersects.md) uses object shapes.

INTERSECTS() tests the opposite relationship to [DISJOINT()](disjoint.md).

GPLv2 fill\_help\_tables.sql
