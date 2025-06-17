# MariaDB Connector/J 1.4.5 Changelog

The most recent [_**Stable**_](../../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.4.5/)[Release Notes](../../mariadb-connector-j-14-release-notes/mariadb-connector-j-145-release-notes.md)[Changelog](mariadb-connector-j-145-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 24 May 2016

For the highlights of this release, see the[release notes](../../mariadb-connector-j-14-release-notes/mariadb-connector-j-145-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #4e8c715](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4e8c715) \[[CONJ-218](https://jira.mariadb.org/browse/CONJ-218)] MariaDbDatabaseMetaData getTables() follow the jdbc recommendation TABLE\_TYPE "TABLE" replacing "BASE\_TABLE"
* [Revision #fa6fd29](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fa6fd29), [Revision #747d265](https://github.com/mariadb-corporation/mariadb-connector-j/commit/747d265) \[[CONJ-290](https://jira.mariadb.org/browse/CONJ-290)] Timestamps format error when using prepareStatement with options useFractionalSeconds and useServerPrepStmts
* [Revision #63b7baa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/63b7baa) \[[CONJ-294](https://jira.mariadb.org/browse/CONJ-294)] PrepareStatement failover handling : use master connection to a minimum
* [Revision #5a2a4e5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5a2a4e5), [Revision #ffe9527](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ffe9527), [Revision #fd669bc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fd669bc) \[[CONJ-297](https://jira.mariadb.org/browse/CONJ-297)] Useless memory consumption when using Statement.setQueryTimeout
* [Revision #cb61d37](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cb61d37), [Revision #8969e1f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8969e1f), [Revision #ac49a5f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ac49a5f) \[misc] separate CI aurora
* [Revision #3ba9c73](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3ba9c73) \[misc] add github badge
* [Revision #e2eb7b7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e2eb7b7) \[misc] add javadoc documentation

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
