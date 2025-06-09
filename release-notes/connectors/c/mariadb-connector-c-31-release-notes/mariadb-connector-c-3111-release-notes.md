# MariaDB Connector/C 3.1.11 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-c-3111-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-31-changelogs/mariadb-connector-c-3111-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 4 Nov 2020

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of the MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Notable Changes

* [CONC-508](https://jira.mariadb.org/browse/CONC-508): Added support for passwords > 255 characters
* [CONC-501](https://jira.mariadb.org/browse/CONC-501): Added support for TLS v1.3 cipher suites (OpenSSL only)
* [MDEV-21612](https://jira.mariadb.org/browse/MDEV-21612): Removed unused command COM\_MULTI
* If character set "auto" was specified on Windows, and GetConsoleCP returns a positive number, Ansi code page identifier (GetACP) will be used
* Updated bundled zlib (now version 1.2.11)

## Bugs Fixed

* [CONC-513](https://jira.mariadb.org/browse/CONC-513): MSAN use-of-uninitialized-value in strstr()
* [CONC-512](https://jira.mariadb.org/browse/CONC-512): truncation check for float values fails on i386 due to Intel FPU optimization bug in gcc
* [CONC-510](https://jira.mariadb.org/browse/CONC-510): Fix crash when loading plugins in mysql\_server\_init()
* [CONC-507](https://jira.mariadb.org/browse/CONC-507): Fixed race condition in ma\_net\_init (Kudos to Alexander Sapin)
* [MDEV-23564](https://jira.mariadb.org/browse/MDEV-23564): CMake failed on MacOSX due to deprecated GSS API methods

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-31-changelogs/mariadb-connector-c-3111-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
