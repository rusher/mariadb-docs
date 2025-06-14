# MariaDB Connector/ODBC 2.0.12 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-odbc/2.0.12)[Release Notes](mariadb-connector-odbc-2012-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-20-changelogs/mariadb-connector-odbc-2012-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 15 Sep 2016

This is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB\
Connector/ODBC.

MariaDB Connector/ODBC 2.0.12 is built on top of[MariaDB Connector/C 2.3](../../c/mariadb-connector-c-23-release-notes/mariadb-connector-c-231-release-notes.md) and uses the\
binary prepared statement protocol.

## Bug Fixes

* [ODBC-47](https://jira.mariadb.org/browse/ODBC-47) - Inconsistent data if blob field fetched in parts with SQLGetData
* [ODBC-45](https://jira.mariadb.org/browse/ODBC-45) - Error binding boolean data type to SQL\_C\_CHAR - conversion of SQL\_C\_CHAR parameters to SQL\_BIT has been corrected
* [ODBC-48](https://jira.mariadb.org/browse/ODBC-48) - ISO Standard Procedure Call Bug
* [ODBC-51](https://jira.mariadb.org/browse/ODBC-51) - SQLTables fails with HY090 "Invalid string or buffer length". Connector returned error when it had to convert empty string to SQL\_C\_WCHAR

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-20-changelogs/mariadb-connector-odbc-2012-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
