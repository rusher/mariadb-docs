# MariaDB Connector/ODBC 3.0.0 Alpha Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-odbc/3.0.0)[Release Notes](mariadb-connector-odbc-300-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-30-changelogs/mariadb-connector-odbc-300-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 19 Jan 2017

This is an [Alpha](../../../mariadb-release-criteria.md) release of MariaDB Connector/ODBC 3.0.

As with any other pre-production release, caution should be taken when\
installing this **alpha** release on production systems or systems with\
critical data. Not all of the features planned for the stable (GA) MariaDB\
Connector/ODBC 3.0 release are implemented yet.

MariaDB Connector/ODBC 3.0.0 is built on top of[MariaDB Connector/C 3.0](../../c/mariadb-connector-c-30-release-notes/mariadb-connector-c-301-release-notes.md) and uses the\
binary prepared statement protocol.

For `SQLExecDirect` calls, uses the `mariadb_stmt_execute_direct` MariaDB\
C API command, which is faster than using `mysql_stmt_prepare + mysql_stmt_execute`,\
but only with [MariaDB 10.2](../../../mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) server.

This release was built with SSL support. You can use SSLKEY, SSLCERT, SSLCA,\
SSLCAPATH, SSLCIPHER, SSLVERIFY, SSLCRL and SSLCRLPATH connection string/DSN\
options to configure your connection properties.

Internally, Connector/ODBC 3.0 depends much less on Connector/C internal\
features than previous versions, with the eventual goal of only using the open\
Connector/C API.

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-30-changelogs/mariadb-connector-odbc-300-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
