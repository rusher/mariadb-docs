# InnoDB Persistent Statistics

InnoDB statistics are stored on disk and are therefore persistent. Prior to [MariaDB 10.0](/kb/en/what-is-mariadb-100/), InnoDB statistics were not stored on disk, meaning that on server restarts the statistics would need to be recalculated, which is both needless computation, as well as leading to inconsistent query plans.

There are a number of variables that control persistent statistics:

* [innodb_stats_persistent](../../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_persistent) - when set (the default) enables InnoDB persistent statistics.
* [innodb_stats_auto_recalc](../../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_auto_recalc) - when set (the default), persistent statistics are automatically recalculated when the table changes significantly (more than 10% of the rows)
* [innodb_stats_persistent_sample_pages](../../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_persistent_sample_pages) - Number of index pages sampled (default 20) when estimating cardinality and statistics for indexed columns. Increasing this value will increases index statistics accuracy, but use more I/O resources when running [ANALYZE TABLE](../../../../../reference/sql-statements-and-structure/sql-statements/table-statements/analyze-table.md).

These settings can be overwritten on a per-table basis by use of the [STATS_PERSISTENT](../../../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#stats_persistent), [STATS_AUTO_RECALC](../../../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#stats_auto_recalc) and [STATS_SAMPLE_PAGES](../../../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#stats_sample_pages) clauses in a [CREATE TABLE](../../../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md) or [ALTER TABLE](../../../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md) statement.

Details of the statistics are stored in two system tables in the [mysql database](the-mysql-database-table):

* [innodb_table_stats](/kb/en/mysqlinnodb_table_stats/)
* [innodb_index_stats](/kb/en/mysqlinnodb_index_stats/)

The [ANALYZE TABLE](../../../../../reference/sql-statements-and-structure/sql-statements/table-statements/analyze-table.md) statement can be used to reload InnoDB statistics. [RENAME TABLE](../../../../../reference/sql-statements-and-structure/sql-statements/data-definition/rename-table.md) has the same effect, triggering a reload of the statistics.

#

#### MariaDB starting with [10.11.12](/kb/en/mariadb-101112-release-notes/)

Prior to [MariaDB 10.11.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-1011-series/mariadb-10-11-12-release-notes), [MariaDB 11.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-6-release-notes) and [MariaDB 11.8.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-11-8-series/mariadb-11-8-2-release-notes), [FLUSH TABLES](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) also caused InnoDB statistics to be reloaded or recalculated. From [MariaDB 10.11.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-1011-series/mariadb-10-11-12-release-notes), [MariaDB 11.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-6-release-notes) and [MariaDB 11.8.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-11-8-series/mariadb-11-8-2-release-notes), this is no longer the case.

#

# See Also

* [Index Statistics](../../optimization-and-indexes/index-statistics.md)
* [Engine-independent Statistics](engine-independent-table-statistics.md)
* [Histogram-based Statistics](histogram-based-statistics.md)