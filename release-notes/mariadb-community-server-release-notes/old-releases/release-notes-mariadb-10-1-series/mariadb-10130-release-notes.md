# MariaDB 10.1.30 Release Notes

The most recent release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.30)[Release Notes](mariadb-10130-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10130-changelog.md)[Overview of 10.1](changes-improvements-in-mariadb-10-1.md)

**Release date:** 22 Dec 2017

[MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is the previous stable series of MariaDB. It is an evolution\
of [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.1.30](mariadb-10130-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **see the**[**What is MariaDB 10.1?**](changes-improvements-in-mariadb-10-1.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* [MDEV-12323](https://jira.mariadb.org/browse/MDEV-12323) - Rollback progress log messages during crash recovery are intermixed with unrelated log messages
* [MDEV-14701](https://jira.mariadb.org/browse/MDEV-14701) - install\_db shows corruption
* [MDEV-13407](https://jira.mariadb.org/browse/MDEV-13407) - innodb.drop\_table\_background failed
* [MDEV-14008](https://jira.mariadb.org/browse/MDEV-14008) - Assertion failing: \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())
* [MDEV-12323](https://jira.mariadb.org/browse/MDEV-12323) - Rollback progress log messages during crash recovery are intermixed with unrelated log messages
* [MDEV-12352](https://jira.mariadb.org/browse/MDEV-12352) - InnoDB shutdown should not be blocked by a large transaction rollback
* [MDEV-13797](https://jira.mariadb.org/browse/MDEV-13797) - InnoDB may hang if shutdown is initiated soon after startup while rolling back recovered incomplete transactions
* [MDEV-12837](https://jira.mariadb.org/browse/MDEV-12837) - WSREP: BF lock wait long
* [MDEV-14587](https://jira.mariadb.org/browse/MDEV-14587) - dict\_stats\_process\_entry\_from\_defrag\_pool() fails to call dict\_table\_close() when index==NULL
* As per the [MariaDB Deprecation Policy](../../../mariadb-platform-deprecation-policy.md), this will be the last release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) for Ubuntu 17.04 "zesty"

### Security Fixes

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2017-15365](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-15365)
  * [CVE-2018-3133](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3133)

## Notes

For a complete list of changes made in [MariaDB 10.1.30](mariadb-10130-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-101-series/mariadb-10130-changelog.md).

A file format compatibility bug that was introduced in [MariaDB 10.1.0](mariadb-10-1-0-release-notes.md) was fixed in [MariaDB 10.1.21](mariadb-10121-release-notes.md).\
Using [page\_compression](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-page-compression) or non-default [innodb\_page\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) created files that were incompatible with [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) or MySQL 5.6. [MariaDB 10.1.21](mariadb-10121-release-notes.md) and higher will convert affected files from earlier [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) releases to a compatible format.**This prevents a downgrade to earlier** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **versions.**[See the commit for details.](https://github.com/MariaDB/server/commit/ab1e6fefd869242d962cb91a006f37bb9ad534a7)

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
