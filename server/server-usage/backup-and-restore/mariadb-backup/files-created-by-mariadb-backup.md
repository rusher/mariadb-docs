# Files Created by mariadb-backup

{% include "../../../.gitbook/includes/mariadb-backup-was-previous....md" %}

`mariadb-backup` creates the following files:

### `backup-my.cnf`

During the backup, any server options relevant to `mariadb-backup` are written to the `backup-my.cnf` option file, so that they can be re-read later during the `--prepare` stage.

### `ib_logfile0`

In [MariaDB 10.2.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10210-release-notes) and later, mariadb-backup creates an empty InnoDB redo log file called `ib_logfile0` as part of the --prepare stage. This file has 3 roles:

1. In the source server, `ib_logfile0` is the first (and possibly the only) InnoDB redo log file.
2. In the non-prepared backup, `ib_logfile0` contains all of the InnoDB redo log copied during the backup. Previous versions of mariadb-backup would use a file called xtrabackup\_logfile for this.
3. During the --prepare stage, `ib_logfile0` would previously be deleted. Now during the `--prepare` stage, `ib_logfile0` is initialized as an empty InnoDB redo log file. That way, if the backup is manually restored, any pre-existing InnoDB redo log files would get overwritten by the empty one. This helps to prevent certain kinds of known issues. For example, see mariadb-backup Overview: Manual Restore with Pre-existing InnoDB Redo Log files.

### `xtrabackup_logfile`

In [MariaDB 10.2.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1029-release-notes) and before, mariadb-backup creates `xtrabackup_logfile` to store the InnoDB redo log, In later versions, ib\_logfile0 is created instead.

### `xtrabackup_binlog_info`

This file stores the binary log file name and position that corresponds to the backup.

This file also stores the value of the gtid\_current\_pos system variable that correspond to the backup.

For example:

```bash
mariadb-bin.000096 568 0-1-2
```

The values in this file are only guaranteed to be consistent with the backup if the --no-lock option was **not** provided when the backup was taken.

### `xtrabackup_binlog_pos_innodb`

This file is created by mariadb-backup to provide the binary log file name and position when the --no-lock option is used. It can be used instead of the file "xtrabackup\_binlog\_info" to obtain transactionally consistent binlog coordinates from the backup of a master server with the --no-lock option to minimize the impact on a running server.

Whenever a transaction is committed inside InnoDB when the binary log is enabled, the corresponding binlog coordinates are written to the InnoDB redo log along with the transaction commit. This allows one to restore the binlog coordinates corresponding to the last commit done by InnoDB along with a backup.

The limitation of using "xtrabackup\_binlog\_pos\_innodb" with the "--no-lock" option is that no DDL or modification of non-transactional tables should be done during the backup. If the last event in the binlog is a DDL/non-transactional update, the coordinates in the file "xtrabackup\_binlog\_pos\_innodb" will be too old. But as long as only InnoDB updates are done during the backup, the coordinates will be correct.

### `xtrabackup_checkpoints`

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

#### `backup_type`

If the backup is a non-prepared full backup or a non-prepared partial backup, then `backup_type` is set to `full-backuped`.

If the backup is a non-prepared incremental backup, then `backup_type` is set to `incremental`.

If the backup has already been prepared, then `backup_type` is set to `log-applied`.

#### `from_lsn`

If `backup_type` is `full-backuped`, then `from_lsn` has the value of `0`.

If `backup_type` is `incremental`, then `from_lsn` has the value of the log sequence number (LSN) at which the backup started reading from the InnoDB redo log. This is internally used by mariadb-backup when preparing incremental backups.

This value can be manually set during an incremental backup with the --incremental-lsn option. However, it is generally better to let mariadb-backup figure out the `from_lsn` automatically by specifying a parent backup with the --incremental-basedir option.

#### `to_lsn`

`to_lsn` has the value of the log sequence number (LSN) of the last checkpoint in the InnoDB redo log. This is internally used by mariadb-backup when preparing incremental backups.

#### `last_lsn`

`last_lsn` has the value of the last log sequence number (LSN) read from the InnoDB redo log. This is internally used by mariadb-backup when preparing incremental backups.

