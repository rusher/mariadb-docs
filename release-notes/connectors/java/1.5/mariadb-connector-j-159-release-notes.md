# MariaDB Connector/J 1.5.9 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../3.5/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.5.9/)[Release Notes](mariadb-connector-j-159-release-notes.md)[Changelog](../changelogs/1.5/mariadb-connector-j-159-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 20 Mar 2017

MariaDB Connector/J 1.5.9 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

## Notable Changes

This version is a bug-fix release.

### Bugfix

* [CONJ-423](https://jira.mariadb.org/browse/CONJ-423) : Permit having the MySQL driver and MariaDB driver in the same classpath
* [CONJ-431](https://jira.mariadb.org/browse/CONJ-431) : multi-values queries return only one generated key
* [CONJ-437](https://jira.mariadb.org/browse/CONJ-437) : ResultSet.getString on field with ZEROFILL doesn't have the '0' leading char when using binary protocol
* [CONJ-435](https://jira.mariadb.org/browse/CONJ-435) : avoid "All pipe instances are busy" exception on multiple connections to the same named pipe
* [CONJ-446](https://jira.mariadb.org/browse/CONJ-446) : ResultSet first() throws an exception for scroll type if `TYPE_FORWARD_ONLY`, only when streaming
* [CONJ-440](https://jira.mariadb.org/browse/CONJ-440) : handle very big blob (1Gb)
* [CONJ-434](https://jira.mariadb.org/browse/CONJ-434) : 1.5.8 regression : ResultSet returns duplicate entries when using fetchsize
* [CONJ-429](https://jira.mariadb.org/browse/CONJ-429) : ResultSet.getDouble/getFloat may throw a `NumberFormatException`
* [CONJ-438](https://jira.mariadb.org/browse/CONJ-438) : using option `rewriteBatchedStatements` permits rewrite when a query has a column/table that contains the 'select' keyword

### Password encoding.

[CONJ-212](https://jira.mariadb.org/browse/CONJ-212) : Implement password encoding charset option to permit connecting using a password created with a connection that had a different charset

| passwordCharacterEncoding |
| ------------------------- |
| passwordCharacterEncoding |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
