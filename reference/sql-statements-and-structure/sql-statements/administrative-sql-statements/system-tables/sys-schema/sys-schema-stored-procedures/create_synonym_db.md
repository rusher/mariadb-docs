# create_synonym_db

#

# Syntax

```
create_synonym_db(db_name,synonym)

# db_name (VARCHAR(64))

# synonym (VARCHAR(64))
```

#

# Description

`create_synonym_db` is a [stored procedure](/en/stored-procedures/) available with the [Sys Schema](../sys-schema-sys_config-table.md).

Takes a source database name *db_name* and *synonym* name and creates a synonym database with views that point to all of the tables within the source database. Useful for example for creating a synonym for the [performance_schema](../../performance-schema/performance-schema-status-variables.md) or [information_schema](../../../../../../../server-usage/programming-customizing-mariadb/views/information-schema-views-table.md) databases.

Returns an error if the source database doesn't exist, or the synonym already exists.

#

# Example

```
SHOW DATABASES;
+--------------------+
| Database |
+--------------------+
| information_schema |
| mysql |
| performance_schema |
| sys |
| test |
+--------------------+

CALL sys.create_synonym_db('performance_schema', 'perf');
+-----------------------------------------+
| summary |
+-----------------------------------------+
| Created 81 views in the `perf` database |
+-----------------------------------------+

SHOW DATABASES;
+--------------------+
| Database |
+--------------------+
| information_schema |
| mysql |
| perf |
| performance_schema |
| sys |
| test |
+--------------------+

SHOW FULL TABLES FROM perf;
+------------------------------------------------------+------------+
| Tables_in_perf | Table_type |
+------------------------------------------------------+------------+
| accounts | VIEW |
| cond_instances | VIEW |
| events_stages_current | VIEW |
| events_stages_history | VIEW |
| events_stages_history_long | VIEW |
...
```