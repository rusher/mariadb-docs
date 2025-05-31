# Information Schema QUERY\_CACHE\_INFO Table

## Description

The table is not a standard Information Schema table, and is a MariaDB extension.

The `QUERY_CACHE_INFO` table is created by the [QUERY\_CACHE\_INFO](../../../../../plugins/other-plugins/query-cache-information-plugin.md) plugin, and allows you to see the contents of the [query cache](../../../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md). It creates a table in the [information\_schema](../) database that shows all queries that are in the cache. You must have the `PROCESS` privilege (see [GRANT](../../../../account-management-sql-statements/grant.md)) to use this table.

It contains the following columns:

| Column                     | Description                                                                                                                                                                                                      |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Column                     | Description                                                                                                                                                                                                      |
| STATEMENT\_SCHEMA          | Database used when query was included                                                                                                                                                                            |
| STATEMENT\_TEXT            | Query text                                                                                                                                                                                                       |
| RESULT\_BLOCKS\_COUNT      | Number of result blocks                                                                                                                                                                                          |
| RESULT\_BLOCKS\_SIZE       | Size in bytes of result blocks                                                                                                                                                                                   |
| RESULT\_BLOCKS\_SIZE\_USED | Size in bytes of used blocks                                                                                                                                                                                     |
| LIMIT                      | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| MAX\_SORT\_LENGTH          | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| GROUP\_CONCAT\_MAX\_LENGTH | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| CHARACTER\_SET\_CLIENT     | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| CHARACTER\_SET\_RESULT     | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| COLLATION                  | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| TIMEZONE                   | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| DEFAULT\_WEEK\_FORMAT      | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| DIV\_PRECISION\_INCREMENT  | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| SQL\_MODE                  | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| LC\_TIME\_NAMES            | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| CLIENT\_LONG\_FLAG         | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| CLIENT\_PROTOCOL\_41       | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| PROTOCOL\_TYPE             | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| MORE\_RESULTS\_EXISTS      | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| IN\_TRANS                  | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| AUTOCOMMIT                 | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| PACKET\_NUMBER             | Added [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes).                                             |
| HITS                       | Incremented each time the query cache is hit. Added [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1032-release-notes). |

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
