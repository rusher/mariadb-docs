
# OCTET_LENGTH

## Syntax


```
OCTET_LENGTH(str)
```

## Description


`OCTET_LENGTH()` returns the length of the given string, in octets (bytes). This is a synonym for [LENGTHB()](lengthb.md), and, when [Oracle mode from MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/sql_modeoracle#functions) is not set, a synonym for [LENGTH()](length.md).


A multi-byte character counts as multiple bytes. This means that for a string containing five two-byte characters, `OCTET_LENGTH()` returns 10, whereas [CHAR_LENGTH()](char_length.md) returns 5.


If `str` is not a string value, it is converted into a string. If `str` is `NULL`, the function returns `NULL`.


## Examples


When [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/sql_modeoracle) from [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103) is not set:


```
SELECT CHAR_LENGTH('π'), LENGTH('π'), LENGTHB('π'), OCTET_LENGTH('π');
+-------------------+--------------+---------------+--------------------+
| CHAR_LENGTH('π')  | LENGTH('π')  | LENGTHB('π')  | OCTET_LENGTH('π')  |
+-------------------+--------------+---------------+--------------------+
|                 1 |            2 |             2 |                  2 |
+-------------------+--------------+---------------+--------------------+
```

In [Oracle mode from MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/sql_modeoracle#functions):


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
* [LENGTH()](length.md)
* [LENGTHB()](lengthb.md)
* [Oracle mode from MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/sql_modeoracle)

