
# ST_OVERLAPS

## Syntax


```
ST_OVERLAPS(g1,g2)
```

## Description


Returns `<code>1</code>` or `<code>0</code>` to indicate whether geometry *`<code>g1</code>`* spatially overlaps geometry *`<code>g2</code>`*.


The term spatially overlaps is used if two geometries of equal dimensions intersect and their
intersection results in a geometry of the same dimension but not equal to
either of the given geometries.


ST_OVERLAPS() uses object shapes, while [OVERLAPS()](overlaps.md), based on the original MySQL implementation, uses object bounding rectangles.

