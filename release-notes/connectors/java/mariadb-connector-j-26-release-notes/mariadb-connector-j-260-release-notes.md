# MariaDB Connector/J 2.6.0 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-j-260-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-26-changelogs/mariadb-connector-j-260-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 20 Mar 2020

MariaDB Connector/J 2.6.0 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**NOTE:** MariaDB Connector/J 2.6.0 is fully compatible with the latest release of\
version 2.5. Further maintenance releases will not be provided for version 2.5.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

## Notable Updates

* [CONJ-768](https://jira.mariadb.org/browse/CONJ-768) - Check Galera allowed state when connecting when option `galeraAllowedState` is set, and not only on validation
* [CONJ-759](https://jira.mariadb.org/browse/CONJ-759) - on failover, catalog changed might not be set when automatically recreating a connection.
* [CONJ-761](https://jira.mariadb.org/browse/CONJ-761) - remove unnecessary dependencies for fedora tar creation
* [CONJ-763](https://jira.mariadb.org/browse/CONJ-763) - Custom SocketFactory now can change options
* [CONJ-764](https://jira.mariadb.org/browse/CONJ-764) - DatabaseMetaData.getExportedKeys should return "PRIMARY" for PK\_NAME column
* [CONJ-765](https://jira.mariadb.org/browse/CONJ-765) - Allow MariaDbDatabaseMetaData#getExportedKeys to return the exported keys for all tables
* [CONJ-766](https://jira.mariadb.org/browse/CONJ-766) - Adding a socket timeout until complete authentication, to avoid hangs is server doesn't support pipelining
* [CONJ-767](https://jira.mariadb.org/browse/CONJ-767) - permit using Aurora RO endpoint
* [CONJ-771](https://jira.mariadb.org/browse/CONJ-771) - enablePacketDebug must not reset stack on failover
* [CONJ-772](https://jira.mariadb.org/browse/CONJ-772) - JDBC Conversion Function support parsing correction

## Changelog

For a complete list of changes made in MariaDB Connector/J 2.6.0, with links to detailed\
information on each push, see the [changelog](../changelogs/mariadb-connector-j-26-changelogs/mariadb-connector-j-260-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
