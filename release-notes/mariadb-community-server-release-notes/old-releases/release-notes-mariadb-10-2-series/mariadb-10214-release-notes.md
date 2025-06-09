# MariaDB 10.2.14 Release Notes

The most recent release of [MariaDB 10.2](what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.14)[Release Notes](mariadb-10214-release-notes.md)[Changelog](../../../changelogs/changelogs-mariadb-102-series/mariadb-10214-changelog.md)[Overview of 10.2](what-is-mariadb-102.md)

**Release date:** 27 Mar 2018

[MariaDB 10.2](what-is-mariadb-102.md) is the current stable series of MariaDB. It is an evolution\
of [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.2.14](mariadb-10214-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.2**](what-is-mariadb-102.md) **see the**[**What is MariaDB 10.2?**](what-is-mariadb-102.md) **page.**

Upgrading from earlier 10.2.x versions is **highly recommended** for all **Galera** users due to bug [MDEV-12837](https://jira.mariadb.org/browse/MDEV-12837) which caused serious stability issues with earlier versions. See the bug issue page for more information.

Thanks, and enjoy MariaDB!

## Notable Changes

* [MyRocks](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks) is now [Gamma (RC)](../../../mariadb-release-criteria.md)
* [MDEV-14533](https://jira.mariadb.org/browse/MDEV-14533) - Added the [DISKS plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-disks-table), for monitoring disk space
* [MDEV-14611](https://jira.mariadb.org/browse/MDEV-14611) - [ALTER TABLE EXCHANGE PARTITION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) does not work properly when used with DATA DIRECTORY.
* [MDEV-15333](https://jira.mariadb.org/browse/MDEV-15333) - MariaDB (still) slow start
* [MDEV-12255](https://jira.mariadb.org/browse/MDEV-12255) - Wrong result with [innodb\_prefix\_index\_cluster\_optimization](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables)
* [MDEV-12396](https://jira.mariadb.org/browse/MDEV-12396) - [IMPORT TABLESPACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#import-tablespace) cleanup
* [MDEV-14648](https://jira.mariadb.org/browse/MDEV-14648) - Restore fix for MySQL BUG#39053 - [UNINSTALL PLUGIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin) does not allow the storage engine to cleanup open connections
* [MDEV-15249](https://jira.mariadb.org/browse/MDEV-15249) - IMPORT fixes
* [MDEV-14988](https://jira.mariadb.org/browse/MDEV-14988) - [innodb\_read\_only](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) tries to modify files if transactions were recovered in COMMITTED state
* [MDEV-14773](https://jira.mariadb.org/browse/MDEV-14773) - [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table) hangs for InnoDB table with [FULLTEXT index](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes) (fixing a recent regression from upstream)
* [MDEV-15529](https://jira.mariadb.org/browse/MDEV-15529) - IMPORT TABLESPACE unnecessarily uses the doublewrite buffer
* [MDEV-15554](https://jira.mariadb.org/browse/MDEV-15554) - InnoDB page\_cleaner shutdown sometimes hangs
* [MDEV-14545](https://jira.mariadb.org/browse/MDEV-14545) - [Mariabackup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backing-up-and-restoring-databases/mariabackup) - Backup fails due to MLOG\_INDEX\_LOAD record
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

## Notes

For a complete list of changes made in [MariaDB 10.2.14](mariadb-10214-release-notes.md) with links to detailed\
information on each push, see the [changelog](../../../changelogs/changelogs-mariadb-102-series/mariadb-10214-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.2.14](mariadb-10214-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-2-14-mariadb-10-1-32-and-mariadb-connector-j-2-2-3-and-1-7-3-now-available/).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
