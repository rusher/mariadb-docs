
# SPIDER_COPY_TABLES

## Syntax


```
SPIDER_COPY_TABLES(spider_table_name, 
  source_link_id, destination_link_id_list [,parameters])
```

## Description


A [UDF](../../../../server-usage/programming-customizing-mariadb/user-defined-functions/user-defined-functions-security.md) installed with the [Spider Storage Engine](spider_copy_tables.md), this function copies table data from `<code>source_link_id</code>` to `<code>destination_link_id_list</code>`. The service does not need to be stopped in order to copy.


If the Spider table is partitioned, the name must be of the format `<code>table_name#P#partition_name</code>`. The partition name can be viewed in the `<code>mysql.spider_tables</code>` table, for example:


```
SELECT table_name FROM mysql.spider_tables;
+-------------+
| table_name  |
+-------------+
| spt_a#P#pt1 |
| spt_a#P#pt2 |
| spt_a#P#pt3 |
+-------------+
```

Returns `<code>1</code>` if the data was copied successfully, or `<code>0</code>` if copying the data failed.

