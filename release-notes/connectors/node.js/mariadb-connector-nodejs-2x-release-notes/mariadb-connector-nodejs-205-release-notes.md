# MariaDB Connector/Node.js 2.0.5 Release Notes

The most recent [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of [MariaDB Connector/Node.js](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-nodejs/README.md) is:[**MariaDB Connector/Node.js 3.4.2**](../mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-4-2-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-nodejs-205-release-notes.md)[Changelog](../changelogs/mariadb-connector-nodejs-2x-changelogs/mariadb-connector-nodejs-205-changelog.md)[Connector/Node.js Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-nodejs/README.md)

**Release date:** 13 May 2019

MariaDB Connector/Node.js 2.0.5 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/Node.js see the**[**About MariaDB Connector/Node.js**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connectornodejs/README.md) **page**

## Notable Changes

* \[[CONJS-69](https://jira.mariadb.org/browse/CONJS-69)] permit set numeric parameter bigger than javascript 2^53-1 limitation
* \[[CONJS-68](https://jira.mariadb.org/browse/CONJS-68)] error when reading datetime data and timezone option is set
* \[[CONJS-58](https://jira.mariadb.org/browse/CONJS-58)] parse Query when receiving LOAD LOCAL INFILE, to prevent man in the middle attack
* \[[CONJS-62](https://jira.mariadb.org/browse/CONJS-62)] support named timezones and daylight savings time
* \[[CONJS-63](https://jira.mariadb.org/browse/CONJS-63)] add type definitions for typescript
* \[[CONJS-64](https://jira.mariadb.org/browse/CONJS-64)] handle Error packet during resultset to permit query timeout with SET STATEMENT max\_statement\_time= FOR
* \[[CONJS-66](https://jira.mariadb.org/browse/CONJS-66)] SET datatype handling (returning array)
* \[[CONJS-67](https://jira.mariadb.org/browse/CONJS-67)] Changing user does not takes in account connector internal state (transaction status)

### Pool improvement

New Options

| Option        | Description                                                                                                                                                                                                                                                                      | Type      | Default                        |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------ |
| Option        | Description                                                                                                                                                                                                                                                                      | Type      | Default                        |
| `idleTimeout` | Indicate idle time after which a pool connection is released. Value must be lower than [@@wait\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables). In seconds (0 means never release) | _integer_ | 1800                           |
| `minimumIdle` | Permit to set a minimum number of connection in pool. Recommendation is to use fixed pool, so not setting this value.                                                                                                                                                            | _integer_ | _set to connectionLimit value_ |

This permits to set a minimum pool size, meaning that after a period of inactivity, the pool will decrease the inner number of connection to a minimum number of connections (defined with `minimumIdle`).\
By default, connections not used after `idleTimeout` (default to 30 minutes) will be discarded, avoiding reaching server [@@wait\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables).

Pool handle connection creation automatically, with now some delayed after failing to establish a connection, to avoid using CPU unnecessary.\
Authentication error in pool have now a better handling.

## Changelog

For a complete list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-nodejs-2x-changelogs/mariadb-connector-nodejs-205-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
