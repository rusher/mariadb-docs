# SPIDER_DIRECT_SQL

#

# Syntax

```
SPIDER_DIRECT_SQL('sql', 'tmp_table_list', 'parameters')
```

#

# Description

A [UDF](../../../../server-usage/programming-customizing-mariadb/user-defined-functions/user-defined-functions-calling-sequences.md) installed with the [Spider Storage Engine](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/spider-status-variables.md), this function is used to execute the SQL string `sql` on the remote server, as defined in `parameters`. If any resultsets are returned, they are stored in the `tmp_table_list`.

The function returns `1` if the SQL executes successfully, or `0` if it fails.

#

# Examples

```
SELECT SPIDER_DIRECT_SQL('SELECT * FROM s', '', 'srv "node1", port "8607"');
+----------------------------------------------------------------------+
| SPIDER_DIRECT_SQL('SELECT * FROM s', '', 'srv "node1", port "8607"') |
+----------------------------------------------------------------------+
| 1 |
+----------------------------------------------------------------------+
```

#

# See also

* [SPIDER_BG_DIRECT_SQL](spider_bg_direct_sql.md)