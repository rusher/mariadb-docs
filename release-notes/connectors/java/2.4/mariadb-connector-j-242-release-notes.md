# MariaDB Connector/J 2.4.2 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-j-242-release-notes.md)[Changelog](../changelogs/2.4/mariadb-connector-j-242-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

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
information on each push, see the [changelog](../changelogs/2.4/mariadb-connector-j-242-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
