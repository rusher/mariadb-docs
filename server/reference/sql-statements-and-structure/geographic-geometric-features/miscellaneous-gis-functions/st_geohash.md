
# ST_GeoHash


##### MariaDB starting with [11.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md)
ST_GeoHash was added in [MariaDB 11.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md).


## Syntax


```
ST_GeoHash(longitude, latitude, max_length)
ST_GeoHash(point, max_length)
```

## Description


Returns the geohash corresponding to the input values, or NULL if any argument is NULL. Geohashes encode latitude and longitude coordinates into a text string made up only of numeric and lowercase latin letter characters.


The `<code>longitude</code>` parameter is a numeric value in the interval [180, -180]. `<code>latitude</code>` is a numeric value in the interval [90, -90].


In the case of `<code>point</code>`, the x coordinate is treated as the latitude and the y coordinate is treated as the latitude. The same constraints apply.


The `<code>max_length</code>` parameter is the upper limit on the resulting string size and cannot exceed 100.


The [ST_LatFromGeoHash](st_latfromgeohash.md) function decodes a given geohash and returns the latitude.


## Examples


```
SELECT ST_GeoHash(ST_GeomFromText('POINT(1 1)'),15), ST_GeoHash(0,30,15);
+----------------------------------------------+---------------------+
| ST_GeoHash(ST_GeomFromText('POINT(1 1)'),15) | ST_GeoHash(0,30,15) |
+----------------------------------------------+---------------------+
| s00twy01mtw037m                              | sj248j248j248j2     |
+----------------------------------------------+---------------------+
```

## See Also


* [ST_LatFromGeoHash](st_latfromgeohash.md)
* [Geometry Constructors](../geometry-constructors/README.md)
* [ST_GeomFromText](../wkt/st_geomfromtext.md)

