
# VEC_FromText


##### MariaDB starting with [11.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-116.md)
[Vectors](../README.md) were introduced in [MariaDB 11.7](../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md).


## Syntax


```
VEC_FromText(s)
```

## Description


`VEC_FromText` converts a text representation of the vector (json array of numbers) to a vector (little-endian IEEE float sequence of bytes, 4 bytes per float).


## Example


```
select hex(vec_fromtext('[1,2,3]')); 
+------------------------------+
| hex(vec_fromtext('[1,2,3]')) |
+------------------------------+
| 0000803F0000004000004040     |
+------------------------------+
```
