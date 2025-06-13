# LENGTH

## Syntax

```
LENGTH(str)
```

## Description

Returns the length of the string `str`.

In the default mode, when [Oracle mode from MariaDB 10.3](broken-reference) is not set, the length is measured in bytes. In this case, a multi-byte character counts as multiple bytes. This means that for a string\
containing five two-byte characters, `LENGTH()` returns 10, whereas [CHAR\_LENGTH()](char_length.md) returns 5.

When running [Oracle mode from MariaDB 10.3](broken-reference), the length is measured in characters, and `LENGTH` is a synonym for [CHAR\_LENGTH()](char_length.md).

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

When [Oracle mode](broken-reference) from [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103) is not set:

```
SELECT CHAR_LENGTH('π'), LENGTH('π'), LENGTHB('π'), OCTET_LENGTH('π');
+-------------------+--------------+---------------+--------------------+
| CHAR_LENGTH('π')  | LENGTH('π')  | LENGTHB('π')  | OCTET_LENGTH('π')  |
+-------------------+--------------+---------------+--------------------+
|                 1 |            2 |             2 |                  2 |
+-------------------+--------------+---------------+--------------------+
```

In [Oracle mode from MariaDB 10.3](broken-reference):

```
SELECT CHAR_LENGTH('π'), LENGTH('π'), LENGTHB('π'), OCTET_LENGTH('π');
+-------------------+--------------+---------------+--------------------+
| CHAR_LENGTH('π')  | LENGTH('π')  | LENGTHB('π')  | OCTET_LENGTH('π')  |
+-------------------+--------------+---------------+--------------------+
|                 1 |            1 |             2 |                  2 |
+-------------------+--------------+---------------+--------------------+
```

## See Also

* [CHAR\_LENGTH()](char_length.md)
* [LENGTHB()](lengthb.md)
* [OCTET\_LENGTH()](octet_length.md)
* [Oracle mode from MariaDB 10.3](broken-reference)

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
