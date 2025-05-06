# SPIDER\_FLUSH\_TABLE\_MON\_CACHE

## Syntax

```
SPIDER_FLUSH_TABLE_MON_CACHE()
```

## Description

A [UDF](../../../../server-usage/user-defined-functions/) installed with the [Spider Storage Engine](../), this function is used for refreshing monitoring server information. It returns a value of `1`.

## Examples

```
SELECT SPIDER_FLUSH_TABLE_MON_CACHE();
+--------------------------------+
| SPIDER_FLUSH_TABLE_MON_CACHE() |
+--------------------------------+
|                              1 |
+--------------------------------+
```

CC BY-SA / Gnu FDL
