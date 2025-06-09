# MariaDB Connector/Node.js 3.2.0 Release Notes

The most recent [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of [MariaDB Connector/Node.js](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-nodejs/README.md) is:[**MariaDB Connector/Node.js 3.4.2**](mariadb-connector-node-js-3-4-2-release-notes.md)

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/nodejs-connector)[Release Notes](mariadb-connector-node-js-3-2-0-release-notes.md)[Changelog](../changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-2-0-changelog.md)[Connector/Node.js Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-nodejs/README.md)

**Release date:** 19 Jun 2023

MariaDB Connector/Node.js 3.2.0 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/Node.js see the**[**About MariaDB Connector/Node.js**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connectornodejs/README.md) **page**

## Notable changes

* [CONJS-250](https://jira.mariadb.org/browse/CONJS-250) 'undefined' parameters are now permitted, for compatibility with mysql/mysql2 behavior
* [CONJS-257](https://jira.mariadb.org/browse/CONJS-257) permit to import sql file directly
* [CONJS-253](https://jira.mariadb.org/browse/CONJS-253) Node.js 20 is now tested and supported

### API addition

* importFile(options) → Promise
* connection.importFile({file:'...', 'database': '...'}) → Promise
* pool.importFile({file:'...', 'database': '...'}) → Promisepromise)

example:

```js
await conn.importFile({
        file: '/tmp/someFile.sql', 
        database: 'myDb'
    });
```

## Issues Fixed

* [CONJS-252](https://jira.mariadb.org/browse/CONJS-252) missing deprecated option supportBigNumbers and bigNumberStrings in Typescript
* [CONJS-254](https://jira.mariadb.org/browse/CONJS-254) ensuring option connectTimeout is respected : timeout is removed when socket is successfully established, in place of returning connection object. Wasn't set when using pipe/unix socket
* [CONJS-255](https://jira.mariadb.org/browse/CONJS-255) In some case, pipelining was use even option explicitly disable it
* [CONJS-256](https://jira.mariadb.org/browse/CONJS-256) method changeUser can lead to error when using multi-authentication and pipelining
* [CONJS-258](https://jira.mariadb.org/browse/CONJS-258) All eventEmitters methods are not available on connections
* [CONJS-259](https://jira.mariadb.org/browse/CONJS-259) SqlError sqlMessage property alias for text addition
