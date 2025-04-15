# ST_DISTANCE

#

# Syntax

```
ST_DISTANCE(g1,g2)
```

#

# Description

Returns the distance between two geometries, or null if not given valid inputs.

#

# Example

```
SELECT ST_Distance(POINT(1,2),POINT(2,2));
+------------------------------------+
| ST_Distance(POINT(1,2),POINT(2,2)) |
+------------------------------------+
| 1 |
+------------------------------------+
```