# <=>

#

# Syntax

```
<=>
```

#

# Description

NULL-safe equal operator. It performs an equality comparison like
the [= operator](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/equality-propagation-optimization.md), but returns 1 rather than NULL if both operands are
NULL, and 0 rather than NULL if one operand is NULL.

`a <=> b` is equivalent to `a = b OR (a IS NULL AND b IS NULL)`.

When used in row comparisons these two queries return the same results:

```
SELECT (t1.a, t1.b) <=> (t2.x, t2.y) 
FROM t1 INNER JOIN t2;

SELECT (t1.a <=> t2.x) AND (t1.b <=> t2.y)
FROM t1 INNER JOIN t2;
```

See also [NULL Values in MariaDB](/en/null-values-in-mariadb/).

#

# Examples

```
SELECT 1 <=> 1, NULL <=> NULL, 1 <=> NULL;
+---------+---------------+------------+
| 1 <=> 1 | NULL <=> NULL | 1 <=> NULL |
+---------+---------------+------------+
| 1 | 1 | 0 |
+---------+---------------+------------+

SELECT 1 = 1, NULL = NULL, 1 = NULL;
+-------+-------------+----------+
| 1 = 1 | NULL = NULL | 1 = NULL |
+-------+-------------+----------+
| 1 | NULL | NULL |
+-------+-------------+----------+
```

#

# See Also

* [Operator Precedence](../operator-precedence.md)