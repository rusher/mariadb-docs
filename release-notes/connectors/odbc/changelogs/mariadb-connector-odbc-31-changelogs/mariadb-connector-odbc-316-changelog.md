# MariaDB Connector/ODBC 3.1.6 Changelog

The most recent [_**Stable**_](../../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](../../mariadb-connector-odbc-3-1-release-notes/mariadb-connector-odbc-3-1-6-release-notes.md)[Changelog](mariadb-connector-odbc-316-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 21 Jan 2020

For the highlights of this release, see the[release notes](../../mariadb-connector-odbc-3-1-release-notes/mariadb-connector-odbc-3-1-6-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/mariadb-connector-odbc) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #c114673](https://github.com/mariadb-corporation/mariadb-connector-odbc/commit/c114673)\
  2020-01-21 10:35:57 +0100
  * [ODBC-269](https://jira.mariadb.org/browse/ODBC-269) fix/testcase and version bump -> 3.1.6.\
    BEGIN NOT ATOMIC...END statement would not execute. The connector erroneously dected it as a batch of statements, that caused execution error.\
    Updated C/C subproject to 3.1.6 tag.\
    Added WIN32\_MEAN\_AND\_LEAN definition on Windows - it's required for C/C\
    build.
