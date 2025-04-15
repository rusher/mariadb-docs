
# UNCOMPRESS

## Syntax


```
UNCOMPRESS(string_to_uncompress)
```

## Description


Uncompresses a string compressed by the `<code>[COMPRESS()](compress.md)</code>` function. If the
argument is not a compressed value, the result is `<code>NULL</code>`. This function
requires MariaDB to have been compiled with a compression library such
as zlib. Otherwise, the return value is always `<code>NULL</code>`. The [have_compress](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#have_compress) server system variable indicates whether a compression library is present.


## Examples


```
SELECT UNCOMPRESS(COMPRESS('a string'));
+----------------------------------+
| UNCOMPRESS(COMPRESS('a string')) |
+----------------------------------+
| a string                         |
+----------------------------------+

SELECT UNCOMPRESS('a string');
+------------------------+
| UNCOMPRESS('a string') |
+------------------------+
| NULL                   |
+------------------------+
```
