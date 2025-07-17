# Connector/C 3.1.7 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-c-317-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-31-changelogs/mariadb-connector-c-317-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-c/README.md)

**Release date:** 29 Jan 2020

This is a [_**Stable (GA)**_](../../../community-server/about/release-criteria.md) release of the MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Notable Changes

* Included in [MariaDB 10.4.12](../../../community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10412-release-notes.md), [MariaDB 10.3.22](../../../community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10322-release-notes.md), and [MariaDB 10.2.31](../../../community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10231-release-notes.md)
* TLS/SSL: when the client doesn't procide a CA file and the option ssl\_verify\_server\_cert was set, the peer cerificate will be validated against the system CA.
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2020-2574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2574)

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-31-changelogs/mariadb-connector-c-317-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
