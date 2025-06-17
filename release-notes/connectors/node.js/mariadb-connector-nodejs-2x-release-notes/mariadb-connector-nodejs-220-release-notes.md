# MariaDB Connector/Node.js 2.2.0 Release Notes

The most recent [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of [MariaDB Connector/Node.js](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-nodejs/README.md) is:[**MariaDB Connector/Node.js 3.4.2**](../mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-4-2-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-nodejs-220-release-notes.md)[Changelog](../changelogs/mariadb-connector-nodejs-2x-changelogs/mariadb-connector-nodejs-220-changelog.md)[Connector/Node.js Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-nodejs/README.md)

**Release date:** 4 Feb 2019

MariaDB Connector/Node.js 2.2.0 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/Node.js see the**[**About MariaDB Connector/Node.js**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connectornodejs/README.md) **page**

### New option force Server version detection [CONJS-119](https://jira.mariadb.org/browse/CONJS-119)

Azure is using a proxy that will return a MySQL handshake not reflecting real server.

A new option `forceVersionCheck` is added to permit issuing a new `SELECT @@Version` command on connection creation,

to retrieve the correct server version. Connector will then act according to that server version.

### Query timeout implementation [CONJS-20](https://jira.mariadb.org/browse/CONJS-20)

This option is only permitted for MariaDB server >= 10.1.2, and permits to set a timeout to query operation.

Driver internally use `SET STATEMENT max_statement_time=<timeout> FOR <command>` permitting to cancel operation when timeout is reached,

Implementation of max\_statement\_time is engine dependent, so there might be some differences: For example, with Galera engine, a commits will ensure replication to other nodes to be done, possibly then exceeded timeout, to ensure proper server state.

example:

```js
//query that takes more than 20s
connection
  .query({sql: 'information_schema.tables, information_schema.tables as t2', timeout: 100 })
  .then(...)
  .catch(err => {
          // SQLError: (conn=2987, no: 1969, SQLState: 70100) Query execution was interrupted (max_statement_time exceeded)
          // sql: select * from information_schema.columns as c1, information_schema.tables, information_schema.tables as t2 - parameters:[]
          // at Object.module.exports.createError (C:\projets\mariadb-connector-nodejs.git\lib\misc\errors.js:55:10)
          // at PacketNodeEncoded.readError (C:\projets\mariadb-connector-nodejs.git\lib\io\packet.js:510:19)
          // at Query.readResponsePacket (C:\projets\mariadb-connector-nodejs.git\lib\cmd\resultset.js:46:28)
          // at PacketInputStream.receivePacketBasic (C:\projets\mariadb-connector-nodejs.git\lib\io\packet-input-stream.js:104:9)
          // at PacketInputStream.onData (C:\projets\mariadb-connector-nodejs.git\lib\io\packet-input-stream.js:160:20)
          // at Socket.emit (events.js:210:5)
          // at addChunk (_stream_readable.js:309:12)
          // at readableAddChunk (_stream_readable.js:290:11)
          // at Socket.Readable.push (_stream_readable.js:224:10)
          // at TCP.onStreamRead (internal/stream_base_commons.js:182:23) {
          //     fatal: true,
          //         errno: 1969,
          //         sqlState: '70100',
          //         code: 'ER_STATEMENT_TIMEOUT'
          // }
  });
```

### Fast-authentication improvement [CONJS-110](https://jira.mariadb.org/browse/CONJS-110)

* add mysql\_native\_password to fast-authentication path
* plugin 'mysql\_native\_password' is used by default if default server plugin is unknown
* unexpected packet type during handshake result will throw a good error.

### Pool leak detection [CONJS-117](https://jira.mariadb.org/browse/CONJS-117)

A new option `leakDetection` permits to indicate a timeout to log connection borrowed from pool.

When a connection is borrowed from pool and this timeout is reached, a message will be logged to console indicating a possible connection leak.

Another message will tell if the possible logged leak has been released.

A value of 0 (default) meaning Leak detection is disable

Additionally, some error messages have improved:

* Connection timeout now indicate that this correspond to socket failing to establish
* differentiate timeout error when closing pool to standard connection retrieving timeout

### misc:

* [CONJS-120](https://jira.mariadb.org/browse/CONJS-120) Permit values in SQL object to permits compatibility with mysql/mysql2
* [CONJS-118](https://jira.mariadb.org/browse/CONJS-118) missing import for Error when asking for connection when pool is closed. Thanks to @WayneMDB
* correcting typescript import of @types/node to version >8 thanks to @SimonSchick
* dependencies update

## Changelog

For a complete list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-nodejs-2x-changelogs/mariadb-connector-nodejs-220-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
