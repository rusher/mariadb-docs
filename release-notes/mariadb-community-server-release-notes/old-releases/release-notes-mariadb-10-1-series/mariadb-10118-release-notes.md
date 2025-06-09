# MariaDB 10.1.18 Release Notes

The most recent release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.18)[Release Notes](mariadb-10118-release-notes.md)[Changelog](../../../changelogs/changelogs-mariadb-101-series/mariadb-10118-changelog.md)[Overview of 10.1](changes-improvements-in-mariadb-10-1.md)

**Release date:** 30 Sep 2016

[MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is the current stable series of MariaDB. It is an evolution\
of [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.1.18](mariadb-10118-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **see the**[**What is MariaDB 10.1?**](changes-improvements-in-mariadb-10-1.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.32-78.1
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/tokudb) updated to 5.6.32-78.1
* [Innodb](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.33
* [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/performance-schema) updated to 5.6.33
* Optimizer sometimes use "index" instead of "range" access for UPDATE ([MDEV-10649](https://jira.mariadb.org/browse/MDEV-10649))
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2016-5616](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-5616)
  * [CVE-2016-5624](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-5624)
  * [CVE-2016-5626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-5626)
  * [CVE-2016-3492](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-3492)
  * [CVE-2016-5629](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-5629)
  * [CVE-2016-8283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-8283)
  * [CVE-2016-6663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-6663) This vulnerability was discovered by [Dawid Golunski](https://legalhackers.com).

## Changelog

For a complete list of changes made in [MariaDB 10.1.18](mariadb-10118-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../../changelogs/changelogs-mariadb-101-series/mariadb-10118-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
