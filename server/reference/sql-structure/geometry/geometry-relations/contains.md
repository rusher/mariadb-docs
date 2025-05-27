
# CONTAINS

## Syntax


```
Contains(g1,g2)
```

## Description


Returns `1` or `0` to indicate whether a geometry `g1` completely contains geometry `g2`. CONTAINS() is based on the original MySQL implementation and uses object bounding rectangles, while [ST_CONTAINS()](st-contains.md) uses object shapes.


This tests the opposite relationship to [Within()](within.md).


GPLv2 fill_help_tables.sql

