# Connector/ODBC 2.0.13 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-odbc/2.0.13)[Release Notes](mariadb-connector-odbc-2013-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-20-changelogs/mariadb-connector-odbc-2013-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 31 Oct 2016

This is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB\
Connector/ODBC.

MariaDB Connector/ODBC 2.0.13 is built on top of [MariaDB Connector/C 2.3](../../c/mariadb-connector-c-23-release-notes/mariadb-connector-c-231-release-notes.md) and uses the\
binary prepared statement protocol.

## Bug Fixes

* [ODBC-56](https://jira.mariadb.org/browse/ODBC-56) - Fix of wrong calculation of StLen ptr in case of columnwise binding
* [ODBC-58](https://jira.mariadb.org/browse/ODBC-58) - Any field going after a TEXT field in the selecion list, is fetched incorrectly
* [ODBC-61](https://jira.mariadb.org/browse/ODBC-61) - SQLGetInfo(SQL\_FILE\_USAGE) crashes connector

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the [changelog](../changelogs/mariadb-connector-odbc-20-changelogs/mariadb-connector-odbc-2013-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
