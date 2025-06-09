# MariaDB 5.5.40 Release Notes

The most recent release in the [MariaDB 5.5](broken-reference) series is:[**MariaDB 5.5.68**](mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.40)[Release Notes](mariadb-5540-release-notes.md)[Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5540-changelog.md)[Overview of 5.5](broken-reference)

**Release date:** 9 Oct 2014

This is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release. In general this\
means that there are no known serious bugs, except for those marked as feature\
requests, that no bugs were fixed since last release that caused notable code\
changes, and that we believe the code is ready for general usage (based on bug\
inflow).

**For a description of** [**MariaDB 5.5**](broken-reference) **see the**[**What is MariaDB 5.5?**](broken-reference) **page.**

For a list of changes made in this release, with links to detailed\
information on each push, see the[MariaDB 5.5.40 Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5540-changelog.md).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

### Updates & Bug Fixes

[MariaDB 5.5.40](mariadb-5540-release-notes.md) is a maintenance release. It includes several bugfixes and updates, including\
from MySQL 5.5.40. Notable updates include:

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2014-6507](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6507)
  * [CVE-2014-6491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6491)
  * [CVE-2014-6500](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6500)
  * [CVE-2014-6469](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6469)
  * [CVE-2014-6555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6555)
  * [CVE-2014-6559](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6559)
  * [CVE-2014-6494](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6494)
  * [CVE-2014-6496](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6496)
  * [CVE-2014-6464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6464)
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to the version from [Percona Server 5.5.40-36.1](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.40-36.1.html)
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/tokudb) updated to [version 7.5.0](https://docs.tokutek.com/tokudb/tokudb-release-notes.html#tokudb-7-5-0)
* As per the [MariaDB Deprecation Policy](../../../mariadb-platform-deprecation-policy.md), this will be the last release of [MariaDB 5.5](broken-reference) for both Ubuntu 13.10 "Saucy" and Mint 16 "Petra".
* With the recent release of CentOS 7 and RHEL 7, we are pleased to now provide packages for both distributions. Instructions for how to enable the repositories can be found by visiting the "[Installing MariaDB with YUM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum)" page and the [repository configuration tool](https://downloads.mariadb.org/mariadb/repositories/).\
  A full list of all changes is in the [changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5540-changelog.md).

Thanks, and enjoy MariaDB!

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
