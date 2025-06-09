# MariaDB Connector/J 2.4.2 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-j-242-release-notes.md)[Changelog](../changelogs/mariadb-connectorj-24-changelogs/mariadb-connector-j-242-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 17 Jun 2019

MariaDB Connector/J 2.4.2 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

## Notes

### Evolutions

New option `defaultFetchSize` to set default fetch size. When set, all statements will be initialized with the indicated fetch size.

| defaultFetchSize |
| ---------------- |
| defaultFetchSize |

### Bugs

* [CONJ-703](https://jira.mariadb.org/browse/CONJ-703): ClassNotFoundException when trying to connect using two-authentication in an OSGI environment.
* [CONJ-711](https://jira.mariadb.org/browse/CONJ-711): Xid format id is unsigned integer, currently sending as signed value.
* [CONJ-700](https://jira.mariadb.org/browse/CONJ-700): autoReconnect=true on Basic Failover doesn't reconnect
* [CONJ-707](https://jira.mariadb.org/browse/CONJ-707): failover might throw an unexpected exception with using "failover"/"sequential" configuration on socket error
* [CONJ-709](https://jira.mariadb.org/browse/CONJ-709): includeThreadDumpInDeadlockExceptions is thrown only if option includeInnodbStatusInDeadlockExceptions is set
* [CONJ-710](https://jira.mariadb.org/browse/CONJ-710): Throw complete stackTrace when having an exception on XA Commands
* [CONJ-714](https://jira.mariadb.org/browse/CONJ-714): Error on connection on galera server when in detached mode.
* [CONJ-701](https://jira.mariadb.org/browse/CONJ-701): typo in error message in SelectResultSet.java
* [CONJ-679](https://jira.mariadb.org/browse/CONJ-679): parse Query when receiving LOAD LOCAL INFILE

## Changelog

For a complete list of changes made in MariaDB Connector/J 2.4.2, with links to detailed\
information on each push, see the [changelog](../changelogs/mariadb-connectorj-24-changelogs/mariadb-connector-j-242-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
