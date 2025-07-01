# MariaDB Connector/J 1.6.2 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.6.2/)[Release Notes](mariadb-connector-j-162-release-notes.md)[Changelog](../changelogs/1.6/mariadb-connector-j-162-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 27 Jun 2017

MariaDB Connector/J 1.6.2 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release compatible with java 6 and java 7.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

### Bug

* \[[CONJ-473](https://jira.mariadb.org/browse/CONJ-473)] when useServerPrepStmts is not set, the PREPARE statement must not be cached.
* \[[CONJ-494](https://jira.mariadb.org/browse/CONJ-494)] Handle PrepareStatement.getParameterMetaData() if query cannot be PREPAREd
* \[[CONJ-497](https://jira.mariadb.org/browse/CONJ-497)] escape string correction for big query

### Task

* \[[CONJ-498](https://jira.mariadb.org/browse/CONJ-498)] add java 6 compatibility

This task adds Java 6 compatibility to the MariaDB Connector/J 1.6 release which therefore now replaces MariaDB Connector/J 1.1 (last version 1.1.10).\
MariaDB Connector/J 1.6.x version is now the maintenance version for Java 6 and Java 7.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
