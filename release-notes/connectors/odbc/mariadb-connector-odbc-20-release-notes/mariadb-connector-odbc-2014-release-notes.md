# MariaDB Connector/ODBC 2.0.14 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-odbc/2.0.14)[Release Notes](mariadb-connector-odbc-2014-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-20-changelogs/mariadb-connector-odbc-2014-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 7 Apr 2017

This is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB\
Connector/ODBC.

MariaDB Connector/ODBC 2.0.14 is built on top of[MariaDB Connector/C 2.3](../../c/mariadb-connector-c-23-release-notes/mariadb-connector-c-231-release-notes.md) and uses the\
binary prepared statement protocol.

## Bug Fixes

* [ODBC-72](https://jira.mariadb.org/browse/ODBC-72) SQLGetData incorrectly handles UTF-16 surrogate pairs
* [ODBC-74](https://jira.mariadb.org/browse/ODBC-74) Crash when calling SQLExecDirect with multiple statements
* [ODBC-62](https://jira.mariadb.org/browse/ODBC-62) Problem with export from ACCESS
* [ODBC-69](https://jira.mariadb.org/browse/ODBC-69) Values for Charset connection attribute should be case-insensitive
* [ODBC-71](https://jira.mariadb.org/browse/ODBC-71) ADO .addnew function creates error
* [ODBC-73](https://jira.mariadb.org/browse/ODBC-73) Wrong charset in Recordsets with DAO Object Library
* [ODBC-77](https://jira.mariadb.org/browse/ODBC-77) Execution of 'ANALYZE TABLE' statement would invalidate the statement and connection handles
* [ODBC-78](https://jira.mariadb.org/browse/ODBC-78) SQLGetData would not return SQL\_NO\_DATA for BLOB/TEXT columns if the buffer size is larger than the column data
* [ODBC-83](https://jira.mariadb.org/browse/ODBC-83) Min and Max value for time data type is getting processed incorrectly
* [ODBC-84](https://jira.mariadb.org/browse/ODBC-84) Error in the SQLGetTypeInfo for WCHAR Types
* [ODBC-90](https://jira.mariadb.org/browse/ODBC-90) SQLBulkOperations/SQLSetPos SQL\_ADD would fail if TIMESTAMP column ignored

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-20-changelogs/mariadb-connector-odbc-2014-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
