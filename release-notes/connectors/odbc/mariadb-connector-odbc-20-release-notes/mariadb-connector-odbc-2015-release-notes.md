# Connector/ODBC 2.0.15 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-odbc/2.0.15)[Release Notes](mariadb-connector-odbc-2015-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-20-changelogs/mariadb-connector-odbc-2015-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 23 May 2017

This is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB\
Connector/ODBC.

MariaDB Connector/ODBC 2.0.15 is built on top of [MariaDB Connector/C 2.3](../../c/mariadb-connector-c-23-release-notes/mariadb-connector-c-231-release-notes.md) and uses the\
binary prepared statement protocol.

## Bug Fixes

* [ODBC-97](https://jira.mariadb.org/browse/ODBC-97): Backslash at the end of string in one of statements in multistatement query leads to error
* [ODBC-95](https://jira.mariadb.org/browse/ODBC-95): Batch query with non-preparable statement will crash the connector
* [ODBC-94](https://jira.mariadb.org/browse/ODBC-94): Crash in ODBC Driver SQLExecDirect()
* [ODBC-68](https://jira.mariadb.org/browse/ODBC-68): Sporadic "Server has gone" and "Connection lost" errors on Windows when run in a VM

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the [changelog](../changelogs/mariadb-connector-odbc-20-changelogs/mariadb-connector-odbc-2015-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
