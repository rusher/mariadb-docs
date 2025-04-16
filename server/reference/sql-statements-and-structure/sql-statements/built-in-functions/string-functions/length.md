
# LENGTH

## Syntax


```
LENGTH(str)
```


## Description


Returns the length of the string `str`.


In the default mode, when [Oracle mode from MariaDB 10.3](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md#functions) is not set, the length is measured in bytes. In this case, a multi-byte character counts as multiple bytes. This means that for a string
containing five two-byte characters, `LENGTH()` returns 10, whereas [CHAR_LENGTH()](char_length.md) returns 5.


When running [Oracle mode from MariaDB 10.3](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md#functions), the length is measured in characters, and `LENGTH` is a synonym for [CHAR_LENGTH()](char_length.md).


If `str` is not a string value, it is converted into a string. If `str` is `NULL`, the function returns `NULL`.


## Examples


```
SELECT LENGTH('MariaDB');
+-------------------+
| LENGTH('MariaDB') |
+-------------------+
|                 7 |
+-------------------+
```

When [Oracle mode](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md) from [MariaDB 10.3](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md) is not set:


```
SELECT CHAR_LENGTH('π'), LENGTH('π'), LENGTHB('π'), OCTET_LENGTH('π');
+-------------------+--------------+---------------+--------------------+
| CHAR_LENGTH('π')  | LENGTH('π')  | LENGTHB('π')  | OCTET_LENGTH('π')  |
+-------------------+--------------+---------------+--------------------+
|                 1 |            2 |             2 |                  2 |
+-------------------+--------------+---------------+--------------------+
```

In [Oracle mode from MariaDB 10.3](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md#functions):


```
SELECT CHAR_LENGTH('π'), LENGTH('π'), LENGTHB('π'), OCTET_LENGTH('π');
+-------------------+--------------+---------------+--------------------+
| CHAR_LENGTH('π')  | LENGTH('π')  | LENGTHB('π')  | OCTET_LENGTH('π')  |
+-------------------+--------------+---------------+--------------------+
|                 1 |            1 |             2 |                  2 |
+-------------------+--------------+---------------+--------------------+
```

## See Also


* [CHAR_LENGTH()](char_length.md)
* [LENGTHB()](lengthb.md)
* [OCTET_LENGTH()](octet_length.md)
* [Oracle mode from MariaDB 10.3](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md#simple-syntax-compatibility)

