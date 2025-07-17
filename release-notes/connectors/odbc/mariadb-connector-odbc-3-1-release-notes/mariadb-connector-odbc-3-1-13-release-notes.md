# Connector/ODBC 3.1.13 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-odbc-3-1-13-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-3113-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 7 Jun 2021

This is a [Stable (GA)](../../../community-server/about/release-criteria.md) release of MariaDB Connector/ODBC 3.1.

MariaDB Connector/ODBC 3.1.13 is built on top of[MariaDB Connector/C v.3.1.13](../../c/mariadb-connector-c-31-release-notes/mariadb-connector-c-3113-release-notes.md).

## Notable Changes

* [ODBC-318](https://jira.mariadb.org/browse/ODBC-318) - Added a connection string option to suppress errors on schema parameters in catalog functions.
  * Schema parameters used to be neglected by catalog functions, while the specification says the error has to be returned if those are provided and the driver does not support schemas. [ODBC-316](https://jira.mariadb.org/browse/ODBC-316) has changed that. Because this can break existing applications that misuse the API, the connection string option `SCHEMANOERROR` has been introduced to suppress these errors, if necessary.

## Bug Fixes

* [ODBC-316](https://jira.mariadb.org/browse/ODBC-316) - Issues with Catalog functions
* [ODBC-317](https://jira.mariadb.org/browse/ODBC-317) - Some connection attributes treated using wrong data type
* [ODBC-319](https://jira.mariadb.org/browse/ODBC-319) - Some performance improvements

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-3113-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
