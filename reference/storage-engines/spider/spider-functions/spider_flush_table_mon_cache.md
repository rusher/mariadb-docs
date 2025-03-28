# SPIDER_FLUSH_TABLE_MON_CACHE

#

# Syntax

```
SPIDER_FLUSH_TABLE_MON_CACHE()
```

#

# Description

A [UDF](../../../../server-usage/programming-customizing-mariadb/user-defined-functions/user-defined-functions-calling-sequences.md) installed with the [Spider Storage Engine](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/spider-status-variables.md), this function is used for refreshing monitoring server information. It returns a value of `1`.

#

# Examples

```
SELECT SPIDER_FLUSH_TABLE_MON_CACHE();
+--------------------------------+
| SPIDER_FLUSH_TABLE_MON_CACHE() |
+--------------------------------+
| 1 |
+--------------------------------+
```