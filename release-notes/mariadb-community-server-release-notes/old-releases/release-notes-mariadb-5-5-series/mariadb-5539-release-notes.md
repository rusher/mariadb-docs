# MariaDB 5.5.39 Release Notes

The most recent release in the [MariaDB 5.5](changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.39)[Release Notes](mariadb-5539-release-notes.md)[Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5539-changelog.md)[Overview of 5.5](broken-reference/)

**Release date:** 5 Aug 2014

This is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release. In general this\
means that there are no known serious bugs, except for those marked as feature\
requests, that no bugs were fixed since last release that caused notable code\
changes, and that we believe the code is ready for general usage (based on bug\
inflow).

**For a description of** [**MariaDB 5.5**](broken-reference/) **see the**[**What is MariaDB 5.5?**](broken-reference/) **page.**

For a list of changes made in this release, with links to detailed\
information on each push, see the[MariaDB 5.5.39 Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5539-changelog.md).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

### Updates & Bug Fixes

[MariaDB 5.5.39](mariadb-5539-release-notes.md) is a maintenance release. It includes several bugfixes and updates, including\
from MySQL 5.5.39. Notable updates include:

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2014-4274](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-4274)
  * [CVE-2014-4287](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-4287)
  * [CVE-2014-6463](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6463)
  * [CVE-2014-6478](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6478)
  * [CVE-2014-6484](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6484)
  * [CVE-2014-6495](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6495)
  * [CVE-2014-6505](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6505)
  * [CVE-2014-6520](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6520)
  * [CVE-2014-6530](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6530)
  * [CVE-2014-6551](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6551)
  * [CVE-2015-0391](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0391)
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to the version from [Percona Server 5.5.38-35.2](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.38-35.2.html)
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/tokudb) updated to [version 7.1.7](https://docs.tokutek.com/tokudb/tokudb-release-notes.html#tokudb-7-1-7)
* The [timed\_mutexes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#timed_mutexes) system variable has been deprecated, as it no longer has any effect.

A full list of all changes is in the [changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5539-changelog.md).

Thanks, and enjoy MariaDB!

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
