# IFNULL

## Syntax

```
IFNULL(expr1,expr2)
NVL(expr1,expr2)
```

## Description

If _`expr1`_ is not NULL, IFNULL() returns _`expr1`_; otherwise it return&#x73;_`expr2`_. IFNULL() returns a numeric or string value, depending on the\
context in which it is used.

From [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103), NVL() is an alias for IFNULL().

## Examples

```
SELECT IFNULL(1,0); 
+-------------+
| IFNULL(1,0) |
+-------------+
|           1 |
+-------------+

SELECT IFNULL(NULL,10);
+-----------------+
| IFNULL(NULL,10) |
+-----------------+
|              10 |
+-----------------+

SELECT IFNULL(1/0,10);
+----------------+
| IFNULL(1/0,10) |
+----------------+
|        10.0000 |
+----------------+

SELECT IFNULL(1/0,'yes');
+-------------------+
| IFNULL(1/0,'yes') |
+-------------------+
| yes               |
+-------------------+
```

## See Also

* [NULL values](../../data-types/null-values.md)
* [IS NULL operator](../../sql-structure/operators/comparison-operators/is-null.md)
* [IS NOT NULL operator](../../sql-structure/operators/comparison-operators/is-not-null.md)
* [COALESCE function](../../sql-structure/operators/comparison-operators/coalesce.md)
* [NULLIF function](nullif.md)
* [CONNECT data types](../../../server-usage/storage-engines/connect/connect-data-types.md#null-handling)

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
