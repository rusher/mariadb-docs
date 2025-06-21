# HEX

## Syntax

```
HEX(N_or_S)
```

## Description

If `N_or_S` is a number, returns a string representation of the hexadecimal\
value of `N`, where `N` is a `longlong` ([BIGINT](../../../../data-types/data-types-numeric-data-types/bigint.md)) number. This is equivalent to [CONV](../numeric-functions/conv.md)(N,10,16).

If `N_or_S` is a string, returns a hexadecimal string representation of`N_or_S` where each byte of each character in `N_or_S` is converted to two hexadecimal\
digits. If `N_or_S` is NULL, returns NULL. The inverse of this operation is performed by the [UNHEX](unhex.md)()\
function.

**MariaDB starting with** [**10.5.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1050-release-notes)

HEX() with an [INET6](../../data-types/string-data-types/inet6.md) argument returns a hexadecimal representation of the underlying 16-byte binary string.

## Examples

```
SELECT HEX(255);
+----------+
| HEX(255) |
+----------+
| FF       |
+----------+

SELECT 0x4D617269614442;
+------------------+
| 0x4D617269614442 |
+------------------+
| MariaDB          |
+------------------+

SELECT HEX('MariaDB');
+----------------+
| HEX('MariaDB') |
+----------------+
| 4D617269614442 |
+----------------+
```

From [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1050-release-notes):

```
SELECT HEX(CAST('2001:db8::ff00:42:8329' AS INET6));
+----------------------------------------------+
| HEX(CAST('2001:db8::ff00:42:8329' AS INET6)) |
+----------------------------------------------+
| 20010DB8000000000000FF0000428329             |
+----------------------------------------------+
```

## See Also

* [Hexadecimal literals](../../sql-structure/sql-language-structure/hexadecimal-literals.md)
* [UNHEX()](unhex.md)
* [CONV()](../numeric-functions/conv.md)
* [BIN()](bin.md)
* [OCT()](../numeric-functions/oct.md)

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
