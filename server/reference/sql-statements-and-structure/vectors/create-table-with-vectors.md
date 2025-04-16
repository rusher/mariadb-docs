
# CREATE TABLE with Vectors


##### MariaDB starting with [11.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md)
[Vector search](README.md) was added in [MariaDB 11.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md).


MariaDB has a dedicated [VECTOR(N)](vector-functions/vector-functions-vec_distance.md) data type with a built-in data validation. N is the number of dimensions that all vector values in the column will have. For example,


```
CREATE TABLE embeddings (
        doc_id BIGINT UNSIGNED PRIMARY KEY,
        embedding VECTOR(1536)
);
```

To have a fast vector search one needs to index the vector column, creating a `VECTOR` index:


```
CREATE TABLE embeddings (
        doc_id BIGINT UNSIGNED PRIMARY KEY,
        embedding VECTOR(1536) NOT NULL,
        VECTOR INDEX (embedding)
);
```

Note that there can be only one vector index in the table and the indexed vector column must be `NOT NULL`.


There are two options that can be used to configure the vector index.


* `M` — Larger values mean slower SELECTs and INSERTs, larger index size and higher memory consumption but more accurate results. The valid range is from `3` to `200`.
* `DISTANCE` — Distance function to build the vector index for. Searches using a different distance function will not be able to use a vector index. Valid values are `cosine` and `euclidean` (the default).
For example,


```
CREATE TABLE embeddings (
        doc_id BIGINT UNSIGNED PRIMARY KEY,
        embedding VECTOR(1536) NOT NULL,
        VECTOR INDEX (embedding) M=8 DISTANCE=cosine
);
```
