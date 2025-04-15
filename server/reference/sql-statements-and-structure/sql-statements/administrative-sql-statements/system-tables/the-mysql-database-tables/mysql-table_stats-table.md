# mysql.table_stats Table

The `mysql.table_stats` table is one of three tables storing data used for [Engine-independent table statistics](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md). The others are [mysql.column_stats](/en/mysqlcolumn_stats-table/) and [mysql.index_stats](/en/mysqlindex_stats-table/).

It is populated when the [ANALYZE TABLE](../../../table-statements/analyze-table.md) statement is run, although not by default. See [Collecting Statistics with the ANALYZE TABLE Statement](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md#collecting-statistics-with-the-analyze-table-statement) for details.

It is possible to manually update the table and, unlike most system tables, there are some scenarios where this could be useful. See [Manual updates to statistics tables](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md#manual-updates-to-statistics-tables) for details.

This table uses the [Aria](../../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/aria-encryption/aria-enabling-encryption.md) storage engine.

The `mysql.table_stats` table contains the following fields:

| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| db_name | varchar(64) | NO | PRI | NULL | Database the table is in . |
| table_name | varchar(64) | NO | PRI | NULL | Table name. |
| cardinality | bigint(21) unsigned | YES | | NULL | Number of records in the table. |