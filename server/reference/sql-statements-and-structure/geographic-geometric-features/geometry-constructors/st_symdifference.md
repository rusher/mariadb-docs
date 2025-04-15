# ST_SYMDIFFERENCE

#

# Syntax

```
ST_SYMDIFFERENCE(g1,g2)
```

#

# Description

Returns a geometry that represents the portions of geometry *`g1`* and geometry *`g2`* that don't intersect.

#

# Examples

```
SET @g1 = ST_GEOMFROMTEXT('LINESTRING(10 20, 10 40)');

SET @g2 = ST_GEOMFROMTEXT('LINESTRING(10 15, 10 25)');

SELECT ASTEXT(ST_SYMDIFFERENCE(@g1,@g2));
+----------------------------------------------+
| ASTEXT(ST_SYMDIFFERENCE(@g1,@g2)) |
+----------------------------------------------+
| MULTILINESTRING((10 15,10 20),(10 25,10 40)) |
+----------------------------------------------+

SET @g2 = ST_GeomFromText('LINESTRING(10 20, 10 41)');

SELECT ASTEXT(ST_SYMDIFFERENCE(@g1,@g2));
+-----------------------------------+
| ASTEXT(ST_SYMDIFFERENCE(@g1,@g2)) |
+-----------------------------------+
| LINESTRING(10 40,10 41) |
+-----------------------------------+
```