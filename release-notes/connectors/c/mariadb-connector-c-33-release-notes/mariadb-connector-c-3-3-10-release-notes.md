# MariaDB Connector/C 3.3.10 Release Notes

[Download](https://mariadb.com/downloads/connectors)[Release Notes](mariadb-connector-c-3-3-10-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-33-changelogs/mariadb-connector-c-3-3-10-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-c/README.md)

**Release date:** 21 Jun 2024

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Issues fixed:

* [CONC-505](https://jira.mariadb.org/browse/CONC-505): Don't allow to use unsupported client flags in mysql\_real\_connect
* [CONC-677](https://jira.mariadb.org/browse/CONC-677): Fix memory leak when setting default configuration directories
* [CONC-648](https://jira.mariadb.org/browse/CONC-648): Don't trust error packets received prior to TLS handshake completion. (Kudos to Daniel Lenski for his contribution

## Notable changes

* Allow named pipe connection handle to be used with IO completion port. Pipe handle can be obtained via mysql\_get\_socket() API function.\
  Added support for zstd static library (Kudos to Uilian Ries for his contribution)
* Added support for restricted\_auth in configuration files
* [MDEV-30366](https://jira.mariadb.org/browse/MDEV-30366) - Server now permits to send a result-set containing generated id and affected rows for each bulk operation. This feature can be enabled with option MARIADB\_OPT\_BULK\_UNIT\_RESULTS. The server indicates if this feature is supported by setting MARIADB\_CLIENT\_BULK\_UNIT\_RESULTS in his capability flags.

## Contributions

* Warning fixes (-Wcalloc-transposed-args) in calloc calls (Thanks to Sam James)
* Fixed SSL\_read/write return value check in ma\_tls\_async\_check\_result (Thanks to Josh Hunt)

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-33-changelogs/mariadb-connector-c-3-3-10-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
