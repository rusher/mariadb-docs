# DECODE

## Syntax

```
DECODE(crypt_str,pass_str)
```

In [Oracle mode](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/broken-reference/README.md) from [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1032-release-notes):

```
DECODE(expr, search_expr, result_expr [, search_expr2, result_expr2 ...] [default_expr])
```

In all modes from [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1032-release-notes):

```
DECODE_ORACLE(expr, search_expr, result_expr [, search_expr2, result_expr2 ...] [default_expr])
```

## Description

In the default mode, `DECODE` decrypts the encrypted string _crypt\_str_ using _pass\_str_ as the\
password. _crypt\_str_ should be a string returned from [ENCODE()](encode.md). The resulting string will be the original string only if _pass\_str_ is the same.

In [Oracle mode](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/broken-reference/README.md) from [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1032-release-notes), `DECODE` compares _expr_ to the search expressions, in order. If it finds a match, the corresponding result expression is returned. If no matches are found, the default expression is returned, or NULL if no default is provided.

NULLs are treated as equivalent.

`DECODE_ORACLE` is a synonym for the Oracle-mode version of the function, and is available in all modes.

## Examples

From [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1032-release-notes):

```
SELECT DECODE_ORACLE(2+1,3*1,'found1',3*2,'found2','default');
+--------------------------------------------------------+
| DECODE_ORACLE(2+1,3*1,'found1',3*2,'found2','default') |
+--------------------------------------------------------+
| found1                                                 |
+--------------------------------------------------------+

SELECT DECODE_ORACLE(2+4,3*1,'found1',3*2,'found2','default');
+--------------------------------------------------------+
| DECODE_ORACLE(2+4,3*1,'found1',3*2,'found2','default') |
+--------------------------------------------------------+
| found2                                                 |
+--------------------------------------------------------+

SELECT DECODE_ORACLE(2+2,3*1,'found1',3*2,'found2','default');
+--------------------------------------------------------+
| DECODE_ORACLE(2+2,3*1,'found1',3*2,'found2','default') |
+--------------------------------------------------------+
| default                                                |
+--------------------------------------------------------+
```

Nulls are treated as equivalent:

```
SELECT DECODE_ORACLE(NULL,NULL,'Nulls are equivalent','Nulls are not equivalent');
+----------------------------------------------------------------------------+
| DECODE_ORACLE(NULL,NULL,'Nulls are equivalent','Nulls are not equivalent') |
+----------------------------------------------------------------------------+
| Nulls are equivalent                                                       |
+----------------------------------------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
