# Connector/J 1.6.5 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.6.5/)[Release Notes](mariadb-connector-j-165-release-notes.md)[Changelog](../changelogs/1.6/mariadb-connector-j-165-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 26 Sep 2017

MariaDB Connector/J 1.6.5 is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_\
release compatible with java 6, 7, 8.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

### Bug

* \[[CONJ-525](https://jira.mariadb.org/browse/CONJ-525)] Batch result-set return array correction when DELETE statement when bulk option is used
* \[[CONJ-526](https://jira.mariadb.org/browse/CONJ-526)] better error message getting metadata information when SQL syntax is wrong
* \[[CONJ-527](https://jira.mariadb.org/browse/CONJ-527)] Resultset.last() return wrong value if resultset has only one result
* \[[CONJ-528](https://jira.mariadb.org/browse/CONJ-528)] Error executing LOAD DATA LOCAL INFILE when file is larger than max\_allowed\_packet

### Misc

* ensuring Connection.isValid(timeout) always respect timeout value

### misc :

* correct typo in error message when setting wrong parameter
* handling connection error when no database is provided
* correcting possible race condition when using Statement/PrepareStatement in multi-thread with fetch size set

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
