# MariaDB Connector/J 1.4.6 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.4.6/)[Release Notes](mariadb-connector-j-146-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-14-changelogs/mariadb-connector-j-146-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 15 Jun 2016

MariaDB Connector/J 1.4.6 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For a description of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

## Notable Changes

This version is a bugfix release.

### Corrections

* \[[CONJ-293](https://jira.mariadb.org/browse/CONJ-293)] Permit named pipe connection without host in connection string
* \[[CONJ-309](https://jira.mariadb.org/browse/CONJ-309)] Possible NPE on aurora when failover occur during connection initialisation
* \[[CONJ-312](https://jira.mariadb.org/browse/CONJ-312)] NPE while loading a null from TIMESTAMP field using binary protocol
* \[misc] batch with one parameter correction (using rewriteBatchedStatements option)

## Changelog

For a list of all changes made in this release, with links to detailed\
information on each push, see the[changelog](../changelogs/mariadb-connector-j-14-changelogs/mariadb-connector-j-146-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
