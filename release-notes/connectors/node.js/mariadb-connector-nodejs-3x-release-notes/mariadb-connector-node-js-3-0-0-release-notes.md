# MariaDB Connector/Node.js 3.0.0 GA Release Notes

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-node-js-3-0-0-release-notes.md)[Changelog](../changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-nodejs-300-ga-changelog.md)[Connector/Node.js Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-nodejs/README.md)

**Release date:** 1 Mar 2022

MariaDB Connector/Node.js 3.0.0 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/Node.js see the**[**About MariaDB Connector/Node.js**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connectornodejs/README.md) **page**

see [3.0.0-rc](mariadb-connector-node-js-3-0-0-rc-release-notes.md) for 3.0.0 content from previous version.

## Notable Changes

* merged correction from 2.5.6
* \[[CONJS-185](https://jira.mariadb.org/browse/CONJS-185)] considering BIT(1) as boolean (option bitOneIsBoolean permit to disable that behavior for compatibility)
* pool ensuring multi-request process order
* set parser function once per result-set for better performance

## Changelog

For a complete list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-nodejs-300-ga-changelog.md).
