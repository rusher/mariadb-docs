# MariaDB Connector/J 2.2.6 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/2.2.6/)[Release Notes](mariadb-connector-j-226-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-22-changelogs/mariadb-connector-j-226-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 19 Jul 2018

MariaDB Connector/J 2.2.6 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Minor change:

* \[[CONJ-623](https://jira.mariadb.org/browse/CONJ-623)] Increase connection logging when Primary node connection fails
* \[[CONJ-384](https://jira.mariadb.org/browse/CONJ-384)] Permit knowing affected rows number, not only real changed rows

## Bug correction:

* \[[CONJ-624](https://jira.mariadb.org/browse/CONJ-624)] MariaDbPoolDataSource possible NPE on configuration getter
* \[[CONJ-622](https://jira.mariadb.org/browse/CONJ-622)] The option "connectTimeout" must take in account DriverManager.getLoginTimeout() when set
* \[[CONJ-621](https://jira.mariadb.org/browse/CONJ-621)] wrong escaping when having curly bracket in table/field name
* \[[CONJ-618](https://jira.mariadb.org/browse/CONJ-618)] Client preparestatement parsing error on escaped ' / " in query

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
