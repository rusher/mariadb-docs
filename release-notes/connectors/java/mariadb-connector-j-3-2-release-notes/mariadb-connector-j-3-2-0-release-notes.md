# MariaDB Connector/J 3.2.0 Release Notes

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/java8-connector)[Release Notes](mariadb-connector-j-3-2-0-release-notes.md)[Changelog](../changelogs/mariadb-connectorj-3-2-changelogs/mariadb-connector-j-3-2-0-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 25 Aug 2023

MariaDB Connector/J 3.2.0 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release. It is replacing 3.1 as the maintenance releases.

This is the last release of the 3.2 release series as the release series 3.3 is compatible and is therefore replacing 3.2 as the maintenance releases.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Notable Changes

### Batch Bulk behavior

[CONJ-920](https://jira.mariadb.org/browse/CONJ-920)

Bulk batching enabled by default (option `useBulkStmts`) with permit super fast batching, but batch return array of update counts with Statement.SUCCESS\_NO\_INFO values.\
The problem is that application using optimistic locking fails, expecting exact return value.

`useBulkStmts` is now defaulting to false, with the addition of a new option `useBulkStmtsForInserts`, enabled by default permit to enable bulk for insert command only. This permit to have return values in batching return value, for all cases, permitting optimistic behavior.

This default values are more appropriate for all kind of application. If application doesn't use optimistic locking, enabling `useBulkStmts` is then more appropriate, because UPDATE and DELETE commands in batch will then use faster BULK implementation.

### Maxscale improvement

[CONJ-1084](https://jira.mariadb.org/browse/CONJ-1084)

When using maxscale 23.08.0+, when a maxscale node fails, connector will now priorize reconnection to the maxscales nodes having less connections, to ensure connections repartition after failover.\
This allows a faster return to normal

### other features

* [CONJ-1088](https://jira.mariadb.org/browse/CONJ-1088) Implement `databaseTerm` option for mysql compatibility
* [CONJ-1096](https://jira.mariadb.org/browse/CONJ-1096) adding option `useLocalSessionState` to permit avoiding queries when application only use JDBC methods.

## Bugs Fixed

* [CONJ-1075](https://jira.mariadb.org/browse/CONJ-1075) LOAD DATA INFILE is broken on windows
* [CONJ-1079](https://jira.mariadb.org/browse/CONJ-1079) getGeneratedKeys after batch will not return all generated id's if first batch command return no generated id.
* [CONJ-1080](https://jira.mariadb.org/browse/CONJ-1080) maridb Java connector sslMode=verify-ca complaining unable to find trust certificate.
* [CONJ-1082](https://jira.mariadb.org/browse/CONJ-1082) Multiple session system variables parsing fails
* [CONJ-1083](https://jira.mariadb.org/browse/CONJ-1083) Using /_client prepare_/ prefix to force client side prepared statement
* [CONJ-1091](https://jira.mariadb.org/browse/CONJ-1091) can't make a connection when the Read Replica DB is in a hang state when SocketTimeout=0 set
* [CONJ-1092](https://jira.mariadb.org/browse/CONJ-1092) ensure respecting server collation
* [CONJ-1094](https://jira.mariadb.org/browse/CONJ-1094) Missing mariadb/mysql collation

## Changelog

For a complete list of changes made in MariaDB Connector/J 3.2.0, with links to detailed\
information on each push, see the [changelog](../changelogs/mariadb-connectorj-3-2-changelogs/mariadb-connector-j-3-2-0-changelog.md).

{% @marketo/form formid="4316" formId="4316" %}
