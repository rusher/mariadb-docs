# MariaDB 10.0.10 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.10) |**Release Notes** |[Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10010-changelog.md) |[Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 31 Mar 2014

With this release, [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is now the current stable version of MariaDB.\
It is an evolution of the [MariaDB 5.5 series](broken-reference) with\
several entirely new features not found anywhere else and with backported and\
reimplemented features from MySQL 5.6.

[MariaDB 10.0.10](mariadb-10010-release-notes.md) is a [_**Stable**_](../../../mariadb-release-criteria.md) (_GA_) release. This\
is the eleventh 10.0-based release, and the first stable release. All features\
planned for inclusion in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series are included in this release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

[MariaDB 10.0.10](mariadb-10010-release-notes.md) is primarily a bug-fix and polishing release.

Notable changes of this release include:

* The Audit Plugin is now included in MariaDB ([MDEV-5584](https://jira.mariadb.org/browse/MDEV-5584))
* Improved [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) performance by fixing incorrect calculation of flushed pages ([MDEV-5949](https://jira.mariadb.org/browse/MDEV-5949))
* Fix for [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) duplicate key multi-master corruption bug ([MDEV-5804](https://jira.mariadb.org/browse/MDEV-5804))
* Default [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/tokudb) compression is now `TOKUDB_ZLIB` (instead of `TOKUDB_UNCOMPRESSED`)
* Various algorithm improvements for[engine-independent table statistics](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics)\
  (EITS) ([MDEV-5901](https://jira.mariadb.org/browse/MDEV-5901), [MDEV-5917](https://jira.mariadb.org/browse/MDEV-5917), [MDEV-5950](https://jira.mariadb.org/browse/MDEV-5950), [MDEV-5962](https://jira.mariadb.org/browse/MDEV-5962), [MDEV-5926](https://jira.mariadb.org/browse/MDEV-5926))

For a complete list of changes made in [MariaDB 10.0.10](mariadb-10010-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10010-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
