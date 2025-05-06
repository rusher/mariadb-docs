# DESCRIBE

## Syntax

```
{DESCRIBE | DESC} tbl_name [col_name | wild]
```

## Description

`DESCRIBE` provides information about the columns in a table.\
It is a shortcut for `[SHOW COLUMNS FROM](show/show-columns.md)`.\
These statements also display information for [views](../../../../server-usage/views/).

`col_name` can be a column name, or a string containing the\
SQL "`%`" and "`_`" wildcard characters to\
obtain output only for the columns with names matching the string. There is no\
need to enclose the string within quotes unless it contains spaces or other\
special characters.

```
DESCRIBE city;
+------------+----------+------+-----+---------+----------------+
| Field      | Type     | Null | Key | Default | Extra          |
+------------+----------+------+-----+---------+----------------+
| Id         | int(11)  | NO   | PRI | NULL    | auto_increment |
| Name       | char(35) | YES  |     | NULL    |                |
| Country    | char(3)  | NO   | UNI |         |                |
| District   | char(20) | YES  | MUL |         |                |
| Population | int(11)  | YES  |     | NULL    |                |
+------------+----------+------+-----+---------+----------------+
```

The description for `[SHOW COLUMNS](show/show-columns.md)` provides\
more information about the output columns.

## See Also

* [SHOW COLUMNS](show/show-columns.md)
* [INFORMATION\_SCHEMA.COLUMNS Table](system-tables/information-schema/information-schema-tables/information-schema-columns-table.md)
* [mysqlshow](../../../../clients-and-utilities/legacy-clients-and-utilities/mysqlshow.md)

GPLv2 fill\_help\_tables.sql
