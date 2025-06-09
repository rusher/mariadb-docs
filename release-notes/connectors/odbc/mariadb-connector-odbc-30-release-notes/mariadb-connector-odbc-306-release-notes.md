# MariaDB Connector/ODBC 3.0.6 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-odbc/3.0.6)[Release Notes](mariadb-connector-odbc-306-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-30-changelogs/mariadb-connector-odbc-306-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-odbc/README.md)

**Release date:** 2 Aug 2018

This is a [Stable (GA)](../../../mariadb-release-criteria.md) release of MariaDB Connector/ODBC 3.0.

MariaDB Connector/ODBC 3.0.6 is built on top of[MariaDB Connector/C v.3.0.6](../../c/mariadb-connector-c-30-release-notes/mariadb-connector-c-306-release-notes.md).

## Bug Fixes

* [ODBC-159](https://jira.mariadb.org/browse/ODBC-159) - Creation of temporary tables with multiple statements in one query fails
* [ODBC-166](https://jira.mariadb.org/browse/ODBC-166) - Incorect Display Size for decimal column
* [ODBC-164](https://jira.mariadb.org/browse/ODBC-164) - Do not include C/C project in cmake, if directory is absent. Make cmake link against installed in the system libmariadb in such case
* [ODBC-161](https://jira.mariadb.org/browse/ODBC-161) - Trying to create a file dsn causes odbc administrator to crash
* [ODBC-162](https://jira.mariadb.org/browse/ODBC-162) - SQLNumResultCols returns zero for query with long data and CTE
* [ODBC-158](https://jira.mariadb.org/browse/ODBC-158) - When performing a query with an aggregate function such as Count or Sum from MSAccess, an error is returned
* [ODBC-160](https://jira.mariadb.org/browse/ODBC-160) - Connector did not return length of string returned for SQL\_IDENTIFIER\_QUOTE\_CHAR info type.
* [ODBC-157](https://jira.mariadb.org/browse/ODBC-157) - Display size and Column length do not include fractional part for (date)time types
* [ODBC-154](https://jira.mariadb.org/browse/ODBC-154) - Linking error when building with dynamic C/C linking
* [ODBC-155](https://jira.mariadb.org/browse/ODBC-155) - SQLDescribeCol returns 0 for decimal digits for datetime types with microseconds
* [ODBC-149](https://jira.mariadb.org/browse/ODBC-149) - Connection Crashes with Timestamp INSERT INTO on parameter array operation
* [ODBC-151](https://jira.mariadb.org/browse/ODBC-151) - In SQLBindParameter BufferLength sets SQL\_DESC\_OCTET\_LENGTH for fixed length types
* [ODBC-150](https://jira.mariadb.org/browse/ODBC-150) - DESC(RIBE) statement caused error with the connector
* [ODBC-148](https://jira.mariadb.org/browse/ODBC-148) - DATE and DATETIME values are NULL in Crystal Reports

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-30-changelogs/mariadb-connector-odbc-306-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
