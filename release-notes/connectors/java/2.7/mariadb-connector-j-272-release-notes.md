# MariaDB Connector/J 2.7.2 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-j-272-release-notes.md)[Changelog](../changelogs/2.7/mariadb-connector-j-272-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 29 Jan. 2021

MariaDB Connector/J 2.7.2 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

## Bugs Fixed

* [CONJ-847](https://jira.mariadb.org/browse/CONJ-847) NPE at UpdatableResultSet#close
* [CONJ-849](https://jira.mariadb.org/browse/CONJ-849) driver now doesn't close connection caused java.io.NotSerializableException as a result of incorrect data bind to a prepared statement parameter
* [CONJ-850](https://jira.mariadb.org/browse/CONJ-850) MariaDbResultSetMetaData#getPrecision(int) now returns correct length for character data
* [CONJ-851](https://jira.mariadb.org/browse/CONJ-851) metadata getBestRowIdentifier incompatibility with MySQL 8 correction
* [CONJ-852](https://jira.mariadb.org/browse/CONJ-852) ON DUPLICATE KEY detection failed when using new line

## Changelog

For a complete list of changes made in MariaDB Connector/J 2.7.2, with links to detailed\
information on each push, see the [changelog](../changelogs/2.7/mariadb-connector-j-272-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
