# ST_LatFromGeoHash

#

#### MariaDB starting with [11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-118)

ST_LatFromGeoHash was added in [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-118).

#

# Syntax

```
ST_LatFromGeoHash(geohash)
```

#

# Description

Decodes a given `geohash` string and returns the latitude in the interval [90, -90].

If the argument is NULL, the return value is NULL. If the argument is invalid, an ER_INCORRECT_TYPE error is thrown.

The [ST_GeoHash](st_geohash.md) function can be used to generate geohashes.

#

# Examples

```
SELECT ST_LatFromGeoHash('zzzzzzzzz'), ST_LatFromGeoHash('xvrfxvrfxvrfxvr');
+--------------------------------+--------------------------------------+
| ST_LatFromGeoHash('zzzzzzzzz') | ST_LatFromGeoHash('xvrfxvrfxvrfxvr') |
+--------------------------------+--------------------------------------+
| 90 | 30 |
+--------------------------------+--------------------------------------+
```

#

# See Also

* [ST_GeoHash](st_geohash.md)