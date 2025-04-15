
# HEX

## Syntax


```
HEX(N_or_S)
```

## Description


If `<code>N_or_S</code>` is a number, returns a string representation of the hexadecimal
value of `<code>N</code>`, where `<code>N</code>` is a `<code>longlong</code>` (`<code>[BIGINT](../../../../data-types/data-types-numeric-data-types/bigint.md)</code>`) number. This is equivalent to `<code>[CONV](../../../../storage-engines/converting-tables-from-myisam-to-innodb.md)(N,10,16)</code>`.


If `<code>N_or_S</code>` is a string, returns a hexadecimal string representation of
`<code>N_or_S</code>` where each byte of each character in `<code>N_or_S</code>` is converted to two hexadecimal
digits. If `<code>N_or_S</code>` is NULL, returns NULL. The inverse of this operation is performed by the [UNHEX](unhex.md)()
function.






##### MariaDB starting with [10.5.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md)
HEX() with an [INET6](../secondary-functions/miscellaneous-functions/inet6_aton.md) argument returns a hexadecimal representation of the underlying 16-byte binary string.


## Examples


```
SELECT HEX(255);
+----------+
| HEX(255) |
+----------+
| FF       |
+----------+

SELECT 0x4D617269614442;
+------------------+
| 0x4D617269614442 |
+------------------+
| MariaDB          |
+------------------+

SELECT HEX('MariaDB');
+----------------+
| HEX('MariaDB') |
+----------------+
| 4D617269614442 |
+----------------+
```

From [MariaDB 10.5.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md):


```
SELECT HEX(CAST('2001:db8::ff00:42:8329' AS INET6));
+----------------------------------------------+
| HEX(CAST('2001:db8::ff00:42:8329' AS INET6)) |
+----------------------------------------------+
| 20010DB8000000000000FF0000428329             |
+----------------------------------------------+
```

## See Also


* [Hexadecimal literals](../../../sql-language-structure/hexadecimal-literals.md)
* [UNHEX()](unhex.md)
* [CONV()](../../../../storage-engines/converting-tables-from-myisam-to-innodb.md)
* [BIN()](../../../../../../maxscale/mariadb-maxscale-14/maxscale-14-routers/binlogrouter.md)
* [OCT()](../numeric-functions/oct.md)

