
# SPIDER_DIRECT_SQL

## Syntax


```
SPIDER_DIRECT_SQL('sql', 'tmp_table_list', 'parameters')
```

## Description


A [UDF](../../../../server-usage/programming-customizing-mariadb/user-defined-functions/user-defined-functions-security.md) installed with the [Spider Storage Engine](spider_copy_tables.md), this function is used to execute the SQL string `<code>sql</code>` on the remote server, as defined in `<code>parameters</code>`. If any resultsets are returned, they are stored in the `<code>tmp_table_list</code>`.


The function returns `<code>1</code>` if the SQL executes successfully, or `<code>0</code>` if it fails.


## Examples


```
SELECT SPIDER_DIRECT_SQL('SELECT * FROM s', '', 'srv "node1", port "8607"');
+----------------------------------------------------------------------+
| SPIDER_DIRECT_SQL('SELECT * FROM s', '', 'srv "node1", port "8607"') |
+----------------------------------------------------------------------+
|                                                                    1 |
+----------------------------------------------------------------------+
```

## See also


* [SPIDER_BG_DIRECT_SQL](spider_bg_direct_sql.md)

