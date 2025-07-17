# Connector/ODBC 3.0.8 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-odbc/3.0.8/)[Release Notes](mariadb-connector-odbc-308-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-30-changelogs/mariadb-connector-odbc-308-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 4 Jan 2019

This is a [Stable (GA)](../../../community-server/about/release-criteria.md) release of MariaDB Connector/ODBC 3.0.

MariaDB Connector/ODBC 3.0.8 is built on top of[MariaDB Connector/C v.3.0.8](../../c/mariadb-connector-c-30-release-notes/mariadb-connector-c-308-release-notes.md).

## Bug Fixes

* [ODBC-207](https://jira.mariadb.org/browse/ODBC-207) - Fix multi-statement parameter structures realloc, that could cause segfault on 2nd execution
* [ODBC-203](https://jira.mariadb.org/browse/ODBC-203) - Empty results if executing mutliple selects in a batch and data fetched as SQL\_C\_WCHAR
* [ODBC-204](https://jira.mariadb.org/browse/ODBC-204) - SQLGetData did not return empty wide string

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-30-changelogs/mariadb-connector-odbc-308-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
