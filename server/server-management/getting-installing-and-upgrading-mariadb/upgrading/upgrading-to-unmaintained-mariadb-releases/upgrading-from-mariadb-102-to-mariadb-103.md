
# Upgrading from MariaDB 10.2 to MariaDB 10.3


### How to Upgrade


For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md) instead.


For MariaDB Galera Cluster, see [Upgrading from MariaDB 10.2 to MariaDB 10.3 with Galera Cluster](https://mariadb.com/kb/en/upgrading-from-mariadb-102-to-mariadb-103-with-galera-cluster) instead.


Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [Mariabackup](../../../backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md).



The suggested upgrade procedure is:


1. Modify the repository configuration, so the system's package manager installs [MariaDB 10.3](../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md). For example,

  * On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](../../binary-packages/rpm/yum.md#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
  * On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](../../binary-packages/rpm/installing-mariadb-with-zypper.md#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.
1. [Stop MariaDB](../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md). The server should be cleanly shut down, with no incomplete transactions remaining. [innodb_fast_shutdown](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown) must be set to `0` or `1` and [innodb_force_recovery](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_force_recovery) must be less than `3`.
1. Uninstall the old version of MariaDB.

  * On Debian, Ubuntu, and other similar Linux distributions, execute the following: 
`sudo apt-get remove mariadb-server`
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, execute the following: 
`sudo yum remove MariaDB-server`
  * On SLES, OpenSUSE, and other similar Linux distributions, execute the following: 
`sudo zypper remove MariaDB-server`
1. Install the new version of MariaDB.

  * On Debian, Ubuntu, and other similar Linux distributions, see [Installing MariaDB Packages with APT](../../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md#installing-mariadb-packages-with-apt) for more information.
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Installing MariaDB Packages with YUM](../../binary-packages/rpm/yum.md#installing-mariadb-packages-with-yum) for more information.
  * On SLES, OpenSUSE, and other similar Linux distributions, see [Installing MariaDB Packages with ZYpp](../../binary-packages/rpm/installing-mariadb-with-zypper.md#installing-mariadb-packages-with-zypp) for more information.
1. Make any desired changes to configuration options in [option files](../../configuring-mariadb-with-option-files.md), such as `my.cnf`. This includes removing any options that are no longer supported.
1. [Start MariaDB](../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
1. Run `[mysql_upgrade](../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md)`.

  * `mysql_upgrade` does two things:

    1. Ensures that the system tables in the `[mysq](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md)l` database are fully compatible with the new version.
    1. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .


### Incompatible Changes Between 10.2 and 10.3


On most servers upgrading from 10.2 should be painless. However, there are some things that have changed which could affect an upgrade:


#### Options That Have Changed Default Values



| Option | Old default value | New default value |
| --- | --- | --- |
| Option | Old default value | New default value |
| [innodb_flush_method](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_flush_method) | (empty) | fsync |
| [innodb_spin_wait_delay](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_spin_wait_delay) | 6 | 4 |
| [performance_schema_max_stage_classes](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_stage_classes) | 150 | 160 |
| [plugin_maturity](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#plugin_maturity) | unknown | One less than the server maturity |



#### Options That Have Been Removed or Renamed


The following options should be removed or renamed if you use them in your [option files](../../configuring-mariadb-with-option-files.md):



| Option | Reason |
| --- | --- |
| Option | Reason |
| [innodb_buffer_pool_populate](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_populate) | Used in XtraDB-only |
| [innodb_cleaner_lsn_age_factor](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_cleaner_lsn_age_factor) | Used in XtraDB-only |
| [innodb_corrupt_table_action](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_corrupt_table_action) | Used in XtraDB-only |
| [innodb_empty_free_list_algorithm](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_empty_free_list_algorithm) | Used in XtraDB-only |
| [innodb_fake_changes](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_fake_changes) | Used in XtraDB-only |
| [innodb_file_format](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_file_format) | The [InnoDB file format](../../../../reference/storage-engines/innodb/innodb-file-format.md) is now Barracuda, and the old Antelope file format is no longer supported. |
| [innodb_file_format_check](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_file_format_check) | No longer necessary as the Antelope [InnoDB file format](../../../../reference/storage-engines/innodb/innodb-file-format.md) is no longer supported. |
| [innodb_file_format_max](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_file_format_max) | No longer necessary as the Antelope [InnoDB file format](../../../../reference/storage-engines/innodb/innodb-file-format.md) is no longer supported. |
| [innodb_foreground_preflush](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_foreground_preflush) | Used in XtraDB-only |
| [innodb_instrument_semaphores](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_instrument_semaphores) |  |
| [innodb_kill_idle_transaction](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_kill_idle_transaction) | Used in XtraDB-only |
| [innodb_large_prefix](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_large_prefix) | Large index key prefixes were made default from [MariaDB 10.2](../../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md), and limiting tables to small prefixes is no longer permitted in [MariaDB 10.3](../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md). |
| [innodb_locking_fake_changes](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_locking_fake_changes) | Used in XtraDB-only |
| [innodb_log_arch_dir](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_arch_dir) | Used in XtraDB-only |
| [innodb_log_arch_expire_sec](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_arch_expire_sec) | Used in XtraDB-only |
| [innodb_log_archive](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_archive) | Used in XtraDB-only |
| [innodb_log_block_size](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_block_size) | Used in XtraDB-only |
| [innodb_log_checksum_algorithm](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_checksum_algorithm) | Translated to [innodb_log_checksums](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_checksums) (NONE to OFF, everything else to ON); only existed to allow easier upgrade from earlier XtraDB versions. |
| [innodb_mtflush_threads](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_mtflush_threads) | Replaced by the [innodb_page_cleaners](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_page_cleaners) system variable. |
| [innodb_sched_priority_cleaner](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_sched_priority_cleaner) | Used in XtraDB-only |
| [innodb_show_locks_held](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_show_locks_held) | Used in XtraDB-only |
| [innodb_show_verbose_locks](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_show_verbose_locks) | Used in XtraDB-only |
| [innodb_support_xa](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_support_xa) | XA transactions are always supported. |
| [innodb_use_fallocate](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_fallocate) |  |
| [innodb_use_global_flush_log_at_trx_commit](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_global_flush_log_at_trx_commit) | Used in XtraDB-only |
| [innodb_use_mtflush](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_mtflush) | Replaced by the [innodb_page_cleaners](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_page_cleaners) system variable. |
| [innodb_use_stacktrace](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_stacktrace) | Used in XtraDB-only |
| [innodb_use_trim](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_use_trim) |  |



#### Reserved Words


* New [reserved words](../../../../reference/sql-statements-and-structure/sql-language-structure/reserved-words.md): EXCEPT and INTERSECT. These can no longer be used as [identifiers](../../../../reference/sql-statements-and-structure/sql-language-structure/identifier-names.md) without being quoted.


#### SQL_MODE=ORACLE


* [MariaDB 10.3](../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md) has introduced major new Oracle compatibility features. If you upgrade and are using this setting, please check the [changes carefully](../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md).


#### Functions


* As a result of implementing Table Value Constructors, the [VALUES function](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/miscellaneous-functions/values-value.md) has been renamed to VALUE().
* Functions that used to only return 64-bit now can return 32-bit results ([MDEV-12619](https://jira.mariadb.org/browse/MDEV-12619)). This could cause incompatibilities with strongly-typed clients.


#### mysqldump


* [mysqldump](../../../../clients-and-utilities/legacy-clients-and-utilities/mysqldumpslow.md) in [MariaDB 10.3](../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md) includes logic to cater for the [mysql.transaction_registry table](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-transaction_registry-table.md). `mysqldump` from an earlier MariaDB release cannot be used on [MariaDB 10.3](../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md) and beyond.


#### MariaDB Backup and Percona XtraBackup


* [Percona XtraBackup](../../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md) is not compatible with [MariaDB 10.3](../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md). Installations currently using XtraBackup should upgrade to [MariaDB Backup](../../migrating-to-mariadb/migrating-to-mariadb-from-sql-server/mariadb-backups-overview-for-sql-server-users.md) before upgrading to [MariaDB 10.3](../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md).


#### Privileges


* If a user has the [SUPER privilege](../../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md) but not the `DELETE HISTORY` privilege, running [mysql_upgrade](../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md) will grant `DELETE HISTORY` as well.


### Major New Features To Consider


You might consider using the following major new features in [MariaDB 10.3](../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md):


* [System-versioned tables](../../../../reference/sql-statements-and-structure/temporal-tables/system-versioned-tables.md)
* [Sequences](../../../../reference/sql-statements-and-structure/sequences/README.md)
* See also [System Variables Added in MariaDB 10.3](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-10-3.md).


### See Also


* [The features in MariaDB 10.3](../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md)
* [Upgrading from MariaDB 10.2 to MariaDB 10.3 with Galera Cluster](upgrading-from-mariadb-102-to-mariadb-103-with-galera-cluster)
* [Upgrading from MariaDB 10.1 to MariaDB 10.2](upgrading-from-mariadb-101-to-mariadb-102.md)
* [Upgrading from MariaDB 10.0 to MariaDB 10.1](upgrading-from-mariadb-100-to-mariadb-101.md)

<span></span>
