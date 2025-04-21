
# SHOW TABLE_STATISTICS

## Syntax


```
SHOW TABLE_STATISTICS
```

## Description


The `SHOW TABLE_STATISTICS` statementis part of the [User Statistics](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature. It was removed as a separate statement in [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes), but effectively replaced by the generic [SHOW information_schema_table](../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) statement. The [information_schema.TABLE_STATISTICS](../system-tables/information-schema/information-schema-tables/information-schema-table_statistics-table.md) table shows statistics on table usage


The [userstat](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#userstat) system variable must be set to 1 to activate this feature. See the [User Statistics](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) and [information_schema.TABLE_STATISTICS](../system-tables/information-schema/information-schema-tables/information-schema-table_statistics-table.md) articles for more information.


## Example


```
SHOW TABLE_STATISTICS\G
*************************** 1. row ***************************
           Table_schema: mysql
             Table_name: proxies_priv
              Rows_read: 2
           Rows_changed: 0
Rows_changed_x_#indexes: 0
*************************** 2. row ***************************
           Table_schema: test
             Table_name: employees_example
              Rows_read: 7
           Rows_changed: 0
Rows_changed_x_#indexes: 0
*************************** 3. row ***************************
           Table_schema: mysql
             Table_name: user
              Rows_read: 16
           Rows_changed: 0
Rows_changed_x_#indexes: 0
*************************** 4. row ***************************
           Table_schema: mysql
             Table_name: db
              Rows_read: 2
           Rows_changed: 0
Rows_changed_x_#indexes: 0
```
