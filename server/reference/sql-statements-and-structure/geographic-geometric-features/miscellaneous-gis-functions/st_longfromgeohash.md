
# ST_LongFromGeoHash


##### MariaDB starting with [11.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md)
ST_LongFromGeoHash was added in [MariaDB 11.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md).


## Syntax


```
ST_LongFromGeoHash(geohash)
```

## Description


Decodes a given `<code>geohash</code>` string and returns the longitude in the interval [180, -180].


If the argument is NULL, the return value is NULL. If the argument is invalid, an ER_INCORRECT_TYPE error is thrown.


The [ST_GeoHash](st_geohash.md) function can be used to generate geohashes.


## Examples


```
SELECT ST_LongFromGeoHash('zzzzzzzzz'), ST_LongFromGeoHash('sj248j248j248j2');           
+---------------------------------+---------------------------------------+
| ST_LongFromGeoHash('zzzzzzzzz') | ST_LongFromGeoHash('sj248j248j248j2') |
+---------------------------------+---------------------------------------+
|                             180 |                                     0 |
+---------------------------------+---------------------------------------+
```

## See Also


* [ST_GeoHash](st_geohash.md)
* [ST_LatFromGeoHash](st_latfromgeohash.md)

