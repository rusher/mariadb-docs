# MariaDB Connector/C 2.1.0 Release Notes

The most recent [_**Stable**_](../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-c/2.1.0)[Release Notes](mariadb-connector-c-210-release-notes.md)[Changelog](changelogs/mariadb-connector-c-210-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-c/README.md)

**Release date:** 29 Jan 2015

This is a [_**Stable**_](../../mariadb-release-criteria.md) _**(GA)**_ release of the MariaDB\
Connector/C, formerly known as MariaDB Client Library for C. In general,\
marking this release as _stable_ means that there are no known serious bugs,\
except for those marked as feature requests, that no bugs were fixed since last\
release that caused a notable code changes, and that we believe the code is\
ready for general usage (based on bug inflow).

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## New features

* Non blocking (asynchronous) API. For a detailed description see[Non-blocking Client Library](broken-reference).
* New dialog and mysql\_clear\_text authentication plugins.

## New configuration options

CMake build now supports the following additional configuration options:

* -DINSTALL\_LAYOUT=DEFAULT or RPM\
  Allow to overwrite default directories
* -DLIB\_INSTALL\_DIR
* -DINCLUDE\_INSTALL\_DIR
* -DDOCS\_INSTALL\_DIR
* -DPLUGINS\_INSTALL\_DIR
* -DBIN\_INSTALL\_DIR

## Bug fixes

* Reduce build time by creating OBJECT library (introduced in CMake 2.8.8)
* Out-of-source build touches files in source dir ([CONC-88](https://jira.mariadb.org/browse/CONC-88))
* Incorrect output for mariadb\_config ([CONC-99](https://jira.mariadb.org/browse/CONC-99))
* Segmentation fault when using named pipes ([CONC-94](https://jira.mariadb.org/browse/CONC-94))
* Crash in prepared statements when using NULL values ([CONC-92](https://jira.mariadb.org/browse/CONC-92))
* Check if connection is valid before resetting statement ([CONC-97](https://jira.mariadb.org/browse/CONC-97), [CONC-98](https://jira.mariadb.org/browse/CONC-98))
* Socket was closed twice in threaded environment ([CONC-99](https://jira.mariadb.org/browse/CONC-99))
* SSL connection with require X509 privilege doesn't work ([CONC-95](https://jira.mariadb.org/browse/CONC-95))
* mysql\_options doesn't support MYSQL\_SECURE\_AUTH option ([CONC-104](https://jira.mariadb.org/browse/CONC-104))
* Remove longlong definition from mysql.h to prevent collides with other projects ([CONC-105](https://jira.mariadb.org/browse/CONC-105))
* Protect certification loading by a mutex ([CONC-102](https://jira.mariadb.org/browse/CONC-102))
* Fixed installation layout problems ([CONC-107](https://jira.mariadb.org/browse/CONC-107))
* Export missing plugin symbols ([CONC-111](https://jira.mariadb.org/browse/CONC-111))
* Windows version of libmariadb doesn't export all symbols ([CONC-114](https://jira.mariadb.org/browse/CONC-114))
* Fixed memory leak when reconnecting ([CONC-118](https://jira.mariadb.org/browse/CONC-118))

For a complete list and description please check the[Jira bug system](https://jira.mariadb.org/browse/CONC)

## Changelog

For a list of changes made in this release, with links to detailed\
information on each push, see the[changelog](changelogs/mariadb-connector-c-210-changelog.md).

{% @marketo/form formid="4316" formId="4316" %}
