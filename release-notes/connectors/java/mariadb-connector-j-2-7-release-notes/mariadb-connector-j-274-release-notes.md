# MariaDB Connector/J 2.7.4 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-j-274-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-27-changelogs/mariadb-connector-j-274-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 11 Aug 2021

MariaDB Connector/J 2.7.4 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Bugs Fixed

* [CONJ-890](https://jira.mariadb.org/browse/CONJ-890) getImportedKeys/getTables regression returning an empty resultset for null/empty catalog
* [CONJ-863](https://jira.mariadb.org/browse/CONJ-863) Ensure socket state when SocketTimeout occurs
* [CONJ-873](https://jira.mariadb.org/browse/CONJ-873) IndexOutOfBoundsException when executing prepared queries using automatic key generation in parallel
* [CONJ-884](https://jira.mariadb.org/browse/CONJ-884) MariaDbPoolDataSource leaks connections when the mariadb server restarts
* [CONJ-893](https://jira.mariadb.org/browse/CONJ-893) DatabaseMetaData.getColumns regression causing TINYINT(x) with x > 1 to return BIT type in place of TINYINT
* [CONJ-889](https://jira.mariadb.org/browse/CONJ-889) CallableStatement using function throw wrong error on getter

## Changelog

For a complete list of changes made in MariaDB Connector/J 2.7.4, with links to detailed\
information on each push, see the [changelog](../changelogs/mariadb-connector-j-27-changelogs/mariadb-connector-j-274-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
