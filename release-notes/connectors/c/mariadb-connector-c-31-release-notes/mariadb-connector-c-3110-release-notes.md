# Connector/C 3.1.10 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-c-3110-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-31-changelogs/mariadb-connector-c-3110-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 17 September 2020

This is a [_**Stable (GA)**_](../../../community-server/about/release-criteria.md) release of the MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Notable Changes

* [CONC-500](https://jira.mariadb.org/browse/CONC-500): Fixed error when loading intermediate chained certificates
* [MDEV-18818](https://jira.mariadb.org/browse/MDEV-18818): Fixed wrong zlib in mariadb\_config when building inside server package
* [CONC-498](https://jira.mariadb.org/browse/CONC-498): MYSQL\_UNIX\_ADDR and MYSQL\_PORT are now defined
* Added new build option WIITH\_ICONV=ON/OFF. When set to OFF (default) API function mariadb\_convert\_string will always return -1 and sets errorcode to ENOTSUP.
* mariadb\_config now tries to determine the path of execution or uses MARIADB\_CONFIG environment variable before falling back and using CMAKE\_INSTALL\_PREFIX for location of libraries and include files
* added --variables option for mariadb\_config. Supported values are pkgincludedir, pkglibdir and pkgplugindir.

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-31-changelogs/mariadb-connector-c-3110-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
