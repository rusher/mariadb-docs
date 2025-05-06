
# VEC_DISTANCE_EUCLIDEAN


##### MariaDB starting with [11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-11-7-rolling-releases/what-is-mariadb-117)
Vectors were introduced in [MariaDB 11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-11-7-rolling-releases/what-is-mariadb-117).


## Syntax


```
VEC_DISTANCE_EUCLIDEAN(v, s)
```

## Description


`VEC_Distance_Euclidean` is an SQL function that calculates a Euclidean (L2) distance between two points.


If the vector index was not built for the euclidean function (see [CREATE TABLE with Vectors](../create-table-with-vectors.md)), the index will not be used, and a full table scan performed instead. The [VEC_DISTANCE](vector-functions-vec_distance.md) function is a generic function that behaves either as VEC_DISTANCE_EUCLIDEAN or [VEC_DISTANCE_COSINE](vec_distance_cosine.md), depending on the underlying index type.


## Example


```
INSERT INTO v VALUES 
     (1, x'e360d63ebe554f3fcdbc523f4522193f5236083d'),
     (2, x'f511303f72224a3fdd05fe3eb22a133ffae86a3f'),
     (3,x'f09baa3ea172763f123def3e0c7fe53e288bf33e'),
     (4,x'b97a523f2a193e3eb4f62e3f2d23583e9dd60d3f'),
     (5,x'f7c5df3e984b2b3e65e59d3d7376db3eac63773e'),
     (6,x'de01453ffa486d3f10aa4d3fdd66813c71cb163f'),
     (7,x'76edfc3e4b57243f10f8423fb158713f020bda3e'),
     (8,x'56926c3fdf098d3e2c8c5e3d1ad4953daa9d0b3e'),
     (9,x'7b713f3e5258323f80d1113d673b2b3f66e3583f'),
     (10,x'6ca1d43e9df91b3fe580da3e1c247d3f147cf33e');

SELECT id FROM v 
  ORDER BY VEC_Distance_Euclidean(v, x'6ca1d43e9df91b3fe580da3e1c247d3f147cf33e');
+----+
| id |
+----+
| 10 |
|  7 |
|  3 |
|  9 |
|  2 |
|  1 |
|  5 |
|  4 |
|  6 |
|  8 |
+----+
```

## See Also


* [VEC_DISTANCE](vector-functions-vec_distance.md)
* [VEC_DISTANCE_COSINE](vec_distance_cosine.md)
* [Vector Overview](../vector-overview.md)
* [CREATE TABLE with Vectors](../create-table-with-vectors.md)


CC BY-SA / Gnu FDL

