# Release Notes for MariaDB Enterprise Server 10.3.18-3

This third release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.3 is a maintenance release, including a variety of fixes.

MariaDB Enterprise Server 10.3.18-3 was released on 2019-09-30.

## Issues Fixed

### Can result in data loss

* Due to a race condition in InnoDB, an exclusive lock to an inserted record could be wrongly granted to multiple transactions when the [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) transaction commits. This could lead to a server crash or data loss. ([MDEV-15326](https://jira.mariadb.org/browse/MDEV-15326))
* INSERT...ON DUPLICATE KEY UPDATE, when there is more than one key, could result in inconsistent data between master and slave for replication mode [MIXED](https://mariadb.com/kb/en/MIXED) and [STATEMENT](https://mariadb.com/kb/en/STATEMENT). This has been fixed for [MIXED](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-3/MIXED/README.md), but cannot be controlled by the replication for [STATEMENT](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-3/STATEMENT/README.md) based replication.
* Inconsistent Slaves need to be set up again from the Master. ([MDEV-17614](https://jira.mariadb.org/browse/MDEV-17614))
* Wrong value on instantly added column can occur after [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) and a following [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) of PRIMARY KEY. ([MDEV-20066](https://jira.mariadb.org/browse/MDEV-20066))

### Can result in a hang or crash

* Replication could hang for [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) transactions as [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) has its own concurrency control [innodb\_thread\_concurrency](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_thread_concurrency). ([MDEV-20247](https://jira.mariadb.org/browse/MDEV-20247))
* Fix potential crash in ON UPDATE CASCADE when the foreign table is [system versioned](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables). ([MDEV-20311](https://jira.mariadb.org/browse/MDEV-20311))

### Can result in unexpected behavior

* After setting SET [foreign\_key\_checks=0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#foreign_key_checks) it is possible to drop indexes from referenced (parent) tables, which could cause [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) to behave as if table `doesn't exist in engine` ([MDEV-17187](https://jira.mariadb.org/browse/MDEV-17187))
* Fix for corner case where [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backing-up-and-restoring-databases/mariabackup) could fail because encrypted data files could not be copied if created shortly before the backup was started. ([MDEV-18128](https://jira.mariadb.org/browse/MDEV-18128))
* [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backing-up-and-restoring-databases/mariabackup) could fail in the prepare face if the redo log is bigger than 512GB. ([MDEV-20060](https://jira.mariadb.org/browse/MDEV-20060))
* Basic 3-way join queries are not parsed. ([MDEV-19421](https://jira.mariadb.org/browse/MDEV-19421))

### Related to performance

* Optimized scanning of the undo log versions while scanning the secondary index versions. ([MDEV-20301](https://jira.mariadb.org/browse/MDEV-20301))

## Interface Changes

* [in\_predicate\_conversion\_threshold](https://mariadb.com/kb/en/*_server-system-variables/#in_predicate_conversion_threshold) system variable added
* [mysqld --in-predicate-conversion-threshold](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) command-line option added

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.3.18-3 is provided for:

* CentOS 8
* CentOS 7
* CentOS 6
* Debian 10
* Debian 9
* Debian 8
* Red Hat Enterprise Linux 8
* Red Hat Enterprise Linux 7
* Red Hat Enterprise Linux 6
* Ubuntu 18.04
* Ubuntu 16.04
* Microsoft Windows

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies)".

#### Note

CentOS 6, Debian 8, and Red Hat Enterprise Linux 6 are no longer supported as per the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies). Older releases are available from the [MariaDB Downloads page](https://mariadb.com/downloads). Instructions for installation are included as a README file within the download.

Copyright © 2025 MariaDB
