
# TOUCHES

## Syntax


```
Touches(g1,g2)
```

## Description


Returns `<code>1</code>` or `<code>0</code>` to indicate whether `<code>g1</code>` spatially touches `<code>g2</code>`. Two
geometries spatially touch if the interiors of the geometries do not intersect,
but the boundary of one of the geometries intersects either the boundary or the
interior of the other.


TOUCHES() is based on the original MySQL implementation and uses object bounding rectangles, while [ST_TOUCHES()](st-touches.md) uses object shapes.

