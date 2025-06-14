# MariaDB Connector/C 3.1.0 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-c/3.1.0/)[Release Notes](mariadb-connector-c-310-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-31-changelogs/mariadb-connector-c-310-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 8 Apr 2019

This is an [_**Alpha**_](../../../mariadb-release-criteria.md) release of the MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## New Features

* Included in [MariaDB 10.4.4](../../../mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1044-release-notes.md)
* [Replication/Binlog API](https://github.com/MariaDB/mariadb-connector-c/wiki/binlog_api): The main mechanism used in replication is the binary log. If binary logging is enabled, all updates to the database (data manipulation and data definition) are written into the binary log as binlog events. Clients may read the binary log from master using the replication API in order to access the data.

## Bug fixes

* [CONC-395](https://jira.mariadb.org/browse/CONC-395): Dashes and underscores are not interchangeable in options in my.cnf

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-31-changelogs/mariadb-connector-c-310-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
