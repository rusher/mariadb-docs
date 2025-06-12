# MariaDB 5.3.8 Release Notes

The most recent release in the [MariaDB 5.3 series](broken-reference/) is:[**MariaDB 5.3.12**](mariadb-5312-release-notes.md)

[Download](https://downloads.mariadb.org/mariadb/5.3.8) |**Release Notes** |[Changelog](broken-reference/) |[Overview of 5.3](broken-reference/)

**Release date:** 28 Aug 2012

[MariaDB 5.3.8](mariadb-538-release-notes.md) is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release. In\
general this means that there are no known serious bugs, except for those\
marked as feature requests, that no bugs were fixed since last release that\
caused notable code changes, and that we believe the code is ready for\
general usage (based on bug inflow).

**For a description of** [**MariaDB 5.3**](broken-reference/) **see the**[**What is MariaDB 5.3**](broken-reference/) **page.**

For a list of changes made in [MariaDB 5.3.8](mariadb-538-release-notes.md), with links to detailed\
information on each push, see the[MariaDB 5.3.8 Changelog](broken-reference/).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

## Includes [MariaDB 5.2](../release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md) and MySQL 5.1.65

This version of MariaDB includes the latest changes to [MariaDB 5.2](../release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md), and, by\
extension, [MariaDB 5.1](../release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md), including MySQL 5.1.65. See[Changes in MySQL 5.1.65](https://dev.mysql.com/doc/refman/5.1/en/news-5-1-65.html)\
for what changed between this and previous MySQL versions.

## Bug fixes and other improvements

This release fixes numerous cases of the incorrect identifier quoting in the replication code. They were open [SQL injection](https://en.wikipedia.org/wiki/SQL_injection) vulnerabilities, that allowed, to a certain extent, to bypass the database privilege system and modify the data, that one was granted no access to. See [MDEV-382](https://jira.mariadb.org/browse/MDEV-382) ([CVE-2012-4414](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-4414)) for details.

This MariaDB release includes several other bug fixes and improvements. It is recommended for all users of [MariaDB 5.3](changes-improvements-in-mariadb-5-3.md).

See the [MariaDB 5.3.8 Changelog](broken-reference/) for a list of every change\
made in [MariaDB 5.3.8](mariadb-538-release-notes.md), with links to detailed information on each push.

## Alternative Linux binaries

In this version of MariaDB we are starting to provide alternative Linux binaries built on a different build machine. Binaries created on this box require at least GLIBC\_2.14. For continuity, we are still providing binaries built with the same toolchain as previous releases. The alternative binaries have a "(GLIBC\_2.14)" label to distinguish them from the others.

Be notified of new releases automatically by adding the[releases rss feed](https://montyprogram.com/news/feed/mariadb_releases/) to\
your favorite feed reader or by [subscribing](https://mariadb.org) to the\
announce 'at' mariadb.org announcement list (this is a low traffic,\
announce-only list).

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
