# Connector/C 2.2.1 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-c/2.2.1)[Release Notes](mariadb-connector-c-221-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-22-changelogs/mariadb-connector-c-221-changelog.md)[About of MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 18 Nov 2015

This is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of the MariaDB\
Connector/C, formerly known as MariaDB Client Library for C. In general,\
marking this release as _stable_ means that there are no known serious bugs,\
except for those marked as feature requests, that no bugs were fixed since last\
release that caused a notable code changes, and that we believe the code is\
ready for general usage (based on bug inflow).

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## New features

* [CONC-147](https://jira.mariadb.org/browse/CONC-147): Allow client to bind to a specific network address:\
  On clients with multiple possible TCP routes to a server, it's now possible to bind the\
  client to a specific address.This can be done either via mysql\_options(mysql, MYSQL\_OPT\_BIND, bind\_address) or by an entry "[bind-address=your\_bind\_address](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#bind_address)" in the configuration file.

## Bug fixes

* [CONC-150](https://jira.mariadb.org/browse/CONC-150): Source package doesn't contain mariadb\_config.c.in
* Add version information for executables, dynamic and static libraries (Windows only)
* Digitally sign executables and dynamic link libraries (Windows only)
* Fixed build errors for Microsoft Visuall Studio 2015
* Fix for mariadb\_convert\_string - charset names for utf16 and utf32 are changed so iconv understands it. Also if endianness is not specified, BE charsets used by default, to avoid BOMs

## Changelog

For a list of changes made in this release, with links to detailed\
information on each push, see the [changelog](../changelogs/mariadb-connector-c-22-changelogs/mariadb-connector-c-221-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
