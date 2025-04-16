
# Partitions Metadata

The [PARTITIONS](../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-partitions-table.md) table in the [INFORMATION_SCHEMA](../../ref/mariadb-internals/information-schema-plugins-show-and-flush-statements.md) database contains information about partitions.


The [SHOW TABLE STATUS](../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-table-status.md) statement contains a `Create_options` column, that contains the string 'partitioned' for partitioned tables.


The [SHOW CREATE TABLE](../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-table.md) statement returns the [CREATE TABLE](../../ref/sql-statements-and-structure/vectors/create-table-with-vectors.md) statement that can be used to re-create a table, including the partitions definition.

