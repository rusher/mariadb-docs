# SPIDER_COPY_TABLES

#

# Syntax

```
SPIDER_COPY_TABLES(spider_table_name, 
 source_link_id, destination_link_id_list [,parameters])
```

#

# Description

A [UDF](../../../../server-usage/programming-customizing-mariadb/user-defined-functions/user-defined-functions-calling-sequences.md) installed with the [Spider Storage Engine](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/spider-status-variables.md), this function copies table data from `source_link_id` to `destination_link_id_list`. The service does not need to be stopped in order to copy.

If the Spider table is partitioned, the name must be of the format `table_name#P#partition_name`. The partition name can be viewed in the `mysql.spider_tables` table, for example:

```
SELECT table_name FROM mysql.spider_tables;
+-------------+
| table_name |
+-------------+
| spt_a#P#pt1 |
| spt_a#P#pt2 |
| spt_a#P#pt3 |
+-------------+
```

Returns `1` if the data was copied successfully, or `0` if copying the data failed.