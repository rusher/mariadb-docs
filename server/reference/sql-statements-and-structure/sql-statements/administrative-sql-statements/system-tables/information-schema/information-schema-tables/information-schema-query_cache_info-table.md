
# Information Schema QUERY_CACHE_INFO Table

## Description


The table is not a standard Information Schema table, and is a MariaDB extension.


The `QUERY_CACHE_INFO` table is created by the [QUERY_CACHE_INFO](../../../../../../plugins/other-plugins/query-cache-information-plugin.md) plugin, and allows you to see the contents of the [query cache](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/query-cache.md). It creates a table in the [information_schema](../README.md) database that shows all queries that are in the cache. You must have the `PROCESS` privilege (see [GRANT](../../../../account-management-sql-commands/grant.md)) to use this table.


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| STATEMENT_SCHEMA | Database used when query was included |
| STATEMENT_TEXT | Query text |
| RESULT_BLOCKS_COUNT | Number of result blocks |
| RESULT_BLOCKS_SIZE | Size in bytes of result blocks |
| RESULT_BLOCKS_SIZE_USED | Size in bytes of used blocks |
| LIMIT | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| MAX_SORT_LENGTH | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| GROUP_CONCAT_MAX_LENGTH | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| CHARACTER_SET_CLIENT | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| CHARACTER_SET_RESULT | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| COLLATION | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| TIMEZONE | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| DEFAULT_WEEK_FORMAT | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| DIV_PRECISION_INCREMENT | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| SQL_MODE | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| LC_TIME_NAMES | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| CLIENT_LONG_FLAG | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| CLIENT_PROTOCOL_41 | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| PROTOCOL_TYPE | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| MORE_RESULTS_EXISTS | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| IN_TRANS | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| AUTOCOMMIT | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| PACKET_NUMBER | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes). |
| HITS | Incremented each time the query cache is hit. Added [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1032-release-notes). |



For example:



```
SELECT * FROM information_schema.QUERY_CACHE_INFO;
+------------------+-----------------+---------------------+--------------------+-------------------------+
| STATEMENT_SCHEMA | STATEMENT_TEXT  | RESULT_BLOCKS_COUNT | RESULT_BLOCKS_SIZE | RESULT_BLOCKS_SIZE_USED |
+------------------+-----------------+---------------------+--------------------+-------------------------+
...
| test             | SELECT * FROM a |                   1 |                512 |                     143 |
| test             | select * FROM a |                   1 |                512 |                     143 |
...
+------------------+-----------------+---------------------+--------------------+-------------------------
```



CC BY-SA / Gnu FDL

