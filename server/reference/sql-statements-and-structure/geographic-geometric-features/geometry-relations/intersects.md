
# INTERSECTS

## Syntax


```
INTERSECTS(g1,g2)
```

## Description


Returns `<code>1</code>` or `<code>0</code>` to indicate whether geometry *`<code>g1</code>`* spatially intersects geometry *`<code>g2</code>`*.


INTERSECTS() is based on the original MySQL implementation and uses object bounding rectangles, while [ST_INTERSECTS()](st-intersects.md) uses object shapes.


INTERSECTS() tests the opposite relationship to [DISJOINT()](disjoint.md).

