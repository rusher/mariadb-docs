# Connector/ODBC 3.2.4 Release Notes

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/odbc-connector/)[Release Notes](mariadb-connector-odbc-3-2-4-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-3-2-changelogs/mariadb-connector-odbc-3-2-4-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 14 Nov 2024

This is a [Stable (GA)](../../../community-server/about/release-criteria.md) release of MariaDB Connector/ODBC 3.2.

## Notable Items

* MariaDB Connector/ODBC 3.2.4 is built on top of [MariaDB Connector/C v.3.4.3](../../c/mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-3-release-notes.md).

## Issues Fixed

* [ODBC-438](https://jira.mariadb.org/browse/ODBC-438) - High Prepared\_stmt\_count after freeing statement handles
* [ODBC-442](https://jira.mariadb.org/browse/ODBC-442) - "Verify certificate" checkbox in TLS options of the setup dialog gets checked by default. This may result in it being saved and used unintentionally for connections.
* [ODBC-437](https://jira.mariadb.org/browse/ODBC-437) - Latest ODBC driver returns NULL characters in strings with characters requiring >1 byte in utf8 representation
* [ODBC-443](https://jira.mariadb.org/browse/ODBC-443) - Incorrect value for charset utf8mb4 and longtext column with multibyte unicode characters
* [ODBC-444](https://jira.mariadb.org/browse/ODBC-444) - Errors "\[42000] \[ma-3.2.3]You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'WHERE @@sql\_mode LIKE '%ansi\_quotes%'" while running queries with MariaDB ODBC 3.2.3 and MySql 5.7
* [ODBC-440](https://jira.mariadb.org/browse/ODBC-440) - MSI doesn't update DSNs referring 3.1 driver
* [ODBC-441](https://jira.mariadb.org/browse/ODBC-441) - Setup dialog is missing fields for prepared statements cache control. Added fields for the cache size and the maximal length of cached statement.

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-3-2-changelogs/mariadb-connector-odbc-3-2-4-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
