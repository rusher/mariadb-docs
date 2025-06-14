# MariaDB 10.1.27 Release Notes

The most recent release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

A regression was discovered after the release of [MariaDB 10.1.27](mariadb-10127-release-notes.md). It has been pulled from the downloads system, but some mirrors may still have it. **Do not download or install this version.** Stay with [MariaDB 10.1.26](mariadb-10126-release-notes.md) until 10.1.28 is released.

[Download](https://downloads.mariadb.org/mariadb/10.1.27)[Release Notes](mariadb-10127-release-notes.md)[Changelog](../../../changelogs/changelogs-mariadb-101-series/mariadb-10127-changelog.md)[Overview of 10.1](changes-improvements-in-mariadb-10-1.md)

**Release date:** 25 Sep 2017

[MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is the previous stable series of MariaDB. It is an evolution\
of [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.1.27](mariadb-10127-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **see the**[**What is MariaDB 10.1?**](changes-improvements-in-mariadb-10-1.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.6.37-82.2
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/tokudb) updated to 5.6.37-82.2

### Encryption

* Temporary files created by merge sort and row log are encrypted if [innodb\_encrypt\_log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) is set to `1`, regardless of whether the table encrypted or not ([MDEV-12634](https://jira.mariadb.org/browse/MDEV-12634)).
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

A file format compatibility bug that was introduced in [MariaDB 10.1.0](mariadb-10-1-0-release-notes.md) was fixed in [MariaDB 10.1.21](mariadb-10121-release-notes.md).\
Using [page\_compression](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-page-compression) or non-default [innodb\_page\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) created files that were incompatible with [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) or MySQL 5.6. [MariaDB 10.1.21](mariadb-10121-release-notes.md) and higher will convert affected files from earlier [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) releases to a compatible format.**This prevents a downgrade to earlier** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **versions.**[See the commit for details.](https://github.com/MariaDB/server/commit/ab1e6fefd869242d962cb91a006f37bb9ad534a7)

## Changelog

For a complete list of changes made in [MariaDB 10.1.27](mariadb-10127-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../../changelogs/changelogs-mariadb-101-series/mariadb-10127-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
