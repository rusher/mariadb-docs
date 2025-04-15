# BIN

#

# Syntax

```
BIN(N)
```

#

# Description

Returns a string representation of the binary value of the given longlong (that is, `[BIGINT](../../../../data-types/data-types-numeric-data-types/bigint.md)`) number. This is equivalent to `[CONV(N,10,2)](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/subquery-optimizations/conversion-of-big-in-predicates-into-subqueries.md)`. The argument should be positive. If it is a `FLOAT`, it will be truncated. Returns `NULL` if the argument is `NULL`.

#

# Examples

```
SELECT BIN(12);
+---------+
| BIN(12) |
+---------+
| 1100 |
+---------+
```

#

# See Also

* [Binary literals](../../../sql-language-structure/binary-literals.md)
* [CONV()](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/subquery-optimizations/conversion-of-big-in-predicates-into-subqueries.md)
* [OCT()](octet_length.md)
* [HEX()](hex.md)