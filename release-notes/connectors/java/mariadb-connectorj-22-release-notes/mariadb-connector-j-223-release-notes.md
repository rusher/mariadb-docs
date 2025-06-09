# MariaDB Connector/J 2.2.3 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/2.2.3/)[Release Notes](mariadb-connector-j-223-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-22-changelogs/mariadb-connector-j-223-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 14 Mar 2018

MariaDB Connector/J 2.2.3 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Bug Fixes

* \[[CONJ-583](https://jira.mariadb.org/browse/CONJ-583)] possible hang indefinitely using master/slave configuration and failover occurs
* \[[CONJ-586](https://jira.mariadb.org/browse/CONJ-586)] erroneous transaction state when first command result as an error
* \[[CONJ-587](https://jira.mariadb.org/browse/CONJ-587)] using allowMasterDownConnection option can lead to NPE when using setReadOnly()
* \[[CONJ-588](https://jira.mariadb.org/browse/CONJ-588)] using option 'allowMasterDownConnection' won't permit to connect if all master are down
* \[[CONJ-534](https://jira.mariadb.org/browse/CONJ-534)] Connection.isValid() must be routed to Master and Slave connections to avoid any server timeout

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
