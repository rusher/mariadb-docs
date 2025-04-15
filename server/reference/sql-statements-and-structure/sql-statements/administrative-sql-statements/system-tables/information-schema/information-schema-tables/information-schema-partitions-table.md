# Information Schema PARTITIONS Table

The [Information Schema](/en/information_schema/) `PARTITIONS` contains information about [table partitions](../../../../../../../server-management/partitioning-tables/partitioning-overview.md), with each record corresponding to a single partition or subpartition of a partitioned table. Each non-partitioned table also has a record in the `PARTITIONS` table, but most of the values are `NULL`.

It contains the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| TABLE_CATALOG | Always def. |
| TABLE_SCHEMA | Database name. |
| TABLE_NAME | Table name containing the partition. |
| PARTITION_NAME | Partition name. |
| SUBPARTITION_NAME | Subpartition name, or NULL if not a subpartition. |
| PARTITION_ORDINAL_POSITION | Order of the partition starting from 1. |
| SUBPARTITION_ORDINAL_POSITION | Order of the subpartition starting from 1. |
| PARTITION_METHOD | The partitioning type; one of [RANGE](../../../../../../../server-management/partitioning-tables/partitioning-types/range-partitioning-type.md), [LIST](../../../../../../../server-management/partitioning-tables/partitioning-types/list-partitioning-type.md), [HASH](../../../../../../../server-management/partitioning-tables/partitioning-types/hash-partitioning-type.md), [LINEAR HASH](../../../../../../../server-management/partitioning-tables/partitioning-types/linear-hash-partitioning-type.md), [KEY](../../../../../../../server-management/partitioning-tables/partitioning-types/key-partitioning-type.md) or [LINEAR KEY](../../../../../../../server-management/partitioning-tables/partitioning-types/linear-key-partitioning-type.md). |
| SUBPARTITION_METHOD | Subpartition type; one of HASH, LINEAR HASH, KEY or LINEAR KEY, or NULL if not a subpartition. |
| PARTITION_EXPRESSION | Expression used to create the partition by the [CREATE TABLE](../../../../data-definition/create/create-tablespace.md) or [ALTER TABLE](../../../../data-definition/alter/alter-table.md) statement. |
| SUBPARTITION_EXPRESSION | Expression used to create the subpartition by the [CREATE TABLE](../../../../data-definition/create/create-tablespace.md) or [ALTER TABLE](../../../../data-definition/alter/alter-table.md) statement, or NULL if not a subpartition. |
| PARTITION_DESCRIPTION | For a RANGE partition, contains either MAXINTEGER or an integer, as set in the VALUES LESS THAN clause. For a LIST partition, contains a comma-separated list of integers, as set in the VALUES IN. For a SYSTEM_TIME INTERVAL partition, shows a defined upper boundary timestamp for historical values (the last history partition can contain values above the upper boundary). NULL if another type of partition. |
| TABLE_ROWS | Number of rows in the table (may be an estimate for some storage engines). |
| AVG_ROW_LENGTH | Average row length, that is DATA_LENGTH divided by TABLE_ROWS |
| DATA_LENGTH | Total number of bytes stored in all rows of the partition. |
| MAX_DATA_LENGTH | Maximum bytes that could be stored in the partition. |
| INDEX_LENGTH | Size in bytes of the partition index file. |
| DATA_FREE | Unused bytes allocated to the partition. |
| CREATE_TIME | Time the partition was created |
| UPDATE_TIME | Time the partition was last modified. |
| CHECK_TIME | Time the partition was last checked, or NULL for storage engines that don't record this information. |
| CHECKSUM | Checksum value, or NULL if none. |
| PARTITION_COMMENT | Partition comment, truncated to 80 characters, or an empty string if no comment. |
| NODEGROUP | Node group, only used for MySQL Cluster, defaults to 0. |
| TABLESPACE_NAME | Always default. |