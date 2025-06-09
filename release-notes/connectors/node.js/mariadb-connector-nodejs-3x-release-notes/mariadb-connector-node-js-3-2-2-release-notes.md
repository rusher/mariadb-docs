# MariaDB Connector/Node.js 3.2.2 Release Notes

The most recent [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of [MariaDB Connector/Node.js](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-nodejs/README.md) is:[**MariaDB Connector/Node.js 3.4.2**](mariadb-connector-node-js-3-4-2-release-notes.md)

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/nodejs-connector)[Release Notes](mariadb-connector-node-js-3-2-2-release-notes.md)[Changelog](../changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-2-2-changelog.md)[Connector/Node.js Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-nodejs/README.md)

**Release date:** 16 Oct 2023

MariaDB Connector/Node.js 3.2.2 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/Node.js see the**[**About MariaDB Connector/Node.js**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connectornodejs/README.md) **page**

## Issues Fixed

* [CONJS-270](https://jira.mariadb.org/browse/CONJS-270) Always send connection attributes, even when option `connectAttributes` is not set
* [CONJS-269](https://jira.mariadb.org/browse/CONJS-269) avoid useless "set names utf8mb4" on connection creation if not needed
* [CONJS-268](https://jira.mariadb.org/browse/CONJS-268) importFile method doesn't always throw error when imported commands fails #253
* [CONJS-267](https://jira.mariadb.org/browse/CONJS-267) Ensure that option collation with id > 255 are respected
