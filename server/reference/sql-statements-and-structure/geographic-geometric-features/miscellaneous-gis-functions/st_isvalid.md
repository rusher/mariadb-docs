# ST_IsValid

#

#### MariaDB starting with [11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-118)

ST_IsValid was added in [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-118).

#

# Syntax

```
ST_IsValid(g)
```

#

# Description

Given a geometry input, returns 1 if the argument is geometrically valid according to the OGC specifications, 0 if the argument is not geometrically valid.

Unlike [ST_Validate](st_validate.md), requires valid GIS data, or `ERROR 3037 (22023): Invalid GIS data provided to function st_isvalid` is returned.

#

# Examples

```
SELECT ST_IsValid(ST_GeomFromText('LINESTRING (0 0, 1 1)'));
+------------------------------------------------------+
| ST_IsValid(ST_GeomFromText('LINESTRING (0 0, 1 1)')) |
+------------------------------------------------------+
| 1 |
+------------------------------------------------------+

SELECT ST_IsValid(ST_GeomFromText('LINESTRING (0 0, 0 0)'));
+------------------------------------------------------+
| ST_IsValid(ST_GeomFromText('LINESTRING (0 0, 0 0)')) |
+------------------------------------------------------+
| 0 |
+------------------------------------------------------+
```

A [POINT](../point-properties/point-properties-y.md) requires both x and y co-ordinates:

```
SELECT ST_IsValid(ST_GeomFromText('POINT (0)')); 
ERROR 3037 (22023): Invalid GIS data provided to function st_isvalid.
```

#

# See Also

* [Geometry Constructors](/en/geometry-constructors/)
* [ST_AsText](../wkt/st_astext.md)