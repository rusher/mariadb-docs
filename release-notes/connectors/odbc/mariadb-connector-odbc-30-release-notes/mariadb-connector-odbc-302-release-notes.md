# Connector/ODBC 3.0.2 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-odbc/3.0.2)[Release Notes](mariadb-connector-odbc-302-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-30-changelogs/mariadb-connector-odbc-302-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 12 Oct 2017

This is a [Stable (GA)](../../../community-server/about/release-criteria.md) release of MariaDB Connector/ODBC 3.0.

MariaDB Connector/ODBC 3.0.2 is built on top of[MariaDB Connector/C 3.0](../../c/mariadb-connector-c-30-release-notes/mariadb-connector-c-302-release-notes.md) and uses the\
binary prepared statement protocol.

For Parameter Arrays operations (column-wise) with INSERT and UPDATE statements, and for`SQLBulkOperations`/`SQLSetPos` (SQL\_ADD/SQL\_UPDATE) it uses MariaDB's bulk\
operations feature, which allows sending batches of parameter sets, instead of\
sending them row by row. This only works with a server version >= [MariaDB 10.2.7](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1027-release-notes.md).

For `SQLExecDirect` calls, uses the `mariadb_stmt_execute_direct` MariaDB\
C API command, which is faster than using `mysql_stmt_prepare + mysql_stmt_execute`,\
but only with [MariaDB 10.2](../../../community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) server.

This release was built with SSL support. You can use SSLKEY, SSLCERT, SSLCA,\
SSLCAPATH, SSLCIPHER, SSLVERIFY, SSLCRL and SSLCRLPATH connection string/DSN\
options to configure your connection properties.

Internally, Connector/ODBC 3.0 depends much less on Connector/C internal\
features than previous versions, with the eventual goal of only using the open\
Connector/C API. Build with dynamic linking against Connector/C library is now supported.

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-30-changelogs/mariadb-connector-odbc-302-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
