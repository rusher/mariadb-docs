# EXP

#

# Syntax

```
EXP(X)
```

#

# Description

Returns the value of e (the base of natural logarithms) raised to the
power of X. The inverse of this function is [LOG()](../../../../../server-management/server-monitoring-logs/slow-query-log/log_slow_always_query_time-system-variable.md) (using a single
argument only) or [LN()](ln.md).

If `X` is `NULL`, this function returns `NULL`.

#

# Examples

```
SELECT EXP(2);
+------------------+
| EXP(2) |
+------------------+
| 7.38905609893065 |
+------------------+

SELECT EXP(-2);
+--------------------+
| EXP(-2) |
+--------------------+
| 0.1353352832366127 |
+--------------------+

SELECT EXP(0);
+--------+
| EXP(0) |
+--------+
| 1 |
+--------+

SELECT EXP(NULL);
+-----------+
| EXP(NULL) |
+-----------+
| NULL |
+-----------+
```