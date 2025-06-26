# MariaDB Connector/J 3.0.1 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-j-301-release-notes.md)[Changelog](../changelogs/mariadb-connectorj-30-changelogs/mariadb-connector-j-301-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 11 Aug 2021

MariaDB Connector/J 3.0.1 is a [_**Beta**_](../../../mariadb-release-criteria.md) _**(Beta)**_ release.

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

**NOTE:** MariaDB Connector/J 3.0.1 is fully compatible with the latest release\
of version 2.7. Further maintenance releases will not be provided for version\
2.7 after MariaDB Connector/J 3.0 becomes stable (GA).

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Notable Changes

See [mariadb-connector-j-300-release-notes.md](mariadb-connector-j-300-release-notes.md) for 3.0 release.\
with the following fixes :

## Bugs Fixed

* [CONJ-879](https://jira.mariadb.org/browse/CONJ-879) Provide JPMS module descriptor
* [CONJ-880](https://jira.mariadb.org/browse/CONJ-880) metadata query performance correction
* [CONJ-884](https://jira.mariadb.org/browse/CONJ-884) MariaDbPoolDataSource leaks connections when the mariadb server restarts
* [CONJ-885](https://jira.mariadb.org/browse/CONJ-885) org.mariadb.jdbc.internal.util.pool.Pool swallows SQLException during addConnection
* [CONJ-891](https://jira.mariadb.org/browse/CONJ-891) getImportedKeys with null catalog restrict result to current database
* [CONJ-894](https://jira.mariadb.org/browse/CONJ-894) Adding useMysqlMetadata for 2.7 compatibility

## Changelog

For a complete list of changes made in MariaDB Connector/J 3.0.1, with links to detailed\
information on each push, see the [changelog](../changelogs/mariadb-connectorj-30-changelogs/mariadb-connector-j-301-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
