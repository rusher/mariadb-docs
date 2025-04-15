# CHAR_LENGTH

#

# Syntax

```
CHAR_LENGTH(str)
CHARACTER_LENGTH(str)
```

#

# Description

Returns the length of the given string argument, measured in characters. A multi-byte character counts as a single character. This means that for a string containing five two-byte characters, [LENGTH()](lengthb.md) (or [OCTET_LENGTH()](octet_length.md) in [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/sql_modeoracle)) returns 10, whereas `CHAR_LENGTH()` returns 5. If the argument is `NULL`, it returns `NULL`.

If the argument is not a string value, it is converted into a string.

It is synonymous with the `CHARACTER_LENGTH()` function.

#

# Examples

```
SELECT CHAR_LENGTH('MariaDB');
+------------------------+
| CHAR_LENGTH('MariaDB') |
+------------------------+
| 7 |
+------------------------+
```

When [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/sql_modeoracle) from [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-103) is not set:

```
SELECT CHAR_LENGTH('π'), LENGTH('π'), LENGTHB('π'), OCTET_LENGTH('π');
+-------------------+--------------+---------------+--------------------+
| CHAR_LENGTH('π') | LENGTH('π') | LENGTHB('π') | OCTET_LENGTH('π') |
+-------------------+--------------+---------------+--------------------+
| 1 | 2 | 2 | 2 |
+-------------------+--------------+---------------+--------------------+
```

In [Oracle mode from MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/sql_modeoracle#functions):

```
SELECT CHAR_LENGTH('π'), LENGTH('π'), LENGTHB('π'), OCTET_LENGTH('π');
+-------------------+--------------+---------------+--------------------+
| CHAR_LENGTH('π') | LENGTH('π') | LENGTHB('π') | OCTET_LENGTH('π') |
+-------------------+--------------+---------------+--------------------+
| 1 | 1 | 2 | 2 |
+-------------------+--------------+---------------+--------------------+
```

#

# See Also

* [LENGTH()](lengthb.md)
* [LENGTHB()](lengthb.md)
* [OCTET_LENGTH()](octet_length.md)
* [Oracle mode from MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/sql_modeoracle#simple-syntax-compatibility)