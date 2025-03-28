# ISNULL

#

# Syntax

```
ISNULL(expr)
```

#

# Description

If *`expr`* is NULL, ISNULL() returns 1, otherwise it returns 0.

See also [NULL Values in MariaDB](/kb/en/null-values-in-mariadb/).

#

# Examples

```
SELECT ISNULL(1+1);
+-------------+
| ISNULL(1+1) |
+-------------+
| 0 |
+-------------+

SELECT ISNULL(1/0);
+-------------+
| ISNULL(1/0) |
+-------------+
| 1 |
+-------------+
```