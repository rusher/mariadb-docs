# MariaDB Connector/J 2.7.1 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../3.5/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-j-271-release-notes.md)[Changelog](../changelogs/2.7/mariadb-connector-j-271-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 23 Nov 2020

MariaDB Connector/J 2.7.1 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Notable changes

* [CONJ-842](https://jira.mariadb.org/browse/CONJ-842) Byte array parameters are now sent as long data

## Bugs Fixed

* [CONJ-834](https://jira.mariadb.org/browse/CONJ-834) use of BULK batch is conditioned by capability, not checking server version
* [CONJ-835](https://jira.mariadb.org/browse/CONJ-835) GSS Imports set in OSGI Bundle
* [CONJ-839](https://jira.mariadb.org/browse/CONJ-839) Wrong exception message when rewriteBatchedStatements is enabled
* [CONJ-841](https://jira.mariadb.org/browse/CONJ-841) ResultSetMetaData::getColumnTypeName() returns incorrect type name for LONGTEXT
* [CONJ-837](https://jira.mariadb.org/browse/CONJ-837) prepared statement cache leak on ResultSet CONCUR\_UPDATABLE concurrency
* [CONJ-843](https://jira.mariadb.org/browse/CONJ-843) ParameterMetaData::getParameterType for CallableStatement parameter return expected "BINARY" value for BINARY type

### Minor

* [CONJ-845](https://jira.mariadb.org/browse/CONJ-845) test suite now test SkySQL with replication setting
* [CONJ-838](https://jira.mariadb.org/browse/CONJ-838) have a 'replica' alias for 'slave' connection option

## Changelog

For a complete list of changes made in MariaDB Connector/J 2.7.1, with links to detailed\
information on each push, see the [changelog](../changelogs/2.7/mariadb-connector-j-271-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
