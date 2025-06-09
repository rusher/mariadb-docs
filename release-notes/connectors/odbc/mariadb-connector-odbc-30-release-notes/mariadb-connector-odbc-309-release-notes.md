# MariaDB Connector/ODBC 3.0.9 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-odbc-309-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-30-changelogs/mariadb-connector-odbc-309-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-odbc/README.md)

**Release date:** 3 May 2019

This is a [Stable (GA)](../../../mariadb-release-criteria.md) release of MariaDB Connector/ODBC 3.0.

MariaDB Connector/ODBC 3.0.9 is built on top of[MariaDB Connector/C v.3.0.9](../../c/mariadb-connector-c-30-release-notes/mariadb-connector-c-309-release-notes.md).

**Please note:** This is the final release in the MariaDB Connector/ODBC 3.0\
series. It will be replaced by the Connector/ODBC 3.1 series, which goes stable in\
its next release.

## Bug Fixes

* [ODBC-211](https://jira.mariadb.org/browse/ODBC-211) - Wrong precision for decimal(1,0) field
* [ODBC-225](https://jira.mariadb.org/browse/ODBC-225) - Excel does not show the list of tables
* [ODBC-245](https://jira.mariadb.org/browse/ODBC-245) - SQLTables returns current DB tables if CatalogName is NULL
* [ODBC-246](https://jira.mariadb.org/browse/ODBC-246) - SQLTables ShemaName parameter is not processed
* [ODBC-238](https://jira.mariadb.org/browse/ODBC-238) - Add parameter that corresponds to MYSQL\_OPT\_SSL\_ENFORCE
* [ODBC-239](https://jira.mariadb.org/browse/ODBC-239) - Switch from deprecated mysql\_options to mysql\_optionsv
* [ODBC-232](https://jira.mariadb.org/browse/ODBC-232) - SQLGetData would crash, if application unbinded result buffers after execution
* [ODBC-228](https://jira.mariadb.org/browse/ODBC-228) - Add parameter that corresponds to MARIADB\_OPT\_TLS\_VERSION
* [ODBC-229](https://jira.mariadb.org/browse/ODBC-229) - Add parameters that correspond to MYSQL\_READ\_DEFAULT\_FILE
* [ODBC-234](https://jira.mariadb.org/browse/ODBC-234) - SQLGetTypeInfo does not work with sql\_mode='Oracle'
* [ODBC-231](https://jira.mariadb.org/browse/ODBC-231) - ODBC Error 0000 in SSIS with longtext
* [ODBC-219](https://jira.mariadb.org/browse/ODBC-219) - Stored procedures fail with error "Prepared statement not a cursor-specification"
* [ODBC-216](https://jira.mariadb.org/browse/ODBC-216) - SQLColAttribute and SQL\_DESC\_FIXED\_PREC\_SCALE returns wrong value for BigInt
* [ODBC-213](https://jira.mariadb.org/browse/ODBC-213) - SQL\_DESC\_PARAMETER\_TYPE descriptor field should be SQLSMALLINT

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-30-changelogs/mariadb-connector-odbc-309-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
