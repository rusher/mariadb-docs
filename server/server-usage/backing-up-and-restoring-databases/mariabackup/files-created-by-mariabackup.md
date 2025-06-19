# Files Created by Mariabackup

Mariabackup creates the following files:

## `backup-my.cnf`

During the backup, any server options relevant to Mariabackup are written to the `backup-my.cnf` [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), so that they can be re-read later during the `--prepare` stage.

## `ib_logfile0`

In [MariaDB 10.2.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10210-release-notes) and later, Mariabackup creates an empty [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md) file called `ib_logfile0` as part of the [--prepare](mariabackup-options.md#-prepare) stage. This file has 3 roles:

1. In the source server, `ib_logfile0` is the first (and possibly the only) [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md) file.
2. In the non-prepared backup, `ib_logfile0` contains all of the [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md) copied during the backup. Previous versions of Mariabackup would use a file called [xtrabackup_logfile](#xtrabackup_logfile) for this.
3. During the [--prepare](mariabackup-options.md#-prepare) stage, `ib_logfile0` would previously be deleted. Now during the `--prepare` stage, `ib_logfile0` is initialized as an empty [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md) file. That way, if the backup is manually restored, any pre-existing [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md) files would get overwritten by the empty one. This helps to prevent certain kinds of known issues. For example, see [Mariabackup Overview: Manual Restore with Pre-existing InnoDB Redo Log files](mariabackup-overview.md#manual-restore-with-pre-existing-innodb-redo-log-files).

## `xtrabackup_logfile`

In [MariaDB 10.2.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1029-release-notes) and before, Mariabackup creates `xtrabackup_logfile` to store the [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md), In later versions, [ib_logfile0](#ib_logfile0) is created instead.

## `xtrabackup_binlog_info`

This file stores the [binary log](../../../server-management/server-monitoring-logs/binary-log/) file name and position that corresponds to the backup.

This file also stores the value of the [gtid_current_pos](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md#gtid_current_pos) system variable that correspond to the backup.

For example:

```bash
mariadb-bin.000096 568 0-1-2
```

The values in this file are only guaranteed to be consistent with the backup if the [--no-lock](mariabackup-options.md#-no-lock) option was **not** provided when the backup was taken.

## `xtrabackup_binlog_pos_innodb`

This file is created by mariabackup to provide the binary log file name and position when the [--no-lock](mariabackup-options.md#-no-lock) option is used. It can be used instead of the file "xtrabackup\_binlog\_info" to obtain transactionally consistent binlog coordinates from the backup of a master server with the --no-lock option to minimize the impact on a running server.

Whenever a transaction is committed inside InnoDB when the binary log is enabled, the corresponding binlog coordinates are written to the InnoDB redo log along with the transaction commit. This allows one to restore the binlog coordinates corresponding to the last commit done by InnoDB along with a backup.

The limitation of using "xtrabackup\_binlog\_pos\_innodb" with the "--no-lock" option is that no DDL or modification of non-transactional tables should be done during the backup. If the last event in the binlog is a DDL/non-transactional update, the coordinates in the file "xtrabackup\_binlog\_pos\_innodb" will be too old. But as long as only InnoDB updates are done during the backup, the coordinates will be correct.

## `xtrabackup_checkpoints`

The `xtrabackup_checkpoints` file contains metadata about the backup.

For example:

```bash
backup_type = full-backuped
from_lsn = 0
to_lsn = 1635102
last_lsn = 1635102
recover_binlog_info = 0
```

See below for a description of the fields.

If the `--extra-lsndir` option is provided, then an extra copy of this file will be saved in that directory.

### `backup_type`

If the backup is a non-prepared [full backup](full-backup-and-restore-with-mariabackup.md) or a non-prepared [partial backup](partial-backup-and-restore-with-mariabackup.md), then `backup_type` is set to `full-backuped`.

If the backup is a non-prepared [incremental backup](incremental-backup-and-restore-with-mariabackup.md), then `backup_type` is set to `incremental`.

If the backup has already been prepared, then `backup_type` is set to `log-applied`.

### `from_lsn`

If `backup_type` is `full-backuped`, then `from_lsn` has the value of `0`.

If `backup_type` is `incremental`, then `from_lsn` has the value of the [log sequence number (LSN)](../../storage-engines/innodb/innodb-redo-log.md#log-sequence-number-lsn) at which the backup started reading from the [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md). This is internally used by Mariabackup when preparing incremental backups.

This value can be manually set during an [incremental backup](incremental-backup-and-restore-with-mariabackup.md) with the [--incremental-lsn](mariabackup-options.md#-incremental-lsn) option. However, it is generally better to let Mariabackup figure out the `from_lsn` automatically by specifying a parent backup with the [--incremental-basedir](mariabackup-options.md#-incremental-basedir) option.

### `to_lsn`

`to_lsn` has the value of the [log sequence number (LSN)](../../storage-engines/innodb/innodb-redo-log.md#log-sequence-number-lsn) of the last checkpoint in the [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md). This is internally used by Mariabackup when preparing incremental backups.

### `last_lsn`

`last_lsn` has the value of the last [log sequence number (LSN)](../../storage-engines/innodb/innodb-redo-log.md#log-sequence-number-lsn) read from the [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md). This is internally used by Mariabackup when preparing incremental backups.

## `xtrabackup_info`

The `xtrabackup_info` file contains information about the backup. The fields in this file are listed below.

If the [--extra-lsndir](mariabackup-options.md#-extra-lsndir) option is provided, then an extra copy of this file will be saved in that directory.

### `uuid`

If a UUID was provided by the [--incremental-history-uuid](mariabackup-options.md#-incremental-history-uuid) option, then it will be saved here. Otherwise, this will be the empty string.

### `name`

If a name was provided by the [--history](mariabackup-options.md#-history) or the [---incremental-history-name](mariabackup-options.md#-incremental-history-name) options, then it will be saved here. Otherwise, this will be the empty string.

### `tool_name`

The name of the Mariabackup executable that performed the backup. This is generally `mariabackup`.

### `tool_command`

The arguments that were provided to Mariabackup when it performed the backup.

### `tool_version`

The version of Mariabackup that performed the backup.

### `ibbackup_version`

The version of Mariabackup that performed the backup.

### `server_version`

The version of MariaDB Server that was backed up.

### `start_time`

The time that the backup started.

### `end_time`

The time that the backup ended.

### `lock_time`

The amount of time that Mariabackup held its locks.

### `binlog_pos`

This field stores the [binary log](../../../server-management/server-monitoring-logs/binary-log/) file name and position that corresponds to the backup.

This field also stores the value of the [gtid_current_pos](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md#gtid_current_pos) system variable that correspond to the backup.

The values in this field are only guaranteed to be consistent with the backup if the [--no-lock](mariabackup-options.md#-no-lock) option was **not** provided when the backup was taken.

### `innodb_from_lsn`

This is identical to `from_lsn` in [xtrabackup_checkpoints](#xtrabackup_checkpoints).

If the backup is a [full backup](full-backup-and-restore-with-mariabackup.md), then `innodb_from_lsn` has the value of `0`.

If the backup is an [incremental backup](incremental-backup-and-restore-with-mariabackup.md), then `innodb_from_lsn` has the value of the [log sequence number (LSN)](../../storage-engines/innodb/innodb-redo-log.md#log-sequence-number-lsn) at which the backup started reading from the [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md).

### `innodb_to_lsn`

This is identical to `to_lsn` in [xtrabackup_checkpoints](#xtrabackup_checkpoints).

`innodb_to_lsn` has the value of the [log sequence number (LSN)](../../storage-engines/innodb/innodb-redo-log.md#log-sequence-number-lsn) of the last checkpoint in the [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md).

### `partial`

If the backup is a [partial backup](partial-backup-and-restore-with-mariabackup.md), then this value will be `Y`.

Otherwise, this value will be `N`.

### `incremental`

If the backup is an [incremental backup](incremental-backup-and-restore-with-mariabackup.md), then this value will be `Y`.

Otherwise, this value will be `N`.

### `format`

This field's value is the format of the backup.

If the [--stream](mariabackup-options.md#-stream) option was set to `xbstream`, then this value will be `xbstream`.

If the [--stream](mariabackup-options.md#-stream) option was **not** provided, then this value will be `file`.

### `compressed`

If the [--compress](mariabackup-options.md#-compress) option was provided, then this value will be `compressed`.

Otherwise, this value will be `N`.

## `xtrabackup_slave_info`

If the [--slave-info](mariabackup-options.md#-slave-info) option is provided, then this file contains the [CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) command that can be used to set up a new server as a slave of the original server's master after the backup has been restored.

Mariabackup does **not** check if [GTIDs](../../../ha-and-performance/standard-replication/gtid.md) are being used in replication. It takes a shortcut and assumes that if the [gtid_slave_pos](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md#gtid_slave_pos) system variable is non-empty, then it writes the [CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) command with the [MASTER_USE_GTID](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_use_gtid) option set to `slave_pos`. Otherwise, it writes the [CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) command with the [MASTER_LOG_FILE](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_log_file) and [MASTER_LOG_POS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_log_pos) options using the master's [binary log](../../../server-management/server-monitoring-logs/binary-log/) file and position. See [MDEV-19264](https://jira.mariadb.org/browse/MDEV-19264) for more information.

## `xtrabackup_galera_info`

If the [--galera-info](mariabackup-options.md#-galera-info) option is provided, then this file contains information about a [Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/en/galera/README.md) node's state.

The file contains the values of the [wsrep_local_state_uuid](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_local_state_uuid) and [wsrep_last_committed](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_last_committed) status variables.

The values are written in the following format:

```bash
wsrep_local_state_uuid:wsrep_last_committed
```

For example:

```bash
d38587ce-246c-11e5-bcce-6bbd0831cc0f:1352215
```

## `<table>.delta`

If the backup is an [incremental backup](incremental-backup-and-restore-with-mariabackup.md), then this file contains changed pages for the table.

## `<table>.delta.meta`

If the backup is an [incremental backup](incremental-backup-and-restore-with-mariabackup.md), then this file contains metadata about `<table>.delta` files. The fields in this file are listed below.

### `page_size`

This field contains either the value of [innodb_page_size](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_page_size) or the value of the [KEY_BLOCK_SIZE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-table.md#key_block_size) table option for the table if the [ROW_FORMAT](../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-table.md#row_format) table option for the table is set to [COMPRESSED](../../../reference/storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md).

### `zip_size`

If the [ROW_FORMAT](../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-table.md#row_format) table option for this table is set to [COMPRESSED](../../../reference/storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md), then this field contains the value of the compressed page size.

### `space_id`

This field contains the value of the table's `space_id`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
