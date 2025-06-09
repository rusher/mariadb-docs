# MariaDB Connector/ODBC 3.0.3 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-odbc/3.0.3)[Release Notes](mariadb-connector-odbc-303-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-30-changelogs/mariadb-connector-odbc-303-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-odbc/README.md)

**Release date:** 8 Feb 2018

This is a [Stable (GA)](../../../mariadb-release-criteria.md) release of MariaDB Connector/ODBC 3.0.

MariaDB Connector/ODBC 3.0.3 is built on top of[MariaDB Connector/C v.3.0.3](../../c/mariadb-connector-c-30-release-notes/mariadb-connector-c-303-release-notes.md) and uses the\
binary prepared statement protocol.

## Bug Fixes

* [ODBC-134](https://jira.mariadb.org/browse/ODBC-134): Fetch would fail if an unbound column contained NULL and if that\
  column some arbitrary descriptor field that was set by the application (but\
  not length/indicator buffer pointers). The bug affected ADO, as that is\
  something it can do in some cases with CursorLocation adUseClient
* [ODBC-119](https://jira.mariadb.org/browse/ODBC-119): The connector ordered SQLStatistics results using the wrong\
  columns. This could cause MS Access to pick the wrong column as a unique\
  index.
* [ODBC-131](https://jira.mariadb.org/browse/ODBC-131): While linking a table, MS Access threw an error when it received an\
  unexpected length for SQLSMALLINT and SQLINTEGER columns in a SQLColumns\
  resultset.
* [ODBC-126](https://jira.mariadb.org/browse/ODBC-126): Core dump when procedure returned more than 1 result set
* [ODBC-123](https://jira.mariadb.org/browse/ODBC-123): Crashes reading a MariaDB table with LibreOffice
* [ODBC-120](https://jira.mariadb.org/browse/ODBC-120): Performance issue. Connector did redundant calls of\
  mysql\_stmt\_data\_seek

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-30-changelogs/mariadb-connector-odbc-303-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
