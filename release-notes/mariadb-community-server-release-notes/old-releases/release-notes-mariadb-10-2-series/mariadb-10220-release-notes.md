# MariaDB 10.2.20 Release Notes

The most recent release of [MariaDB 10.2](what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.20/)[Release Notes](mariadb-10220-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10220-changelog.md)[Overview of 10.2](what-is-mariadb-102.md)

**Release date:** 24 Dec 2018

[MariaDB 10.2](what-is-mariadb-102.md) is the previous stable series of MariaDB. It is an evolution\
of [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.2.20](mariadb-10220-release-notes.md) will be a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.2**](what-is-mariadb-102.md) **see the**[**What is MariaDB 10.2?**](what-is-mariadb-102.md) **page.**

Upgrading from earlier 10.2.x versions is **highly recommended** for all **Galera** users due to bug [MDEV-12837](https://jira.mariadb.org/browse/MDEV-12837) which caused serious stability issues with earlier versions. See the bug issue page for more information.

Thanks, and enjoy MariaDB!

## Notable Changes

* Data type validation:
  * [MDEV-17833](https://jira.mariadb.org/browse/MDEV-17833): ALTER TABLE is not enforcing prefix index size limit
  * [MDEV-17989](https://jira.mariadb.org/browse/MDEV-17989): InnoDB: Failing assertion: dict\_tf2\_is\_valid(flags, flags2)
* [MDEV-17765](https://jira.mariadb.org/browse/MDEV-17765): Locking bug fix for SPATIAL INDEX
* [MDEV-17923](https://jira.mariadb.org/browse/MDEV-17923), [MDEV-17904](https://jira.mariadb.org/browse/MDEV-17904), [MDEV-17938](https://jira.mariadb.org/browse/MDEV-17938): Fixes for FULLTEXT INDEX
* Fixes for regressions introduced in MariaDB Server 10.2.19 by the backup-safe TRUNCATE TABLE ([MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564), innodb\_safe\_truncate=ON) and innodb\_undo\_log\_truncate:
  * [MDEV-17780](https://jira.mariadb.org/browse/MDEV-17780), [MDEV-17816](https://jira.mariadb.org/browse/MDEV-17816), [MDEV-17849](https://jira.mariadb.org/browse/MDEV-17849), [MDEV-17851](https://jira.mariadb.org/browse/MDEV-17851), [MDEV-17885](https://jira.mariadb.org/browse/MDEV-17885)
* Several improvements to MariaDB Server and backup for dealing with encrypted or page\_compressed pages:
  * [MDEV-12112](https://jira.mariadb.org/browse/MDEV-12112): corruption in encrypted table may be overlooked
  * [MDEV-17958](https://jira.mariadb.org/browse/MDEV-17958): On little-endian systems, remove bug-compatible variant of innodb\_checksum\_algorithm=crc32
  * [MDEV-17957](https://jira.mariadb.org/browse/MDEV-17957): Make innodb\_checksum\_algorithm stricter for strict\_\* values
  * [MDEV-18025](https://jira.mariadb.org/browse/MDEV-18025): mariadb-backup fails to detect corrupted page\_compressed=1 tables
* The [Galera library](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md) in the repositories has been updated to version 25.3.25
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

When upgrading from [MariaDB 10.2.16](mariadb-10216-release-notes.md) or earlier to [MariaDB 10.2.17](mariadb-10217-release-notes.md) or higher,\
running [mysql\_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade) is **required** due to changes introduced in[MDEV-14637](https://jira.mariadb.org/browse/MDEV-14637).

## Changelog

For a complete list of changes made in [MariaDB 10.2.20](mariadb-10220-release-notes.md) with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-10220-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.2.20](mariadb-10220-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-2-20-and-mariadb-connector-c-3-0-8-now-available/).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% @marketo/form formid="4316" formId="4316" %}
