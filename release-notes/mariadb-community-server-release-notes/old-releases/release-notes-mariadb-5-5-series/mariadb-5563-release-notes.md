# MariaDB 5.5.63 Release Notes

The most recent release in the [MariaDB 5.5](broken-reference) series is:[**MariaDB 5.5.68**](mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.63)[Release Notes](mariadb-5563-release-notes.md)[Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5563-changelog.md)[Overview of 5.5](broken-reference)

**Release date:** 30 Jan 2019

This is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

**For a description of** [**MariaDB 5.5**](broken-reference) **see the**[**What is MariaDB 5.5?**](broken-reference) **page.**

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

## Updates & Bug Fixes

[MariaDB 5.5.63](mariadb-5563-release-notes.md) is a maintenance release.

* [HeidiSQL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/graphical-and-enhanced-clients/heidisql) updated to 9.5
* Client library was hardened to reject server requests to send a file by default. It only accepts them if they follow an SQL statement [LOAD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile). An application can still use [mysql\_options](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_options) API method to disable or enable the `MYSQL_OPT_LOCAL_INFILE` option permanently.
* [MDEV-18349](https://jira.mariadb.org/browse/MDEV-18349) - InnoDB file size changes are not safe when file system crashes
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2019-2529](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2529)

## Changelog

A full list of all changes is in the [changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5563-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 5.5.63](mariadb-5563-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-5-5-63-now-available/).

Thanks, and enjoy MariaDB!

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
