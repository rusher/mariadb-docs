# MariaDB 10.5.1 Release Notes

The most recent release of [MariaDB 10.5](what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](mariadb-10-5-28-release-notes.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download](https://downloads.mariadb.org/mariadb/10.5.1)[Release Notes](mariadb-1051-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-1051-changelog.md)[Overview of 10.5](what-is-mariadb-105.md)

**Release date:** 14 Feb 2020

[MariaDB 10.5](what-is-mariadb-105.md) is the current _development_ series of MariaDB. It is an evolution\
of [MariaDB 10.4](broken-reference) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL.

[MariaDB 10.5.1](mariadb-1051-release-notes.md) is a [_**Beta**_](../../mariadb-release-criteria.md) release.

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

**For an overview of** [**MariaDB 10.5**](what-is-mariadb-105.md) **see the**[**What is MariaDB 10.5?**](what-is-mariadb-105.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

This will be the first beta release in the [MariaDB 10.5](what-is-mariadb-105.md) series.

Notable changes of this release include:

### InnoDB

* Remove dummy tablespace for the [redo log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-redo-log) ([MDEV-18115](https://jira.mariadb.org/browse/MDEV-18115))
* Optimize access to InnoDB page header fields ([MDEV-21133](https://jira.mariadb.org/browse/MDEV-21133))
* Remove multiple [InnoDB buffer pool](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-buffer-pool) instances ([MDEV-15058](https://jira.mariadb.org/browse/MDEV-15058))
  * Deprecate and ignore [innodb\_buffer\_pool\_instances](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_instances) and [innodb\_page\_cleaners](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_page_cleaners)
  * Columns that indicated the buffer pool instance from the Information Schema [innodb\_buffer\_page](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_buffer_page-table), [innodb\_buffer\_page\_lru](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_buffer_page_lru-table), [innodb\_buffer\_pool\_stats](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_buffer_pool_stats-table), [innodb\_cmpmem](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_cmpmem-and-innodb_cmpmem_reset-tables) and [innodb\_cmpmem\_reset](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_cmpmem-and-innodb_cmpmem_reset-tables) tables now return a dummy value of `0`.
* Deprecate and ignore [innodb\_log\_optimize\_ddl](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_optimize_ddl) ([MDEV-19747](https://jira.mariadb.org/browse/MDEV-19747))
* Prefer MDL to dict\_sys.latch for innodb background tasks ([MDEV-16678](https://jira.mariadb.org/browse/MDEV-16678))
* Use fdatasync() for redo log where appropriate ([MDEV-21382](https://jira.mariadb.org/browse/MDEV-21382))
* Replace recv\_sys.heap with list of buf\_block\_t ([MDEV-21351](https://jira.mariadb.org/browse/MDEV-21351))
* Several fixes to server hangs ([MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264))

### Optimizer

* Allow packed values of non-sorted fields in the sort buffer ([MDEV-21263](https://jira.mariadb.org/browse/MDEV-21263))

### Replication and Galera

* [slave\_parallel\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#slave_parallel_mode) now defaults to `optimistic` ([MDEV-18648](https://jira.mariadb.org/browse/MDEV-18648)).
* Make REPLICA a synonym for [SLAVE in SQL statements](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements) ([MDEV-20601](https://jira.mariadb.org/browse/MDEV-20601))
* [Galera](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/) [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) support ([commit](https://github.com/MariaDB/server/commit/41bc736871))
* Add new mode to wsrep\_OSU\_method in which Galera checks storage engine of the effected table ([MDEV-20051](https://jira.mariadb.org/browse/MDEV-20051))
* Galera: Replicate MariaDB GTID to other nodes in the cluster ([MDEV-20720](https://jira.mariadb.org/browse/MDEV-20720))

### PCRE

* Migrate to [PCRE2](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/pcre) ([MDEV-14024](https://jira.mariadb.org/browse/MDEV-14024))

### Compatibility

* Show internal type for TIMESTAMP, DATETIME, and TIME columns ([MDEV-19906](https://jira.mariadb.org/browse/MDEV-19906))

### Variables

* Numerous deprecated variables removed ([MDEV-18650](https://jira.mariadb.org/browse/MDEV-18650))
  * [multi\_range\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#multi_range_count)
  * [thread\_concurrency](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#thread_concurrency)
  * [timed\_mutexes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#timed_mutexes)

## Changelog

For a complete list of changes made in [MariaDB 10.5.1](mariadb-1051-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-1051-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.5.1](mariadb-1051-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-5-1-now-available/).

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
