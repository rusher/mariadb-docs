# UNCOMPRESSED\_LENGTH

## Syntax

```
UNCOMPRESSED_LENGTH(compressed_string)
```

## Description

Returns the length that the compressed string had before being\
compressed with `[COMPRESS()](compress.md)`.

`UNCOMPRESSED_LENGTH()` returns `NULL` or an incorrect result if the string is not compressed.

Until [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), returns `MYSQL_TYPE_LONGLONG`, or [bigint(10)](../../../data-types/numeric-data-types/bigint.md), in all cases. From [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), returns `MYSQL_TYPE_LONG`, or [int(10)](../../../data-types/numeric-data-types/int.md), when the result would fit within 32-bits.

## Examples

```
SELECT UNCOMPRESSED_LENGTH(COMPRESS(REPEAT('a',30)));
+-----------------------------------------------+
| UNCOMPRESSED_LENGTH(COMPRESS(REPEAT('a',30))) |
+-----------------------------------------------+
|                                            30 |
+-----------------------------------------------+
```

GPLv2 fill\_help\_tables.sql
