# ST_WITHIN

#

# Syntax

```
ST_WITHIN(g1,g2)
```

#

# Description

Returns `1` or `0` to indicate whether geometry *`g1`* is spatially within geometry *`g2`*.

This tests the opposite relationship as `[ST_CONTAINS()](/en/st_contains/)`.

ST_WITHIN() uses object shapes, while [WITHIN()](within.md), based on the original MySQL implementation, uses object bounding rectangles.

#

# Examples

```
SET @g1 = ST_GEOMFROMTEXT('POINT(174 149)');

SET @g2 = ST_GEOMFROMTEXT('POLYGON((175 150, 20 40, 50 60, 125 100, 175 150))');

SELECT ST_WITHIN(@g1,@g2);
+--------------------+
| ST_WITHIN(@g1,@g2) |
+--------------------+
| 1 |
+--------------------+

SET @g1 = ST_GEOMFROMTEXT('POINT(176 151)');

SELECT ST_WITHIN(@g1,@g2);
+--------------------+
| ST_WITHIN(@g1,@g2) |
+--------------------+
| 0 |
+--------------------+
```