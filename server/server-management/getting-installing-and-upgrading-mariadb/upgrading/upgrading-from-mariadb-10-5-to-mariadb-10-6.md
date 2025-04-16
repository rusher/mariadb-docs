
# Upgrading from MariaDB 10.5 to MariaDB 10.6


### How to Upgrade


For Windows, see [Upgrading MariaDB on Windows](upgrading-mariadb-on-windows.md).


For MariaDB Galera Cluster, see [Upgrading from MariaDB 10.5 to MariaDB 10.6 with Galera Cluster](../../../server-usage/replication-cluster-multi-master/galera-cluster/upgrading-galera-cluster/upgrading-from-mariadb-10-5-to-mariadb-10-6-with-galera-cluster.md).


Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [Mariabackup](../../backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md).



The suggested upgrade procedure is:


1. Modify the repository configuration, so the system's package manager installs [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md). For example,

  * On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](../binary-packages/rpm/yum.md#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
  * On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](../binary-packages/rpm/installing-mariadb-with-zypper.md#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.
1. [Stop MariaDB](../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
1. Uninstall the old version of MariaDB.

  * On Debian, Ubuntu, and other similar Linux distributions, execute the following: 
`sudo apt-get remove mariadb-server`
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, execute the following: 
`sudo yum remove MariaDB-server`
  * On SLES, OpenSUSE, and other similar Linux distributions, execute the following: 
`sudo zypper remove MariaDB-server`
1. Install the new version of MariaDB.

  * On Debian, Ubuntu, and other similar Linux distributions, see [Installing MariaDB Packages with APT](../binary-packages/automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md#installing-mariadb-packages-with-apt) for more information.
  * On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Installing MariaDB Packages with YUM](../binary-packages/rpm/yum.md#installing-mariadb-packages-with-yum) for more information.
  * On SLES, OpenSUSE, and other similar Linux distributions, see [Installing MariaDB Packages with ZYpp](../binary-packages/rpm/installing-mariadb-with-zypper.md#installing-mariadb-packages-with-zypp) for more information.
1. Make any desired changes to configuration options in [option files](../configuring-mariadb-with-option-files.md), such as `my.cnf`. This includes removing any options that are no longer supported.
1. [Start MariaDB](../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
1. Run [mariadb-upgrade](../../../clients-and-utilities/mariadb-upgrade.md).

  * `mariadb-upgrade` does two things:

    1. Ensures that the system tables in the [mysql](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md) database are fully compatible with the new version.
    1. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .


### Incompatible Changes Between 10.5 and 10.6


On most servers upgrading from 10.5 should be painless. However, there are some things that have changed which could affect an upgrade:


The bahaviour of sorting non-deterministic variables in a Select query can be changed ,
see ([MDEV-27745](https://jira.mariadb.org/browse/MDEV-27745))


#### Reserved Word


* New [reserved word](../../../reference/sql-statements-and-structure/sql-language-structure/reserved-words.md): OFFSET. This can no longer be used as an [identifier](../../../reference/sql-statements-and-structure/sql-language-structure/identifier-names.md) without being quoted.


#### InnoDB COMPRESSED Row Format


From [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md) until [MariaDB 10.6.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1065-release-notes.md), tables that are of the `COMPRESSED` row format are read-only by default. This was intended to be the first step towards removing write support and deprecating the feature.


This plan has been scrapped, and from [MariaDB 10.6.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1066-release-notes.md), `COMPRESSED` tables are no longer read-only by default.


From [MariaDB 10.6.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1060-release-notes.md) to [MariaDB 10.6.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1065-release-notes.md), set the [innodb_read_only_compressed](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_read_only_compressed) variable to `OFF` to make the tables writable.


#### Character Sets


From [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md), the `utf8` [character set](../../../reference/data-types/string-data-types/character-sets/README.md) (and related collations) is by default an alias for `utf8mb3` rather than the other way around. It can be set to imply `utf8mb4` by changing the value of the [old_mode](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old_mode) system variable.


#### Options That Have Changed Default Values



| Option | Old default value | New default value |
| --- | --- | --- |
| Option | Old default value | New default value |
| [character_set_client](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client) | utf8 | utf8mb3 |
| [character_set_connection](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_connection) | utf8 | utf8mb3 |
| [character_set_results](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_results) | utf8 | utf8mb3 |
| [character_set_system](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_system) | utf8 | utf8mb3 |
| [innodb_flush_method](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_flush_method) | fsync | O_DIRECT |
| [old_mode](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old_mode) | Empty | UTF8_IS_UTF8MB3 |



#### Options That Have Been Removed or Renamed


The following options should be removed or renamed if you use them in your [option files](../configuring-mariadb-with-option-files.md):



| Option | Reason |
| --- | --- |
| Option | Reason |
| [innodb_adaptive_max_sleep_delay](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_max_sleep_delay) |  |
| [innodb_background_scrub_data_check_interval](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_check_interval) |  |
| [innodb_background_scrub_data_compressed](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_compressed) |  |
| [innodb_background_scrub_data_interval](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_interval) |  |
| [innodb_background_scrub_data_uncompressed](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_uncompressed) |  |
| [innodb_buffer_pool_instances](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_instances) |  |
| [innodb_checksum_algorithm](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm) | The variable is still present, but the *innodb and *none options have been removed as the crc32 algorithm only is supported from [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md). |
| [innodb_commit_concurrency](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_commit_concurrency) |  |
| [innodb_concurrency_tickets](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_concurrency_tickets) |  |
| [innodb_file_format](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_file_format) |  |
| [innodb_large_prefix](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_large_prefix) |  |
| [innodb_lock_schedule_algorithm](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_lock_schedule_algorithm) |  |
| [innodb_log_checksums](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_checksums) |  |
| [innodb_log_compressed_pages](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_compressed_pages) |  |
| [innodb_log_files_in_group](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_files_in_group) |  |
| [innodb_log_optimize_ddl](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_optimize_ddl) |  |
| [innodb_page_cleaners](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_page_cleaners) |  |
| [innodb_replication_delay](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_replication_delay) |  |
| [innodb_scrub_log](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_scrub_log) |  |
| [innodb_scrub_log_speed](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_scrub_log_speed) |  |
| [innodb_sync_array_size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_sync_array_size) |  |
| [innodb_thread_concurrency](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_thread_concurrency) |  |
| [innodb_thread_sleep_delay](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_thread_sleep_delay) |  |
| [innodb_undo_logs](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_undo_logs) |  |



#### Deprecated Options


The following options have been deprecated. They have not yet been removed, but will be in a future version, and should ideally no longer be used.



| Option | Reason |
| --- | --- |
| Option | Reason |
| [wsrep_replicate_myisam](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_replicate_myisam) | Use [wsrep_mode](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_mode) instead. |
| [wsrep_strict_ddl](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_strict_ddl) | Use [wsrep_mode](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-system-variables.md#wsrep_mode) instead. |



### Major New Features To Consider


* See also [System Variables Added in MariaDB 10.6](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-variables-added-in-mariadb-10-6.md).


### See Also


* [The features in MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md)



* [Upgrading from MariaDB 10.5 to MariaDB 10.6 with Galera Cluster](https://mariadb.com/kb/en/upgrading-from-mariadb-105-to-mariadb-106-with-galera-cluster)



* [Upgrading from MariaDB 10.4 to MariaDB 10.5](upgrading-from-mariadb-10-4-to-mariadb-10-5.md)
* [Upgrading from MariaDB 10.3 to MariaDB 10.4](upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-103-to-mariadb-104.md)
* [Upgrading from MariaDB 10.2 to MariaDB 10.3](upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-102-to-mariadb-103.md)

<span></span>
