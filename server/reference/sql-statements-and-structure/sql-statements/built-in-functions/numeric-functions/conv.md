
# CONV

## Syntax


```
CONV(N,from_base,to_base)
```

## Description


Converts numbers between different number bases. Returns a string
representation of the number *`N`*, converted from base *`from_base`*
to base *`to_base`*.


Returns `NULL` if any argument is `NULL`, or if the second or third argument are not in the allowed range.


The argument *`N`* is interpreted as an integer, but may be specified as an
integer or a string. The minimum base is 2 and the maximum base is 36 (prior to [MariaDB 11.4.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-11-4-series/mariadb-11-4-0-release-notes)) or 62 (from [MariaDB 11.4.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-11-4-series/mariadb-11-4-0-release-notes)). If *`to_base`* is a negative number, *`N`* is regarded as a signed number.
Otherwise, *`N`* is treated as unsigned. `CONV()` works with 64-bit
precision.


Some shortcuts for this function are also available: [BIN()](../string-functions/bin.md), [OCT()](oct.md), [HEX()](../string-functions/hex.md), [UNHEX()](../string-functions/unhex.md). Also, MariaDB allows [binary](../../../sql-language-structure/binary-literals.md) literal values and [hexadecimal](../../../sql-language-structure/hexadecimal-literals.md) literal values.


## Examples


```
SELECT CONV('a',16,2);
+----------------+
| CONV('a',16,2) |
+----------------+
| 1010           |
+----------------+

SELECT CONV('6E',18,8);
+-----------------+
| CONV('6E',18,8) |
+-----------------+
| 172             |
+-----------------+

SELECT CONV(-17,10,-18);
+------------------+
| CONV(-17,10,-18) |
+------------------+
| -H               |
+------------------+

SELECT CONV(12+'10'+'10'+0xa,10,10);
+------------------------------+
| CONV(12+'10'+'10'+0xa,10,10) |
+------------------------------+
| 42                           |
+------------------------------+
```
