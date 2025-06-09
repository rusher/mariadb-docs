# SHOW INDEX\_STATISTICS

## Syntax

```
SHOW INDEX_STATISTICS
```

## Description

The `SHOW INDEX_STATISTICS` statement was introduced in [MariaDB 5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2) as part of the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature. It was removed as a separate statement in [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes), but effectively replaced by the generic [SHOW information\_schema\_table](broken-reference) statement. The [information\_schema.INDEX\_STATISTICS](../system-tables/information-schema/information-schema-tables/information-schema-index_statistics-table.md) table shows statistics on index usage and makes it possible to do such things as locating unused indexes and generating the commands to remove them.

The [userstat](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#userstat) system variable must be set to 1 to activate this feature. See the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) and [information\_schema.INDEX\_STATISTICS](../system-tables/information-schema/information-schema-tables/information-schema-index_statistics-table.md) table for more information.

## Example

```
SHOW INDEX_STATISTICS;
+--------------+-------------------+------------+-----------+
| Table_schema | Table_name        | Index_name | Rows_read |
+--------------+-------------------+------------+-----------+
| test         | employees_example | PRIMARY    |         1 |
+--------------+-------------------+------------+-----------+
```

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
