# MariaDB Connector/J 1.3.6 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.3.6/)[Release Notes](mariadb-connector-j-136-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-13-changelogs/mariadb-connector-j-136-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 29 Feb 2016

MariaDB Connector/J 1.3.6 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For a description of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

For a list of all changes made in this release, with links to detailed\
information on each push, see the[changelog](../changelogs/mariadb-connector-j-13-changelogs/mariadb-connector-j-136-changelog.md).

This version is a bugfix release.

## Notable changes and additions

### Major

* [CONJ-252](https://jira.mariadb.org/browse/CONJ-252) : Correction of charset parameter on Statement.setCharacterStream() and setClob
* [CONJ-253](https://jira.mariadb.org/browse/CONJ-253) : Protocol encoding correction for binary field
* [CONJ-254](https://jira.mariadb.org/browse/CONJ-254) : Correction of error in boolean when using scala anorm string interpolation

### Minor

* [CONJ-255](https://jira.mariadb.org/browse/CONJ-255) : getBoolean() improvement (for field not normally considered as boolean). TinyInt value >= 2 are now considered as true.
* [CONJ-257](https://jira.mariadb.org/browse/CONJ-257) : Server preparedStatement now used even for query without parameters.
* [CONJ-258](https://jira.mariadb.org/browse/CONJ-258) : multithreading correction on possible race condition on statement.close()

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
