# MariaDB Connector/C 3.1.21 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-c-3-1-21-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-31-changelogs/mariadb-connector-c-3-1-21-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 22 May 2023

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Notable changes

Updated bundled zlib library (version 1.2.13)

## Issues fixed:

* [CONC-619](https://jira.mariadb.org/browse/CONC-619): Fixed NULL pointer dereference in unpack\_fields().
* [CONC-632](https://jira.mariadb.org/browse/CONC-632): Clear server status and remove pending result sets in mysql\_reset\_connection().
* [CONC-633](https://jira.mariadb.org/browse/CONC-633): If prepare step failed in mariadb\_stmt\_execute\_direct now both mysql\_stmt\_error and mysql\_error return the error message from prepare step instead of error message of execute.
* [CONC-635](https://jira.mariadb.org/browse/CONC-635): Disable TLS for named pipe and shared memory connections.
* [CONC-637](https://jira.mariadb.org/browse/CONC-637): Fixed build if GSSAPI plugin is disabled
* [CONC-638](https://jira.mariadb.org/browse/CONC-638): Fixed memory leak in ps\_bugs unittest
* [CONC-642](https://jira.mariadb.org/browse/CONC-642): Set CR\_OUT\_OF\_MEMORY error in mysql\_use\_result() api function if allocation of memory failed

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-31-changelogs/mariadb-connector-c-3-1-21-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
