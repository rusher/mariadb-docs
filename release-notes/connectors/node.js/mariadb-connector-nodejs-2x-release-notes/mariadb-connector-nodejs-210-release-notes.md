# MariaDB Connector/Node.js 2.1.0 Release Notes

The most recent [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of [MariaDB Connector/Node.js](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-nodejs/README.md) is:[**MariaDB Connector/Node.js 3.4.2**](../mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-4-2-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-nodejs-210-release-notes.md)[Changelog](../changelogs/mariadb-connector-nodejs-2x-changelogs/mariadb-connector-nodejs-210-changelog.md)[Connector/Node.js Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-nodejs/README.md)

**Release date:** 12 Jul 2019

MariaDB Connector/Node.js 2.1.0 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/Node.js see the**[**About MariaDB Connector/Node.js**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connectornodejs/README.md) **page**

## Notable Changes

* \[[CONJS-19](https://jira.mariadb.org/browse/CONJS-19)] implement Ed25519 plugin
* \[[CONJS-57](https://jira.mariadb.org/browse/CONJS-57)] Multiple alternative authentication methods for the same user ([MariaDB 10.4](broken-reference))
* \[[CONJS-61](https://jira.mariadb.org/browse/CONJS-61)] Permit handling expired password
* \[[CONJS-85](https://jira.mariadb.org/browse/CONJS-85)] Implement pool events according to mysql/mysql2 API
* \[[CONJS-87](https://jira.mariadb.org/browse/CONJS-87)] Array parameter automatic conversion
* \[[CONJS-89](https://jira.mariadb.org/browse/CONJS-89)] Performance improvement on decoding string
* \[[CONJS-88](https://jira.mariadb.org/browse/CONJS-88)] Charset collation option separation
* \[[CONJS-74](https://jira.mariadb.org/browse/CONJS-74)] Types definition must be string, not byte when using option typeCast
* \[[CONJS-75](https://jira.mariadb.org/browse/CONJS-75)] Missing import dependencies for typeScript
* \[[CONJS-79](https://jira.mariadb.org/browse/CONJS-79)] Read errors while processing LOCAL INFILE can cause process crash
* \[[CONJS-83](https://jira.mariadb.org/browse/CONJS-83)] Add poolCluster 'remove' event
* \[[CONJS-84](https://jira.mariadb.org/browse/CONJS-84)] option restoreNodeTimeout is not respected when removeNodeErrorCount is set
* \[[CONJS-73](https://jira.mariadb.org/browse/CONJS-73)] Setting timezone to current IANA might provoke server automatic retrieval

New Options

| Option                        | Description                                                                                                                                                                                                                                           | Type      | Default              |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | -------------------- |
| Option                        | Description                                                                                                                                                                                                                                           | Type      | Default              |
| `collation`                   | (used in replacement of charset) Permit to defined collation used for connection. This will defined the charset encoding used for exchanges with database and defines the order used when comparing strings. It's mainly used for micro-optimizations | _string_  | UTF8MB4\_UNICODE\_CI |
| `permitConnectionWhenExpired` | Permit a user with expired password to connect. Only possible operation in this case will be to change password ('SET PASSWORD=PASSWORD('XXX')')                                                                                                      | _boolean_ | false                |

The option `charset` now corresponds to charset, still permitting collation for compatibility, but then a warning is thrown to console.

#### Pool events

Pools now emits events.

| event        | Description                                                                                               |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| event        | Description                                                                                               |
| `acquire`    | This event emits a connection is acquired from pool.                                                      |
| `connection` | This event is emitted when a new connection is added to the pool. Has a connection object parameter       |
| `enqueue`    | This event is emitted when a command cannot be satisfied immediately by the pool and is queued.           |
| `release`    | This event is emitted when a connection is released back into the pool. Has a connection object parameter |

Example:

```
pool.on('connection', (conn) => console.log(`connection ${conn.threadId} has been created in pool`);
Pool
```

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
