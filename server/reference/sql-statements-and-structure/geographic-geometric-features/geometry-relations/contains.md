
# CONTAINS

## Syntax


```
Contains(g1,g2)
```

## Description


Returns `<code>1</code>` or `<code>0</code>` to indicate whether a geometry `<code>g1</code>` completely contains geometry `<code>g2</code>`. CONTAINS() is based on the original MySQL implementation and uses object bounding rectangles, while [ST_CONTAINS()](st-contains.md) uses object shapes.


This tests the opposite relationship to [Within()](within.md).

