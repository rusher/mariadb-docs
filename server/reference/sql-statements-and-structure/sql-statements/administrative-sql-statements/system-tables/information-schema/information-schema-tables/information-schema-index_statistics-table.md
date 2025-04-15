# Information Schema INDEX_STATISTICS Table

The [Information Schema](/en/information_schema/) `INDEX_STATISTICS` table shows statistics on index usage and makes it possible to do such things as locating unused indexes and generating the commands to remove them.

This is part of the [User Statistics](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature, which is not enabled by default.

It contains the following columns:

| Field | Type | Notes |
| --- | --- | --- |
| Field | Type | Notes |
| TABLE_SCHEMA | VARCHAR(192) | The schema (database) name. |
| TABLE_NAME | VARCHAR(192) | The table name. |
| INDEX_NAME | VARCHAR(192) | The index name (as visible in [SHOW CREATE TABLE](../../../show/show-create-table.md)). |
| ROWS_READ | BIGINT(21) | The number of rows read from this index. |
| QUERIES | BIGINT(21) | Incremented for each index the query is part of. This assists one to see how effective the index is. From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-115) |

#

# Example

```
SELECT * FROM information_schema.INDEX_STATISTICS 
WHERE TABLE_NAME = "author";
+--------------+------------+------------+-----------+
| TABLE_SCHEMA | TABLE_NAME | INDEX_NAME | ROWS_READ |
+--------------+------------+------------+-----------+
| books | author | by_name | 15 |
+--------------+------------+------------+-----------+
```