# Partitioning Limitations

The following limitations apply to partitioning in MariaDB:

* Each table can contain a maximum of 8192 partitions. Until [MariaDB 10.0.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1003-release-notes), the limit was 1024.
* Queries are never parallelized, even when they involve multiple partitions.
* A table can only be partitioned if the storage engine supports partitioning.
* All partitions must use the same storage engine. For a workaround, see [Using CONNECT - Partitioning and Sharding](../storage-engines/connect/using-connect/using-connect-partitioning-and-sharding.md).
* A partitioned table cannot contain, or be referenced by, [foreign keys](../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md).
* The [query cache](../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md) is not aware of partitioning and partition pruning. Modifying a partition will invalidate the entries related to the whole table.
* Updates can run more slowly when [binlog\_format=ROW](../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#row-based-logging) and a partitioned table is updated than an equivalent update of a non-partitioned table.
* All columns used in the partitioning expression for a partitioned table must be part of every unique key that the table may have.
* In versions prior to [MariaDB 11.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes), it is not possible to create partitions on tables that contain [GEOMETRY types](../../reference/sql-structure/geometry/geometry-types.md).

## See Also

* [INFORMATION\_SCHEMA.PARTITIONS](../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-partitions-table.md) contains information about existing partitions.
* [Partition Maintenance](partition-maintenance.md) for suggestions on using partitions

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
