# MariaDB Java Client 1.1.7 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../3.5/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/client-java/1.1.7/) |**Release Notes** |[Changelog](../changelogs/1.1/mariadb-java-client-117-changelog.md) |[Java Client Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-the-mariadb-java-client/README.md)

**Release date:** 03 Apr 2014

MariaDB Java Client 1.1.7 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release. In general this means that there are no known serious bugs,\
except for those marked as feature requests, that no bugs were fixed\
since last release that caused notable code changes, and that we\
believe the code is ready for general usage (based on bug inflow).

**For a description of the MariaDB Java Client see the**[**About the MariaDB Java Client**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-the-mariadb-java-client/README.md) **page.**

For a list of all changes made in this release, with links to detailed\
information on each push, see the[changelog](../changelogs/1.1/mariadb-java-client-117-changelog.md).

## New functionality

* Support for LOAD DATA LOCAL INFILE
* new MySQLStatement methods: `unwrap()` and `isWrapperFor()`

## Bugs fixed in this release

Some of the bugs fixed include:

* Fixed "unknown command" error when running with Galera cluster
* Fixed `findColumn()` which returns now the correct number if a select list\
  contains the same column name more than once. ([CONJ-84](https://jira.mariadb.org/browse/CONJ-84))
* Fixed "MySQL Protocol limit reached" error when sending data > 2GB

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
