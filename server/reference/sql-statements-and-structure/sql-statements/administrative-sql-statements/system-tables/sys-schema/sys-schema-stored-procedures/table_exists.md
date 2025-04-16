
# table_exists

## Syntax


```
table_exists(in_db_name,in_table_name, out_table_type)

# in_db_name VARCHAR(64)
# in_table_name VARCHAR(64)
# out_table_type ENUM('', 'BASE TABLE', 'VIEW', 'TEMPORARY')
```

## Description


`table_exists` is a [stored procedure](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md) available with the [Sys Schema](../sys-schema-views/sys-schema-views-host_summary_by_statement_latency-and-xhost_summary_by_sta.md).


Given a database *in_db_name* and table name *in_table_name*, returns the table type in the OUT parameter *out_table_type*. The return value is an ENUM field containing one of:


* '' - the table does not exist
* 'BASE TABLE' - a regular table
* 'VIEW' - a view
* 'TEMPORARY' - a temporary table


## Examples


```
CALL sys.table_exists('mysql', 'time_zone', @table_type); SELECT @table_type;
+-------------+
| @table_type |
+-------------+
| BASE TABLE  |
+-------------+

CALL sys.table_exists('mysql', 'user', @table_type); SELECT @table_type;
+-------------+
| @table_type |
+-------------+
| VIEW        |
+-------------+
```
