
# CONV

## Syntax


```
CONV(N,from_base,to_base)
```

## Description


Converts numbers between different number bases. Returns a string
representation of the number *`<code>N</code>`*, converted from base *`<code>from_base</code>`*
to base *`<code>to_base</code>`*.


Returns `<code>NULL</code>` if any argument is `<code>NULL</code>`, or if the second or third argument are not in the allowed range.


The argument *`<code>N</code>`* is interpreted as an integer, but may be specified as an
integer or a string. The minimum base is 2 and the maximum base is 36 (prior to [MariaDB 11.4.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-0-release-notes.md)) or 62 (from [MariaDB 11.4.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-0-release-notes.md)). If *`<code>to_base</code>`* is a negative number, *`<code>N</code>`* is regarded as a signed number.
Otherwise, *`<code>N</code>`* is treated as unsigned. `<code>CONV()</code>` works with 64-bit
precision.


Some shortcuts for this function are also available: [BIN()](../../../../../../maxscale/mariadb-maxscale-14/maxscale-14-routers/binlogrouter.md), [OCT()](oct.md), [HEX()](../../../sql-language-structure/hexadecimal-literals.md), [UNHEX()](../string-functions/unhex.md). Also, MariaDB allows [binary](../../../sql-language-structure/binary-literals.md) literal values and [hexadecimal](../../../sql-language-structure/hexadecimal-literals.md) literal values.


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
