
# Upgrading from MariaDB 10.4 to MariaDB 10.5


### How to Upgrade


For Windows, see [Upgrading MariaDB on Windows](upgrading-mariadb-on-windows.md) instead.


For MariaDB Galera Cluster, see [Upgrading from MariaDB 10.4 to MariaDB 10.5 with Galera Cluster](../../../server-usage/replication-cluster-multi-master/galera-cluster/upgrading-galera-cluster/upgrading-from-mariadb-10-4-to-mariadb-10-5-with-galera-cluster.md).


Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [Mariabackup](../../backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md).



The suggested upgrade procedure is:


1. Modify the repository configuration, so the system's package manager installs [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md). For example,

  * On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](../binary-packages/rpm/yum.md#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
  * On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](../binary-packages/rpm/installing-mariadb-with-zypper.md#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.
1. [Stop MariaDB](../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
1. Uninstall the old version of MariaDB.

  * On Debian, Ubuntu, and other similar Linux distributions, execute the following: 
`<code class="fixed" style="white-space:pre-wrap">sudo apt-get remove mariadb-server</code>`
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, execute the following: 
`<code class="fixed" style="white-space:pre-wrap">sudo yum remove MariaDB-server</code>`
  * On SLES, OpenSUSE, and other similar Linux distributions, execute the following: 
`<code class="fixed" style="white-space:pre-wrap">sudo zypper remove MariaDB-server</code>`
1. Install the new version of MariaDB.

  * On Debian, Ubuntu, and other similar Linux distributions, see [Installing MariaDB Packages with APT](../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md#installing-mariadb-packages-with-apt) for more information.
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Installing MariaDB Packages with YUM](../binary-packages/rpm/yum.md#installing-mariadb-packages-with-yum) for more information.
  * On SLES, OpenSUSE, and other similar Linux distributions, see [Installing MariaDB Packages with ZYpp](../binary-packages/rpm/installing-mariadb-with-zypper.md#installing-mariadb-packages-with-zypp) for more information.
1. Make any desired changes to configuration options in [option files](../configuring-mariadb-with-option-files.md), such as `<code>my.cnf</code>`. This includes removing any options that are no longer supported.
1. [Start MariaDB](../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
1. Run [mysql_upgrade](../../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md).

  * `<code>mysql_upgrade</code>` does two things:

    1. Ensures that the system tables in the [mysql](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md) database are fully compatible with the new version.
    1. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .


### Incompatible Changes Between 10.4 and 10.5


On most servers upgrading from 10.4 should be painless. However, there are some things that have changed which could affect an upgrade:


#### Binary name changes


All binaries previously beginning with mysql now begin with mariadb, with symlinks for the corresponding mysql command.


Usually that shouldn't cause any changed behavior, but when starting the MariaDB server via [systemd](../starting-and-stopping-mariadb/systemd.md), or via the [mysqld_safe](../../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md) script symlink, the server process will now always be started as `<code>mariadbd</code>`, not `<code>mysqld</code>`.


So anything looking for the `<code>mysqld</code>` name in the system process list, like e.g. monitoring solutions, now needs for `<code>mariadbd</code>` instead when the server / service is not started directly, but via `<code>mysqld_safe</code>` or as a system service.


#### GRANT PRIVILEGE changes


A number of statements changed the privileges that they require. The old privileges were historically inappropriately chosen in the upstream. 10.5.2 fixes this problem. Note, these changes are incompatible to previous versions. A number of GRANT commands might be needed after upgrade.


* `<code>SHOW BINLOG EVENTS</code>` now requires the `<code>BINLOG MONITOR</code>` privilege (requred `<code>REPLICATION SLAVE</code>` prior to 10.5.2).
* `<code>SHOW SLAVE HOSTS</code>` now requires the `<code>REPLICATION MASTER ADMIN</code>` privilege (required `<code>REPLICATION SLAVE</code>` prior to 10.5.2).
* `<code>SHOW SLAVE STATUS</code>` now requires the `<code>REPLICATION SLAVE ADMIN</code>` or the `<code>SUPER</code>` privilege (required `<code>REPLICATION CLIENT</code>` or `<code>SUPER</code>` prior to 10.5.2).
* `<code>SHOW RELAYLOG EVENTS</code>` now requires the `<code>REPLICATION SLAVE ADMIN</code>` privilege (required `<code>REPLICATION SLAVE</code>` prior to 10.5.2).


#### Options That Have Changed Default Values



| Option | Old default value | New default value |
| --- | --- | --- |
| Option | Old default value | New default value |
| [innodb_adaptive_hash_index](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index) | ON | OFF |
| [innodb_checksum_algorithm](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm) | crc32 | full_crc32 |
| [innodb_log_optimize_ddl](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_optimize_ddl) | ON | OFF |
| [slave_parallel_mode](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#slave_parallel_mode) | conservative | optimistic |
| [performance_schema_max_cond_classes](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_cond_classes) | 80 | 90 |
| [performance_schema_max_file_classes](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_file_classes) | 50 | 80 |
| [performance_schema_max_mutex_classes](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_mutex_classes) | 200 | 210 |
| [performance_schema_max_rwlock_classes](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_rwlock_classes) | 40 | 50 |
| [performance_schema_setup_actors_size](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_setup_actors_size) | 100 | -1 |
| [performance_schema_setup_objects_size](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_setup_objects_size) | 100 | -1 |



#### Options That Have Been Removed or Renamed


The following options should be removed or renamed if you use them in your [option files](../configuring-mariadb-with-option-files.md):



| Option | Reason |
| --- | --- |
| Option | Reason |
| [innodb_checksums](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_checksums) | Deprecated and functionality replaced by [innodb_checksum_algorithms](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm) in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md). |
| [innodb_idle_flush_pct](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_idle_flush_pct) | Has had no effect since merging InnoDB 5.7 from mysql-5.7.9 ([MariaDB 10.2.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md)). |
| [innodb_locks_unsafe_for_binlog](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_locks_unsafe_for_binlog) | Deprecated in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md). Use [READ COMMITTED transaction isolation level](../../../reference/sql-statements-and-structure/sql-statements/transactions/set-transaction.md#read-committed) instead. |
| [innodb_rollback_segments](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_rollback_segments) | Deprecated and replaced by [innodb_undo_logs](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_undo_logs) in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md). |
| [innodb_stats_sample_pages](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_sample_pages) | Deprecated in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md). Use [innodb_stats_transient_sample_pages](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_transient_sample_pages) instead. |
| [max_long_data_size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_long_data_size) | Deprecated and replaced by [max_allowed_packet](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_allowed_packet) in [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md). |
| [multi_range_count](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#multi_range_count) | Deprecated and has had no effect since [MariaDB 5.3](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md). |
| [thread_concurrency](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#thread_concurrency) | Deprecated and has had no effect since [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md). |
| [timed_mutexes](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#timed_mutexes) | Deprecated and has had no effect since [MariaDB 5.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md). |



#### Deprecated Options


The following options have been deprecated. They have not yet been removed, but will be in a future version, and should ideally no longer be used.



| Option | Reason |
| --- | --- |
| Option | Reason |
| [innodb_adaptive_max_sleep_delay](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_max_sleep_delay) | No need for thread throttling any more. |
| [innodb_background_scrub_data_check_interval](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_check_interval) | Problematic ‘background scrubbing’ code removed. |
| [innodb_background_scrub_data_interval](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_interval) | Problematic ‘background scrubbing’ code removed. |
| [innodb_background_scrub_data_compressed](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_compressed) | Problematic ‘background scrubbing’ code removed. |
| [innodb_background_scrub_data_uncompressed](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_uncompressed) | Problematic ‘background scrubbing’ code removed. |
| [innodb_buffer_pool_instances](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_instances) | Having more than one buffer pool is no longer necessary. |
| [innodb_commit_concurrency](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_commit_concurrency) | No need for thread throttling any more. |
| [innodb_concurrency_tickets](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_concurrency_tickets) | No need for thread throttling any more. |
| [innodb_log_files_in_group](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_files_in_group) | Redo log was unnecessarily split into multiple files. Limited to 1 from [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md). |
| [innodb_log_optimize_ddl](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_optimize_ddl) | Prohibited optimizations. |
| [innodb_page_cleaners](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_page_cleaners) | Having more than one page cleaner task no longer necessary. |
| [innodb_replication_delay](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_replication_delay) | No need for thread throttling any more. |
| [innodb_scrub_log](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_scrub_log) | Never really worked as intended, redo log format is being redone. |
| [innodb_scrub_log_speed](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_scrub_log_speed) | Never really worked as intended, redo log format is being redone. |
| [innodb_thread_concurrency](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_thread_concurrency) | No need for thread throttling any more. |
| [innodb_thread_sleep_delay](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_thread_sleep_delay) | No need for thread throttling any more. |
| [innodb_undo_logs](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_undo_logs) | It always makes sense to use the maximum number of rollback segments. |
| [large_page_size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#large_page_size) | Unused since multiple page size support was added. |



### Major New Features To Consider


You might consider using the following major new features in [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md):


* The [S3 storage engine](../../../reference/storage-engines/s3-storage-engine/s3-storage-engine-status-variables.md) allows one to archive MariaDB tables in Amazon S3, or any third-party public or private cloud that implements S3 API.
* [ColumnStore](../../../../columnstore/using-mariadb-columnstore/mariadb-columnstore-with-spark.md) columnar storage engine.
* See also [System Variables Added in MariaDB 10.5](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-variables-added-in-mariadb-10-5.md).


### See Also


* [The features in MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)



* [Upgrading from MariaDB 10.4 to MariaDB 10.5 with Galera Cluster](https://mariadb.com/kb/en/upgrading-from-mariadb-104-to-mariadb-105-with-galera-cluster)



* [Upgrading from MariaDB 10.3 to MariaDB 10.4](upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-103-to-mariadb-104.md)
* [Upgrading from MariaDB 10.2 to MariaDB 10.3](upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-102-to-mariadb-103.md)
* [Upgrading from MariaDB 10.1 to MariaDB 10.2](upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-101-to-mariadb-102.md)

