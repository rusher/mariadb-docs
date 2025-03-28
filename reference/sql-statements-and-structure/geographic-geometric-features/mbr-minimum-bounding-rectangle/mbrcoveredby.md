# MBRCoveredBy

#

#### MariaDB starting with [11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-118)

MBRCoveredBy was added in [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-118).

#

# Syntax

```
MBRCoveredBy(g1, g2)
```

#

# Description

Returns 1 if the [minimum bounding rectangle](mbr-definition.md) of `g1` is covered by the minimum bounding rectangle of `g2`, otherwise 0.

Returns NULL If any argument is NULL, or an argument is an empty geometry.

#

# Examples

```
SET @g1a = ST_GeomFromText('Point(5 6)');
SET @g1b = ST_GeomFromText('Point(5 11)');
SET @g2 = ST_GeomFromText('Polygon((0 0,0 10,10 10,10 0,0 0))');

SELECT MBRCoveredby(@g1a,@g2), MBRCoveredby(@g1b,@g2);
+------------------------+------------------------+
| MBRCoveredby(@g1a,@g2) | MBRCoveredby(@g1b,@g2) |
+------------------------+------------------------+
| 1 | 0 |
+------------------------+------------------------+
```

#

# See Also