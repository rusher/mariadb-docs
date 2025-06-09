# MariaDB 10.6.7 Release Notes

The most recent release of [MariaDB 10.6](what-is-mariadb-106.md) is:[**MariaDB 10.6.21**](mariadb-10-6-21-release-notes.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.6.21/)

[Download 10.6.7](https://downloads.mariadb.org/mariadb/10.6.7)[Release Notes](mariadb-1067-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-106-series/mariadb-1067-changelog.md)[Overview of 10.6](what-is-mariadb-106.md)

**Release date:** 12 Feb 2022

[MariaDB 10.6](what-is-mariadb-106.md) is the current long-term maintenance stable series of MariaDB. It is an evolution\
of [MariaDB 10.5](../mariadb-10-5-series/what-is-mariadb-105.md) with several entirely new features.

[MariaDB 10.6.7](mariadb-1067-release-notes.md) is a [_**Stable (GA)**_](../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.6**](what-is-mariadb-106.md) **see the**[**What is MariaDB 10.6?**](what-is-mariadb-106.md) **page.**

Thanks, and enjoy MariaDB!

* This release fixes a blocking problem with the [MariaDB 10.6.6](mariadb-1066-release-notes.md) release when manually running [mariadb-upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade). ([MDEV-27789](https://jira.mariadb.org/browse/MDEV-27789))
* See [MariaDB 10.6.6](mariadb-1066-release-notes.md) for other changes since the previous release.

### InnoDB

* Set [innodb\_change\_buffering=none](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_change_buffering) by default ([MDEV-27734](https://jira.mariadb.org/browse/MDEV-27734))

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2021-46665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46665)
  * [CVE-2021-46664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46664)
  * [CVE-2021-46661](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46661)
  * [CVE-2021-46668](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46668)
  * [CVE-2021-46663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46663)

## Changelog

For a complete list of changes and bugfixes made in [MariaDB 10.6.7](mariadb-1067-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-106-series/mariadb-1067-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.6.7](mariadb-1067-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-8-2-rc-and-mariadb-10-7-3-10-6-7-10-5-15-10-4-24-10-3-34-and-10-2-43-now-available/).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
