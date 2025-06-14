# MariaDB Connector/C 3.1.26 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://mariadb.com/downloads/connectors)[Release Notes](mariadb-connector-c-3-1-26-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-31-changelogs/mariadb-connector-c-3-1-26-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-c/README.md)

**Release date:** 12 Nov 2024

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

MariaDB Connector/C 3.1.25 was not released separately but is included in [MariaDB Community Server 10.5.27](../../../mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-10-5-27-release-notes.md). MariaDB Connector/C 3.1.26 includes additional bug fixes for the Connector.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Issues fixed:

* Fixed possible crash if not default plugin was loaded.
* [CONC-730](https://jira.mariadb.org/browse/CONC-730): Undefined behavior in the reference ed25519 implementation
* [CONC-527](https://jira.mariadb.org/browse/CONC-527): Fixed error "SEC\_E\_ALGORITHM\_MISMATCH" connecting Windows client to Ubuntu

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-31-changelogs/mariadb-connector-c-3-1-26-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
