# MariaDB Connector/C 3.4.0 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](mariadb-connector-c-3-4-5-release-notes.md)

[Release Notes](mariadb-connector-c-3-4-0-release-notes.md)[Changelog](../changelogs/mariadb-connectorc-3-4-changelogs/mariadb-connector-c-3-4-0-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 24 June 2022

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Notable changes

**TLS encryption**

[CONC-692](https://jira.mariadb.org/browse/CONC-692): Provide X509 peer certificate information:

Added a new structure MARIADB\_X509\_INFO, which contains information about peer certificate.\
The information can be obtained via mysql\_get\_infov API function:

```js
MARIADB_X509_INFO *info;
mariadb_get_infov(mysql, MARIADB_TLS_PEER_CERT_INFO, &info);
```

[MDEV-31857](https://jira.mariadb.org/browse/MDEV-31857): enable MYSQL\_OPT\_SSL\_VERIFY\_SERVER\_CERT by default

Using TLS/SSL has been simplified with MariaDB Server 11.4. Before version 11.4, proper TLS/SSL configuration required multiple manual steps for the server and all the clients connecting to it.

For MariaDB Connector/C before 3.4 to establish an TLS/SSL encrypted connection, or a MariaDB Server release series previous to 11.4, three options can be used:

[MDEV-30366](https://jira.mariadb.org/browse/MDEV-30366) - Server now permits to send a result-set containing generated id and affected rows for each bulk operation. This feature can be enabled with option MARIADB\_OPT\_BULK\_UNIT\_RESULTS. The server indicates if this feature is supported by setting MARIADB\_CLIENT\_BULK\_UNIT\_RESULTS in his capability flags.

* Added support for restricted\_auth in configuration files
* Support for new collations which were added in MariaDB Server 11.5

## Issues fixed

[CONC-605](https://jira.mariadb.org/browse/CONC-605): Don't allow to use unsupported client flags in mysql\_real\_connect[CONC-677](https://jira.mariadb.org/browse/CONC-677): Fix memory leak when setting default configuration directories[CONC-648](https://jira.mariadb.org/browse/CONC-648): Don't trust error packets received prior to TLS handshake completion. (Kudos to Daniel Lenski for his contribution[CONC-683](https://jira.mariadb.org/browse/CONC-683): Check pending results when closing statement[CONC-688](https://jira.mariadb.org/browse/CONC-688): mariadb\_rpl\_fetch() crashes if table is partitioned

## Contributions

* Warning fixes (-Wcalloc-transposed-args) in calloc calls (Thanks to Sam James)
* Fixed SSL\_read/write return value check in ma\_tls\_async\_check\_result (Thanks to Josh Hunt)

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-33-changelogs/mariadb-connector-c-331-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
