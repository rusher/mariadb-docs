# MariaDB Connector/ODBC 3.1.19 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-odbc-3-1-19-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-3-1-19-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 7 Jul 2023

This is a [Stable (GA)](../../../mariadb-release-criteria.md) release of MariaDB Connector/ODBC 3.1.

MariaDB Connector/ODBC 3.1.19 is built on top of[MariaDB Connector/C v.3.3.5](../../c/mariadb-connector-c-33-release-notes/mariadb-connector-c-332-release-notes.md).

## Bug Fixes

* [ODBC-350](https://jira.mariadb.org/browse/ODBC-350) - Invalid BIT column value from subselect
* [ODBC-390](https://jira.mariadb.org/browse/ODBC-390) - Using SQL\_ATTR\_QUERY\_TIMEOUT leaks memory
* [ODBC-391](https://jira.mariadb.org/browse/ODBC-391) - With lower\_case\_table\_names=2 server the driver may not read indexes in SQLStatistics. This issue caused [ODBC-370](https://jira.mariadb.org/browse/ODBC-370) - MS Access could not detect table's indexes
* [ODBC-392](https://jira.mariadb.org/browse/ODBC-392) - SQLSetConnectAttr(SQL\_ATTR\_CURRENT\_CATALOG) can work incorrectly

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-3-1-19-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
