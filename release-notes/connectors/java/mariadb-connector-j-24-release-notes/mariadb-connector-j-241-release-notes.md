# MariaDB Connector/J 2.4.1 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.com/Connectors/java/connector-java-2.4.1/)[Release Notes](mariadb-connector-j-241-release-notes.md)[Changelog](../changelogs/mariadb-connectorj-24-changelogs/mariadb-connector-j-241-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 18 Mar 2019

MariaDB Connector/J 2.4.1 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

### Evolutions

* \[misc] enabled running of 'SHOW ENGINE INNODB STATUS' for error code 1213 (@mtykhenko)
* \[misc] reduce mutex using select @@innodb\_read\_only for aurora (@matsuzayaws)

### Bugs

* \[misc] updating checkstyle version dependency
* \[misc] permit using SSL on localsocket
* \[misc] java PID using java 9 ProcessHandle if existing, relying on JNA if present
* [CONJ-687](https://jira.mariadb.org/browse/CONJ-687): addition of option "useMysqlMetadata" to permit MySQL meta compatibility
* [CONJ-682](https://jira.mariadb.org/browse/CONJ-682): internal pool correction: when receiving an RST during connection validation, the pool will end up throwing connection timeout exception in place of reusing another connection.

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
