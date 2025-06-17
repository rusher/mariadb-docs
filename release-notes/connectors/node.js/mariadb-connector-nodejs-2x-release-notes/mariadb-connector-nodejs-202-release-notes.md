# MariaDB Connector/Node.js 2.0.2 Release Notes

The most recent [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of [MariaDB Connector/Node.js](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-nodejs/README.md) is:[**MariaDB Connector/Node.js 3.4.2**](../mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-4-2-release-notes.md)

[Download](https://mariadb.com/downloads/?showall=1\&tab=connectors\&group=mariadbconnectors\&product=Node.js%20connector\&version=2.0.2)[Release Notes](mariadb-connector-nodejs-202-release-notes.md)[Changelog](../changelogs/mariadb-connector-nodejs-2x-changelogs/mariadb-connector-nodejs-202-changelog.md)[Connector/Node.js Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-nodejs/README.md)

**Release date:** 13 Dec 2018

MariaDB Connector/Node.js 2.0.2 is a [_**Release Candidate (RC)**_](../../../mariadb-release-criteria.md) release.

**For an overview of MariaDB Connector/Node.js see the**[**About MariaDB Connector/Node.js**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connectornodejs/README.md) **page**

## Notable Updates

New options:

| noControlAfterUse |
| ----------------- |
| noControlAfterUse |

### correction

* using option connectAttributes value \_server\_host is correctly filled on Performance Schema.
* batch improvement
  * error is now thrown when no values
  * BULK better handling when socket fail during command
  * Object with toSqlString function parameter support
  * null value correction when using BULK
  * timezone correction when not using "local" default values
  * now support very long parameter (> 16M)
  * rewrite correctly parse double slash
  * timezone option parsing correction (correctly handle negative values)
* test coverage improvement
* minor performance improvement
* pool end() now correctly wait for all connections ending

## Changelog

For a complete list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-nodejs-2x-changelogs/mariadb-connector-nodejs-202-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
