# ST_PointFromWKB

#

# Syntax

```
ST_PointFromWKB(wkb[,srid])
PointFromWKB(wkb[,srid])
```

#

# Description

Constructs a [POINT](../point-properties/point-properties-y.md) value using its [WKB](well-known-binary-wkb-format.md) representation and [SRID](/en/srid/).

`ST_PointFromWKB()` and `PointFromWKB()` are synonyms.

#

# Examples

```
SET @g = ST_AsBinary(ST_PointFromText('POINT(0 4)'));

SELECT ST_AsText(ST_PointFromWKB(@g)) AS p;
+------------+
| p |
+------------+
| POINT(0 4) |
+------------+
```