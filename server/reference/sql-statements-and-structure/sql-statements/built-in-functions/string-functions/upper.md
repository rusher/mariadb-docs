
# UPPER

## Syntax


```
UPPER(str)
UCASE(str)
```

## Description


Returns the string `str` with all characters changed to uppercase
according to the current character set mapping. The default is latin1
(cp1252 West European).


`UCASE` is a synonym.


```
SELECT UPPER(surname), givenname FROM users ORDER BY surname;
+----------------+------------+
| UPPER(surname) | givenname  |
+----------------+------------+
| ABEL           | Jacinto    |
| CASTRO         | Robert     |
| COSTA          | Phestos    |
| MOSCHELLA      | Hippolytos |
+----------------+------------+
```

`UPPER()` is ineffective when applied to binary strings ([BINARY](../../../../data-types/string-data-types/binary.md), [VARBINARY](../../../../data-types/string-data-types/varbinary.md), [BLOB](../../../../data-types/string-data-types/blob.md)). The description of [LOWER](lower.md)() shows how to perform lettercase conversion of binary strings.


Prior to [MariaDB 11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113), the query optimizer did not handle queries of the format `UCASE(varchar_col)=...`. An [optimizer_switch](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/optimizer-switch.md) option, `sargable_casefold=ON`, was added in [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes) to handle this case. ([MDEV-31496](https://jira.mariadb.org/browse/MDEV-31496))

