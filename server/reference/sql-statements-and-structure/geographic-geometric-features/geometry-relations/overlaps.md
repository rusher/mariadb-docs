
# OVERLAPS

## Syntax


```
OVERLAPS(g1,g2)
```

## Description


Returns `<code>1</code>` or `<code>0</code>` to indicate whether `<code>g1</code>` spatially overlaps `<code>g2</code>`.
The term spatially overlaps is used if two geometries of equal dimensions intersect and their
intersection results in a geometry of the same dimension but not equal to
either of the given geometries.


OVERLAPS() is based on the original MySQL implementation and uses object bounding rectangles, while [ST_OVERLAPS()](st-overlaps.md) uses object shapes.

