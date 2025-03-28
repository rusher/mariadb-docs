# Information Schema TABLE_STATISTICS Table

The [Information Schema](/en/information_schema/) `TABLE_STATISTICS` table shows statistics on table usage.

This is part of the [User Statistics](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature, which is not enabled by default.

It contains the following columns:

| Field | Type | Notes |
| --- | --- | --- |
| Field | Type | Notes |
| TABLE_SCHEMA | varchar(192) | The schema (database) name. |
| TABLE_NAME | varchar(192) | The table name. |
| ROWS_READ | bigint(21) | The number of rows read from the table. |
| ROWS_CHANGED | bigint(21) | The number of rows changed in the table. |
| ROWS_CHANGED_X_INDEXES | bigint(21) | The number of rows changed in the table, multiplied by the number of indexes changed. |
| ROWS_INSERTED | bigint(21) | From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-115) |
| ROWS_UPDATED | bigint(21) | From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-115) |
| ROWS_DELETED | bigint(21) | From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-115) |
| KEY_READ_HITS | bigint(21) | From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-115) |
| KEY_READ_MISSES | bigint(21) | From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-115) |

#

### Example

```
SELECT * FROM INFORMATION_SCHEMA.TABLE_STATISTICS WHERE TABLE_NAME='user';
+--------------+------------+-----------+--------------+------------------------+
| TABLE_SCHEMA | TABLE_NAME | ROWS_READ | ROWS_CHANGED | ROWS_CHANGED_X_INDEXES |
+--------------+------------+-----------+--------------+------------------------+
| mysql | user | 5 | 2 | 2 |
+--------------+------------+-----------+--------------+------------------------+
```