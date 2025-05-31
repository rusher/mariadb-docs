# LTRIM

## Syntax

```
LTRIM(str)
```

## Description

Returns the string `str` with leading space characters removed.

Returns NULL if given a NULL argument. If the result is empty, returns either an empty string, or, from [MariaDB 10.3.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1036-release-notes) with [SQL\_MODE=Oracle](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/comparison/sql_modeoracle), NULL.

The Oracle mode version of the function can be accessed outside of Oracle mode by using `LTRIM_ORACLE` as the function name.

## Examples

```
SELECT QUOTE(LTRIM('   MariaDB   '));
+-------------------------------+
| QUOTE(LTRIM('   MariaDB   ')) |
+-------------------------------+
| 'MariaDB   '                  |
+-------------------------------+
```

Oracle mode version from [MariaDB 10.3.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1036-release-notes):

```
SELECT LTRIM(''),LTRIM_ORACLE('');
+-----------+------------------+
| LTRIM('') | LTRIM_ORACLE('') |
+-----------+------------------+
|           | NULL             |
+-----------+------------------+
```

## See Also

* [RTRIM](rtrim.md) - trailing spaces removed
* [TRIM](trim.md) - removes all given prefixes or suffixes

GPLv2 fill\_help\_tables.sql
