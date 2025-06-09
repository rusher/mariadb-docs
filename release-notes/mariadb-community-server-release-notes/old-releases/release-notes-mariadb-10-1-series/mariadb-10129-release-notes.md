# MariaDB 10.1.29 Release Notes

The most recent release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.29)[Release Notes](mariadb-10129-release-notes.md)[Changelog](../../../changelogs/changelogs-mariadb-101-series/mariadb-10129-changelog.md)[Overview of 10.1](changes-improvements-in-mariadb-10-1.md)

**Release date:** 14 Nov 2017

[MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is the previous stable series of MariaDB. It is an evolution\
of [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.1.29](mariadb-10129-release-notes.md) will be a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **see the**[**What is MariaDB 10.1?**](changes-improvements-in-mariadb-10-1.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

### Mariabackup

* [MDEV-14333](https://jira.mariadb.org/browse/MDEV-14333) Mariabackup --apply-log-only crashes if incomplete transactions with update\_undo logs are present
* [MDEV-12108](https://jira.mariadb.org/browse/MDEV-12108) Fix backup for Innodb tables with DATA DIRECTORY
* [MDEV-13560](https://jira.mariadb.org/browse/MDEV-13560) mariabackup --copy-back: Copy all undo tablespace files
* [MDEV-14102](https://jira.mariadb.org/browse/MDEV-14102) Restore --remove-original option for mariabackup
* [MDEV-13822](https://jira.mariadb.org/browse/MDEV-13822) mariabackup --incremental --prepare incorrectly sets file size

### InnoDB/XtraDB

* [MDEV-13328](https://jira.mariadb.org/browse/MDEV-13328) ALTER TABLE…DISCARD TABLESPACE takes a lot of time
* [MDEV-14219](https://jira.mariadb.org/browse/MDEV-14219) Allow online table rebuild when encryption or compression parameters change
* [MDEV-14051](https://jira.mariadb.org/browse/MDEV-14051) 'Undo log record is too big.' error occurring in very narrow range of string lengths
* [MDEV-14076](https://jira.mariadb.org/browse/MDEV-14076) InnoDB: Failing assertion when accessing [INFORMATION\_SCHEMA.INNODB\_SYS\_TABLESPACES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tablespaces-table) upon upgrade from 10.1.0 to 10.1.20
* [MDEV-12676](https://jira.mariadb.org/browse/MDEV-12676) MySQL#78423 InnoDB FTS duplicate key error
* [MDEV-13051](https://jira.mariadb.org/browse/MDEV-13051) MySQL#86607 InnoDB crash after failed ADD INDEX and table\_definition\_cache eviction
* [MDEV-13838](https://jira.mariadb.org/browse/MDEV-13838): Wrong result after altering a partitioned table

### General

* [Mroonga](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/mroonga) updated to 7.07.

### Security Fixes

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2017-10378](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10378), [MDEV-13819](https://jira.mariadb.org/browse/MDEV-13819)
  * [CVE-2017-10268](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-10268)

## Notes

For a complete list of changes made in [MariaDB 10.1.29](mariadb-10129-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../../changelogs/changelogs-mariadb-101-series/mariadb-10129-changelog.md).

A file format compatibility bug that was introduced in [MariaDB 10.1.0](mariadb-10-1-0-release-notes.md) was fixed in [MariaDB 10.1.21](mariadb-10121-release-notes.md).\
Using [page\_compression](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-page-compression) or non-default [innodb\_page\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) created files that were incompatible with [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) or MySQL 5.6. [MariaDB 10.1.21](mariadb-10121-release-notes.md) and higher will convert affected files from earlier [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) releases to a compatible format.**This prevents a downgrade to earlier** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **versions.**[See the commit for details.](https://github.com/MariaDB/server/commit/ab1e6fefd869242d962cb91a006f37bb9ad534a7)

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
