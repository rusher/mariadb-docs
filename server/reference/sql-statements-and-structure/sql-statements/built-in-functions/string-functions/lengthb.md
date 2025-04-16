
# LENGTHB

## Syntax


```
LENGTHB(str)
```

## Description


`LENGTHB()` returns the length of the given string, in bytes. When [Oracle mode](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md) is not set, this is a synonym for [LENGTH](lengthb.md).


A multi-byte character counts as multiple bytes. This means that for a string containing five two-byte characters, `LENGTHB()` returns 10, whereas [CHAR_LENGTH()](char_length.md) returns 5.


If `str` is not a string value, it is converted into a string. If `str` is `NULL`, the function returns `NULL`.


## Examples


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
* [LENGTH()](lengthb.md)
* [OCTET_LENGTH()](octet_length.md)

