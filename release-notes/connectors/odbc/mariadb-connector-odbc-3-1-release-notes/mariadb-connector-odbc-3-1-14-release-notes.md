# Connector/ODBC 3.1.14 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-odbc-3-1-14-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-3114-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 29 Oct 2021

This is a [Stable (GA)](../../../community-server/about/release-criteria.md) release of MariaDB Connector/ODBC 3.1.

MariaDB Connector/ODBC 3.1.14 is built on top of[MariaDB Connector/C v.3.2.4](../../c/mariadb-connector-c-32-release-notes/mariadb-connector-c-324-release-notes.md).

## Notable Changes

* [ODBC-331](https://jira.mariadb.org/browse/ODBC-331) - C/ODBC is now based on Connector/C 3.2 release series
* [ODBC-320](https://jira.mariadb.org/browse/ODBC-320) - ODBC Connector package for MacOS is now notarized
* [ODBC-341](https://jira.mariadb.org/browse/ODBC-341) - Added read/write timeout connection string options READ\_TIMEOUT and WRITE\_TIMEOUT

## Bug Fixes

* [ODBC-299](https://jira.mariadb.org/browse/ODBC-299) - FindIconv.cmake too old to work on MacOS 11 (Big Sur)
* [ODBC-311](https://jira.mariadb.org/browse/ODBC-311) - Connector/ODBC libraries go to the wrong directories and it breaks packaging
* [ODBC-321](https://jira.mariadb.org/browse/ODBC-321) - Driver crash in MultiByteToWideChar
* [ODBC-324](https://jira.mariadb.org/browse/ODBC-324) - Excel+MariaDB driver not showing table with SYSTEM VERSIONING
* [ODBC-326](https://jira.mariadb.org/browse/ODBC-326) - Connecting Excel with MariaDB through Microsoft Query - String data right truncated
* [ODBC-330](https://jira.mariadb.org/browse/ODBC-330) - MSI is not created when connectors is built from source - Windows
* [ODBC-334](https://jira.mariadb.org/browse/ODBC-334) - Using the hostname for the server doesn't work in ODBC Data Source name Gui with MariaDB ODBC
* [ODBC-340](https://jira.mariadb.org/browse/ODBC-340) - FreeBSD - Undefined symbol "OPENSSL\_init\_ssl"

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-3114-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
