
# ST_Simplify


##### MariaDB starting with [11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-11-8-series/what-is-mariadb-118)
ST_Simplify was added in [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-11-8-series/what-is-mariadb-118).


## Syntax


```
ST_Simplify(g, max_distance)
```

## Description


Takes as input a geometry (g) and a double (max_distance). It applies the [Ramer–Douglas–Peucker algorithm](https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm) on `g` and returns the resulting geometry.


The goal of the Douglas-Peucker algorithm is to provide generalized simplifications by returning a geometry that is similar to `g` but uses only a subset of points. To perform the simplification, all the vertices that are shorter than `max_distance` are removed.


The algorithm may produce self-intersections and therefore result in invalid geometries. [ST_IsValid](st_isvalid.md) can be used to test validity of the result.


If the max_distance is not positive or is NULL, an ER_WRONG_ARGUMENT will occur.


## Examples


```
SELECT ST_AsText(ST_Simplify(ST_GeomFromText('LINESTRING(0 0,0 2,2 2,2 4,4 4,4 6,6 6)'), 0.5));
+-----------------------------------------------------------------------------------------+
| ST_AsText(ST_Simplify(ST_GeomFromText('LINESTRING(0 0,0 2,2 2,2 4,4 4,4 6,6 6)'), 0.5)) |
+-----------------------------------------------------------------------------------------+
| LINESTRING(0 0,0 2,2 2,2 4,4 4,4 6,6 6)                                                 |
+-----------------------------------------------------------------------------------------+

SELECT ST_AsText(ST_Simplify(ST_GeomFromText('LINESTRING(0 0,0 2,2 2,2 4,4 4,4 6,6 6)'), 1));  
+---------------------------------------------------------------------------------------+
| ST_AsText(ST_Simplify(ST_GeomFromText('LINESTRING(0 0,0 2,2 2,2 4,4 4,4 6,6 6)'), 1)) |
+---------------------------------------------------------------------------------------+
| LINESTRING(0 0,0 2,2 2,2 4,6 6)                                                       |
+---------------------------------------------------------------------------------------+
```

## See Also


* [Geometry Constructors](../geometry-constructors/README.md)
* [ST_AsText](../wkt/st_astext.md)
* [ST_GeomFromText](../wkt/st_geomfromtext.md)

