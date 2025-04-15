
# Hexadecimal Literals

Hexadecimal literals can be written using any of the following syntaxes:


* x'`<code>value</code>`'
* X'`<code>value</code>`' (SQL standard)
* 0x`<code>value</code>` (ODBC)


`<code>value</code>` is a sequence of hexadecimal digits (from `<code>0</code>` to `<code>9</code>` and from `<code>A</code>` to `<code>F</code>`). The case of the digits does not matter. With the first two syntaxes, `<code>value</code>` must consist of an even number of digits. With the last syntax, digits can be even, and they are treated as if they had an extra 0 at the beginning.


Normally, hexadecimal literals are interpreted as binary string, where each pair of digits represents a character. When used in a numeric context, they are interpreted as integers. (See the example below). In no case can a hexadecimal literal be a decimal number.


The first two syntaxes; `<code>X'value'</code>` and x'`<code>value</code>`, follow the SQL standard, and behave as a string in all contexts in MariaDB since [MariaDB 10.0.3](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1003-release-notes.md) and [MariaDB 5.5.31](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5531-release-notes.md) (fixing [MDEV-4489](https://jira.mariadb.org/browse/MDEV-4489)). The latter syntax, 0x`<code>value</code>`, is a MySQL/MariaDB extension for hex hybrids and behaves as a string or as a number depending on context. MySQL treats all syntaxes the same, so there may be different results in MariaDB and MySQL (see below).


## Examples


Representing the `<code>a</code>` character with the three syntaxes explained above:


```
SELECT x'61', X'61', 0x61;
+-------+-------+------+
| x'61' | X'61' | 0x61 |
+-------+-------+------+
| a     | a     | a    |
+-------+-------+------+
```

Hexadecimal literals in a numeric context:


```
SELECT 0 + 0xF, -0xF;
+---------+------+
| 0 + 0xF | -0xF |
+---------+------+
|      15 |  -15 |
+---------+------+
```

### Fun with Types


```
CREATE TABLE t1 (a INT, b VARCHAR(10));
INSERT INTO t1 VALUES (0x31, 0x61),(COALESCE(0x31), COALESCE(0x61));

SELECT * FROM t1;
+------+------+
| a    | b    |
+------+------+
|   49 | a    |
|    1 | a    |
+------+------+
```

The reason for the differing results above is that when 0x31 is inserted directly to the column, it's treated as a number, while when 0x31 is passed to [COALESCE()](../operators/comparison-operators/coalesce.md), it's treated as a string, because:


* HEX values have a string data type by default.
* COALESCE() has the same data type as the argument.


### Differences Between MariaDB and MySQL


```
SELECT x'0a'+0;
+---------+
| x'0a'+0 |
+---------+
|       0 |
+---------+
1 row in set, 1 warning (0.00 sec)

Warning (Code 1292): Truncated incorrect DOUBLE value: '\x0A'

SELECT X'0a'+0;
+---------+
| X'0a'+0 |
+---------+
|       0 |
+---------+
1 row in set, 1 warning (0.00 sec)

Warning (Code 1292): Truncated incorrect DOUBLE value: '\x0A'

SELECT 0x0a+0;
+--------+
| 0x0a+0 |
+--------+
|     10 |
+--------+
```

In MySQL (up until at least MySQL 8.0.26):


```
SELECT x'0a'+0;
+---------+
| x'0a'+0 |
+---------+
|      10 |
+---------+

SELECT X'0a'+0;
+---------+
| X'0a'+0 |
+---------+
|      10 |
+---------+

SELECT 0x0a+0;
+--------+
| 0x0a+0 |
+--------+
|     10 |
+--------+
```

## See Also


* [HEX()](hexadecimal-literals.md)
* [UNHEX()](../sql-statements/built-in-functions/string-functions/unhex.md)

