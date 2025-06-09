# MariaDB Connector/Node.js 2.1.3 Release Notes

The most recent [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of [MariaDB Connector/Node.js](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-nodejs/README.md) is:[**MariaDB Connector/Node.js 3.4.2**](../mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-4-2-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-nodejs-213-release-notes.md)[Changelog](../changelogs/mariadb-connector-nodejs-2x-changelogs/mariadb-connector-nodejs-213-changelog.md)[Connector/Node.js Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-nodejs/README.md)

**Release date:** 19 Nov 2019

MariaDB Connector/Node.js 2.1.3 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/Node.js see the**[**About MariaDB Connector/Node.js**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connectornodejs/README.md) **page**

## Notable Changes

* [CONJS-109](https://jira.mariadb.org/browse/CONJS-109) Missing mysql only collation definition
* [CONJS-108](https://jira.mariadb.org/browse/CONJS-108) typescript escape/escapeId definition
* [CONJS-107](https://jira.mariadb.org/browse/CONJS-107) Change user callback function not called when no option is set and changing collation only if collation option is correct
* [CONJS-106](https://jira.mariadb.org/browse/CONJS-106) properly escape boolean parameter false
* [CONJS-105](https://jira.mariadb.org/browse/CONJS-105) Typecast provided date function erroneous parsing
* [CONJS-104](https://jira.mariadb.org/browse/CONJS-104) Pam authentication must permit to provide multiple passwords

PAM authentication with multiple steps can be achieved using password as array:

```js
const mariadb = require('mariadb');

  mariadb.createConnection({host: 'mydb.com', user: 'myUser', password: ['myPwd', 'myAuthToken']})
    .then(conn => {
       ...
    })
    .catch(err => {
      ...
    });
```

## Misc

* better cluster error when pool is full
* adding test coverage

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
