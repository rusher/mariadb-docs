# MariaDB Connector/J 1.5.7 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.5.7/)[Release Notes](mariadb-connector-j-157-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-15-changelogs/mariadb-connector-j-157-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 13 Jan 2017

MariaDB Connector/J 1.5.7 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

## Notable Changes

This version is a bug-fix release.

### Bugfix

* [CONJ-407](https://jira.mariadb.org/browse/CONJ-407) : handling failover when packet > max\_allowed\_packet reset the connection state.
* [CONJ-403](https://jira.mariadb.org/browse/CONJ-403) : possible NPE on ResultSet.close() correction
* [CONJ-405](https://jira.mariadb.org/browse/CONJ-405) : Calendar instance not cleared before being used in ResultSet.getTimestamp

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
