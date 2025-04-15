
# UPPER

## Syntax


```
UPPER(str)
UCASE(str)
```

## Description


Returns the string `<code>str</code>` with all characters changed to uppercase
according to the current character set mapping. The default is latin1
(cp1252 West European).


`<code>UCASE</code>` is a synonym.


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

`<code>UPPER()</code>` is ineffective when applied to binary strings ([BINARY](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md), [VARBINARY](../../../../data-types/string-data-types/varbinary.md), [BLOB](../../../../data-types/string-data-types/blob.md)). The description of [LOWER](lower.md)() shows how to perform lettercase conversion of binary strings.


Prior to [MariaDB 11.3](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-113.md), the query optimizer did not handle queries of the format `<code>UCASE(varchar_col)=...</code>`. An [optimizer_switch](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/optimizer-switch.md) option, `<code>sargable_casefold=ON</code>`, was added in [MariaDB 11.3.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md) to handle this case. ([MDEV-31496](https://jira.mariadb.org/browse/MDEV-31496))

