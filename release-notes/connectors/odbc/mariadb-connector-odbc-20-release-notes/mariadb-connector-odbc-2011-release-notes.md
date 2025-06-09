# MariaDB Connector/ODBC 2.0.11 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-odbc/2.0.11)[Release Notes](mariadb-connector-odbc-2011-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-20-changelogs/mariadb-connector-odbc-2011-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 9 Jun 2016

This is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB\
Connector/ODBC.

MariaDB Connector/ODBC 2.0.11 is built on top of[MariaDB Connector/C 2.2](../../c/mariadb-connector-c-22-release-notes/mariadb-connector-c-220-release-notes.md) and uses the\
binary prepared statement protocol.

## Bug Fixes

* [ODBC-44](https://jira.mariadb.org/browse/ODBC-44) - incorrect binding of TIMESTAMP to TIME type. It would affect work with MS Access if table had time and auto\_increment fields.
* [ODBC-41](https://jira.mariadb.org/browse/ODBC-41) - basically ensuring that the number of columns (counter in descriptor) is reset before issuing a new query.
* [ODBC-38](https://jira.mariadb.org/browse/ODBC-38) - SQLColumns (and some others along with it) returned ODBC3 SQL types, while MS Access is an ODBC2 application.
* [ODBC-37](https://jira.mariadb.org/browse/ODBC-37) - the variable used for length in bind structure in SQLGetData, was bigger than "unsigned long" on 64bit machines.

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-20-changelogs/mariadb-connector-odbc-2011-changelog.md).

{% @marketo/form formid="4316" formId="4316" %}
