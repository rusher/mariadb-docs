# MariaDB Connector/J 1.6.3 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.6.3/)[Release Notes](mariadb-connector-j-163-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-16-changelogs/mariadb-connector-j-163-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 31 July 2017

MariaDB Connector/J 1.6.3 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release compatible with java 6, 7, 8.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

### Bug

* \[[CONJ-502](https://jira.mariadb.org/browse/CONJ-502)] isolation leak when using multiple pools on same VM on failover
* \[[CONJ-503](https://jira.mariadb.org/browse/CONJ-503)] regression on aurora Connection Connection.isReadOnly()
* \[[CONJ-505](https://jira.mariadb.org/browse/CONJ-505)] correcting issue that ended throwing "Unknown prepared statement handler given to mysqld\_stmt\_execute"
* \[[CONJ-496](https://jira.mariadb.org/browse/CONJ-496)] return rounded numeric when querying on a decimal field in place of throwing an exception for compatibility

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
