# MariaDB 10.1.21 Release Notes

The most recent release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.21)[Release Notes](mariadb-10121-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10121-changelog.md)[Overview of 10.1](changes-improvements-in-mariadb-10-1.md)

**Release date:** 18 Jan 2017

[MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is the current stable series of MariaDB. It is an evolution\
of [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.1.21](mariadb-10121-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **see the**[**What is MariaDB 10.1?**](changes-improvements-in-mariadb-10-1.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* [Innodb](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.35

A file format compatibility bug that was introduced in [MariaDB 10.1.0](mariadb-10-1-0-release-notes.md) was fixed in this version of MariaDB. Using [page\_compression](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-page-compression) or non-default [innodb\_page\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) created files that were incompatible with [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) or MySQL 5.6. [MariaDB 10.1.21](mariadb-10121-release-notes.md) and higher will convert affected files from earlier [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) releases to a compatible format.**This prevents a downgrade to earlier** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **versions.**[See the commit for details.](https://github.com/MariaDB/server/commit/ab1e6fefd869242d962cb91a006f37bb9ad534a7)

* [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/performance-schema) updated to 5.6.35
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2016-6664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-6664)
  * [CVE-2017-3238](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3238)
  * [CVE-2017-3243](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3243)
  * [CVE-2017-3244](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3244)
  * [CVE-2017-3257](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3257)
  * [CVE-2017-3258](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3258)
  * [CVE-2017-3265](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3265)
  * [CVE-2017-3291](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3291)
  * [CVE-2017-3312](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3312)
  * [CVE-2017-3317](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3317)
  * [CVE-2017-3318](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3318)

## Changelog

For a complete list of changes made in [MariaDB 10.1.21](mariadb-10121-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10121-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
