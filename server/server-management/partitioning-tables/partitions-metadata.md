# Partitions Metadata

The [PARTITIONS](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-partitions-table.md) table in the [INFORMATION_SCHEMA](../../server-usage/programming-customizing-mariadb/views/information-schema-views-table.md) database contains information about partitions.

The [SHOW TABLE STATUS](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-table-status.md) statement contains a `Create_options` column, that contains the string 'partitioned' for partitioned tables.

The [SHOW CREATE TABLE](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-table.md) statement returns the [CREATE TABLE](../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md) statement that can be used to re-create a table, including the partitions definition.