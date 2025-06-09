# MariaDB Connector/ODBC 3.0.1 Beta Changelog

The most recent [_**Stable**_](../../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-odbc/3.0.1)[Release Notes](../../mariadb-connector-odbc-30-release-notes/mariadb-connector-odbc-301-release-notes.md)[Changelog](mariadb-connector-odbc-301-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 1 Aug 2017

For the highlights of this release, see the[release notes](../../mariadb-connector-odbc-30-release-notes/mariadb-connector-odbc-301-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/mariadb-connector-odbc) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #e5dd744](https://github.com/mariadb-corporation/mariadb-connector-odbc/commit/e5dd744)\
  2017-07-31 02:30:34 +0200
  * \[[ODBC-105](https://jira.mariadb.org/browse/ODBC-105)] Starting from v. 10.2.7, server encloses COLUMN\_DEFAULT in the [INFORMATION\_SCHEMA.COLUMNS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-columns-table) table, in single quotes for literal strings. Connector now considers the server version, when constructing the query for SQLColumns .
* [Revision #ee0a63d](https://github.com/mariadb-corporation/mariadb-connector-odbc/commit/ee0a63d)\
  2017-07-31 01:19:28 +0200
  * Fix of small error in CMakeLists.txt (addition to previous commit). Fix of possible memleak. Could occur if cursor was closed after a query that did not produce result-set or contain parameters. Pretty extravagant, but it looks like more likely to be the case with UnixODBC.
* [Revision #b269d37](https://github.com/mariadb-corporation/mariadb-connector-odbc/commit/b269d37)\
  2017-07-30 19:47:57 +0200
  * \[[ODBC-106](https://jira.mariadb.org/browse/ODBC-106)] Support of MariaDB prepared statements bulk operations.
* [Revision #0f68677](https://github.com/mariadb-corporation/mariadb-connector-odbc/commit/0f68677)\
  2017-05-19 02:27:26 +0200
  * Has all changes from latest 2.0 releases merged
