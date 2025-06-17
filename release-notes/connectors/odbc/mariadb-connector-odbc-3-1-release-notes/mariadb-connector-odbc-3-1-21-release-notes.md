# MariaDB Connector/ODBC 3.1.21 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/odbc-connector)[Release Notes](mariadb-connector-odbc-3-1-21-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-3-1-21-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 24 Feb 2025

This is a [Stable (GA)](../../../mariadb-release-criteria.md) release of MariaDB Connector/ODBC 3.1.

MariaDB Connector/ODBC 3.1.21 is built on top of[MariaDB Connector/C v.3.3.14](../../c/mariadb-connector-c-33-release-notes/mariadb-connector-c-3-3-14-release-notes.md).

## Bug Fixes

* [ODBC-405](https://jira.mariadb.org/browse/ODBC-405) -Values of DECIMAL type variables cannot be read. Reading the recordset's field values causes error "Multiple-step OLE DB operation generated errors. Check each OLE DB status value, if available. No work was done."
* [ODBC-418](https://jira.mariadb.org/browse/ODBC-418) - Widechar string data gets truncated if contains NULL character
* [ODBC-430](https://jira.mariadb.org/browse/ODBC-430) - The maximum size of VARCHAR and VARBINARY is 65535, while SQLGetTypeInfo reports 255 for them
* [ODBC-435](https://jira.mariadb.org/browse/ODBC-435) - SQLPrimaryKeys call returns incorrect KEY\_SEQ field
* [ODBC-443](https://jira.mariadb.org/browse/ODBC-443) - Incorrect value for charset utf8mb4 and longtext column with multibyte unicode characters
* [ODBC-448](https://jira.mariadb.org/browse/ODBC-448) - Fetching bigint data to double buffer fails for big values

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-3-1-21-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
