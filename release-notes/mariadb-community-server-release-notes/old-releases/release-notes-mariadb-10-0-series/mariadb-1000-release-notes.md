# MariaDB 10.0.0 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.0) |**Release Notes** |[Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-1000-changelog.md) |[Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 12 Nov 2012

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is the development version of MariaDB. It is built on the[MariaDB 5.5 series](broken-reference) with backported features from MySQL 5.6\
and entirely new features not found anywhere else.

[MariaDB 10.0.0](mariadb-1000-release-notes.md) is an [_**Alpha**_](../../../mariadb-release-criteria.md) release.\
This is the first 10.0-based release, and we are releasing it now to get it\
into the hands of any who might want to test it. Not all features planned for\
the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series are included in this release. Additional features will\
be pushed in future releases.**Do not use alpha releases on production systems.**

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

For a list of changes made in [MariaDB 10.0.0](mariadb-1000-release-notes.md), with links to detailed\
information on each push, see the[MariaDB 10.0.0 Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-1000-changelog.md).

## Based on [MariaDB 5.5](broken-reference)

The [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series builds off of the [MariaDB 5.5](broken-reference) series. It also includes features imported from MySQL 5.6, and completely new features.

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

## New Features in [MariaDB 10.0.0](mariadb-1000-release-notes.md) Alpha

### New Features

* Better error messages (all error numbers now include a descriptive text what the number means)
* [SHOW EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-explain) feature
* [Multi source replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/multi-source-replication) — Original code from [Taobao, developed by Peng Lixun](https://mysql.taobao.org/index.php/Patch_source_code#Multi-master_replication).

### New Features Backported from MySQL 5.6

* New InnoDB — from MySQL 5.6.5
* Performance schema — from MySQL 5.6.5 (without host cache)
* Optimized read only transaction (for InnoDB). This includes support for TRANSACTION READ ONLY.
* LIMIT ... ORDER BY optimization

### Security Fixes

* A fix is included for multiple SQL injection vulnerabilities in the replication code. See [MDEV-382](https://jira.mariadb.org/browse/MDEV-382) ([CVE-2012-4414](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-4414)) for details.

### Other Features

Other features are planned for inclusion in the Stable (GA) version of [MariaDB\
10.0](changes-improvements-in-mariadb-10-0.md). They are listed on the [What is MariaDB 10.0?](changes-improvements-in-mariadb-10-0.md) and[Plans for 10x](broken-reference) pages.

Thanks, and enjoy MariaDB!

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
