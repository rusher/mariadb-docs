# MariaDB Connector/Node.js 3.2.2 Release Notes

{% include "../../../.gitbook/includes/latest-nodejs.md" %}

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/nodejs-connector) | [Release Notes](mariadb-connector-node-js-3-2-2-release-notes.md) | [Changelog](../changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-2-2-changelog.md) | [Connector/Node.js Overview](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs/mariadb-connector-node-js-guide)

**Release date:** 16 Oct 2023

MariaDB Connector/Node.js 3.2.2 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

{% hint style="success" %}
**For an overview of MariaDB Connector/Node.js see the** [**About MariaDB Connector/Node.js**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs/mariadb-connector-node-js-guide) **page**
{% endhint %}

## Issues Fixed

* [CONJS-270](https://jira.mariadb.org/browse/CONJS-270) Always send connection attributes, even when option `connectAttributes` is not set
* [CONJS-269](https://jira.mariadb.org/browse/CONJS-269) avoid useless "set names utf8mb4" on connection creation if not needed
* [CONJS-268](https://jira.mariadb.org/browse/CONJS-268) importFile method doesn't always throw error when imported commands fails #253
* [CONJS-267](https://jira.mariadb.org/browse/CONJS-267) Ensure that option collation with id > 255 are respected

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
