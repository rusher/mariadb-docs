# Connector/J 1.5.7 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.5.7/)[Release Notes](mariadb-connector-j-157-release-notes.md)[Changelog](../changelogs/1.5/mariadb-connector-j-157-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 13 Jan 2017

MariaDB Connector/J 1.5.7 is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

## Notable Changes

This version is a bug-fix release.

### Bugfix

* [CONJ-407](https://jira.mariadb.org/browse/CONJ-407) : handling failover when packet > max\_allowed\_packet reset the connection state.
* [CONJ-403](https://jira.mariadb.org/browse/CONJ-403) : possible NPE on ResultSet.close() correction
* [CONJ-405](https://jira.mariadb.org/browse/CONJ-405) : Calendar instance not cleared before being used in ResultSet.getTimestamp

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
