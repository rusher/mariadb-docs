
# VECTOR


##### MariaDB starting with [11.7.1](https://mariadb.com/kb/en/mariadb-1171-release-notes/)
The VECTOR data type was added in [MariaDB 11.7.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-11-7-rolling-releases/mariadb-11-7-1-release-notes)


## Syntax


```
VECTOR(N)
```


## Description


The VECTOR data type was added as part of the [vectors](../../sql-statements-and-structure/vectors/README.md) feature, which permits MariaDB Server to perform as a relational vector database. `N` represents the fixed number of dimensions of the vector up to a maximum of 65532. The `N` dimension will be determined by the embedding algorithm.


## Example


```
CREATE TABLE t1 (id INT AUTO_INCREMENT PRIMARY KEY, v VECTOR(5) NOT NULL, VECTOR INDEX (v));
```

## See Also


* [CREATE TABLE with Vectors](../../sql-statements-and-structure/vectors/create-table-with-vectors.md)

