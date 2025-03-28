# HEX

#

# Syntax

```
HEX(N_or_S)
```

#

# Description

If `N_or_S` is a number, returns a string representation of the hexadecimal
value of `N`, where `N` is a `longlong` (`[BIGINT](../../../../data-types/data-types-numeric-data-types/bigint.md)`) number. This is equivalent to `[CONV](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/subquery-optimizations/conversion-of-big-in-predicates-into-subqueries.md)(N,10,16)`.

If `N_or_S` is a string, returns a hexadecimal string representation of
`N_or_S` where each byte of each character in `N_or_S` is converted to two hexadecimal
digits. If `N_or_S` is NULL, returns NULL. The inverse of this operation is performed by the [UNHEX](unhex.md)()
function.

#

#### MariaDB starting with [10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1050-release-notes)

HEX() with an [INET6](../../../../data-types/string-data-types/inet6.md) argument returns a hexadecimal representation of the underlying 16-byte binary string.

#

# Examples

```
SELECT HEX(255);
+----------+
| HEX(255) |
+----------+
| FF |
+----------+

SELECT 0x4D617269614442;
+------------------+
| 0x4D617269614442 |
+------------------+
| MariaDB |
+------------------+

SELECT HEX('MariaDB');
+----------------+
| HEX('MariaDB') |
+----------------+
| 4D617269614442 |
+----------------+
```

From [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1050-release-notes):

```
SELECT HEX(CAST('2001:db8::ff00:42:8329' AS INET6));
+----------------------------------------------+
| HEX(CAST('2001:db8::ff00:42:8329' AS INET6)) |
+----------------------------------------------+
| 20010DB8000000000000FF0000428329 |
+----------------------------------------------+
```

#

# See Also

* [Hexadecimal literals](../../../sql-language-structure/hexadecimal-literals.md)
* [UNHEX()](unhex.md)
* [CONV()](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/subquery-optimizations/conversion-of-big-in-predicates-into-subqueries.md)
* [BIN()](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/binlog_checkpoint_event.md)
* [OCT()](octet_length.md)