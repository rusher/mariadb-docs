# innodb_buffer_stats_by_schema and x$innodb_buffer_stats_by_schema Sys Schema Views

#

#### MariaDB starting with [10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-106)

These [Sys Schema](../sys-schema-sys_config-table.md) views were introduced in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-106).

Querying these views can have a noticeable performance impact on a production server.

#

# Description

The `innodb_buffer_stats_by_schema` and `x$innodb_buffer_stats_by_schema` views summarize information from the [Information Schema INNODB_BUFFER_PAGE table](../../information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_buffer_page-table.md), grouped by schema. Rows are sorted by descending buffer size by default.

The `innodb_buffer_stats_by_schema` view is intended to be easier for human reading, while the `x$innodb_buffer_stats_by_schema` view provides the data in raw form, intended for tools that process the data.

They contain the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| object_schema | Object schema name, or InnoDB System if the table belongs to the [InnoDB storage engine](../../../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md). |
| allocated | Total number of bytes allocated for the schema. |
| data | Total number of data bytes allocated for the schema. |
| pages | Total number of pages allocated for the schema. |
| pages_hashed | Total number of hashed pages allocated for the schema. |
| pages_old | Total number of old pages allocated for the schema. |
| rows_cached | Total number of cached rows for the schema. |

#

# Example

```
SELECT * FROM sys.innodb_buffer_stats_by_schema\G
*************************** 1. row ***************************
object_schema: InnoDB System
 allocated: 160.00 KiB
 data: 6.21 KiB
 pages: 10
 pages_hashed: 10
 pages_old: 10
 rows_cached: 21
*************************** 2. row ***************************
object_schema: mysql
 allocated: 112.00 KiB
 data: 1.73 KiB
 pages: 7
 pages_hashed: 7
 pages_old: 7
 rows_cached: 5
*************************** 3. row ***************************
object_schema: test
 allocated: 64.00 KiB
 data: 0 bytes
 pages: 4
 pages_hashed: 4
 pages_old: 4
 rows_cached: 0

SELECT * FROM sys.x$innodb_buffer_stats_by_schema\G
*************************** 1. row ***************************
object_schema: InnoDB System
 allocated: 163840
 data: 6362
 pages: 10
 pages_hashed: 0
 pages_old: 0
 rows_cached: 21
*************************** 2. row ***************************
object_schema: mysql
 allocated: 114688
 data: 1775
 pages: 7
 pages_hashed: 0
 pages_old: 0
 rows_cached: 5
*************************** 3. row ***************************
object_schema: test
 allocated: 65536
 data: 0
 pages: 4
 pages_hashed: 0
 pages_old: 0
 rows_cached: 0
```