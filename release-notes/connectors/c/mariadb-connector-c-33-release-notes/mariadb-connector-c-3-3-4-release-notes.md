# MariaDB Connector/C 3.3.4 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-c-3-3-4-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-33-changelogs/mariadb-connector-c-3-3-4-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 7 Feb 2023

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Issues fixed:

* [CONC-627](https://jira.mariadb.org/browse/CONC-627): Don't substitute parameters in server error message
* [CONC-626](https://jira.mariadb.org/browse/CONC-626): Fix memory leak in prepared statements if realloc failed
* [CONC-625](https://jira.mariadb.org/browse/CONC-625): Fixed error numbers
* [CONC-624](https://jira.mariadb.org/browse/CONC-624): Check error code ranges and provide support for variadic arguments in prepared statement errors.
* [CONC-623](https://jira.mariadb.org/browse/CONC-623): Check return value of parameter callback function and return error.
* [CONC-622](https://jira.mariadb.org/browse/CONC-622): Fix double free() if asnyc connect failed

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-33-changelogs/mariadb-connector-c-3-3-4-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
