# MariaDB 10.5.4 Release Notes

The most recent release of [MariaDB 10.5](what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](mariadb-10-5-28-release-notes.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download](https://downloads.mariadb.org/mariadb/10.5.4/)[Release Notes](mariadb-1054-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-1054-changelog.md)[Overview of 10.5](what-is-mariadb-105.md)

**Release date:** 24 Jun 2020

[MariaDB 10.5](what-is-mariadb-105.md) is the current _stable_ series of MariaDB. It is an evolution\
of [MariaDB 10.4](broken-reference) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL.

[MariaDB 10.5.4](mariadb-1054-release-notes.md) is a [_**Stable (GA)**_](../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.5**](what-is-mariadb-105.md) **see the**[**What is MariaDB 10.5?**](what-is-mariadb-105.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

This is the first Stable (GA) release in the [MariaDB 10.5](what-is-mariadb-105.md) series.

* This release of MariaDB Server includes the [S3 storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine). Note, that plugins have [independent maturity levels](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/plugins-table-information-schema) and S3 storage engine in 10.5.4 has Alpha maturity.
* This release of MariaDB Server includes the [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) storage engine. Note, that plugins have [independent maturity levels](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/plugins-table-information-schema) and MariaDB ColumnStore in 10.5.4 has Beta maturity.
* New [Gamma](../../mariadb-release-criteria.md) version of the [Spider Storage Engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider), 3.3.15.
* [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table) now reliably deletes table remnants inside a storage engine even if the .frm file is missing ([MDEV-11412](https://jira.mariadb.org/browse/MDEV-11412))
* Accelerated `crc32()` function for AMD64, ARMv8, POWER 8 ([MDEV-22669](https://jira.mariadb.org/browse/MDEV-22669))
* Lots of bug fixes, see the [changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-1054-changelog.md).
* [Galera wsrep library](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md) updated to 26.4.5

### Variables

* Limit [innodb\_encryption\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_encryption_threads) to 255 ([MDEV-22258](https://jira.mariadb.org/browse/MDEV-22258)).
* Minimum value of [max\_sort\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#max_sort_length) raised to 8 (previously 4)\
  so fixed size [data types](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types) like [DOUBLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/double) and [BIGINT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/bigint) are not truncated for lower values of max\_sort\_length ([MDEV-22715](https://jira.mariadb.org/browse/MDEV-22715)).

### InnoDB

* [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table) improvements: [MDEV-8069](https://jira.mariadb.org/browse/MDEV-8069), [MDEV-11412](https://jira.mariadb.org/browse/MDEV-11412), [MDEV-22456](https://jira.mariadb.org/browse/MDEV-22456)
* InnoDB Performance improvements: [MDEV-15053](https://jira.mariadb.org/browse/MDEV-15053), [MDEV-22593](https://jira.mariadb.org/browse/MDEV-22593), [MDEV-22697](https://jira.mariadb.org/browse/MDEV-22697), [MDEV-22871](https://jira.mariadb.org/browse/MDEV-22871), [MDEV-22841](https://jira.mariadb.org/browse/MDEV-22841)

## Changelog

For a complete list of changes made in [MariaDB 10.5.4](mariadb-1054-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-1054-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.5.4](mariadb-1054-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-5-4-now-available/).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
