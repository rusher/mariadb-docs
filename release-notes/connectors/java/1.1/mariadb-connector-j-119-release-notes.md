# MariaDB Connector/J 1.1.9 Release notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../3.5/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.1.9/)[Release Notes](mariadb-connector-j-119-release-notes.md)[Changelog](../changelogs/1.1/mariadb-connector-j-119-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-the-mariadb-connector-j/README.md)

**Release date:** 18 Jun 2015

MariaDB Connector/J 1.1.9 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release. In general this means that there are no known serious bugs,\
except for those marked as feature requests, that no bugs were fixed\
since last release that caused notable code changes, and that we\
believe the code is ready for general usage (based on bug inflow).

**For a description of the MariaDB Connector/J see the**[**About the MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-the-mariadb-connector-j/README.md) **page.**

For a list of all changes made in this release, with links to detailed\
information on each push, see the[changelog](../changelogs/1.1/mariadb-connector-j-119-changelog.md).

## Bugs fixed in this release

* [CONJ-158](https://jira.mariadb.org/browse/CONJ-158) : Tests fail with max\_allowed packets = 16M
* [CONJ-157](https://jira.mariadb.org/browse/CONJ-157) : Batch statements rewrite has broken the hibernate functionality
* [CONJ-156](https://jira.mariadb.org/browse/CONJ-156) : SecurityManager being used incorrectly
* [CONJ-155](https://jira.mariadb.org/browse/CONJ-155) : Can't insert semicolons with rewriteBatchedStatements=true
* [CONJ-153](https://jira.mariadb.org/browse/CONJ-153) : Add ability to run tests against another mariadb server than localhost
* [CONJ-152](https://jira.mariadb.org/browse/CONJ-152) : Exception when on a second empty executeBatch on a prepareStatement with rewriteBatchedStatements=true
* [CONJ-151](https://jira.mariadb.org/browse/CONJ-151) : performance degraded after upgrading from 1.1.7 to 1.1.8
* [CONJ-150](https://jira.mariadb.org/browse/CONJ-150) : Parsing of JDBC urls doesn't work correctly
* [CONJ-149](https://jira.mariadb.org/browse/CONJ-149) : ResultSetMetaData.getTableName returns table alias instead of real table name
* [CONJ-142](https://jira.mariadb.org/browse/CONJ-142) : Using a semicolon in a string with "rewriteBatchedStatements=true" fails

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
