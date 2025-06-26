# MariaDB Connector/C 3.4.1 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://mariadb.com/downloads/connectors)[Release Notes](mariadb-connector-c-3-4-1-release-notes.md)[Changelog](../changelogs/mariadb-connectorc-3-4-changelogs/mariadb-connector-c-3-4-1-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 20 Aug 2024

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Issues fixed:

* [CONC-698](https://jira.mariadb.org/browse/CONC-698): certificate info is read on every connect
* [CONC-704](https://jira.mariadb.org/browse/CONC-704): parse\_connection\_string ignores empty string in last parameter
* [CONC-700](https://jira.mariadb.org/browse/CONC-700): Fix gcc-14 -Wcalloc-transposed-args
* [MDEV-34424](https://jira.mariadb.org/browse/MDEV-34424) Replica server crashes when using ed25519 plugin
* TLS (schannel) fixes: - don't verify fingerprint twice

## Notable Changes

* expired TLS certificate is always rejected, even if it can be auto-verified or a fingerprint is correct
* new PARSEC authentication plugin is included, but disabled by default

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connectorc-3-4-changelogs/mariadb-connector-c-3-4-1-changelog.md).

{% include "https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/~/reusable/vX1KAy0t1XuYJaGsK28T/" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
