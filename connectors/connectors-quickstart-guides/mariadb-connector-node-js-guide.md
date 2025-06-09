# About MariaDB Connector/Node.js

{% hint style="info" %}
The most recent [_**Stable (GA)**_](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-release-criteria) release of [MariaDB Connector/Node.js](https://github.com/mariadb-corporation/docs-connectors/blob/test/en/about-mariadb-connector-nodejs/README.md) is:[**MariaDB Connector/Node.js 3.4.2**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-4-2-release-notes)
{% endhint %}

[Download MariaDB Connector/Node.js](https://mariadb.com/downloads/connectors/connectors-data-access/nodejs-connector/)

MariaDB Connector/Node.js is used to connect applications developed on Node.js to\
MariaDB and MySQL databases. The library is LGPL\
licensed.

| Date        | Release | Status                                                                                 | Min. Node.js Compat. | Release Notes                                                                                                                                                              | Changelog                                                                                                                                                                  |
| ----------- | ------- | -------------------------------------------------------------------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Date        | Release | Status                                                                                 | Min. Node.js Compat. | Release Notes                                                                                                                                                              | Changelog                                                                                                                                                                  |
| 25 Apr 2025 | 3.4.2   | [Stable (GA)](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-release-criteria) | Node 10+             | [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-4-2-release-notes) | [Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-4-2-changelog) |
| 02 Apr 2025 | 3.4.1   | [Stable (GA)](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-release-criteria) | Node 10+             | [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-4-1-release-notes) | [Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-4-1-changelog) |
| 24 Oct 2024 | 3.4.0   | [Stable (GA)](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-release-criteria) | Node 10+             | [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-4-0-release-notes) | [Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-4-0-changelog) |
| 18 Sep 2024 | 3.3.2   | [Stable (GA)](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-release-criteria) | Node 10+             | [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-3-2-release-notes) | [Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-3-2-changelog) |
| 5 Jun 2024  | 3.3.1   | [Stable (GA)](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-release-criteria) | Node 10+             | [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-3-1-release-notes) | [Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-3-1-changelog) |
| 21 Mar 2024 | 3.3.0   | [Stable (GA)](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-release-criteria) | Node 10+             | [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-3-0-release-notes) | [Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-3-0-changelog) |

[see all Connector/Node.js releases](../mariadb-connector-nodejs/list-of-mariadb-connector-nodejs-releases.md)

## About MariaDB Connector/Node.js

MariaDB Connector/Node.js is a native Javascript driver.

### Obtaining the Driver

The required files can be downloaded from:[connector](https://mariadb.com/downloads/connector)

The source code is available on GitHub:[mariadb-connector-nodejs](https://github.com/MariaDB/mariadb-connector-nodejs)

MariaDB Connector/Node.js on npm, the package manager for JavaScript:[mariadb](https://www.npmjs.com/package/mariadb)

### Installing the Driver

The driver can be installed using npm:

```bash
npm install mariadb
```

### Choosing a Version

Driver versions are compatible with all MariaDB servers and MySQL 5.x (>= 5.5.3).\
Tested with MariaDB server versions 5.5, 10.0, 10.1, 10.2, 10.3 and 10.4 with Node.js 6 to 12 (see [travis results](https://travis-ci.org/MariaDB/mariadb-connector-nodejs) for unix or [appveyor results](https://ci.appveyor.com/project/rusher/mariadb-connector-nodejs) on windows).

### Requirements

MariaDB Connector/Node.js requires Node.js 6 or above, since it is based on Promise.

### License

GNU Lesser General Public License as published by the Free Software Foundation;\
either version 2.1 of the License, or (at your option) any later version.

## Using the Driver

The MariaDB Connector can use different APIs on the back-end: [Promise](../mariadb-connector-nodejs/connector-nodejs-promise-api.md) and [Callback API](../mariadb-connector-nodejs/connector-nodejs-callback-api.md). The default API is Promise. The callback API is provided for compatibility with the mysql and mysql2 APIs.


{% @marketo/form formid="4316" %}
