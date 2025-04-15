
# Files Created by Mariabackup


Mariabackup creates the following files:


## `<code>backup-my.cnf</code>`


During the backup, any server options relevant to Mariabackup are written to the `<code>backup-my.cnf</code>` [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), so that they can be re-read later during the `<code>--prepare</code>` stage.


## `<code>ib_logfile0</code>`


In [MariaDB 10.2.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10210-release-notes.md) and later, Mariabackup creates an empty [InnoDB redo log](../../../reference/storage-engines/innodb/innodb-redo-log.md) file called `<code>ib_logfile0</code>` as part of the `<code>[--prepare](mariabackup-options.md#-prepare)</code>` stage. This file has 3 roles:


1. In the source server, `<code>ib_logfile0</code>` is the first (and possibly the only) [InnoDB redo log](../../../reference/storage-engines/innodb/innodb-redo-log.md) file.
1. In the non-prepared backup, `<code>ib_logfile0</code>` contains all of the [InnoDB redo log](../../../reference/storage-engines/innodb/innodb-redo-log.md) copied during the backup. Previous versions of Mariabackup would use a file called `<code>[xtrabackup_logfile](#xtrabackup_logfile)</code>` for this.
1. During the `<code>[--prepare](mariabackup-options.md#-prepare)</code>` stage, `<code>ib_logfile0</code>` would previously be deleted. Now during the `<code>--prepare</code>` stage, `<code>ib_logfile0</code>` is initialized as an empty [InnoDB redo log](../../../reference/storage-engines/innodb/innodb-redo-log.md) file. That way, if the backup is manually restored, any pre-existing [InnoDB redo log](../../../reference/storage-engines/innodb/innodb-redo-log.md) files would get overwritten by the empty one. This helps to prevent certain kinds of known issues. For example, see [Mariabackup Overview: Manual Restore with Pre-existing InnoDB Redo Log files](mariabackup-overview.md#manual-restore-with-pre-existing-innodb-redo-log-files).


## `<code>xtrabackup_logfile</code>`


In [MariaDB 10.2.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1029-release-notes.md) and before, Mariabackup creates `<code>xtrabackup_logfile</code>` to store the [InnoDB redo log](../../../reference/storage-engines/innodb/innodb-redo-log.md), In later versions, `<code>[ib_logfile0](#ib_logfile0)</code>` is created instead.


## `<code>xtrabackup_binlog_info</code>`


This file stores the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) file name and position that corresponds to the backup.


This file also stores the value of the `<code>[gtid_current_pos](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md#gtid_current_pos)</code>` system variable that correspond to the backup.


For example:


```
mariadb-bin.000096 568 0-1-2
```

The values in this file are only guaranteed to be consistent with the backup if the `<code>[--no-lock](mariabackup-options.md#-no-lock)</code>` option was **not** provided when the backup was taken.


## `<code>xtrabackup_binlog_pos_innodb</code>`


