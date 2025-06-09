# MariaDB Connector/C 3.3.13 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://mariadb.com/downloads/connectors)[Release Notes](mariadb-connector-c-3-3-13-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-33-changelogs/mariadb-connector-c-3-3-13-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 12 Nov 2024

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

MariaDB Connector/C 3.3.12 was not released separately but is included in [MariaDB Community Server 10.6.20](../../../mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-20-release-notes.md), [10.11.10](../../../mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-10-release-notes.md), and [11.2.6](../../../mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes.md). MariaDB Connector/C 3.3.13 includes additional bug fixes for the Connector.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Notable changes

* Added TLSv1.3 support for Schannel (Windows)
* Added new option -DWITH\_BOOST\_CONTEXT. CMake option -DWITH\_BOOST\_CONTEXT=ON adds boost::context as a dependency of libmariadb to provide a fallback on non-natively supported architectures. boost::context is preferred over ucontext when both are available.

## Issues fixed:

* Fixed possible crash if not default plugin was loaded.
* [CONC-730](https://jira.mariadb.org/browse/CONC-730): Undefined behavior in the reference ed25519 implementation
* [CONC-527](https://jira.mariadb.org/browse/CONC-527): Fixed error "SEC\_E\_ALGORITHM\_MISMATCH" connecting Windows client to Ubuntu
* [CONC-735](https://jira.mariadb.org/browse/CONC-735): A reconnect doesn't do node failover when using a connection string with multiple hosts
* [MDEV-34859](https://jira.mariadb.org/browse/MDEV-34859): Failed to initialise non-blocking API on OpenBSD arm64

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-33-changelogs/mariadb-connector-c-3-3-13-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
