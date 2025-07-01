# MariaDB Connector/J 1.3.2 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../3.5/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.3.2/)[Release Notes](mariadb-connector-j-132-release-notes.md)[Changelog](../changelogs/1.3/mariadb-connector-j-132-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 23 Nov 2015

MariaDB Connector/J 1.3.2 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For a description of the MariaDB Connector/J see the**[**About the MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-the-mariadb-connector-j/README.md) **page.**

For a list of all changes made in this release, with links to detailed\
information on each push, see the[changelog](../changelogs/1.3/mariadb-connector-j-132-changelog.md).

This version is a bugfix release

#### Notable changes and additions

* [CONJ-221](https://jira.mariadb.org/browse/CONJ-221): preparedStatement : Error when using statement setObject(int, object, sqlType) with object with Long type and sql type Types.BIGINT
* [CONJ-219](https://jira.mariadb.org/browse/CONJ-219): Correcting Datasource parameter handling.
* [CONJ-222](https://jira.mariadb.org/browse/CONJ-222): INSERT ... SELECT are now not rewritten when option rewriteBatchedStatements is set.
* [CONJ-223](https://jira.mariadb.org/browse/CONJ-223): MetaData.getParameterCount() on prepareStatement now return correct result.
* [CONJ-220](https://jira.mariadb.org/browse/CONJ-220): prepareStatement : setCharacterStream and setBlob possible IndexOutOfBoundsException depending on stream length.
* Code cleaned to avoid connection leak

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
