# MariaDB Connector/J 3.0.7 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../3.5/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-j-307-release-notes.md)[Changelog](../changelogs/3.0/mariadb-connector-j-307-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 4 Aug 2022

MariaDB Connector/J 3.0.7 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

### Bugs Fixed

* [CONJ-993](https://jira.mariadb.org/browse/CONJ-993) SQLDataException reading DATA\_TYPE on DatabaseMetaData.getTypeInfo() after 3.0.4
* [CONJ-986](https://jira.mariadb.org/browse/CONJ-986) Permit specific Statement.setLocalInfileInputStream for compatibility
* [CONJ-987](https://jira.mariadb.org/browse/CONJ-987) Version 3.0.0 returns String for VARBINARY instead of byte\[] as 2.7.6 did
* [CONJ-989](https://jira.mariadb.org/browse/CONJ-989) Binary column read as String
* [CONJ-990](https://jira.mariadb.org/browse/CONJ-990) Setting timezone=UTC result in SQLSyntaxErrorException
* [CONJ-991](https://jira.mariadb.org/browse/CONJ-991) Regression: binary(16) is returned as String by getObject()
* [CONJ-994](https://jira.mariadb.org/browse/CONJ-994) Version 3.x rejects previously accepted boolean string parameter for BOOLEAN field

## Changelog

For a complete list of changes made in MariaDB Connector/J 3.0.7, with links to detailed\
information on each push, see the [changelog](../changelogs/3.0/mariadb-connector-j-307-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
