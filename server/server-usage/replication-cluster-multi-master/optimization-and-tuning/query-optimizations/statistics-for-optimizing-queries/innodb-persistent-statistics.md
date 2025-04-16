
# InnoDB Persistent Statistics

InnoDB statistics are stored on disk and are therefore persistent. Prior to [MariaDB 10.0](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md), InnoDB statistics were not stored on disk, meaning that on server restarts the statistics would need to be recalculated, which is both needless computation, as well as leading to inconsistent query plans.


There are a number of variables that control persistent statistics:


* [innodb_stats_persistent](../../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_stats_persistent) - when set (the default) enables InnoDB persistent statistics.
* [innodb_stats_auto_recalc](../../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_stats_auto_recalc) - when set (the default), persistent statistics are automatically recalculated when the table changes significantly (more than 10% of the rows)
* [innodb_stats_persistent_sample_pages](../../../../../ref/storage-engines/innodb/innodb-system-variables.md#innodb_stats_persistent_sample_pages) - Number of index pages sampled (default 20) when estimating cardinality and statistics for indexed columns. Increasing this value will increases index statistics accuracy, but use more I/O resources when running [ANALYZE TABLE](../../../../../ref/sql-statements-and-structure/sql-statements/table-statements/analyze-table.md).


These settings can be overwritten on a per-table basis by use of the [STATS_PERSISTENT](../../../../../ref/sql-statements-and-structure/vectors/create-table-with-vectors.md#stats_persistent), [STATS_AUTO_RECALC](../../../../../ref/sql-statements-and-structure/vectors/create-table-with-vectors.md#stats_auto_recalc) and [STATS_SAMPLE_PAGES](../../../../../ref/sql-statements-and-structure/vectors/create-table-with-vectors.md#stats_sample_pages) clauses in a [CREATE TABLE](../../../../../ref/sql-statements-and-structure/vectors/create-table-with-vectors.md) or [ALTER TABLE](../../../../../ref/sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md) statement.


Details of the statistics are stored in two system tables in the [mysql database](../../../../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md):


* [innodb_table_stats](../../../../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-innodb_table_stats.md)
* [innodb_index_stats](../../../../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-innodb_index_stats.md)


The [ANALYZE TABLE](../../../../../ref/sql-statements-and-structure/sql-statements/table-statements/analyze-table.md) statement can be used to recalculate InnoDB statistics.


The [RENAME TABLE](../../../../../ref/sql-statements-and-structure/sql-statements/data-definition/rename-table.md) statement triggers a reload of the statistics.






##### MariaDB starting with [10.11.12](https://mariadb.com/kb/en/mariadb-101112-release-notes/)
Prior to [MariaDB 10.11.12](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-12-release-notes.md), [MariaDB 11.4.6](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-6-release-notes.md) and [MariaDB 11.8.2](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-8-series/mariadb-11-8-2-release-notes.md), [FLUSH TABLES](../../../../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) also caused InnoDB statistics to be reloaded. From [MariaDB 10.11.12](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-12-release-notes.md), [MariaDB 11.4.6](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-6-release-notes.md) and [MariaDB 11.8.2](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-8-series/mariadb-11-8-2-release-notes.md), this is no longer the case. 


## See Also


* [Index Statistics](../../optimization-and-indexes/index-statistics.md)
* [Engine-independent Statistics](engine-independent-table-statistics.md)
* [Histogram-based Statistics](histogram-based-statistics.md)

