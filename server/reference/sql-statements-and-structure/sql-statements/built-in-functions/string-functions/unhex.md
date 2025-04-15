# UNHEX

#

# Syntax

```
UNHEX(str)
```

#

# Description

Performs the inverse operation of [HEX](hex.md)(str). That is, it interprets
each pair of hexadecimal digits in the argument as a number and
converts it to the character represented by the number. The resulting
characters are returned as a binary string.

If `str` is `NULL`, `UNHEX()` returns `NULL`.

#

# Examples

```
SELECT HEX('MariaDB');
+----------------+
| HEX('MariaDB') |
+----------------+
| 4D617269614442 |
+----------------+

SELECT UNHEX('4D617269614442');
+-------------------------+
| UNHEX('4D617269614442') |
+-------------------------+
| MariaDB |
+-------------------------+

SELECT 0x4D617269614442;
+------------------+
| 0x4D617269614442 |
+------------------+
| MariaDB |
+------------------+

SELECT UNHEX(HEX('string'));
+----------------------+
| UNHEX(HEX('string')) |
+----------------------+
| string |
+----------------------+

SELECT HEX(UNHEX('1267'));
+--------------------+
| HEX(UNHEX('1267')) |
+--------------------+
| 1267 |
+--------------------+
```

#

# See Also

* [Hexadecimal literals](../../../sql-language-structure/hexadecimal-literals.md)
* [HEX()](hex.md)
* [CONV()](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/subquery-optimizations/conversion-of-big-in-predicates-into-subqueries.md)