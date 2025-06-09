# MariaDB 5.5.45 Release Notes

The most recent release in the [MariaDB 5.5](broken-reference) series is:[**MariaDB 5.5.68**](mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.45)[Release Notes](mariadb-5545-release-notes.md)[Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5545-changelog.md)[Overview of 5.5](broken-reference)

**Release date:** 6 Aug 2015

This is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release. In general this\
means that there are no known serious bugs, except for those marked as feature\
requests, that no bugs were fixed since last release that caused notable code\
changes, and that we believe the code is ready for general usage (based on bug\
inflow).

**For a description of** [**MariaDB 5.5**](broken-reference) **see the**[**What is MariaDB 5.5?**](broken-reference) **page.**

For a list of changes made in this release, with links to detailed\
information on each push, see the[MariaDB 5.5.45 Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5545-changelog.md).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

### Updates & Bug Fixes

[MariaDB 5.5.45](mariadb-5545-release-notes.md) is a maintenance release. It includes several bugfixes and\
updates, including from MySQL 5.5.45. Notable updates include:

* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to 5.5.44-37.3
* Diffie-Helman modulus increased to 2048 bits ([MDEV-8352](https://jira.mariadb.org/browse/MDEV-8352))
* Add [mysqlbinlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) --binlog-row-event-max-size support ([MDEV-8340](https://jira.mariadb.org/browse/MDEV-8340))
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2015-4816](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4816)
  * [CVE-2015-4819](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4819)
  * [CVE-2015-4879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4879)

A full list of all changes is in the [changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5545-changelog.md).

Thanks, and enjoy MariaDB!

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
