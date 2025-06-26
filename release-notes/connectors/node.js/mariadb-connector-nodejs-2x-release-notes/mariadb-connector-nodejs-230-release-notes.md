# MariaDB Connector/Node.js 2.3.0 Release Notes

The most recent [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of [MariaDB Connector/Node.js](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-nodejs/README.md) is:[**MariaDB Connector/Node.js 3.4.2**](../mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-4-2-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-nodejs-230-release-notes.md)[Changelog](../changelogs/mariadb-connector-nodejs-2x-changelogs/mariadb-connector-nodejs-230-changelog.md)[Connector/Node.js Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-nodejs/README.md)

**Release date:** 20 Mar 2020

MariaDB Connector/Node.js 2.3.0 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/Node.js see the**[**About MariaDB Connector/Node.js**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connectornodejs/README.md) **page**

2.3.0 has been deprecated to 2.3.1: changing new connection option `timeout` to `queryTimeout` to avoid any confusion.

* [CONJS-127](https://jira.mariadb.org/browse/CONJS-127) - Resultset with same identifier skip data. Now an error will be thrown.
* [CONJS-126](https://jira.mariadb.org/browse/CONJS-126) - permit setting session query timeout per option
* [CONJS-124](https://jira.mariadb.org/browse/CONJS-124) - Force connection.escapeId to emit backtick #101
* [CONJS-123](https://jira.mariadb.org/browse/CONJS-123) - exporting SqlError class to permit instanceOf checks #100
* [CONJS-122](https://jira.mariadb.org/browse/CONJS-122) - fix undefined localTz with timezone: 'Z' issue #92
* [CONJS-121](https://jira.mariadb.org/browse/CONJS-121) - Connection.escapeId must always quote value to permit reserved words

misc:

* appveyor testing server version upgrade
* better debug logging trace format
* correct ssl test

## Changelog

For a complete list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-nodejs-2x-changelogs/mariadb-connector-nodejs-230-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
