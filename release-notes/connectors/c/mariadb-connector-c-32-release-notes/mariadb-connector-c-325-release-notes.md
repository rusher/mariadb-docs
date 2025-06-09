# MariaDB Connector/C 3.2.5 Release Notes

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-c-325-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-32-changelogs/mariadb-connector-c-325-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 10 Nov 2021

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Notable changes

* [CONC-566](https://jira.mariadb.org/browse/CONC-566): If a stored procedure was executed as server side cursor and server doesn't set the SERVER\_STATUS\_CURSOR\_EXISTS status flag, the result set will not be processed as a server side cursor.
* [MDEV-26761](https://jira.mariadb.org/browse/MDEV-26761): If mariadb\_stmt\_execute\_direct fails, the number of parameters (obtained by response packet of mysql\_stmt\_prepare) will be set back to the number of prebinded parameters to avoid memory overrun.
* [CONC-568](https://jira.mariadb.org/browse/CONC-568): The API function mysql\_load\_plugin\_v() now returns the plugin handle (instead of raising an error and returning a NULL handle) even if the plugin was already loaded. This will avoid possible race conditions, when one thread is loading the plugin while another thread waits for the lock to load the same plugin.
* Xcode compatibility update (Thanks to Sergei Krivonos for his contribution)
* [CONC-570](https://jira.mariadb.org/browse/CONC-570): Removed callback function for crypto threads, since the callback function cannot be cleared (this affects OpenSSL <= 1.0.2 only)

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-32-changelogs/mariadb-connector-c-325-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
