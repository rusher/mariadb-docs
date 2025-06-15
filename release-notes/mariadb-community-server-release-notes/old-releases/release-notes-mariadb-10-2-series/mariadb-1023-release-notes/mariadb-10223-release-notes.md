# MariaDB 10.2.23 Release Notes

The most recent release of [MariaDB 10.2](../what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.23/)[Release Notes](mariadb-10223-release-notes.md)[Changelog](../../../../changelogs/changelogs-mariadb-102-series/mariadb-10223-changelog.md)[Overview of 10.2](../what-is-mariadb-102.md)

**Release date:** 25 Mar 2019

[MariaDB 10.2](../what-is-mariadb-102.md) is the previous stable series of MariaDB. It is an evolution\
of [MariaDB 10.1](../../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.2.23](mariadb-10223-release-notes.md) will be a [_**Stable (GA)**_](../../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.2**](../what-is-mariadb-102.md) **see the**[**What is MariaDB 10.2?**](../what-is-mariadb-102.md) **page.**

Upgrading from earlier 10.2.x versions is **highly recommended** for all**Galera** users due to bug [MDEV-12837](https://jira.mariadb.org/browse/MDEV-12837) which caused serious stability issues\
with earlier versions. See the bug issue page for more information.

Thanks, and enjoy MariaDB!

## Notable Changes

* InnoDB `ALTER TABLE` fixes: [MDEV-18016](https://jira.mariadb.org/browse/MDEV-18016), [MDEV-18630](https://jira.mariadb.org/browse/MDEV-18630), [MDEV-18775](https://jira.mariadb.org/browse/MDEV-18775), [MDEV-18732](https://jira.mariadb.org/browse/MDEV-18732),[MDEV-18749](https://jira.mariadb.org/browse/MDEV-18749), [MDEV-18637](https://jira.mariadb.org/browse/MDEV-18637), [MDEV-13818](https://jira.mariadb.org/browse/MDEV-13818), [MDEV-17595](https://jira.mariadb.org/browse/MDEV-17595)
* Performance improvements:
  * [MDEV-18878](https://jira.mariadb.org/browse/MDEV-18878): InnoDB Purge: Optimize away futile table lookups
  * [MDEV-14984](https://jira.mariadb.org/browse/MDEV-14984): Regression in connect performance
  * [MDEV-18936](https://jira.mariadb.org/browse/MDEV-18936): Purge thread fails to exit on shutdown
* Corruption bug fixes:
  * [MDEV-18272](https://jira.mariadb.org/browse/MDEV-18272): InnoDB fails to rollback after exceeding FOREIGN KEY recursion depth
  * [MDEV-9519](https://jira.mariadb.org/browse/MDEV-9519): Data corruption on Galera cluster size change
* [Mariabackup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backing-up-and-restoring-databases/mariabackup):
  * [MDEV-18204](https://jira.mariadb.org/browse/MDEV-18204): fix incremental MyRocks backup
  * [MDEV-18611](https://jira.mariadb.org/browse/MDEV-18611): mariabackup terminated while copying InnoDB redo log
  * [MDEV-18669](https://jira.mariadb.org/browse/MDEV-18669): mariabackup writes timestamp in version line
  * [MDEV-18855](https://jira.mariadb.org/browse/MDEV-18855): Mariabackup should fetch innodb\_compression\_level from running server
* Debug symbols on CentOS 7, RHEL 7, and SLES 12 distributions have been moved\
  into `debuginfo` packages ([MDEV-18893](https://jira.mariadb.org/browse/MDEV-18893))
* The [Galera library](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md) in the repositories has\
  been updated to version 25.3.26
* As per the [MariaDB Deprecation Policy](../../../../mariadb-platform-deprecation-policy.md), this will be\
  the last release of [MariaDB 10.2](../what-is-mariadb-102.md) for Ubuntu 14.04 Trusty,\
  Debian has also stopped supporting the ppc64el architecture for Debian 8\
  Jessie and so this is the last release of [MariaDB 10.2](../what-is-mariadb-102.md) on Jessie for that\
  architecture
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

When upgrading from [MariaDB 10.2.16](../mariadb-10216-release-notes.md) or earlier to [MariaDB 10.2.17](../mariadb-10217-release-notes.md) or higher,\
running `[mysql_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade)` is **required** due to changes introduced in[MDEV-14637](https://jira.mariadb.org/browse/MDEV-14637).

## Changelog

For a complete list of changes made in [MariaDB 10.2.23](mariadb-10223-release-notes.md) with links to detailed\
information on each push, see the [changelog](../../../../changelogs/changelogs-mariadb-102-series/mariadb-10223-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.2.23](mariadb-10223-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-2-23-and-mariadb-connector-j-2-4-1-now-available/).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
