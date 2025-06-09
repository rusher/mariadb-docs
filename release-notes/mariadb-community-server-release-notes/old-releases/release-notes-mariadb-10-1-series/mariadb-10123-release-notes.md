# MariaDB 10.1.23 Release Notes

[Download](https://downloads.mariadb.org/mariadb/10.1.23)[Release Notes](mariadb-10123-release-notes.md)[Changelog](../../../changelogs/changelogs-mariadb-101-series/mariadb-10123-changelog.md)[Overview of 10.1](changes-improvements-in-mariadb-10-1.md)

**Release date:** 3 May 2017

[MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is the current stable series of MariaDB. It is an evolution\
of [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.1.23](mariadb-10123-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **see the**[**What is MariaDB 10.1?**](changes-improvements-in-mariadb-10-1.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

Updating from [MariaDB 10.1.21](mariadb-10121-release-notes.md) to [MariaDB 10.1.22](mariadb-10122-release-notes.md) or higher is **highly recommended** due to two high-priority regression fixes. See [MDEV-11842](https://jira.mariadb.org/browse/MDEV-11842) and [MDEV-12075](https://jira.mariadb.org/browse/MDEV-12075) for details.

* [MDEV-12602](https://jira.mariadb.org/browse/MDEV-12602): Fixed some race conditions in InnoDB encryption
* [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backing-up-and-restoring-databases/mariabackup) alpha introduced, see [this blog post](https://mariadb.com/resources/blog/mariadb-backup-released-mariadb-server-10123) for more information
* [Galera wsrep library](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md) updated to 25.3.20
* Packages for Ubuntu 17.04 "zesty" [added](https://downloads.mariadb.org/mariadb/repositories/)
* As per the [MariaDB Deprecation Policy](../../../mariadb-platform-deprecation-policy.md), this will be the last release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) for Ubuntu 12.04 LTS "Precise" and Mint 13 LTS "Maya"
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2017-3308](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3308)
  * [CVE-2017-3309](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3309)
  * [CVE-2017-3453](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3453)
  * [CVE-2017-3456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3456)
  * [CVE-2017-3464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3464)

A file format compatibility bug that was introduced in [MariaDB 10.1.0](mariadb-10-1-0-release-notes.md) was fixed in [MariaDB 10.1.21](mariadb-10121-release-notes.md).\
Using [page\_compression](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-page-compression) or non-default [innodb\_page\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) created files that were incompatible with [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) or MySQL 5.6. [MariaDB 10.1.21](mariadb-10121-release-notes.md) and higher will convert affected files from earlier [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) releases to a compatible format.**This prevents a downgrade to earlier** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **versions.**[See the commit for details.](https://github.com/MariaDB/server/commit/ab1e6fefd869242d962cb91a006f37bb9ad534a7)

## Changelog

For a complete list of changes made in [MariaDB 10.1.23](mariadb-10123-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../../changelogs/changelogs-mariadb-101-series/mariadb-10123-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
