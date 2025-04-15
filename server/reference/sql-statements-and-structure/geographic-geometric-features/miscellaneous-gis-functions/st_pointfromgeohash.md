
# ST_PointFromGeoHash


##### MariaDB starting with [11.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md)
ST_PointFromGeoHash was added in [MariaDB 11.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md).


## Syntax


```
ST_PointFromGeoHash(geohash, srid)
```

## Description


Takes a given `<code>geohash</code>` string and returns a point where the x is the longitude and the y is the latitude.


The latitude is returned as a numeric value in the interval [180, -180]. The longitude is returned as a numeric value in the interval [90, -90]. If the argument is NULL, the return value is NULL. If the argument is invalid, an ER_GIS_INVALID_DATA is thrown.


## Examples


```
SELECT ST_ASTEXT(ST_POINTFROMGEOHASH("s00twy01mtw037m",0));
+-----------------------------------------------------+
| ST_ASTEXT(ST_POINTFROMGEOHASH("s00twy01mtw037m",0)) |
+-----------------------------------------------------+
| POINT(1 1)                                          |
+-----------------------------------------------------+

SELECT ST_ASTEXT(ST_POINTFROMGEOHASH(ST_GEOHASH(180,90,20),0));
+---------------------------------------------------------+
| ST_ASTEXT(ST_POINTFROMGEOHASH(ST_GEOHASH(180,90,20),0)) |
+---------------------------------------------------------+
| POINT(180 90)                                           |
+---------------------------------------------------------+
```

## See Also


* [ST_GeoHash](st_geohash.md)

