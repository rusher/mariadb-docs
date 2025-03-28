# ST_LENGTH

#

# Syntax

```
ST_LENGTH(ls)
```

#

# Description

Returns as a double-precision number the length of the
[LineString](../wkb/linestringfromwkb.md) value *`ls`* in its associated spatial reference.

#

# Examples

```
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT ST_LENGTH(ST_GeomFromText(@ls));
+---------------------------------+
| ST_LENGTH(ST_GeomFromText(@ls)) |
+---------------------------------+
| 2.82842712474619 |
+---------------------------------+
```