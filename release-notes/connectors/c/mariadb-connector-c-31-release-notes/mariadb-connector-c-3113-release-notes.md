# Connector/C 3.1.13 Release notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-c-3113-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-31-changelogs/mariadb-connector-c-3113-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 11 May 2021

This is a [_**Stable (GA)**_](../../../community-server/about/release-criteria.md) release of the MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Notable Changes

* [CONC-537](https://jira.mariadb.org/browse/CONC-537): Only read from MYSQL\_HOME if MARIADB\_HOME was not set

## Bugs Fixed

* [CONC-548](https://jira.mariadb.org/browse/CONC-548): Symbol conflict with libsodium
* [CONC-490](https://jira.mariadb.org/browse/CONC-490): Handshake error when CLIENT\_CONNECT\_WITH\_DB flag was set without specifying database
* [CONC-543](https://jira.mariadb.org/browse/CONC-543): Hash functions conflict with GnuTLS
* [CONC-539](https://jira.mariadb.org/browse/CONC-539): Added cipher suites ECDHE-RSA-AES128-SHA256 (0xC027) and ECDHE-RSA-AES256-SHA384 (0xC028) to the cipher map which maps cipher suite names to the corresponding algorithm ids (Windows Schannel)
* [CONC-535](https://jira.mariadb.org/browse/CONC-535): Disabled checksum ignored in events (replication/binlog API)

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-31-changelogs/mariadb-connector-c-3112-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
