# Connector/C 3.0.7 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://mariadb.com/downloads/?showall=1\&tab=connectors\&group=mariadbconnectors\&product=C%2FC%2B%2B%20connector\&version=3.0.7)[Release Notes](mariadb-connector-c-307-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-30-changelogs/mariadb-connector-c-307-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-c/README.md)

**Release date:** 14 Nov 2018

This is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of the MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Notable Bug fixes

* Build fixes when building with ASAN/TSAN
* [CONC-370](https://jira.mariadb.org/browse/CONC-370): Fixed memory leak in configuration file parsing.
* [CONC-371](https://jira.mariadb.org/browse/CONC-371): Incorrect fractional part conversion when converting datetime string to MYSQL\_TIME
* [CONC-283](https://jira.mariadb.org/browse/CONC-283): Fixed pkg-config configuration
* [CONC-364](https://jira.mariadb.org/browse/CONC-364): Not all sockets created in pvio\_socket\_connect function are closed
* multiple fixes in named pipe implementation
* OpenSSL build fixes on Windows platforms

## New features

* [CONC-349](https://jira.mariadb.org/browse/CONC-349): Added new parameter STMT\_ATTR\_STATE to retrieve statement status via api function mysql\_stmt\_attr\_get

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-30-changelogs/mariadb-connector-c-307-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
