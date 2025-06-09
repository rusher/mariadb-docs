# MariaDB Connector/J 2.7.5 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://mariadb.com/downloads/connectors)[Release Notes](mariadb-connector-j-275-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-27-changelogs/mariadb-connector-j-275-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 19 Jan 2022

MariaDB Connector/J 2.7.5 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Notable Change

* [CONJ-897](https://jira.mariadb.org/browse/CONJ-897) The connection id has been added to important log messages for easier correlation of these log messages with MariaDB Server logs
* [CONJ-914](https://jira.mariadb.org/browse/CONJ-914) The connect does not enable session\_track\_schema anymore when connecting to the server, as this is the server default already

## Bugs Fixed

* [CONJ-914](https://jira.mariadb.org/browse/CONJ-914) Error message “\[1036] Unknown variable: session\_track\_schema” when MariaDB Connector/J connects to MariaDB Xpand
* [CONJ-896](https://jira.mariadb.org/browse/CONJ-896) Connection Pools do not validate other connections before use when the socket fails
* [CONJ-895](https://jira.mariadb.org/browse/CONJ-895) Options `useBatchMultiSend` and `usePipelineAuth` are disabled without reason for RDS

## Changelog

For a complete list of changes made in MariaDB Connector/J 2.7.5, with links to detailed\
information on each push, see the [changelog](../changelogs/mariadb-connector-j-27-changelogs/mariadb-connector-j-275-changelog.md).
