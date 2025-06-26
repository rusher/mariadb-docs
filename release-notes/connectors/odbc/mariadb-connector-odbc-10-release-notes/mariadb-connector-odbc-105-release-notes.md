# MariaDB Connector/ODBC 1.0.5 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-odbc/1.0.5)[Release Notes](mariadb-connector-odbc-105-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-10-changelogs/mariadb-connector-odbc-105-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 10 Sep 2015

This is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB\
Connector/ODBC. In general, marking this release as _stable_ means that\
there are no known serious bugs, except for those marked as feature requests,\
that no bugs were fixed since last release that caused a notable code changes,\
and that we believe the code is ready for general usage (based on bug inflow).

MariaDB Connector/ODBC 1.0.5 is built on top of MariaDB Connector/C 2.2 and\
uses the binary prepared statement protocol.

## Bug Fixes

* Fixed setup dialog bugs
* Fixed [ODBC-21](https://jira.mariadb.org/browse/ODBC-21): if stmt prepare fails while the handle reused, further use of\
  the handler rather impossible with the server error of unknown stmt handler\
  in mysqld\_stmt\_reset
* Fixed [ODBC-19](https://jira.mariadb.org/browse/ODBC-19): Using same pointer as StrLen\_Or\_IndPtr for several coulmns,\
  could cause errors if one column bound as SQL\_C\_WCHAR
* Fixed many issues preventing normal functioning of MS Access with the Connector. In\
  particular - [1](https://github.com/MariaDB/mariadb-connector-odbc/issues/1)
* Improved work in threaded environment
* Optimized execution of insert/update/delete statements without parameters
* Added freeing of explicitly allocated descriptors on disconnect
* Fixed various wrong metadata issues
* Fixed string length calculation in SQLGetData
* Fixes and improvements in the connector debug feature

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-10-changelogs/mariadb-connector-odbc-105-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
