# MariaDB Connector/J 3.1.3 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/java8-connector)[Release Notes](mariadb-connector-j-3-1-3-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-3-1-changelogs/mariadb-connector-j-3-1-3-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 22 Mar 2023

MariaDB Connector/J 3.1.3 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Bug fixed

* [CONJ-1054](https://jira.mariadb.org/browse/CONJ-1054) Threadsafety issue when using CredentialPlugin in v3.x
* [CONJ-1056](https://jira.mariadb.org/browse/CONJ-1056) JDBC connector reads incorrect data from unix socket when reading packet size > 32K
* [CONJ-1057](https://jira.mariadb.org/browse/CONJ-1057) Wrong decoding of binary time with value "00:00:00"
* [CONJ-1058](https://jira.mariadb.org/browse/CONJ-1058) JDBC 4.3 org.mariadb.jdbc.Statement enquote\* methods implementation. thanks to @peterhalicky
* [CONJ-1060](https://jira.mariadb.org/browse/CONJ-1060) BIT default metadata doesn't take care of transformedBitIsBoolean option
* report 2.7.9 bug fixes :
  * [CONJ-1062](https://jira.mariadb.org/browse/CONJ-1062) correcting TlsSocketPlugin to use Driver classloader
  * [CONJ-1063](https://jira.mariadb.org/browse/CONJ-1063) DatabaseMetaData.getTypeInfo() returns wrong value for UNSIGNED\_ATTRIBUTE

## Changelog

For a complete list of changes made in MariaDB Connector/J 3.1.3, with links to detailed\
information on each push, see the [changelog](../changelogs/mariadb-connector-j-3-1-changelogs/mariadb-connector-j-3-1-3-changelog.md).

{% @marketo/form formid="4316" formId="4316" %}
