
# COMPRESS

## Syntax


```
COMPRESS(string_to_compress)
```

## Description


Compresses a string and returns the result as a binary string. This
function requires MariaDB to have been compiled with a compression
library such as zlib. Otherwise, the return value is always `NULL`. The
compressed string can be uncompressed with `[UNCOMPRESS()](uncompress.md)`.


The [have_compress](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#have_compress) server system variable indicates whether a compression library is present.


## Examples


```
SELECT LENGTH(COMPRESS(REPEAT('a',1000)));
+------------------------------------+
| LENGTH(COMPRESS(REPEAT('a',1000))) |
+------------------------------------+
|                                 21 |
+------------------------------------+

SELECT LENGTH(COMPRESS(''));
+----------------------+
| LENGTH(COMPRESS('')) |
+----------------------+
|                    0 |
+----------------------+

SELECT LENGTH(COMPRESS('a'));
+-----------------------+
| LENGTH(COMPRESS('a')) |
+-----------------------+
|                    13 |
+-----------------------+

SELECT LENGTH(COMPRESS(REPEAT('a',16)));
+----------------------------------+
| LENGTH(COMPRESS(REPEAT('a',16))) |
+----------------------------------+
|                               15 |
+----------------------------------+
```

## See Also


* [Automatic compression of columns](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/storage-engine-independent-column-compression.md)


GPLv2 fill_help_tables.sql

