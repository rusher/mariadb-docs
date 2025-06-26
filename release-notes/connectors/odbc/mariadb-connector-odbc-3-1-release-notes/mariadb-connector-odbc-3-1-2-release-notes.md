# MariaDB Connector/ODBC 3.1.2 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-odbc-3-1-2-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-312-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 23 Jul 2019

This is a [Stable (GA)](../../../mariadb-release-criteria.md) release of MariaDB Connector/ODBC 3.1.

MariaDB Connector/ODBC 3.1.2 is built on top of[MariaDB Connector/C v.3.1.2](../../c/mariadb-connector-c-31-release-notes/mariadb-connector-c-312-release-notes.md).

## Notable Changes

* [ODBC-210](https://jira.mariadb.org/browse/ODBC-210) - Fix compilation warnings on OS X
* [ODBC-250](https://jira.mariadb.org/browse/ODBC-250) - Operations with Dynamic Lists are not thread-safe, and need to be guarded with mutexes
* [ODBC-252](https://jira.mariadb.org/browse/ODBC-252) - Build failed when executed the commands present in "BUILD.md" file
* [ODBC-253](https://jira.mariadb.org/browse/ODBC-253) - MADB\_StmtExecDirect() crashes if StatementText is "\0"
* [ODBC-254](https://jira.mariadb.org/browse/ODBC-254) - FTBFS: Cmake libdir misconfiguration
* [ODBC-256](https://jira.mariadb.org/browse/ODBC-256) - Driver craches on empty statement
* [ODBC-257](https://jira.mariadb.org/browse/ODBC-257) - Double-check CPack for a copy-paste error
* [ODBC-258](https://jira.mariadb.org/browse/ODBC-258) - RFE: make documentation and license dirs configurable
* [ODBC-260](https://jira.mariadb.org/browse/ODBC-260) - Remove all references to internals of MYSQL structure
* [ODBC-255](https://jira.mariadb.org/browse/ODBC-255) - When C/ODBC is upgraded on Windows, allow existing data sources to be moved
* [ODBC-211](https://jira.mariadb.org/browse/ODBC-211) - SQLDescribeCol return precision=0 for field type decimal(1,0)

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-312-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
