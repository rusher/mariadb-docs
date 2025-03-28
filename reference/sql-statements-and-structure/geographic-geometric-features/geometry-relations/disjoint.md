# DISJOINT

#

# Syntax

```
Disjoint(g1,g2)
```

#

# Description

Returns `1` or `0` to indicate whether `g1` is spatially disjoint from
(does not intersect) `g2`.

DISJOINT() tests the opposite relationship to [INTERSECTS()](intersects.md).

DISJOINT() is based on the original MySQL implementation and uses object bounding rectangles, while [ST_DISJOINT()](st_disjoint.md) uses object shapes.