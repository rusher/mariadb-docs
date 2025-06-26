# MariaDB Connector/J 3.0.9 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-j-3-0-9-release-notes.md)[Changelog](../changelogs/mariadb-connectorj-30-changelogs/mariadb-connector-j-3-0-9-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 08 Nov 2022

MariaDB Connector/J 3.0.9 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

### Notable Changes

* merge from 2.7.7 : [CONJ-1016](https://jira.mariadb.org/browse/CONJ-1016) avoid splitting BULK command into multiple commands in case of prepareStatement.setNull() use

### Bugs Fixed

* merge from 2.7.7 : [CONJ-1021](https://jira.mariadb.org/browse/CONJ-1021) GSSAPI authentication might result in connection reset
* merge from 2.7.7 : [CONJ-1019](https://jira.mariadb.org/browse/CONJ-1019) DatabaseMetaData.getImportedKeys should return real value for PK\_NAME column
* [CONJ-1012](https://jira.mariadb.org/browse/CONJ-1012) stored procedure register output parameter as null if set before registerOutParameter command
* [CONJ-1017](https://jira.mariadb.org/browse/CONJ-1017) Calendar possible race condition, cause wrong timestamp setting

## Changelog

For a complete list of changes made in MariaDB Connector/J 3.0.9, with links to detailed\
information on each push, see the [changelog](../changelogs/mariadb-connectorj-30-changelogs/mariadb-connector-j-3-0-9-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
