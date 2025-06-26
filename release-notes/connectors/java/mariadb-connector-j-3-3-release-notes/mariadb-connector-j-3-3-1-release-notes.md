# MariaDB Connector/J 3.3.1 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/java8-connector)[Release Notes](mariadb-connector-j-3-3-1-release-notes.md)[Changelog](../changelogs/mariadb-connectorj-3-3-changelogs/mariadb-connector-j-3-3-1-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 29 Nov 2023

MariaDB Connector/J 3.3.1 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release, and will replace 3.2 as the maintenance releases.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Bugs Fixed

* [CONJ-1120](https://jira.mariadb.org/browse/CONJ-1120) java 8 compatibility error in 3.3.0
* [CONJ-1123](https://jira.mariadb.org/browse/CONJ-1123) missing OSGi javax.crypto dependency
* [CONJ-1124](https://jira.mariadb.org/browse/CONJ-1124) ensure not having OOM when setting huge fetch size
* [CONJ-1109](https://jira.mariadb.org/browse/CONJ-1109) Regression in clearBatch() for parameterized statements
* [CONJ-1126](https://jira.mariadb.org/browse/CONJ-1126) setting fetchSize directly on a ResultSet object does not reflect the expected change
* [CONJ-1127](https://jira.mariadb.org/browse/CONJ-1127) Statement.getResultSetType () failed to change the result set type
* [CONJ-1128](https://jira.mariadb.org/browse/CONJ-1128) Setting Negative Fetch Size on ResultSet Without Throwing Error

## Changelog

For a complete list of changes made in MariaDB Connector/J 3.3.1, with links to detailed\
information on each push, see the [changelog](../changelogs/mariadb-connectorj-3-3-changelogs/mariadb-connector-j-3-3-1-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
