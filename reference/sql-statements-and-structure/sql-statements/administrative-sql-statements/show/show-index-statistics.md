# SHOW INDEX_STATISTICS

#

# Syntax

```
SHOW INDEX_STATISTICS
```

#

# Description

The `SHOW INDEX_STATISTICS` statement was introduced in [MariaDB 5.2](/en/what-is-mariadb-52/) as part of the [User Statistics](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature. It was removed as a separate statement in [MariaDB 10.1.1](/en/mariadb-1011-release-notes/), but effectively replaced by the generic [SHOW information_schema_table](https://app.gitbook.com/s/iJPrPCGi329TSR8WIXJW/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/mariadb-internals-documentation/information-schema-plugins-show-and-flush-statements) statement. The [information_schema.INDEX_STATISTICS](../system-tables/information-schema/information-schema-tables/information-schema-index_statistics-table.md) table shows statistics on index usage and makes it possible to do such things as locating unused indexes and generating the commands to remove them.

The [userstat](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#userstat) system variable must be set to 1 to activate this feature. See the [User Statistics](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) and [information_schema.INDEX_STATISTICS](../system-tables/information-schema/information-schema-tables/information-schema-index_statistics-table.md) table for more information.

#

# Example

```
SHOW INDEX_STATISTICS;
+--------------+-------------------+------------+-----------+
| Table_schema | Table_name | Index_name | Rows_read |
+--------------+-------------------+------------+-----------+
| test | employees_example | PRIMARY | 1 |
+--------------+-------------------+------------+-----------+
```