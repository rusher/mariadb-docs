# MariaDB Connector/J 2.4.3 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-j-243-release-notes.md)[Changelog](../changelogs/mariadb-connectorj-24-changelogs/mariadb-connector-j-243-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 5 Aug 2019

MariaDB Connector/J 2.4.3 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Notes

New option `blankTableNameMeta` permit to have Resultset metadata getTableName methods always return blank in place of returning real table name as JDBC indicate. This is for ease migration from Oracle since Oracle driver always returns an empty string.

* [CONJ-717](https://jira.mariadb.org/browse/CONJ-717): conversion function support for other data types than default MariaDB conversion type
* [CONJ-722](https://jira.mariadb.org/browse/CONJ-722): Permit suppression of result-set metadata getTableName for oracle compatibility
* [CONJ-719](https://jira.mariadb.org/browse/CONJ-719): Saving values using Java 8 LocalTime does not store fractional parts of seconds
* [CONJ-716](https://jira.mariadb.org/browse/CONJ-716): Correcting possible NPE on non-thread safe NumberFormat (logging)

## Changelog

For a complete list of changes made in MariaDB Connector/J 2.4.3, with links to detailed\
information on each push, see the [changelog](../changelogs/mariadb-connectorj-24-changelogs/mariadb-connector-j-243-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
