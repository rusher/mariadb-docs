# MariaDB 10.2.6 Release Notes

The most recent release of [MariaDB 10.2](what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.6)[Release Notes](mariadb-1026-release-notes.md)[Changelog](../../../changelogs/changelogs-mariadb-102-series/mariadb-1026-changelog.md)[Overview of 10.2](what-is-mariadb-102.md)

**Release date:** 23 May 2017

[MariaDB 10.2](what-is-mariadb-102.md) is the current stable series of MariaDB. It is an evolution\
of [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.2.6](mariadb-1026-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.2**](what-is-mariadb-102.md) **see the**[**What is MariaDB 10.2?**](what-is-mariadb-102.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

This is the first stable release in the [MariaDB 10.2](what-is-mariadb-102.md) series. As such, please refer to the [What is MariaDB 10.2?](what-is-mariadb-102.md) page for details on all of the new features.

* [MyRocks](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/building-myrocks-in-mariadb) alpha storage engine added ([MDEV-9658](https://jira.mariadb.org/browse/MDEV-9658))
* [Window functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions) have been introduced.
* Recursive Common Table Expressions ([MDEV-9864](https://jira.mariadb.org/browse/MDEV-9864))
* [AWS Key Management plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin) added for Windows, CentOS, RHEL, and Fedora packages
* Update InnoDB to 5.7.18 ([MDEV-11751](https://jira.mariadb.org/browse/MDEV-11751))
* [Galera wsrep library](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md) updated to 25.3.20
* Packages for Ubuntu 17.04 "zesty" [added](https://downloads.mariadb.org/mariadb/repositories/)
* [MDEV-10431](https://jira.mariadb.org/browse/MDEV-10431): The `--add-drop-trigger` option has been added to [mysqldump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump)
* [MDEV-12472](https://jira.mariadb.org/browse/MDEV-12472): Ignore XtraDB-specific parameters in InnoDB, warning that they are ignored
* [MDEV-12253](https://jira.mariadb.org/browse/MDEV-12253), [MDEV-12602](https://jira.mariadb.org/browse/MDEV-12602): Numerous Encryption fixes
* [MDEV-11336](https://jira.mariadb.org/browse/MDEV-11336): Disabled defragmentation
* [MDEV-10332](https://jira.mariadb.org/browse/MDEV-10332): Added support for OpenSSL 1.1 and LibreSSL
* [innodb\_deadlock\_detect](mariadb-1026-release-notes.md#xtradbinnodb-server-system-variables/) and [innodb\_stats\_include\_delete\_marked](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) variables introduced
* [MDEV-11117](https://jira.mariadb.org/browse/MDEV-11117): [Auto\_increment](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/auto_increment) columns are no longer permitted in [CHECK constraints](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/constraint), [DEFAULT value expressions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table#default) and [virtual columns](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/generated-columns). They were permitted in earlier versions, but did not work correctly.
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2017-3308](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3308)
  * [CVE-2017-3309](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3309)
  * [CVE-2017-3453](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3453)
  * [CVE-2017-3456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3456)
  * [CVE-2017-3464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3464)

## Notes

* [Percona XtraBackup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview) (as of 2.4) will not work with [MariaDB 10.2](what-is-mariadb-102.md) (and [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md)) compression. However, MariaDB's fork, [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backing-up-and-restoring-databases/mariabackup), will work with compression. A beta version of Mariabackup was included in [MariaDB 10.2.7](mariadb-1027-release-notes.md) and declared stable in [MariaDB 10.2.10](mariadb-10210-release-notes.md).

A file format compatibility bug that was introduced in [MariaDB 10.2.2](mariadb-1022-release-notes.md) was present in this release.\
Creating tables with the attribute [page\_compressed=yes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-page-compression) created InnoDB internal data dictionary records that are incompatible with [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md). [MariaDB 10.2.7](mariadb-1027-release-notes.md) and later will write the dictionary records in a format that is compatible with [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) and will also support the malformed metadata from affected 10.2 versions.**This bug may prevent a downgrade from later** [**MariaDB 10.2**](what-is-mariadb-102.md) **versions to** [**MariaDB 10.2.6**](mariadb-1026-release-notes.md)**.**[See the commit for details.](https://github.com/MariaDB/server/commit/72378a25830184f91005be7e80cfb28381c79f23)

## Changelog

For a complete list of changes made in [MariaDB 10.2.6](mariadb-1026-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../../changelogs/changelogs-mariadb-102-series/mariadb-1026-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
