# MariaDB 10.4.17 Release Notes

The most recent release of [MariaDB 10.4](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/broken-reference/README.md) is:[**MariaDB 10.4.34**](mariadb-10-4-34-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download 10.4.17](https://downloads.mariadb.org/mariadb/10.4.17/)[Release Notes](mariadb-10417-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10417-changelog.md)[Overview of 10.4](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/broken-reference/README.md)

**Release date:** 11 Nov 2020

[MariaDB 10.4](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/broken-reference/README.md) is the previous _stable_ series of MariaDB. It is an evolution\
of [MariaDB 10.3](../release-notes-mariadb-10-3-series/what-is-mariadb-103.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL.

[MariaDB 10.4.17](mariadb-10417-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.4**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/broken-reference/README.md) **see the**[**What is MariaDB 10.4?**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/broken-reference/README.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* Out-of-cycle release to fix regressions in [MariaDB 10.4.16](mariadb-10416-release-notes.md)
* Follow up to [MDEV-19838](https://jira.mariadb.org/browse/MDEV-19838) to alter protocol checks to support the following implementations (which add garbage to the end of some packets):
  * PHP PDO (all versions) ([MDEV-24121](https://jira.mariadb.org/browse/MDEV-24121))
  * mysqlnd (from PHP < 7.3) ([MDEV-24121](https://jira.mariadb.org/browse/MDEV-24121))
  * mysql-connector-python (all versions) ([MDEV-24134](https://jira.mariadb.org/browse/MDEV-24134))
  * and mysql-connector-java (all versions)
* Arbitrary InnoDB buffer pool and data file corruption ([MDEV-24096](https://jira.mariadb.org/browse/MDEV-24096))
* The query optimizer consumed a lot of memory when handling construct in form of `key_column [NOT] IN (large-list-of constants)` ([MDEV-24117](https://jira.mariadb.org/browse/MDEV-24117))
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-`-``#`

## Changelog

For a complete list of changes made in [MariaDB 10.4.17](mariadb-10417-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10417-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.4.17](mariadb-10417-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-5-8-10-4-17-10-3-27-and-10-2-36-now-available/).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
