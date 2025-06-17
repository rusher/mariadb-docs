# MariaDB Connector/J 1.7.3 Changelog

The most recent [_**Stable**_](../../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.7.3/)[Release Notes](../../mariadb-connectorj-17-release-notes/mariadb-connector-j-173-release-notes.md)[Changelog](mariadb-connector-j-173-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 9 Mar 2018

For the highlights of this release, see the[release notes](../../mariadb-connectorj-17-release-notes/mariadb-connector-j-173-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #6c6be83e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6c6be83e) - bump 1.7.3 version
* [Revision #da0da674](https://github.com/mariadb-corporation/mariadb-connector-j/commit/da0da674) - \[misc] checkstyle review correction
* [Revision #b3a368d0](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b3a368d0) - \[[CONJ-586](https://jira.mariadb.org/browse/CONJ-586)] test correction
* [Revision #6bd14426](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6bd14426) - \[[CONJ-534](https://jira.mariadb.org/browse/CONJ-534)] Connection.isValid() must be routed to Master and Slave connections to avoid any server timeout
* [Revision #aa2bf8b6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/aa2bf8b6) - \[[CONJ-586](https://jira.mariadb.org/browse/CONJ-586)] erronous transaction state when first command result as error
* [Revision #37222ea6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/37222ea6) - \[[CONJ-583](https://jira.mariadb.org/browse/CONJ-583)] when using option 'allowMasterDownConnection', changing read-only status can expect master connection to be down
* [Revision #1f1f6d16](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1f1f6d16) - \[[CONJ-583](https://jira.mariadb.org/browse/CONJ-583)] not throwing connection exception if master if down and allowMasterDownConnection is set
* [Revision #daaf8a10](https://github.com/mariadb-corporation/mariadb-connector-j/commit/daaf8a10) - \[misc] using maxscale 2.2.2
* [Revision #0989045a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0989045a) - \[[CONJ-583](https://jira.mariadb.org/browse/CONJ-583)] ensuring that socket exception throw an issue for internal connection query
* [Revision #d4b668bc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d4b668bc) - \[[CONJ-583](https://jira.mariadb.org/browse/CONJ-583)] ensuring test reliability
* [Revision #86020a2f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/86020a2f) - \[[CONJ-583](https://jira.mariadb.org/browse/CONJ-583)] Additional to ensure connection state when using intermediate proxy. If a failover occurs during this internal queries, and there is some intermediate proxy that doesn't do is the job, even writing to socket doesn't permit to ensure socket
* gitrevj: state, leaving the driver hanging indefinitely. Socket timeout is set for internal connection queries
* [Revision #ae52eee6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ae52eee6) - \[[CONJ-583](https://jira.mariadb.org/browse/CONJ-583)] correcting possible hang when a failover occur during establishment of connection in a master/slave configuration
* [Revision #2c260c5e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2c260c5e) - \[misc] change badge labels

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
