
# ST_OVERLAPS

## Syntax


```
ST_OVERLAPS(g1,g2)
```

## Description


Returns `1` or `0` to indicate whether geometry *`g1`* spatially overlaps geometry *`g2`*.


The term spatially overlaps is used if two geometries of equal dimensions intersect and their
intersection results in a geometry of the same dimension but not equal to
either of the given geometries.


ST_OVERLAPS() uses object shapes, while [OVERLAPS()](overlaps.md), based on the original MySQL implementation, uses object bounding rectangles.


CC BY-SA / Gnu FDL

