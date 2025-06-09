# MariaDB Connector/ODBC 2.0.19 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-odbc-2019-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-20-changelogs/mariadb-connector-odbc-2019-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 5 Jun 2019

This is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB\
Connector/ODBC.

## Notes

MariaDB Connector/ODBC 2.0.19 is built on top of[MariaDB Connector/C v.2.3.7](../../c/mariadb-connector-c-23-release-notes/mariadb-connector-c-237-release-notes.md) and uses the\
binary prepared statement protocol.

## Bug Fixes

* [ODBC-43](https://jira.mariadb.org/browse/ODBC-43) - If string parameter bound as date/time sql type, overflow errors are not detected
* [ODBC-70](https://jira.mariadb.org/browse/ODBC-70) - Last part - caring of 0-date passed in the string
* [ODBC-152](https://jira.mariadb.org/browse/ODBC-152) - Problem with SQLColumns / SQLFetch
* [ODBC-169](https://jira.mariadb.org/browse/ODBC-169) - Empty results or error if executing mutliple selects in a batch
* [ODBC-181](https://jira.mariadb.org/browse/ODBC-181) - Insert query error decimal + longtext
* [ODBC-182](https://jira.mariadb.org/browse/ODBC-182) - Wrong data inserted into TIME field if bound as TIMESTAMP, and date fields contain data
* [ODBC-183](https://jira.mariadb.org/browse/ODBC-183) - Connector reports incorrect number of affected rows for statements in batch
* [ODBC-186](https://jira.mariadb.org/browse/ODBC-186) - Several problems with SQLColumns and SQLProcedureColumns
* [ODBC-188](https://jira.mariadb.org/browse/ODBC-188) - Adding Windows ODBC DSN from command line via odbcconf.exe fails
* [ODBC-192](https://jira.mariadb.org/browse/ODBC-192) - ODBC 3.0.6 VBA Error on Query
* [ODBC-194](https://jira.mariadb.org/browse/ODBC-194) - SQLGetData does not return SQL\_NULL\_DATA for datetime types in some cases
* [ODBC-197](https://jira.mariadb.org/browse/ODBC-197) - If Time value is fetched as Timestamp, the fraction part should be 0
* [ODBC-198](https://jira.mariadb.org/browse/ODBC-198) - Incorrect second fraction number if string field is fetched into TIMESTAMP struct
* [ODBC-199](https://jira.mariadb.org/browse/ODBC-199) - If time parameter is bound as timestamp, date fields should be set to current date values
* [ODBC-203](https://jira.mariadb.org/browse/ODBC-203) - Empty results if executing mutliple selects in a batch and data fetched as SQL\_C\_WCHAR
* [ODBC-204](https://jira.mariadb.org/browse/ODBC-204) - SQLGetData did not return empty wide string
* [ODBC-207](https://jira.mariadb.org/browse/ODBC-207) - Fix multi-statement parameter structures realloc, that could cause segfault on 2nd execution
* [ODBC-211](https://jira.mariadb.org/browse/ODBC-211) - Wrong precision for decimal(1,0) field
* [ODBC-213](https://jira.mariadb.org/browse/ODBC-213) - SQL\_DESC\_PARAMETER\_TYPE descriptor field should be SQLSMALLINT
* [ODBC-216](https://jira.mariadb.org/browse/ODBC-216) - SQLColAttribute and SQL\_DESC\_FIXED\_PREC\_SCALE returns wrong value for BigInt
* [ODBC-219](https://jira.mariadb.org/browse/ODBC-219) - Stored procedures fail with error "Prepared statement not a cursor-specification"
* [ODBC-225](https://jira.mariadb.org/browse/ODBC-225) - Excel does not show the list of tables
* [ODBC-231](https://jira.mariadb.org/browse/ODBC-231) - ODBC Error 0000 in SSIS with longtext
* [ODBC-232](https://jira.mariadb.org/browse/ODBC-232) - SQLGetData would crash, if application unbinded result buffers after execution
* [ODBC-234](https://jira.mariadb.org/browse/ODBC-234) - SQLGetTypeInfo does not work with sql\_mode='Oracle'
* [ODBC-229](https://jira.mariadb.org/browse/ODBC-229) - Add parameters that correspond to MYSQL\_READ\_DEFAULT\_FILE
* [ODBC-245](https://jira.mariadb.org/browse/ODBC-245) - SQLTables returns current DB tables if CatalogName is NULL
* [ODBC-246](https://jira.mariadb.org/browse/ODBC-246) - SQLTables ShemaName parameter is not processed

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-20-changelogs/mariadb-connector-odbc-2019-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
