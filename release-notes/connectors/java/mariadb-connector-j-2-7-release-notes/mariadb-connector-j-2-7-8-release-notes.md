# MariaDB Connector/J 2.7.8 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://mariadb.com/downloads/connectors)[Release Notes](mariadb-connector-j-2-7-8-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-27-changelogs/mariadb-connector-j-2-7-8-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 24 Jan 2023

MariaDB Connector/J 2.7.8 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Bugs Fixed

* [CONJ-1039](https://jira.mariadb.org/browse/CONJ-1039) setQueryTimeout on CallableStatement now use server timeout when possible, permitting respecting timeout when store procedure DEFINER differ from connected user
* [CONJ-1041](https://jira.mariadb.org/browse/CONJ-1041) possible ArrayIndexOutOfBoundsException when writing a String to socket prebuffer when pre-buffer is exactly 16M
* [CONJ-1023](https://jira.mariadb.org/browse/CONJ-1023) set missing SSL capability in handshake after SSL exchanges

## Changelog

For a complete list of changes made in MariaDB Connector/J 2.7.8, with links to detailed\
information on each push, see the [changelog](../changelogs/mariadb-connector-j-27-changelogs/mariadb-connector-j-2-7-8-changelog.md).
