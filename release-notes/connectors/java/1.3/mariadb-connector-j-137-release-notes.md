# Connector/J 1.3.7 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.3.7/)[Release Notes](mariadb-connector-j-137-release-notes.md)[Changelog](../changelogs/1.3/mariadb-connector-j-137-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 23 Mar 2016

MariaDB Connector/J 1.3.7 is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_\
release.

**For a description of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

For a list of all changes made in this release, with links to detailed\
information on each push, see the [changelog](../changelogs/1.3/mariadb-connector-j-137-changelog.md).

This version is a bugfix / performance improvement release.

## Notable changes and additions

### Major

* [CONJ-259](https://jira.mariadb.org/browse/CONJ-259) : Server prepare statement failover uses the associated connection
* Performance improvements :
  * using directly the query.getByte("UTF-8") array to avoid recreating a new array
  * rewriteStatement improvement (parsing query to verfy that query can be rewritten + performance) [CONJ-262](https://jira.mariadb.org/browse/CONJ-262)
  * Local file upload correction when using useCompression option

### Minor

* [CONJ-267](https://jira.mariadb.org/browse/CONJ-267) : getString on '0000-00-00' date was returning npe.
* PrepareStatement [setObject(int parameterIndex, Object x, int targetSqlType, int scaleOrLength)](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html#setObject\(int,%20java.lang.Object,%20int,%20int\)) now doesn't lose decimal when using Float or Double object

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
