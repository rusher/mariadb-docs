# MariaDB 10.0.6 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.6) |**Release Notes** |[Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-1006-changelog.md) |[Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 18 Nov 2013

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is the current development version of MariaDB. It is an evolution\
of the [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) series with several entirely new\
features not found anywhere else and with backported and\
reimplemented features from MySQL 5.6.

[MariaDB 10.0.6](mariadb-1006-release-notes.md) is a [_**Beta**_](../../../mariadb-release-criteria.md) release. This is the\
seventh 10.0-based release, and the second beta release. We are releasing it now\
to get it into the hands of any who might want to test it. All features planned\
for inclusion in the stable (GA) [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series are included in this\
release. This is still a beta however, not a final, production-ready, release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

## Bug Fixes

[MariaDB 10.0.6](mariadb-1006-release-notes.md) is primarily a bug-fix release and includes fixes for (among others) the following:

* [MDEV-5248](https://jira.mariadb.org/browse/MDEV-5248) Serious incompatibility and data corruption of DATETIME and DATE types due to get\_innobase\_type\_from\_mysql\_type refactor combined with InnoDB Online DDL
* [MDEV-5275](https://jira.mariadb.org/browse/MDEV-5275) Problems upgrading from MySQL 5.1 to MariaDB
* add missing plugins to deb packages
* various Parallel Replication fixes: [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506), [MDEV-5217](https://jira.mariadb.org/browse/MDEV-5217):

For a list of changes made in [MariaDB 10.0.6](mariadb-1006-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-1006-changelog.md).

Thanks, and enjoy MariaDB!

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
