# OCT

#

# Syntax

```
OCT(N)
```

#

# Description

Returns a string representation of the octal value of N, where N is a longlong ([BIGINT](../../../../data-types/data-types-numeric-data-types/bigint.md)) number. This is equivalent to [CONV(N,10,8)](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/subquery-optimizations/conversion-of-big-in-predicates-into-subqueries.md). Returns NULL if N is NULL.

#

# Examples

```
SELECT OCT(34);
+---------+
| OCT(34) |
+---------+
| 42 |
+---------+

SELECT OCT(12);
+---------+
| OCT(12) |
+---------+
| 14 |
+---------+
```

#

# See Also

* [CONV()](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/subquery-optimizations/conversion-of-big-in-predicates-into-subqueries.md)
* [BIN()](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/binlog_checkpoint_event.md)
* [HEX()](../string-functions/hex.md)