This file is created by mariabackup to provide the binary log file name and position when the [--no-lock](mariabackup-options.md#-no-lock) option is used. It can be used instead of the file "xtrabackup_binlog_info" to obtain transactionally consistent binlog coordinates from the backup of a master server with the --no-lock option to minimize the impact on a running server.


Whenever a transaction is committed inside InnoDB when the binary log is enabled, the corresponding binlog coordinates are written to the InnoDB redo log along with the transaction commit. This allows one to restore the binlog coordinates corresponding to the last commit done by InnoDB along with a backup.


The limitation of using "xtrabackup_binlog_pos_innodb" with the "--no-lock" option is that no DDL or modification of non-transactional tables should be done during the backup. If the last event in the binlog is a DDL/non-transactional update, the coordinates in the file "xtrabackup_binlog_pos_innodb" will be too old. But as long as only InnoDB updates are done during the backup, the coordinates will be correct.


## `<code>xtrabackup_checkpoints</code>`


The `<code>xtrabackup_checkpoints</code>` file contains metadata about the backup.


For example:


```
backup_type = full-backuped
from_lsn = 0
to_lsn = 1635102
last_lsn = 1635102
recover_binlog_info = 0
```

See below for a description of the fields.


If the `<code>[--extra-lsndir](mariabackup-options.md#-extra-lsndir)</code>` option is provided, then an extra copy of this file will be saved in that directory.


### `<code>backup_type</code>`


If the backup is a non-prepared [full backup](full-backup-and-restore-with-mariabackup.md) or a non-prepared [partial backup](partial-backup-and-restore-with-mariabackup.md), then `<code>backup_type</code>` is set to `<code>full-backuped</code>`.


If the backup is a non-prepared [incremental backup](incremental-backup-and-restore-with-mariabackup.md), then `<code>backup_type</code>` is set to `<code>incremental</code>`.


If the backup has already been prepared, then `<code>backup_type</code>` is set to `<code>log-applied</code>`.


### `<code>from_lsn</code>`


If `<code>backup_type</code>` is `<code>full-backuped</code>`, then `<code>from_lsn</code>` has the value of `<code>0</code>`.


If `<code>backup_type</code>` is `<code>incremental</code>`, then `<code>from_lsn</code>` has the value of the [log sequence number (LSN)](../../../reference/storage-engines/innodb/innodb-redo-log.md#log-sequence-number-lsn) at which the backup started reading from the [InnoDB redo log](../../../reference/storage-engines/innodb/innodb-redo-log.md). This is internally used by Mariabackup when preparing incremental backups.


This value can be manually set during an [incremental backup](incremental-backup-and-restore-with-mariabackup.md) with the `<code>[--incremental-lsn](mariabackup-options.md#-incremental-lsn)</code>` option. However, it is generally better to let Mariabackup figure out the `<code>from_lsn</code>` automatically by specifying a parent backup with the `<code>[--incremental-basedir](mariabackup-options.md#-incremental-basedir)</code>` option.


### `<code>to_lsn</code>`


`<code>to_lsn</code>` has the value of the [log sequence number (LSN)](../../../reference/storage-engines/innodb/innodb-redo-log.md#log-sequence-number-lsn) of the last checkpoint in the [InnoDB redo log](../../../reference/storage-engines/innodb/innodb-redo-log.md). This is internally used by Mariabackup when preparing incremental backups.


### `<code>last_lsn</code>`


`<code>last_lsn</code>` has the value of the last [log sequence number (LSN)](../../../reference/storage-engines/innodb/innodb-redo-log.md#log-sequence-number-lsn) read from the [InnoDB redo log](../../../reference/storage-engines/innodb/innodb-redo-log.md). This is internally used by Mariabackup when preparing incremental backups.


## `<code>xtrabackup_info</code>`


The `<code>xtrabackup_info</code>` file contains information about the backup. The fields in this file are listed below.


If the `<code>[--extra-lsndir](mariabackup-options.md#-extra-lsndir)</code>` option is provided, then an extra copy of this file will be saved in that directory.


### `<code>uuid</code>`


If a UUID was provided by the `<code>[--incremental-history-uuid](mariabackup-options.md#-incremental-history-uuid)</code>` option, then it will be saved here. Otherwise, this will be the empty string.


### `<code>name</code>`


If a name was provided by the `<code>[--history](mariabackup-options.md#-history)</code>` or the `<code>[---incremental-history-name](mariabackup-options.md#-incremental-history-name)</code>` options, then it will be saved here. Otherwise, this will be the empty string.


### `<code>tool_name</code>`


The name of the Mariabackup executable that performed the backup. This is generally `<code>mariabackup</code>`.


### `<code>tool_command</code>`


The arguments that were provided to Mariabackup when it performed the backup.


### `<code>tool_version</code>`


The version of Mariabackup that performed the backup.


### `<code>ibbackup_version</code>`


The version of Mariabackup that performed the backup.


### `<code>server_version</code>`


The version of MariaDB Server that was backed up.


### `<code>start_time</code>`


The time that the backup started.


### `<code>end_time</code>`


The time that the backup ended.


### `<code>lock_time</code>`


The amount of time that Mariabackup held its locks.


### `<code>binlog_pos</code>`


This field stores the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) file name and position that corresponds to the backup.


This field also stores the value of the `<code>[gtid_current_pos](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md#gtid_current_pos)</code>` system variable that correspond to the backup.


The values in this field are only guaranteed to be consistent with the backup if the `<code>[--no-lock](mariabackup-options.md#-no-lock)</code>` option was **not** provided when the backup was taken.


### `<code>innodb_from_lsn</code>`


This is identical to `<code>from_lsn</code>` in `<code>[xtrabackup_checkpoints](#xtrabackup_checkpoints)</code>`.


If the backup is a [full backup](full-backup-and-restore-with-mariabackup.md), then `<code>innodb_from_lsn</code>` has the value of `<code>0</code>`.


If the backup is an [incremental backup](incremental-backup-and-restore-with-mariabackup.md), then `<code>innodb_from_lsn</code>` has the value of the [log sequence number (LSN)](../../../reference/storage-engines/innodb/innodb-redo-log.md#log-sequence-number-lsn) at which the backup started reading from the [InnoDB redo log](../../../reference/storage-engines/innodb/innodb-redo-log.md).


### `<code>innodb_to_lsn</code>`


This is identical to `<code>to_lsn</code>` in `<code>[xtrabackup_checkpoints](#xtrabackup_checkpoints)</code>`.


`<code>innodb_to_lsn</code>` has the value of the [log sequence number (LSN)](../../../reference/storage-engines/innodb/innodb-redo-log.md#log-sequence-number-lsn) of the last checkpoint in the [InnoDB redo log](../../../reference/storage-engines/innodb/innodb-redo-log.md).


### `<code>partial</code>`


If the backup is a [partial backup](partial-backup-and-restore-with-mariabackup.md), then this value will be `<code>Y</code>`.


Otherwise, this value will be `<code>N</code>`.


### `<code>incremental</code>`


If the backup is an [incremental backup](incremental-backup-and-restore-with-mariabackup.md), then this value will be `<code>Y</code>`.


Otherwise, this value will be `<code>N</code>`.


### `<code>format</code>`


This field's value is the format of the backup.


If the `<code>[--stream](mariabackup-options.md#-stream)</code>` option was set to `<code>xbstream</code>`, then this value will be `<code>xbstream</code>`.


If the `<code>[--stream](mariabackup-options.md#-stream)</code>` option was **not** provided, then this value will be `<code>file</code>`.


### `<code>compressed</code>`


If the `<code>[--compress](mariabackup-options.md#-compress)</code>` option was provided, then this value will be `<code>compressed</code>`.


Otherwise, this value will be `<code>N</code>`.


## `<code>xtrabackup_slave_info</code>`


If the `<code>[--slave-info](mariabackup-options.md#-slave-info)</code>` option is provided, then this file contains the `<code>[CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md)</code>` command that can be used to set up a new server as a slave of the original server's master after the backup has been restored.


Mariabackup does **not** check if [GTIDs](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) are being used in replication. It takes a shortcut and assumes that if the `<code>[gtid_slave_pos](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md#gtid_slave_pos)</code>` system variable is non-empty, then it writes the `<code>[CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md)</code>` command with the `<code>[MASTER_USE_GTID](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_use_gtid)</code>` option set to `<code>slave_pos</code>`. Otherwise, it writes the `<code>[CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md)</code>` command with the `<code>[MASTER_LOG_FILE](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_log_file)</code>` and `<code>[MASTER_LOG_POS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_log_pos)</code>` options using the master's [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) file and position. See [MDEV-19264](https://jira.mariadb.org/browse/MDEV-19264) for more information.


## `<code>xtrabackup_galera_info</code>`


If the `<code>[--galera-info](mariabackup-options.md#-galera-info)</code>` option is provided, then this file contains information about a [Galera Cluster](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md) node's state.


The file contains the values of the `<code>[wsrep_local_state_uuid](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-status-variables.md#wsrep_local_state_uuid)</code>` and `<code>[wsrep_last_committed](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-status-variables.md#wsrep_last_committed)</code>` status variables.


The values are written in the following format:


```
wsrep_local_state_uuid:wsrep_last_committed
```

For example:


```
d38587ce-246c-11e5-bcce-6bbd0831cc0f:1352215
```

## `<code><table>.delta</code>`


If the backup is an [incremental backup](incremental-backup-and-restore-with-mariabackup.md), then this file contains changed pages for the table.


## `<code><table>.delta.meta</code>`


If the backup is an [incremental backup](incremental-backup-and-restore-with-mariabackup.md), then this file contains metadata about `<code><table>.delta</code>` files. The fields in this file are listed below.


### `<code>page_size</code>`


This field contains either the value of `<code>[innodb_page_size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_page_size)</code>` or the value of the `<code>[KEY_BLOCK_SIZE](../../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md#key_block_size)</code>` table option for the table if the `<code>[ROW_FORMAT](../../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md#row_format)</code>` table option for the table is set to `<code>[COMPRESSED](../../../reference/storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md)</code>`.


### `<code>zip_size</code>`


If the `<code>[ROW_FORMAT](../../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md#row_format)</code>` table option for this table is set to `<code>[COMPRESSED](../../../reference/storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md)</code>`, then this field contains the value of the compressed page size.


### `<code>space_id</code>`


This field contains the value of the table's `<code>space_id</code>`.

