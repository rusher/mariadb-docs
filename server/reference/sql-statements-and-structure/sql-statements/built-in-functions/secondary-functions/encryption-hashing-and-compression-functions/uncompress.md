# UNCOMPRESS

## Syntax

```
UNCOMPRESS(string_to_uncompress)
```

## Description

Uncompresses a string compressed by the `[COMPRESS()](compress.md)` function. If the\
argument is not a compressed value, the result is `NULL`. This function\
requires MariaDB to have been compiled with a compression library such\
as zlib. Otherwise, the return value is always `NULL`. The [have\_compress](../../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#have_compress) server system variable indicates whether a compression library is present.

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

GPLv2 fill\_help\_tables.sql
