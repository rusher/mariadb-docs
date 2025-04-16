
# LTRIM

## Syntax


```
LTRIM(str)
```


## Description


Returns the string `str` with leading space characters removed.


Returns NULL if given a NULL argument. If the result is empty, returns either an empty string, or, from [MariaDB 10.3.6](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1036-release-notes.md) with [SQL_MODE=Oracle](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md), NULL.


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

Oracle mode version from [MariaDB 10.3.6](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1036-release-notes.md):


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

