# INTERSECTS

#

# Syntax

```
INTERSECTS(g1,g2)
```

#

# Description

Returns `1` or `0` to indicate whether geometry *`g1`* spatially intersects geometry *`g2`*.

INTERSECTS() is based on the original MySQL implementation and uses object bounding rectangles, while [ST_INTERSECTS()](/en/st_intersects/) uses object shapes.

INTERSECTS() tests the opposite relationship to [DISJOINT()](disjoint.md).