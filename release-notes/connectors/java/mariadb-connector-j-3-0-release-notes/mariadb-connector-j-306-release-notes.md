# MariaDB Connector/J 3.0.6 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-j-306-release-notes.md)[Changelog](../changelogs/mariadb-connectorj-30-changelogs/mariadb-connector-j-306-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 29 Jun 2022

MariaDB Connector/J 3.0.6 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

### Notable Changes

* `[CONJ-984](https://jira.mariadb.org/browse/CONJ-984)` Permit executing initial command with new option `initSql`
* `[CONJ-976](https://jira.mariadb.org/browse/CONJ-976)` Improve use of pipelining when allowLocalInfile is enabled

### Bugs Fixed

* `[CONJ-985](https://jira.mariadb.org/browse/CONJ-985)` ResultSet.getObject() returns ByteSet instead of Byte\[] for BIT
* `[CONJ-953](https://jira.mariadb.org/browse/CONJ-953)` PreparedStatement.getGeneratedKeys() returns rows when no keys are generated in insert
* `[CONJ-975](https://jira.mariadb.org/browse/CONJ-975)` ArrayIndexOutOfBoundsException when attempt to getTime() from ResultSet
* `[CONJ-979](https://jira.mariadb.org/browse/CONJ-979)` ResultSet.getObject() returns Byte instead of Boolean for tinyint(1)
* `[CONJ-980](https://jira.mariadb.org/browse/CONJ-980)` Permit setObject with java.util.Date parameter

## Changelog

For a complete list of changes made in MariaDB Connector/J 3.0.6, with links to detailed\
information on each push, see the [changelog](../changelogs/mariadb-connectorj-30-changelogs/mariadb-connector-j-306-changelog.md).
