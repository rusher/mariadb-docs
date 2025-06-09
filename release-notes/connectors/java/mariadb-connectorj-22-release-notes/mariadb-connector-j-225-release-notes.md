# MariaDB Connector/J 2.2.5 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/2.2.5/)[Release Notes](mariadb-connector-j-225-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-22-changelogs/mariadb-connector-j-225-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 30 May 2018

MariaDB Connector/J 2.2.5 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

## Minor change:

* \[[CONJ-602](https://jira.mariadb.org/browse/CONJ-602)] Add server hostname to connection packet for proxy
* \[[CONJ-604](https://jira.mariadb.org/browse/CONJ-604)] handle support for mysql 8.0 tx\_isolation replacement by transaction\_isolation
* \[[CONJ-595](https://jira.mariadb.org/browse/CONJ-595)] Create option to configure DONOR/DESYNCED Galera nodes to be unavailable for load-balancing : Usually, Connection.isValid just send an empty packet to the server, and server sends a small response to ensure connectivity. When a new option "useBulkStmts" option is set, the connector will ensure galera server state ("wsrep\_local\_state" correspond to allowed values (4 = sync mode). see [galera state](https://galeracluster.com/library/documentation/node-states.html#node-state-changes) to now more.

## Bug correction:

* \[[CONJ-613](https://jira.mariadb.org/browse/CONJ-613)] Connection using "replication" Parameters fail when no slave is available
* \[[CONJ-605](https://jira.mariadb.org/browse/CONJ-605)] Newlines where breaking calling stored procedures
* \[[CONJ-609](https://jira.mariadb.org/browse/CONJ-609)] Using getDate with function DATE\_ADD() with parameter using string format where return wrong result using the binary protocol
* \[[CONJ-610](https://jira.mariadb.org/browse/CONJ-610)] Option "allowMasterDownConnection" improvement on connection validation and Exceptions on master down

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
