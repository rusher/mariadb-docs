
# UNCOMPRESSED_LENGTH

## Syntax


```
UNCOMPRESSED_LENGTH(compressed_string)
```

## Description


Returns the length that the compressed string had before being
compressed with `<code>[COMPRESS()](compress.md)</code>`.


`<code>UNCOMPRESSED_LENGTH()</code>` returns `<code>NULL</code>` or an incorrect result if the string is not compressed.


Until [MariaDB 10.3.1](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), returns `<code>MYSQL_TYPE_LONGLONG</code>`, or [bigint(10)](../../../../../data-types/data-types-numeric-data-types/bigint.md), in all cases. From [MariaDB 10.3.1](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md), returns `<code>MYSQL_TYPE_LONG</code>`, or [int(10)](../../../../../../../general-resources/learning-and-training/video-presentations-and-screencasts/interviews-related-to-mariadb.md), when the result would fit within 32-bits.


## Examples


```
SELECT UNCOMPRESSED_LENGTH(COMPRESS(REPEAT('a',30)));
+-----------------------------------------------+
| UNCOMPRESSED_LENGTH(COMPRESS(REPEAT('a',30))) |
+-----------------------------------------------+
|                                            30 |
+-----------------------------------------------+
```
