# MariaDB Connector/J 2.7.0 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-j-270-release-notes.md)[Changelog](../changelogs/2.7/mariadb-connector-j-270-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 25 Sep 2020

MariaDB Connector/J 2.7.0 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**NOTE:** MariaDB Connector/J 2.7.0 is fully compatible with the latest release of\
version 2.6. Further maintenance releases will not be provided for version 2.6.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Notable Changes

* [CONJ-810](https://jira.mariadb.org/browse/CONJ-810) normalization of resultset getDate/getTime of timestamp field.
* [CONJ-812](https://jira.mariadb.org/browse/CONJ-812) DatabaseMetadata.getBestRowIdentifier and getMaxProcedureNameLength correction
* [CONJ-816](https://jira.mariadb.org/browse/CONJ-816) Table with primary key with DEFAULT function can be inserted for 10.5 servers
* [CONJ-820](https://jira.mariadb.org/browse/CONJ-820) MySQLPreparedStatement.setObject can now handle java.lang.Character type
* [CONJ-828](https://jira.mariadb.org/browse/CONJ-828) new option `ensureSocketState` to ensure protocol state
* [CONJ-829](https://jira.mariadb.org/browse/CONJ-829) Option to cache callablestatement is now disabled by default
* [CONJ-814](https://jira.mariadb.org/browse/CONJ-814) Small possible improvement of getCrossReference, getExportedKeys and getImportedKey
* [CONJ-825](https://jira.mariadb.org/browse/CONJ-825) XAResource.isSameRM implementation

## Bugs Fixed

* [CONJ-805](https://jira.mariadb.org/browse/CONJ-805) maxFieldSize string truncation occurs on bytes length, not character length
* [CONJ-807](https://jira.mariadb.org/browse/CONJ-807) Correcting possible Get Access Denied error if using multiple classloader
* [CONJ-813](https://jira.mariadb.org/browse/CONJ-813) setConfiguration not being called on classes that extend ConfigurableSocketFactory
* [CONJ-817](https://jira.mariadb.org/browse/CONJ-817) Switched position of REMARKS and PROCEDURE\_TYPE in the getProcedures result
* [CONJ-830](https://jira.mariadb.org/browse/CONJ-830) connector now throw a better error if SSL is mandatory and server doesn't support SSL

## Changelog

For a complete list of changes made in MariaDB Connector/J 2.7.0, with links to detailed\
information on each push, see the [changelog](../changelogs/2.7/mariadb-connector-j-270-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
