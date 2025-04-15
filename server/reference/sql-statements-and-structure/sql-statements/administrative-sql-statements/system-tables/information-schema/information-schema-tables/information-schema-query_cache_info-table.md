
# Information Schema QUERY_CACHE_INFO Table

## Description


The table is not a standard Information Schema table, and is a MariaDB extension.


The `<code>QUERY_CACHE_INFO</code>` table is created by the [QUERY_CACHE_INFO](../../../../../../plugins/other-plugins/query-cache-information-plugin.md) plugin, and allows you to see the contents of the [query cache](../../../../../../plugins/other-plugins/query-cache-information-plugin.md). It creates a table in the [information_schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) database that shows all queries that are in the cache. You must have the `<code>PROCESS</code>` privilege (see [GRANT](../../../../account-management-sql-commands/grant.md)) to use this table.


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| STATEMENT_SCHEMA | Database used when query was included |
| STATEMENT_TEXT | Query text |
| RESULT_BLOCKS_COUNT | Number of result blocks |
| RESULT_BLOCKS_SIZE | Size in bytes of result blocks |
| RESULT_BLOCKS_SIZE_USED | Size in bytes of used blocks |
| LIMIT | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| MAX_SORT_LENGTH | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| GROUP_CONCAT_MAX_LENGTH | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| CHARACTER_SET_CLIENT | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| CHARACTER_SET_RESULT | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| COLLATION | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| TIMEZONE | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| DEFAULT_WEEK_FORMAT | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| DIV_PRECISION_INCREMENT | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| SQL_MODE | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| LC_TIME_NAMES | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| CLIENT_LONG_FLAG | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| CLIENT_PROTOCOL_41 | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| PROTOCOL_TYPE | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| MORE_RESULTS_EXISTS | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| IN_TRANS | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| AUTOCOMMIT | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| PACKET_NUMBER | Added [MariaDB 10.1.8](../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md). |
| HITS | Incremented each time the query cache is hit. Added [MariaDB 10.3.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1032-release-notes.md). |



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

