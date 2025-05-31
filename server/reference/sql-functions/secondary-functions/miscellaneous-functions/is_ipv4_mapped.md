# IS\_IPV4\_MAPPED

## Syntax

```
IS_IPV4_MAPPED(expr)
```

## Description

Returns 1 if a given a numeric binary string IPv6 address, such as returned by [INET6\_ATON()](inet6_aton.md), is a valid IPv4-mapped address, otherwise returns 0.

**MariaDB starting with** [**10.5.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-5-series/mariadb-1050-release-notes)

From [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-5-series/mariadb-1050-release-notes), when the argument is not [INET6](../../../data-types/string-data-types/inet6.md), automatic implicit [CAST](../../string-functions/cast.md) to INET6 is applied. As a consequence, `IS_IPV4_MAPPED` now understands arguments in both text representation and binary(16) representation. Before [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-5-series/mariadb-1050-release-notes), the function understood only binary(16) representation.

## Examples

```
SELECT IS_IPV4_MAPPED(INET6_ATON('::10.0.1.1'));
+------------------------------------------+
| IS_IPV4_MAPPED(INET6_ATON('::10.0.1.1')) |
+------------------------------------------+
|                                        0 |
+------------------------------------------+

SELECT IS_IPV4_MAPPED(INET6_ATON('::ffff:10.0.1.1'));
+-----------------------------------------------+
| IS_IPV4_MAPPED(INET6_ATON('::ffff:10.0.1.1')) |
+-----------------------------------------------+
|                                             1 |
+-----------------------------------------------+
```

CC BY-SA / Gnu FDL
