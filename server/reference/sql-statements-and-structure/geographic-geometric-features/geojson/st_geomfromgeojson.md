
# ST_GeomFromGeoJSON

## Syntax


```
ST_GeomFromGeoJSON(g[, option])
```

## Description


Given a GeoJSON input *g*, returns a geometry object. The *option* specifies what to do if *g* contains geometries with coordinate dimensions higher than 2.



| Option | Description |
| --- | --- |
| Option | Description |
| 1 | Return an error (the default) |
| 2 - 4 | The document is accepted, but the coordinates for higher coordinate dimensions are stripped off. |



Note that this function did not work correctly before [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes) - see [MDEV-12180](https://jira.mariadb.org/browse/MDEV-12180).


## Examples


```
SET @j = '{ "type": "Point", "coordinates": [5.3, 15.0]}';

SELECT ST_AsText(ST_GeomFromGeoJSON(@j));
+-----------------------------------+
| ST_AsText(ST_GeomFromGeoJSON(@j)) |
+-----------------------------------+
| POINT(5.3 15)                     |
+-----------------------------------+
```

## See Also


* [ST_AsGeoJSON](geojson-st_asgeojson.md)

