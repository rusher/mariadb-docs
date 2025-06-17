# MariaDB Connector/ODBC 3.0.5 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-odbc/3.0.5)[Release Notes](mariadb-connector-odbc-305-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-30-changelogs/mariadb-connector-odbc-305-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 12 Jun 2018

This is a [Stable (GA)](../../../mariadb-release-criteria.md) release of MariaDB Connector/ODBC 3.0.

MariaDB Connector/ODBC 3.0.5 is built on top of[MariaDB Connector/C v.3.0.5](../../c/mariadb-connector-c-30-release-notes/mariadb-connector-c-305-release-notes.md). It also includes all fixes from [MariaDB Connector/C v.3.0.4](../../c/mariadb-connector-c-30-release-notes/mariadb-connector-c-304-release-notes.md).

## Bug Fixes

* [ODBC-146](https://jira.mariadb.org/browse/ODBC-146) Wrong decimal value (0) when after longtext field in select clause (using ADO, client side cursor)
* Testing connector against last server build on travis. Those tests permit to check early regression and might failed, so tagged as "Allowed Failures" on travis
* [ODBC-126](https://jira.mariadb.org/browse/ODBC-126) Fetching Multiple Result Set Crash - fix of the case, not covered by this bug fix in previous release
* Connector library now does not export anything beyond the API
* [ODBC-141](https://jira.mariadb.org/browse/ODBC-141) Error using LOAD DATA INFILE
* [ODBC-143](https://jira.mariadb.org/browse/ODBC-143) Wrong SQL\_IDENTIFIER\_QUOTE\_CHAR info in case of ANSI\_QUOTES
* [ODBC-138](https://jira.mariadb.org/browse/ODBC-138) Connector could sometimes return wrong datetime value
* Connector/ODBC is now built with Connector/C as a git sub-project. That fixes build issues like [ODBC-39](https://jira.mariadb.org/browse/ODBC-39), [ODBC-40](https://jira.mariadb.org/browse/ODBC-40), [ODBC-124](https://jira.mariadb.org/browse/ODBC-124) and [ODBC-135](https://jira.mariadb.org/browse/ODBC-135)
* [ODBC-133](https://jira.mariadb.org/browse/ODBC-133) Incorrect return values for decimal data type
* [ODBC-137](https://jira.mariadb.org/browse/ODBC-137) ODBC and Swedish characters
* [ODBC-91](https://jira.mariadb.org/browse/ODBC-91) If the connection handles was reused, the connector would try to use default database from previous connection (and if there wasn't such database the connect would fail)

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-30-changelogs/mariadb-connector-odbc-305-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
