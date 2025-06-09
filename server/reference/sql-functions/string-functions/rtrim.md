# RTRIM

## Syntax

```
RTRIM(str)
```

## Description

Returns the string `str` with trailing space characters removed.

Returns NULL if given a NULL argument. If the result is empty, returns either an empty string, or, from [MariaDB 10.3.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1036-release-notes) with [SQL\_MODE=Oracle](broken-reference), NULL.

The Oracle mode version of the function can be accessed outside of Oracle mode by using `RTRIM_ORACLE` as the function name.

## Examples

```
SELECT QUOTE(RTRIM('MariaDB    '));
+-----------------------------+
| QUOTE(RTRIM('MariaDB    ')) |
+-----------------------------+
| 'MariaDB'                   |
+-----------------------------+
```

Oracle mode version from [MariaDB 10.3.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1036-release-notes):

```
SELECT RTRIM(''),RTRIM_ORACLE('');
+-----------+------------------+
| RTRIM('') | RTRIM_ORACLE('') |
+-----------+------------------+
|           | NULL             |
+-----------+------------------+
```

## See Also

* [LTRIM](ltrim.md) - leading spaces removed
* [TRIM](trim.md) - removes all given prefixes or suffixes

GPLv2 fill\_help\_tables.sql

{% @marketo/form formId="4316" %}
