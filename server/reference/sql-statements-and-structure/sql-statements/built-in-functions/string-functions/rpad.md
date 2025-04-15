
# RPAD

## Syntax


```
RPAD(str, len [, padstr])
```


## Description


Returns the string `<code>str</code>`, right-padded with the string `<code>padstr</code>` to a
length of `<code>len</code>` characters. If `<code>str</code>` is longer than `<code>len</code>`, the return value
is shortened to `<code>len</code>` characters. If `<code>padstr</code>` is omitted, the RPAD function pads spaces.


Prior to [MariaDB 10.3.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), the `<code>padstr</code>` parameter was mandatory.


Returns NULL if given a NULL argument. If the result is empty (a length of zero), returns either an empty string, or, from [MariaDB 10.3.6](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1036-release-notes.md) with [SQL_MODE=Oracle](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md), NULL.


The Oracle mode version of the function can be accessed outside of Oracle mode by using `<code>RPAD_ORACLE</code>` as the function name.


## Examples


```
SELECT RPAD('hello',10,'.');
+----------------------+
| RPAD('hello',10,'.') |
+----------------------+
| hello.....           |
+----------------------+

SELECT RPAD('hello',2,'.');
+---------------------+
| RPAD('hello',2,'.') |
+---------------------+
| he                  |
+---------------------+
```

From [MariaDB 10.3.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), with the pad string defaulting to space.


```
SELECT RPAD('hello',30);
+--------------------------------+
| RPAD('hello',30)               |
+--------------------------------+
| hello                          |
+--------------------------------+
```

Oracle mode version from [MariaDB 10.3.6](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1036-release-notes.md):


```
SELECT RPAD('',0),RPAD_ORACLE('',0);
+------------+-------------------+
| RPAD('',0) | RPAD_ORACLE('',0) |
+------------+-------------------+
|            | NULL              |
+------------+-------------------+
```

## See Also


* [LPAD](lpad.md) - Left-padding instead of right-padding.

