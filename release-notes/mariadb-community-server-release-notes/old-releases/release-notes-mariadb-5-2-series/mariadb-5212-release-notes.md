# MariaDB 5.2.12 Release Notes

The most recent release in the [MariaDB 5.2 series](changes-improvements-in-mariadb-5-2.md) is:[**MariaDB 5.2.14**](mariadb-5214-release-notes.md)

[Download](https://downloads.askmonty.org/mariadb/5.2.12) |**Release Notes** |[Changelog](../../../changelogs/changelogs-mariadb-52-series/mariadb-5212-changelog.md) |[Overview of 5.2](changes-improvements-in-mariadb-5-2.md)

**Release date:** 6 Apr 2012

[MariaDB 5.2.12](mariadb-5212-release-notes.md) is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release. In\
general this means that there are no known serious bugs, except for those\
marked as feature requests, that no bugs were fixed since last release that\
caused notable code changes, and that we believe the code is ready for\
general usage (based on bug inflow).

**For a description of** [**MariaDB 5.2**](changes-improvements-in-mariadb-5-2.md) **see the**[**What is MariaDB 5.2**](changes-improvements-in-mariadb-5-2.md) **page.**

For a list of changes made in [MariaDB 5.2.12](mariadb-5212-release-notes.md), with links to detailed\
information on each push, see the[MariaDB 5.2.12 Changelog](../../../changelogs/changelogs-mariadb-52-series/mariadb-5212-changelog.md).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

## Important Security Fix for Rare Password Bug

[MariaDB 5.2.12](mariadb-5212-release-notes.md) fixes a bug that under certain rare circumstances allowed a user\
to connect with an invalid password. **This is a serious security issue.** We\
recommend upgrading from older versions as soon as possible.

## Includes [MariaDB 5.1.62](../release-notes-mariadb-5-1-series/mariadb-5162-release-notes.md) and MySQL 5.1.62

This version of MariaDB includes [MariaDB 5.1.62](../release-notes-mariadb-5-1-series/mariadb-5162-release-notes.md), and by extension, MySQL\
5.1.62. See the [MariaDB 5.1.62 Release Notes](../release-notes-mariadb-5-1-series/mariadb-5162-release-notes.md) for\
the changes made in [MariaDB 5.1.62](../release-notes-mariadb-5-1-series/mariadb-5162-release-notes.md) and see[Changes in MySQL 5.1.62](https://dev.mysql.com/doc/refman/5.1/en/news-5-1-62.html)\
for what changed between this and previous MySQL versions.

Be notified of new releases automatically by adding the[releases rss feed](https://montyprogram.com/news/feed/mariadb_releases/) to\
your favorite feed reader or by [subscribing](https://mariadb.org) to the\
announce 'at' mariadb.org announcement list (this is a low traffic,\
announce-only list).

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
