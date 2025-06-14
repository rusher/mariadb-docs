# MariaDB Connector/ODBC 3.1.10 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-odbc-3-1-10-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-3110-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-odbc/README.md)

**Release date:** 20 Oct 2020

This is a [Stable (GA)](../../../mariadb-release-criteria.md) release of MariaDB Connector/ODBC 3.1.

MariaDB Connector/ODBC 3.1.10 is built on top of[MariaDB Connector/C v.3.1.10](../../c/mariadb-connector-c-31-release-notes/mariadb-connector-c-3110-release-notes.md).

## Bug Fixes

* [ODBC-289](https://jira.mariadb.org/browse/ODBC-289) - Crash fetching from statement after closing and re-executing
* [ODBC-293](https://jira.mariadb.org/browse/ODBC-293) - C/ODBC binary tarball for RHEL/CentOS has duplicate libraries

## Notable changes

* [ODBC-288](https://jira.mariadb.org/browse/ODBC-288) - Connector misses "interactive client" option.\
  Added INTERACTIVE connection string option to tell server, that the client application is interactive, and interactive\_timeout has to be used.
* [ODBC-202](https://jira.mariadb.org/browse/ODBC-202) - Add charsets recoding function to C/ODBC.\
  Iconv-based conversion function has been moved and adapted from MariaDB Connector/C. It's the same function that was used before. The function is used only on platforms other than Windows.

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-3110-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
