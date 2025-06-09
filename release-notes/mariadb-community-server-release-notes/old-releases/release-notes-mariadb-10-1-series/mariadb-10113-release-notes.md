# MariaDB 10.1.13 Release Notes

The most recent release of [MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.13)[Release Notes](mariadb-10113-release-notes.md)[Changelog](../../../changelogs/changelogs-mariadb-101-series/mariadb-10113-changelog.md)[Overview of 10.1](changes-improvements-in-mariadb-10-1.md)

**Release date:** 25 Mar 2016

[MariaDB 10.1](changes-improvements-in-mariadb-10-1.md) is the current stable series of MariaDB. It is an evolution\
of [MariaDB 10.0](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.1.13](mariadb-10113-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.1**](changes-improvements-in-mariadb-10-1.md) **see the**[**What is MariaDB 10.1?**](../release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* [MDEV-9659](https://jira.mariadb.org/browse/MDEV-9659) [AWS Key management encryption plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin) (currently distributed in source form only).
* [MDEV-6058](https://jira.mariadb.org/browse/MDEV-6058) new server variables; [log\_slow\_admin\_statements](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#log_slow_admin_statements) and [log\_slow\_slave\_statements](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables).
* [MDEV-9443](https://jira.mariadb.org/browse/MDEV-9443) [CREATE ROLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/create-role) and [DROP ROLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/drop-role) are now allowed in [prepared statements](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/prepared-statements).
* [MDEV-9640](https://jira.mariadb.org/browse/MDEV-9640) [INFORMATION\_SCHEMA.INNODB\_TABLESPACES\_ENCRYPTION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_tablespaces_encryption-table) has a new column; `key_id`.
* The [Galera library](https://codership.com/content/using-galera-cluster) has\
  been updated to version 25.3.15.
* The [plugin maturity](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/information-on-plugins/list-of-plugins) has been updated for a number of plugins.
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

### Added Distributions

A repository for the newly-released Ubuntu 16.04 "xenial" has been added.\
Currently the repository is using packages built on Ubuntu 15.10 "wily", but in\
the next release they will be built on xenial builders.

* [MDEV-9781](https://jira.mariadb.org/browse/MDEV-9781) - APT 1.2.7 (and later) prefers SHA2 GPG keys and now prints warnings when a repository is signed using a SHA1 key. We have created a new SHA2 key for use with our Ubuntu 16.04 "xenial" repository.
  * The Key ID is: `C74CD1D8`
  * The full fingerprint of the new key is: `177F 4010 FE56 CA33 3630 0305 F165 6F24 C74C D1D8`
  * The key can be added using the following command:

```bash
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
```

The instructions in the[repository configuration tool](https://downloads.mariadb.org/mariadb/repositories/)\
for Ubuntu 16.04 "xenial" have been updated to refer to this new key.\
Repositories for previous versions of Ubuntu will continue to use the old key.

## Changelog

For a complete list of changes made in [MariaDB 10.1.13](mariadb-10113-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../../changelogs/changelogs-mariadb-101-series/mariadb-10113-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
