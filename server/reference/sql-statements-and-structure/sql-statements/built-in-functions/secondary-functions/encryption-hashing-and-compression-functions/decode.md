
# DECODE

## Syntax


```
DECODE(crypt_str,pass_str)
```

In [Oracle mode](../../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md) from [MariaDB 10.3.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1032-release-notes.md):


```
DECODE(expr, search_expr, result_expr [, search_expr2, result_expr2 ...] [default_expr])
```

In all modes from [MariaDB 10.3.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1032-release-notes.md):


```
DECODE_ORACLE(expr, search_expr, result_expr [, search_expr2, result_expr2 ...] [default_expr])
```

## Description


In the default mode, `<code>DECODE</code>` decrypts the encrypted string *crypt_str* using *pass_str* as the
password. *crypt_str* should be a string returned from [ENCODE()](encode.md). The resulting string will be the original string only if *pass_str* is the same.


In [Oracle mode](../../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md) from [MariaDB 10.3.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1032-release-notes.md), `<code>DECODE</code>` compares *expr* to the search expressions, in order. If it finds a match, the corresponding result expression is returned. If no matches are found, the default expression is returned, or NULL if no default is provided.


NULLs are treated as equivalent.


`<code>DECODE_ORACLE</code>` is a synonym for the Oracle-mode version of the function, and is available in all modes.


## Examples


From [MariaDB 10.3.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1032-release-notes.md):


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
