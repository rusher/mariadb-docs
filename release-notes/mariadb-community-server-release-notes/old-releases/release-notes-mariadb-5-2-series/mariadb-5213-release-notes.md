# MariaDB 5.2.13 Release Notes

The most recent release in the [MariaDB 5.2 series](changes-improvements-in-mariadb-5-2.md) is:[**MariaDB 5.2.14**](mariadb-5214-release-notes.md)

[Download](https://downloads.askmonty.org/mariadb/5.2.13) | **Release Notes** | [Changelog](broken-reference) |[Overview of 5.2](changes-improvements-in-mariadb-5-2.md)

**Release date:** 29 Nov 2012

[MariaDB 5.2.13](mariadb-5213-release-notes.md) is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release. In general this means that there are no known serious bugs, except for those marked as feature requests, that no bugs were fixed since last release that caused notable code changes, and that we believe the code is ready for general usage (based on bug inflow).

**For a description of** [**MariaDB 5.2**](changes-improvements-in-mariadb-5-2.md) **see the** [**What is MariaDB 5.2**](changes-improvements-in-mariadb-5-2.md) **page.**

For a list of changes made in [MariaDB 5.2.13](mariadb-5213-release-notes.md), with links to detailed information on each push, see the [MariaDB 5.2.13 Changelog](broken-reference).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands, interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

## Important Security Fixes

* [MariaDB 5.2.13](mariadb-5213-release-notes.md) includes a fix for [CVE-2012-5611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5611), a vulnerability that allowed an authenticated user to crash MariaDB server or to execute arbitrary code with the privileges of the `mysqld` process. This is a serious security issue. We recommend upgrading from older versions as soon as possible.
* A fix is also included for multiple SQL injection vulnerabilities in the replication code. See [MDEV-382](https://jira.mariadb.org/browse/MDEV-382) ([CVE-2012-4414](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-4414)) for details.

## Includes [MariaDB 5.1.66](../release-notes-mariadb-5-1-series/mariadb-5166-release-notes.md) and MySQL 5.1.66

This version of MariaDB includes [MariaDB 5.1.66](../release-notes-mariadb-5-1-series/mariadb-5166-release-notes.md), and by extension, MySQL 5.1.66. See the [MariaDB 5.1.66 Release Notes](../release-notes-mariadb-5-1-series/mariadb-5166-release-notes.md) for the changes made in [MariaDB 5.1.66](../release-notes-mariadb-5-1-series/mariadb-5166-release-notes.md) and see [Changes in MySQL 5.1.66](https://dev.mysql.com/doc/refman/5.1/en/news-5-1-66.html)\
for what changed between this and previous MySQL versions.

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
