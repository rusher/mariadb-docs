# MariaDB Connector/C 3.0.8 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-c/3.0.8/)[Release Notes](mariadb-connector-c-308-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-30-changelogs/mariadb-connector-c-308-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 21 Dec 2018

This is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of the MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Notable Bug fixes

* Added missing pdb's to windows installer
* Fixed windows build when using external zlib
* mingw fix: use lowercase names for include files
* [CONC-375](https://jira.mariadb.org/browse/CONC-375): Fixed handshake errors when mixing TLSv1.3 cipher suites with cipher suites from other TLS protocols

## New features

* [CONC-312](https://jira.mariadb.org/browse/CONC-312): Added new caching\_sha2\_password authentication plugin for authentication with MySQL 8.0

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-30-changelogs/mariadb-connector-c-308-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
