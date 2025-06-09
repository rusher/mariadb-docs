# MariaDB Connector/Node.js 2.0.3 Release Notes

The most recent [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of [MariaDB Connector/Node.js](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-nodejs/README.md) is:[**MariaDB Connector/Node.js 3.4.2**](../mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-4-2-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-nodejs-203-release-notes.md)[Changelog](../changelogs/mariadb-connector-nodejs-2x-changelogs/mariadb-connector-nodejs-203-changelog.md)[Connector/Node.js Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-nodejs/README.md)

**Release date:** 31 Jan 2019

MariaDB Connector/Node.js 2.0.3 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/Node.js see the**[**About MariaDB Connector/Node.js**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connectornodejs/README.md) **page**

## Notable Changes

* \[[CONJS-56](https://jira.mariadb.org/browse/CONJS-56)] TypeError: Cannot read property 'totalConnections' of undefined
* \[[CONJS-59](https://jira.mariadb.org/browse/CONJS-59)] pool now throw `ER_ACCESS_DENIED_ERROR` in place of a basic timeout error
* \[[CONJS-60](https://jira.mariadb.org/browse/CONJS-60)] handling pipe error when streaming, avoiding hang in case of pipe error.
* \[[CONJS-55](https://jira.mariadb.org/browse/CONJS-55)] Connector throw an error when using incompatible options

## Changelog

For a complete list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-nodejs-2x-changelogs/mariadb-connector-nodejs-203-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
