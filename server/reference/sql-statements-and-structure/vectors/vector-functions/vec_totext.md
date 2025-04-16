
# VEC_ToText


##### MariaDB starting with [11.7](../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md)
[Vectors](../README.md) were introduced in [MariaDB 11.7](../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md).


## Syntax


```
VEC_ToText(v)
```

## Description


`VEC_ToText` converts a binary vector into a json array of numbers (floats). Returns NULL and throws a warning [4201](../../../mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4200-to-4299/e4201.md) if given an invalid vector.


## Example


```
SELECT VEC_ToText(x'e360d63ebe554f3fcdbc523f4522193f5236083d');
+---------------------------------------------------------+
| VEC_ToText(x'e360d63ebe554f3fcdbc523f4522193f5236083d') |
+---------------------------------------------------------+
| [0.418708,0.809902,0.823193,0.598179,0.033255]          |
+---------------------------------------------------------+
```

Invalid vector:


```
SELECT VEC_ToText(x'aabbcc');
+-----------------------+
| VEC_ToText(x'aabbcc') |
+-----------------------+
| NULL                  |
+-----------------------+
1 row in set, 1 warning (0.000 sec)

Warning (Code 4201): Invalid binary vector format. Must use IEEE standard float 
  representation in little-endian format. Use VEC_FromText() to generate it.
```

## See Also


* [Error 4201: Invalid binary vector format](../../../mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4200-to-4299/e4201.md)

