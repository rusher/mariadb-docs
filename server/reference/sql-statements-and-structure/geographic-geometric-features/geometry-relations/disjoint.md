
# DISJOINT

## Syntax


```
Disjoint(g1,g2)
```

## Description


Returns `<code>1</code>` or `<code>0</code>` to indicate whether `<code>g1</code>` is spatially disjoint from
(does not intersect) `<code>g2</code>`.


DISJOINT() tests the opposite relationship to [INTERSECTS()](intersects.md).


DISJOINT() is based on the original MySQL implementation and uses object bounding rectangles, while [ST_DISJOINT()](st_disjoint.md) uses object shapes.

