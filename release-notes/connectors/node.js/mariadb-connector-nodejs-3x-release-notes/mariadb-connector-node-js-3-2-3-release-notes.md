# MariaDB Connector/Node.js 3.2.3 Release Notes

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/nodejs-connector)[Release Notes](mariadb-connector-node-js-3-2-3-release-notes.md)[Changelog](../changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-2-3-changelog.md)[Connector/Node.js Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-nodejs/README.md)

**Release date:** 19 Dec 2023

MariaDB Connector/Node.js 3.2.3 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/Node.js see the**[**About MariaDB Connector/Node.js**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connectornodejs/README.md) **page**

## Notable changes

* [CONJS-207](https://jira.mariadb.org/browse/CONJS-207) Add support for connection redirection, an upcoming MariaDB Server and MaxScale feature

## Issues Fixed

* [CONJS-271](https://jira.mariadb.org/browse/CONJS-271) Wrong binary decoding of 00:00:00 TIME values
* [CONJS-272](https://jira.mariadb.org/browse/CONJS-272) Error doesn't always have parameters according to option
* [CONJS-273](https://jira.mariadb.org/browse/CONJS-273) Bulk insert error when last bunch of parameters is reaching max\_allowed\_packet
* [CONJS-274](https://jira.mariadb.org/browse/CONJS-274) Disabling BULK insert for one batch is not possible