### `xtrabackup_info`

The `xtrabackup_info` file contains information about the backup. The fields in this file are listed below.

If the --extra-lsndir option is provided, then an extra copy of this file will be saved in that directory.

#### `uuid`

If a UUID was provided by the --incremental-history-uuid option, then it will be saved here. Otherwise, this will be the empty string.

#### `name`

If a name was provided by the --history or the ---incremental-history-name options, then it will be saved here. Otherwise, this will be the empty string.

#### `tool_name`

The name of the mariadb-backup executable that performed the backup. This is generally `mariadb-backup`.

#### `tool_command`

The arguments that were provided to mariadb-backup when it performed the backup.

#### `tool_version`

The version of mariadb-backup that performed the backup.

#### `ibbackup_version`

The version of mariadb-backup that performed the backup.

#### `server_version`

The version of MariaDB Server that was backed up.

#### `start_time`

The time that the backup started.

#### `end_time`

The time that the backup ended.

#### `lock_time`

The amount of time that mariadb-backup held its locks.

#### `binlog_pos`

This field stores the binary log file name and position that corresponds to the backup.

This field also stores the value of the gtid\_current\_pos system variable that correspond to the backup.

The values in this field are only guaranteed to be consistent with the backup if the --no-lock option was **not** provided when the backup was taken.

#### `innodb_from_lsn`

This is identical to `from_lsn` in xtrabackup\_checkpoints.

If the backup is a full backup, then `innodb_from_lsn` has the value of `0`.

If the backup is an incremental backup, then `innodb_from_lsn` has the value of the log sequence number (LSN) at which the backup started reading from the InnoDB redo log.

#### `innodb_to_lsn`

This is identical to `to_lsn` in xtrabackup\_checkpoints.

`innodb_to_lsn` has the value of the log sequence number (LSN) of the last checkpoint in the InnoDB redo log.

#### `partial`

If the backup is a partial backup, then this value will be `Y`.

Otherwise, this value will be `N`.

#### `incremental`

If the backup is an incremental backup, then this value will be `Y`.

Otherwise, this value will be `N`.

#### `format`

This field's value is the format of the backup.

If the --stream option was set to `xbstream`, then this value will be `xbstream`.

If the --stream option was **not** provided, then this value will be `file`.

#### `compressed`

If the --compress option was provided, then this value will be `compressed`.

Otherwise, this value will be `N`.

### `xtrabackup_slave_info`

If the --slave-info option is provided, then this file contains the CHANGE MASTER command that can be used to set up a new server as a slave of the original server's master after the backup has been restored.

mariadb-backup does **not** check if GTIDs are being used in replication. It takes a shortcut and assumes that if the gtid\_slave\_pos system variable is non-empty, then it writes the CHANGE MASTER command with the MASTER\_USE\_GTID option set to `slave_pos`. Otherwise, it writes the CHANGE MASTER command with the MASTER\_LOG\_FILE and MASTER\_LOG\_POS options using the master's binary log file and position. See [MDEV-19264](https://jira.mariadb.org/browse/MDEV-19264) for more information.

### `xtrabackup_galera_info`

If the --galera-info option is provided, then this file contains information about a Galera Cluster node's state.

The file contains the values of the [wsrep\_local\_state\_uuid](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_local_state_uuid) and [wsrep\_last\_committed](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_last_committed) status variables.

The values are written in the following format:

```bash
wsrep_local_state_uuid:wsrep_last_committed
```

For example:

```bash
d38587ce-246c-11e5-bcce-6bbd0831cc0f:1352215
```

### `<table>.delta`

If the backup is an incremental backup, then this file contains changed pages for the table.

### `<table>.delta.meta`

If the backup is an incremental backup, then this file contains metadata about `<table>.delta` files. The fields in this file are listed below.

#### `page_size`

This field contains either the value of innodb\_page\_size or the value of the KEY\_BLOCK\_SIZE table option for the table if the ROW\_FORMAT table option for the table is set to COMPRESSED.

#### `zip_size`

If the ROW\_FORMAT table option for this table is set to COMPRESSED, then this field contains the value of the compressed page size.

#### `space_id`

This field contains the value of the table's `space_id`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
