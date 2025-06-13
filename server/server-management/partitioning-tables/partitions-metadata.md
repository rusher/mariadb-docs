# Partitions Metadata

The [PARTITIONS](../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-partitions-table.md) table in the [INFORMATION\_SCHEMA](../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/) database contains information about partitions.

The [SHOW TABLE STATUS](../../reference/sql-statements/administrative-sql-statements/show/show-table-status.md) statement contains a `Create_options` column, that contains the string 'partitioned' for partitioned tables.

The [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) statement returns the [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) statement that can be used to re-create a table, including the partitions definition.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
