
# VEC_DISTANCE_COSINE


##### MariaDB starting with [11.7](../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md)
Vectors were introduced in [MariaDB 11.7](../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md)


## Syntax


```
VEC_DISTANCE_COSINE(v, s)
```

## Description


`<code>VEC_Distance_Cosine</code>` is an SQL function that calculates a [Cosine distance](https://en.wikipedia.org/wiki/Cosine_similarity#Cosine_distance) between two vectors.


If the vector index was not built for the cosine function (see [CREATE TABLE with Vectors](../create-table-with-vectors.md)), the index will not be used, and a full table scan performed instead. The [VEC_DISTANCE](vector-functions-vec_distance.md) function is a generic function that behaves either as [VEC_DISTANCE_EUCLIDEAN](vec_distance_euclidean.md) or VEC_DISTANCE_COSINE, depending on the underlying index type.


## Example


```
select vec_distance_cosine(vec_fromtext('[1,2,3]'), vec_fromtext('[3,5,7]'));
+-----------------------------------------------------------------------+
| vec_distance_cosine(vec_fromtext('[1,2,3]'), vec_fromtext('[3,5,7]')) |
+-----------------------------------------------------------------------+
|                                                   0.00258509695694209 |
+-----------------------------------------------------------------------+
```

## See Also


* [VEC_DISTANCE](vector-functions-vec_distance.md)
* [VEC_DISTANCE_EUCLIDEAN](vec_distance_euclidean.md)
* [Vector Overview](../vector-overview.md)
* [CREATE TABLE with Vectors](../create-table-with-vectors.md)

