# MariaDB Connector/Node.js 3.0.2 Release Notes

The most recent [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of [MariaDB Connector/Node.js](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-nodejs/README.md) is:[**MariaDB Connector/Node.js 3.4.2**](mariadb-connector-node-js-3-4-2-release-notes.md)

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/nodejs-connector)[Release Notes](mariadb-connector-node-js-3-0-2-release-notes.md)[Changelog](../changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-0-2-changelog.md)[Connector/Node.js Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-nodejs/README.md)

**Release date:** 27 Oct 2022

MariaDB Connector/Node.js 3.0.2 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/Node.js see the**[**About MariaDB Connector/Node.js**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connectornodejs/README.md) **page**

## Notable Changes

### permit streaming prepare statement result

Like queryStream, execute command can now be streamed as well for huge resultset, to avoid charging the whole resultset in memory.\
Example :

```js
const prepare = await shareConn.prepare('SELECT * FROM mysql.user where host = ?');
const stream = prepare.executeStream(['localhost']);    
try {
  for await (const row of stream) {
    console.log(row);
  }
} catch (e) {
  queryStream.close();
}
prepare.close();
```

## Issues Fixed

* [CONJS-223](https://jira.mariadb.org/browse/CONJS-223) Metadata column name gets sporadic corrupted
* [CONJS-211](https://jira.mariadb.org/browse/CONJS-211) Session timezone unset on connection re-use with connection pool
* [CONJS-212](https://jira.mariadb.org/browse/CONJS-212) when throwing an error when using option `leakDetectionTimeout`, might result in throwing wrong error with `Cannot read properties of null (reading 'leaked')`
* [CONJS-217](https://jira.mariadb.org/browse/CONJS-217) caching\_sha2\_password never succeed using FAST AUTHENTICATION. With correction, one less exchanges is done when connecting to a MySQL server
* [CONJS-219](https://jira.mariadb.org/browse/CONJS-219) prepare cache was not limited to `prepareCacheLength` but can increase up to 2x the `prepareCacheLength` value, leading to possible ER\_MAX\_PREPARED\_STMT\_COUNT\_REACHED
* [CONJS-228](https://jira.mariadb.org/browse/CONJS-228) improving prepare cache performance
* [CONJS-226](https://jira.mariadb.org/browse/CONJS-226) missing typescript metaAsArray option and documentation
* [CONJS-213](https://jira.mariadb.org/browse/CONJS-213) update error code with recent MariaDB server
* [CONJS-215](https://jira.mariadb.org/browse/CONJS-215) Executing after prepare close throw an undescriptive error
* [CONJS-221](https://jira.mariadb.org/browse/CONJS-221) option debugLen and logParam are not documented
* [CONJS-227](https://jira.mariadb.org/browse/CONJS-227) Allow setting idleTimeout to 0
* [CONJS-214](https://jira.mariadb.org/browse/CONJS-214) missing pool.closed typescript definition
* [CONJS-216](https://jira.mariadb.org/browse/CONJS-216) remove please-upgrade-node dependency
* [CONJS-224](https://jira.mariadb.org/browse/CONJS-224) missing typescript checkNumberRange option definition

{% @marketo/form formid="4316" formId="4316" %}
