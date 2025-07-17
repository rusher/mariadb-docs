# Connector/J 1.6.4 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.6.4/)[Release Notes](mariadb-connector-j-164-release-notes.md)[Changelog](../changelogs/1.6/mariadb-connector-j-164-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 6 Sep 2017

MariaDB Connector/J 1.6.4 is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_\
release compatible with java 6, 7, 8.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

### Bug

* \[[CONJ-517](https://jira.mariadb.org/browse/CONJ-517)] Result-set identification of OK\_Packet with 0xFE header when using option useCompression
* \[[CONJ-514](https://jira.mariadb.org/browse/CONJ-514)] ResultSet method wasNull() always return true after a call on a "null-date" field binary protocol handling
* \[[CONJ-515](https://jira.mariadb.org/browse/CONJ-515)] Improve MariaDB driver stability in case JNA errors

### misc :

* correct typo in error message when setting wrong parameter
* handling connection error when no database is provided
* correcting possible race condition when using Statement/PrepareStatement in multi-thread with fetch size set

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
