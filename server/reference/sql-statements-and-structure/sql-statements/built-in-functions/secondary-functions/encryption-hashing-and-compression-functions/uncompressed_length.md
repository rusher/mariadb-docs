# UNCOMPRESSED_LENGTH

#

# Syntax

```
UNCOMPRESSED_LENGTH(compressed_string)
```

#

# Description

Returns the length that the compressed string had before being
compressed with `[COMPRESS()](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md)`.

`UNCOMPRESSED_LENGTH()` returns `NULL` or an incorrect result if the string is not compressed.

Until [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), returns `MYSQL_TYPE_LONGLONG`, or [bigint(10)](../../../../../data-types/data-types-numeric-data-types/bigint.md), in all cases. From [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), returns `MYSQL_TYPE_LONG`, or [int(10)](../../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/intvar_event.md), when the result would fit within 32-bits.

#

# Examples

```
SELECT UNCOMPRESSED_LENGTH(COMPRESS(REPEAT('a',30)));
+-----------------------------------------------+
| UNCOMPRESSED_LENGTH(COMPRESS(REPEAT('a',30))) |
+-----------------------------------------------+
| 30 |
+-----------------------------------------------+
```