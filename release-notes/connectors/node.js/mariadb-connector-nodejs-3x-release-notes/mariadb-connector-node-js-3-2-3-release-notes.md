# MariaDB Connector/Node.js 3.2.3 Release Notes

{% include "../../../.gitbook/includes/latest-nodejs.md" %}

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/nodejs-connector) | [Release Notes](mariadb-connector-node-js-3-2-3-release-notes.md) | [Changelog](../changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-2-3-changelog.md) | [Connector/Node.js Overview](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs/mariadb-connector-node-js-guide)

**Release date:** 19 Dec 2023

MariaDB Connector/Node.js 3.2.3 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

{% hint style="success" %}
**For an overview of MariaDB Connector/Node.js see the** [**About MariaDB Connector/Node.js**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs/mariadb-connector-node-js-guide) **page**
{% endhint %}

## Notable changes

* [CONJS-207](https://jira.mariadb.org/browse/CONJS-207) Add support for connection redirection, an upcoming MariaDB Server and MaxScale feature

## Issues Fixed

* [CONJS-271](https://jira.mariadb.org/browse/CONJS-271) Wrong binary decoding of 00:00:00 TIME values
* [CONJS-272](https://jira.mariadb.org/browse/CONJS-272) Error doesn't always have parameters according to option
* [CONJS-273](https://jira.mariadb.org/browse/CONJS-273) Bulk insert error when last bunch of parameters is reaching max\_allowed\_packet
* [CONJS-274](https://jira.mariadb.org/browse/CONJS-274) Disabling BULK insert for one batch is not possible

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
