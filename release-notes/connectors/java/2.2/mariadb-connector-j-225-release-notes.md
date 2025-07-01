# MariaDB Connector/J 2.2.5 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../3.5/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/2.2.5/)[Release Notes](mariadb-connector-j-225-release-notes.md)[Changelog](../changelogs/2.2/mariadb-connector-j-225-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

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

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
