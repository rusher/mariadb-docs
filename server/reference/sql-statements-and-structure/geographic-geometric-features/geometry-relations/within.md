
# WITHIN

## Syntax


```
Within(g1,g2)
```

## Description


Returns `<code>1</code>` or `<code>0</code>` to indicate whether `<code>g1</code>` is spatially within `<code>g2</code>`.
This tests the opposite relationship as `<code>[Contains()](contains.md)</code>`.


WITHIN() is based on the original MySQL implementation, and uses object bounding rectangles, while [ST_WITHIN()](st-within.md) uses object shapes.


## Examples


```
SET @g1 = GEOMFROMTEXT('POINT(174 149)');
SET @g2 = GEOMFROMTEXT('POINT(176 151)');
SET @g3 = GEOMFROMTEXT('POLYGON((175 150, 20 40, 50 60, 125 100, 175 150))');

SELECT within(@g1,@g3);
+-----------------+
| within(@g1,@g3) |
+-----------------+
|               1 |
+-----------------+

SELECT within(@g2,@g3);
+-----------------+
| within(@g2,@g3) |
+-----------------+
|               0 |
+-----------------+
```
