# MariaDB Connector/J 2.2.1 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/2.2.1/)[Release Notes](mariadb-connector-j-221-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-22-changelogs/mariadb-connector-j-221-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 22 Dec 2017

MariaDB Connector/J 2.2.1 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

* \[[CONJ-501](https://jira.mariadb.org/browse/CONJ-501)] provide support for authentication plugin ed25519

## Bug Fixes

* \[[CONJ-529](https://jira.mariadb.org/browse/CONJ-529)] on failover, the driver will pause for 250ms if no servers are available before attempting to loop reconnection
* \[[CONJ-548](https://jira.mariadb.org/browse/CONJ-548)] COM\_STMT\_BULK\_EXECUTE not used for INSERT ... SELECT statements
* \[[CONJ-549](https://jira.mariadb.org/browse/CONJ-549)] correction on connection reset when using MariaDbPoolDataSource with options useServerPrepStmts and useResetConnection enabled
* \[[CONJ-555](https://jira.mariadb.org/browse/CONJ-555)] failover caused by client timeout must not reuse connection
* \[[CONJ-558](https://jira.mariadb.org/browse/CONJ-558)] removing extra ".0" to resultset.getString() value for FLOAT/DOUBLE fields
* \[[CONJ-550](https://jira.mariadb.org/browse/CONJ-550)] fetching state correction when reusing statement without having read all results
* \[[CONJ-553](https://jira.mariadb.org/browse/CONJ-553)] RejectedExecutionException was thrown when having large amount of concurrent batches

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
