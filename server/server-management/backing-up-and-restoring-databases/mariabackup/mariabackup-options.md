
# Mariabackup Options


There are a number of options available in `Mariabackup`.


## List of Options


### `--apply-log`


Prepares an existing backup to restore to the MariaDB Server. This is only valid in `innobackupex` mode, which can be enabled with the `[--innobackupex](#-innobackupex)` option.


Files that Mariabackup generates during `[--backup](#-backup)` operations in the target directory are not ready for use on the Server. Before you can restore the data to MariaDB, you first need to prepare the backup.


In the case of full backups, the files are not point in time consistent, since they were taken at different times. If you try to restore the database without first preparing the data, InnoDB rejects the new data as corrupt. Running Mariabackup with the `--prepare` command readies the data so you can restore it to MariaDB Server. When working with incremental backups, you need to use the `--prepare` command and the `[--incremental-dir](#-incremental-dir)` option to update the base backup with the deltas from an incremental backup.


```
$ mariabackup --innobackupex --apply-log
```

Once the backup is ready, you can use the `[--copy-back](#-copy-back)` or the `[--move-back](#-move-back)` commands to restore the backup to the server.


### `--apply-log-only`


If this option is used when preparing a backup, then only the redo log apply stage will be performed, and other stages of crash recovery will be ignored. This option is used with [incremental backups](incremental-backup-and-restore-with-mariabackup.md).



#### Note

This option is not needed or supported anymore. 


### `--backup`


Backs up your databases.


Using this command option, Mariabackup performs a backup operation on your database or databases. The backups are written to the target directory, as set by the `[--target-dir](#-target-dir)` option.


```
$ mariabackup --backup 
      --target-dir /path/to/backup \
      --user user_name --password user_passwd
```

Mariabackup can perform full and incremental backups. A full backup creates a snapshot of the database in the target directory. An incremental backup checks the database against a previously taken full backup, (defined by the `[--incremental-basedir](#-incremental-basedir)` option) and creates delta files for these changes.


In order to restore from a backup, you first need to run Mariabackup with the `[--prepare](#-prepare)` command option, to make a full backup point-in-time consistent or to apply incremental backup deltas to base. Then you can run Mariabackup again with either the `[--copy-back](#-copy-back)` or `[--move-back](#-move-back)` commands to restore the database.


For more information, see [Full Backup and Restore](full-backup-and-restore-with-mariabackup.md) and [Incremental Backup and Restore](incremental-backup-and-restore-with-mariabackup.md).


### `--binlog-info`


Defines how Mariabackup retrieves the binary log coordinates from the server.


```
--binlog-info[=OFF | ON | LOCKLESS | AUTO]
```

The `--binlog-info` option supports the following retrieval methods. When no retrieval method is provided, it defaults to `AUTO`.



| Option | Description |
| --- | --- |
| Option | Description |
| OFF | Disables the retrieval of binary log information |
| ON | Enables the retrieval of binary log information, performs locking where available to ensure consistency |
| LOCKLESS | Unsupported option |
| AUTO | Enables the retrieval of binary log information using ON or LOCKLESS where supported |



Using this option, you can control how Mariabackup retrieves the server's binary log coordinates corresponding to the backup.


When enabled, whether using `ON` or `AUTO`, Mariabackup retrieves information from the binlog during the backup process. When disabled with `OFF`, Mariabackup runs without attempting to retrieve binary log information. You may find this useful when you need to copy data without metadata like the binlog or replication coordinates.


```
$ mariabackup --binlog-info --backup
```

Currently, the `LOCKLESS` option depends on features unsupported by MariaDB Server. See the description of the `[xtrabackup_binlog_pos_innodb](files-created-by-mariabackup.md#xtrabackup_binlog_pos_innodb)` file for more information. If you attempt to run Mariabackup with this option, then it causes the utility to exit with an error.


### `--close-files`


Defines whether you want to close file handles.


Using this option, you can tell Mariabackup that you want to close file handles. Without this option, Mariabackup keeps files open in order to manage DDL operations. When working with particularly large tablespaces, closing the file can make the backup more manageable. However, it can also lead to inconsistent backups. Use at your own risk.


```
$ mariabackup --close-files --prepare
```

### `--compress`


This option was deprecated as it relies on the no longer maintained [QuickLZ](https://github.com/RT-Thread-packages/quicklz/) library. It will be removed in a future release - versions supporting this function will not be affected. It is recommended to instead backup to a stream (stdout), and use a 3rd party compression library to compress the stream, as described in 
[Using Encryption and Compression Tools With Mariabackup](using-encryption-and-compression-tools-with-mariabackup.md).


Defines the compression algorithm for backup files.


```
--compress[=compression_algorithm]
```

The `--compress` option only supports the now deprecated `quicklz` algorithm.



| Option | Description |
| --- | --- |
| Option | Description |
| quicklz | Uses the QuickLZ compression algorithm |



```
$ mariabackup --compress --backup
```

If a backup is compressed using this option, then Mariabackup will record that detail in the `[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)` file.


### `--compress-chunk-size`


Deprecated, for details see the `[--compress](#compress)` option.


Defines the working buffer size for compression threads.


```
--compress-chunk-size=#
```

Mariabackup can perform compression operations on the backup files before writing them to disk. It can also use multiple threads for parallel data compression during this process. Using this option, you can set the chunk size each thread uses during compression. It defaults to 64K.


```
$ mariabackup --backup --compress \
     --compress-threads=12 --compress-chunk-size=5M
```

To further configure backup compression, see the `[--compress](#-compress)` and `[--compress-threads](#-compress-threads)` options.


### `--compress-threads`


Deprecated, for details see the `[--compress](#compress)` option.


Defines the number of threads to use in compression.


```
--compress-threads=#
```

Mariabackup can perform compression operations on the backup files before writing them to disk. Using this option, you can define the number of threads you want to use for this operation. You may find this useful in speeding up the compression of particularly large databases. It defaults to single-threaded.


```
$ mariabackup --compress --compress-threads=12 --backup
```

To further configure backup compression, see the `[--compress](#-compress)` and `[--compress-chunk-size](#-compress-chunk-size)` options.


### `--copy-back`


Restores the backup to the data directory.


Using this command, Mariabackup copies the backup from the target directory to the data directory, as defined by the `[--datadir](#-h-datadir)` option. You must stop the MariaDB Server before running this command. The data directory must be empty. If you want to overwrite the data directory with the backup, use the `[--force-non-empty-directories](#-force-non-empty-directories)` option.


Bear in mind, before you can restore a backup, you first need to run Mariabackup with the `[--prepare](#-prepare)` option. In the case of full backups, this makes the files point-in-time consistent. With incremental backups, this applies the deltas to the base backup. Once the backup is prepared, you can run `--copy-back` to apply it to MariaDB Server.


```
$ mariabackup --copy-back --force-non-empty-directories
```

Running the `--copy-back` command copies the backup files to the data directory. Use this command if you want to save the backup for later. If you don't want to save the backup for later, use the `[--move-back](#-move-back)` command.


### `--core-file`


Defines whether to write a core file.


Using this option, you can configure Mariabackup to dump its core to file in the event that it encounters fatal signals. You may find this useful for review and debugging purposes.


```
$ mariabackup --core-file --backup
```

### `--databases`


Defines the databases and tables you want to back up.


```
--databases="database[.table][ database[.table] ...]"
```

Using this option, you can define the specific database or databases you want to back up. In cases where you have a particularly large database or otherwise only want to back up a portion of it, you can optionally also define the tables on the database.


```
$ mariabackup --backup \
      --databases="example.table1 example.table2"
```

In cases where you want to back up most databases on a server or tables on a database, but not all, you can set the specific databases or tables you don't want to back up using the `[--databases-exclude](#-databases-exclude)` option.


If a backup is a [partial backup](partial-backup-and-restore-with-mariabackup.md), then Mariabackup will record that detail in the `[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)` file.


In `innobackupex` mode, which can be enabled with the `[--innobackupex](#-innobackupex)` option, the `--databases` option can be used as described above, or it can be used to refer to a file, just as the `[--databases-file](https://mariadb.com/kb/en/-databases-file)` option can in the normal mode.


### `--databases-exclude`


Defines the databases you don't want to back up.


```
--databases-exclude="database[.table][ database[.table] ...]"
```

Using this option, you can define the specific database or databases you want to exclude from the backup process. You may find it useful when you want to back up most databases on the server or tables on a database, but would like to exclude a few from the process.


```
$ mariabackup --backup \
      --databases="example" \
      --databases-exclude="example.table1 example.table2"
```

To include databases in the backup, see the `[--databases](#-databases)` option option


If a backup is a [partial backup](partial-backup-and-restore-with-mariabackup.md), then Mariabackup will record that detail in the `[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)` file.


### `--databases-file`


Defines the path to a file listing databases and/or tables you want to back up.


```
--databases-file="/path/to/database-file"
```

Format the databases file to list one element per line, with the following syntax:


```
database[.table]
```

In cases where you need to back up a number of databases or specific tables in a database, you may find the syntax for the `[--databases](#-databases)` and `[--databases-exclude](#-databases-exclude)` options a little cumbersome. Using this option you can set the path to a file listing the databases or databases and tables you want to back up.


For instance, imagine you list the databases and tables for a backup in a file called `main-backup`.


```
$ cat main-backup
example1
example2.table1
example2.table2

$ mariabackup --backup --databases-file=main-backup
```

If a backup is a [partial backup](partial-backup-and-restore-with-mariabackup.md), then Mariabackup will record that detail in the `[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)` file.


### `-h, --datadir`


Defines the path to the database root.


```
--datadir=PATH
```

Using this option, you can define the path to the source directory. This is the directory that Mariabackup reads for the data it backs up. It should be the same as the MariaDB Server `[datadir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir)` system variable.


```
$ mariabackup --backup -h /var/lib64/mysql
```

### `--debug-sleep-before-unlock`


This is a debug-only option used by the Xtrabackup test suite.


### `--decompress`


Deprecated, for details see the `[--compress](#compress)` option.


This option requires that you have the `qpress` utility installed on your system.


Defines whether you want to decompress previously compressed backup files.


When you run Mariabackup with the `[--compress](#-compress)` option, it compresses the subsequent backup files, using the QuickLZ algorithm. Using this option, Mariabackup decompresses the compressed files from a previous backup.


For instance, run a backup with compression,


```
$ mariabackup --compress --backup
```

Then decompress the backup,


```
$ mariabackup --decompress
```

You can enable the decryption of multiple files at a time using the `[--parallel](#-parallel)` option. By default, Mariabackup does not remove the compressed files from the target directory. If you want to delete these files, use the `[--remove-original](#-remove-original)` option.


### `--debug-sync`


Defines the debug sync point. This option is only used by the Mariabackup test suite.


### `--defaults-extra-file`


Defines the path to an extra default [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md).


```
--defaults-extra-file=/path/to/config
```

Using this option, you can define an extra default [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) for Mariabackup. Unlike `[--defaults-file](#-defaults-file)`, this file is read after the default [option files](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) are read, allowing you to only overwrite the existing defaults.


```
$ mariabackup --backup \
      --defaults-file-extra=addition-config.cnf \
      --defaults-file=config.cnf
```

### `--defaults-file`


Defines the path to the default [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md).


```
--defaults-file=/path/to/config
```

Using this option, you can define a default [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) for Mariabackup. Unlike the `[--defaults-extra-file](#-defaults-extra-file)` option, when this option is provided, it completely replaces all default [option files](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md).


```
$ mariabackup --backup \
     --defaults-file="config.cnf
```

### `--defaults-group`


Defines the [option group](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) to read in the [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md).


```
--defaults-group="name"
```

In situations where you find yourself using certain Mariabackup options consistently every time you call it, you can set the options in an [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). The `--defaults-group` option defines what option group Mariabackup reads for its options.


Options you define from the command-line can be set in the configuration file using minor formatting changes. For instance, if you find yourself perform compression operations frequently, you might set `[--compress-threads](#-compress-threads)` and `[--compress-chunk-size](#-compress-chunk-size)` options in this way:


```
[mariabackup]
compress_threads = 12
compress_chunk_size = 64K
```

Now whenever you run a backup with the `[--compress](#-compress)` option, it always performs the compression using 12 threads and 64K chunks.


```
$ mariabackup --compress --backup
```

See [Mariabackup Overview: Server Option Groups](mariabackup-overview.md#server-option-groups) and [Mariabackup Overview: Client Option Groups](mariabackup-overview.md#client-option-groups) for a list of the option groups read by Mariabackup by default.


### `--encrypted-backup`


When this option is used with `--backup`, if Mariabackup encounters a page that has a non-zero `key_version` value, then Mariabackup assumes that the page is encrypted.


Use `--skip-encrypted-backup` instead to allow Mariabackup to copy unencrypted tables that were originally created before MySQL 5.1.48.


### `--export`


If this option is provided during the `--prepare` stage, then it tells Mariabackup to create `.cfg` files for each [InnoDB file-per-table tablespace](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md). These `.cfg` files are used to [import transportable tablespaces](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces) in the process of [restoring partial backups](partial-backup-and-restore-with-mariabackup.md) and [restoring individual tables and partitions](restoring-individual-tables-and-partitions-with-mariabackup.md).


The `--export` option could require rolling back incomplete transactions that had modified the table. This will likely create a "new branch of history" that does not correspond to the server that had been backed up, which makes it impossible to apply another incremental backup on top of such additional changes. The option should only be applied when doing a `--prepare` of the last incremental.


```
$ mariabackup --prepare --export
```

Mariabackup did not support the `[--export](mariabackup-options.md#-export)` option. See [MDEV-13466](https://jira.mariadb.org/browse/MDEV-13466) about that. In earlier versions of MariaDB, this means that Mariabackup could not create `.cfg` files for [InnoDB file-per-table tablespaces](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md) during the `--prepare` stage. You can still [import file-per-table tablespaces](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces) without the `.cfg` files in many cases, so it may still be possible in those versions to [restore partial backups](partial-backup-and-restore-with-mariabackup.md) or to [restore individual tables and partitions](restoring-individual-tables-and-partitions-with-mariabackup.md) with just the `.ibd` files. If you have a [full backup](full-backup-and-restore-with-mariabackup.md) and you need to create `.cfg` files for [InnoDB file-per-table tablespaces](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md), then you can do so by preparing the backup as usual without the `--export` option, and then restoring the backup, and then starting the server. At that point, you can use the server's built-in features to [copy the transportable tablespaces](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces).


### `--extra-lsndir`


Saves an extra copy of the `[xtrabackup_checkpoints](files-created-by-mariabackup.md#xtrabackup_checkpoints)` and `[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)` files into the given directory.


```
--extra-lsndir=PATH
```

When using the `[--backup](#-backup)` command option, Mariabackup produces a number of backup files in the target directory. Using this option, you can have Mariabackup produce additional copies of the `[xtrabackup_checkpoints](files-created-by-mariabackup.md#xtrabackup_checkpoints)` and `[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)` files in the given directory.


```
$ mariabackup --extra-lsndir=extras/ --backup
```

This is especially usefull when using `[--stream](#-stream)` for streaming output, e.g. for [compression and/or encryption using external tools](using-encryption-and-compression-tools-with-mariabackup.md) in combination with [incremental backups](incremental-backup-and-restore-with-mariabackup.md), as the `[xtrabackup_checkpoints](files-created-by-mariabackup.md#xtrabackup_checkpoints)` file necessary to determine the LSN to continue the incremental backup from is still accessible without uncompressing / decrypting the backup file first. Simply pass in the `--extra-lsndir` of the previous backup as 
`[--incremental-basedir](#-incremental-basedir)`


### `--force-non-empty-directories`


Allows `[--copy-back](#-copy-back)` or `[--move-back](#-move-back)` command options to use non-empty target directories.


When using Mariabackup with the `[--copy-back](#-copy-back)` or `[--move-back](#-move-back)` command options, they normally require a non-empty target directory to avoid conflicts. Using this option with either of command allows Mariabackup to use a non-empty directory.


```
$ mariabackup --force-non-empty-directories --copy-back
```

Bear in mind that this option does not enable overwrites. When copying or moving files into the target directory, if Mariabackup finds that the target file already exists, it fails with an error.


### `--ftwrl-wait-query-type`


Defines the type of query allowed to complete before Mariabackup issues the global lock.


```
--ftwrl-wait-query-type=[ALL | UPDATE | SELECT]
```

The `--ftwrl-wait-query-type` option supports the following query types. The default value is `ALL`.



| Option | Description |
| --- | --- |
| Option | Description |
| ALL | Waits until all queries complete before issuing the global lock |
| SELECT | Waits until [SELECT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statements complete before issuing the global lock |
| UPDATE | Waits until [UPDATE](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md) statements complete before issuing the global lock |



When Mariabackup runs, it issues a global lock to prevent data from changing during the backup process. When it encounters a statement in the process of executing, it waits until the statement is finished before issuing the global lock. Using this option, you can modify this default behavior to ensure that it waits only for certain query types, such as for `[SELECT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)` and `[UPDATE](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md)` statements.


```
$ mariabackup --backup  \
      --ftwrl-wait-query-type=UPDATE
```

### `--ftwrl-wait-threshold`


Defines the minimum threshold for identifying long-running queries for FTWRL.


```
--ftwrl-wait-threshold=#
```

When Mariabackup runs, it issues a global lock to prevent data from changing during the backup process and ensure a consistent record. If it encounters statements still in the process of executing, it waits until they complete before setting the lock. Using this option, you can set the threshold at which Mariabackup engages FTWRL. When it `[--ftwrl-wait-timeout](#-ftwrl-wait-timeout)` is not 0 and a statement has run for at least the amount of time given this argument, Mariabackup waits until the statement completes or until
the `[--ftwrl-wait-timeout](#-ftwrl-wait-timeout)` expires before setting the global lock and starting the backup.


```
$ mariabackup --backup \
     --ftwrl-wait-timeout=90 \
     --ftwrl-wait-threshold=30
```

### `--ftwrl-wait-timeout`


Defines the timeout to wait for queries before trying to acquire the global lock. The global lock refers to `[BACKUP STAGE BLOCK_COMMIT](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/backup-commands/backup-stage.md#backup-stage-block_commit)`. The global lock refers to `[FLUSH TABLES WITH READ LOCK (FTWRL)](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md#the-purpose-of-flush-tables-table_list-with-read-lock)`.


```
--ftwrl-wait-timeout=#
```

When Mariabackup runs, it acquires a global lock to prevent data from changing during the backup process and ensure a consistent record. If it encounters statements still in the process of executing, it can be configured to wait until the statements complete before trying to acquire the global lock.


If the `--ftwrl-wait-timeout` is set to 0, then Mariabackup tries to acquire the global lock immediately without waiting. This is the default value.


If the `--ftwrl-wait-timeout` is set to a non-zero value, then Mariabackup waits for the configured number of seconds until trying to acquire the global lock.


Starting in [MariaDB 10.5.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1053-release-notes.md), Mariabackup will exit if it can't acquire the global lock after waiting for the configured number of seconds. In earlier versions, it could wait for the global lock indefinitely, even if `--ftwrl-wait-timeout` was set to a non-zero value.


```
$ mariabackup --backup \
      --ftwrl-wait-query-type=UPDATE \
      --ftwrl-wait-timeout=5
```

### `--galera-info`


Defines whether you want to back up information about a [Galera Cluster](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md) node's state.


When this option is used, Mariabackup creates an additional file called `[xtrabackup_galera_info](files-created-by-mariabackup.md#xtrabackup_galera_info)`, which records information about a [Galera Cluster](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md) node's state. It records the values of the `[wsrep_local_state_uuid](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-status-variables.md#wsrep_local_state_uuid)` and `[wsrep_last_committed](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-status-variables.md#wsrep_last_committed)` status variables.


You should only use this option when backing up a [Galera Cluster](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md) node. If the server is not a [Galera Cluster](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md) node, then this option has no effect.


This option, when enabled and used with [GTID replication](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md), will rotate the binary logs at backup time.


```
$ mariabackup --backup --galera-info
```

### `--history`


Defines whether you want to track backup history in the `PERCONA_SCHEMA.xtrabackup_history` table.


```
--history[=name]
```

When using this option, Mariabackup records its operation in a table on the MariaDB Server. Passing a name to this option allows you group backups under arbitrary terms for later processing and analysis.


```
$ mariabackup --backup --history=backup_all
```

Currently, the table it uses by default is named `mysql.mariadb_backup_history`. Prior to [MariaDB 10.11](../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md), the default table was `PERCONA_SCHEMA.xtrabackup_history`.


Mariabackup will also record this in the `[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)` file.


### `-H, --host`


Defines the host for the MariaDB Server you want to backup.


```
--host=name
```

Using this option, you can define the host to use when connecting to a MariaDB Server over TCP/IP. By default, Mariabackup attempts to connect to the local host.


```
$ mariabackup --backup \
      --host="example.com"
```

### `--include`


This option is a regular expression to be matched against table names in databasename.tablename format. It is
equivalent to the `[--tables](#-tables)` option. This is only valid in `innobackupex` mode, which can be enabled with the `[--innobackupex](#-innobackupex)` option.


### `--incremental`


Defines whether you want to take an increment backup, based on another backup. This is only valid in `innobackupex` mode, which can be enabled with the `[--innobackupex](#-innobackupex)` option.


```
mariabackup --innobackupex --incremental
```

Using this option with the `[--backup](#-backup)` command option makes the operation incremental rather than a complete overwrite. When this option is specified, either the `[--incremental-lsn](#-incremental-lsn) or `[--incremental-basedir](#-incremental-basedir)` options can also be given. If neither option is given, option `[--incremental-basedir](#-incremental-basedir)` is used by default, set to the first timestamped backup directory in the backup base directory.`


```
$ mariabackup --innobackupex --backup --incremental \
     --incremental-basedir=/data/backups \
     --target-dir=/data/backups
```

If a backup is a [incremental backup](incremental-backup-and-restore-with-mariabackup.md), then Mariabackup will record that detail in the `[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)` file.


### `--incremental-basedir`


Defines whether you want to take an incremental backup, based on another backup.


```
--incremental-basedir=PATH
```

Using this option with the `[--backup](#-backup)` command option makes the operation incremental rather than a complete overwrite. Mariabackup will only copy pages from `.ibd` files if they are newer than the backup in the specified directory.


```
$ mariabackup --backup \
     --incremental-basedir=/data/backups \
     --target-dir=/data/backups
```

If a backup is a [incremental backup](incremental-backup-and-restore-with-mariabackup.md), then Mariabackup will record that detail in the `[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)` file.


### `--incremental-dir`


Defines whether you want to take an incremental backup, based on another backup.


```
--increment-dir=PATH
```

Using this option with `[--prepare](#-prepare)` command option makes the operation incremental rather than a complete overwrite. Mariabackup will apply `.delta` files and log files into the target directory.


```
$ mariabackup --prepare \
      --increment-dir=backups/
```

If a backup is a [incremental backup](incremental-backup-and-restore-with-mariabackup.md), then Mariabackup will record that detail in the `[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)` file.


### `--incremental-force-scan`


Defines whether you want to force a full scan for incremental backups.


When using Mariabackup to perform an incremental backup, this option forces it to also perform a full scan of the data pages being backed up, even when there's bitmap data on the changes. MariaDB does not support changed page bitmaps, so this option is useless in those versions. See [MDEV-18985](https://jira.mariadb.org/browse/MDEV-18985) for more information.


```
$ mariabackup --backup \
     --incremental-basedir=/path/to/target \
     --incremental-force-scan
```

### `--incremental-history-name`


Defines a logical name for the backup.


```
--incremental-history-name=name
```

Mariabackup can store data about its operations on the MariaDB Server. Using this option, you can define the logical name it uses in identifying the backup.


```
$ mariabackup --backup \
     --incremental-history-name=morning_backup
```

Currently, the table it uses by default is named `mysql.mariadb_backup_history`. Prior to [MariaDB 10.11](../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md), the default table was `PERCONA_SCHEMA.xtrabackup_history`.


Mariabackup will also record this in the `[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)` file.


### `--incremental-history-uuid`


Defines a UUID for the backup.


```
--incremental-history-uuid=name
```

Mariabackup can store data about its operations on the MariaDB Server. Using this option, you can define the UUID it uses in identifying a previous backup to increment from. It checks `[--incremental-history-name](#-incremental-history-name)`, `[--incremental-basedir](#-incremental-basedir)`, and `[--incremental-lsn](#-incremental-lsn)`. If Mariabackup fails to find a valid lsn, it generates an error.


```
$ mariabackup --backup \
      --incremental-history-uuid=main-backup012345678
```

Currently, the table it uses is named `PERCONA_SCHEMA.xtrabackup_history`, but expect that name to change in future releases. See [MDEV-19246](https://jira.mariadb.org/browse/MDEV-19246) for more information.


Mariabackup will also record this in the `[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)` file.


### `--incremental-lsn`


Defines the sequence number for incremental backups.


```
--incremental-lsn=name
```

Using this option, you can define the sequence number (LSN) value for `[--backup](#-backup)` operations. During backups, Mariabackup only copies `.ibd` pages newer than the specified values.


**WARNING**: Incorrect LSN values can make the backup unusable. It is impossible to diagnose this issue.


### `--innobackupex`


Deprecated


Enables `innobackupex` mode, which is a compatibility mode.


```
$ mariabackup --innobackupex
```

In `innobackupex` mode, Mariabackup has the following differences:


* To prepare a backup, the `[--apply-log](#-apply-log)` option is used instead of the `[--prepare](#-prepare)` option.
* To create an [incremental backup](incremental-backup-and-restore-with-mariabackup.md), the `[--incremental](#-incremental)` option is supported.
* The `[--no-timestamp](#-no-timestamp)` option is supported.
* To create a [partial backup](partial-backup-and-restore-with-mariabackup.md), the `[--include](#--include)` option is used instead of the `[--tables](#-tables)` option.
* To create a [partial backup](partial-backup-and-restore-with-mariabackup.md), the `[--databases](#--databases)` option can still be used, but it's behavior changes slightly.
* The `[--target-dir](#-target-dir)` option is not used to specify the backup directory. The backup directory should instead be specified as a standalone argument.


The primary purpose of `innobackupex` mode is to allow scripts and tools to more easily migrate to Mariabackup if they were originally designed to use the `innobackupex` utility that is included with [Percona XtraBackup](../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md). It is not recommended to use this mode in new scripts, since it is not guaranteed to be supported forever. See [MDEV-20552](https://jira.mariadb.org/browse/MDEV-20552) for more information.


### `--innodb`


This option has no effect. Set only for MySQL option compatibility.


### `--innodb-adaptive-hash-index`


Enables InnoDB Adaptive Hash Index.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option you can explicitly enable the InnoDB Adaptive Hash Index. This feature is enabled by default for Mariabackup. If you want to disable it, use `[--skip-innodb-adaptive-hash-index](#-skip-innodb-adaptive-hash-index)`.


```
$ mariabackup --backup \
      --innodb-adaptive-hash-index
```

### `--innodb-autoextend-increment`


Defines the increment in megabytes for auto-extending the size of tablespace file.


```
--innodb-autoextend-increment=36
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set the increment in megabytes for automatically extending the size of tablespace data file in InnoDB.


```
$ mariabackup --backup \
     --innodb-autoextend-increment=35
```

### `--innodb-buffer-pool-filename`


Using this option has no effect. It is available to provide compatibility with the MariaDB Server.


### `--innodb-buffer-pool-size`


Defines the memory buffer size InnoDB uses the cache data and indexes of the table.


```
--innodb-buffer-pool-size=124M
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can configure the buffer pool for InnoDB operations.


```
$ mariabackup --backup \
      --innodb-buffer-pool-size=124M
```

### `--innodb-checksum-algorithm`


[innodb_checksum_algorithm](../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm) was deprecated in [MariaDB 10.5.10](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10510-release-notes.md) and removed in [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md).


In earlier versions, it is used to define the checksum algorithm.


```
--innodb-checksum-algorithm=crc32
                           | strict_crc32
                           | innodb
                           | strict_innodb
                           | none
                           | strict_none
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can specify the algorithm Mariabackup uses when checksumming on InnoDB tables. Currently, MariaDB supports the following algorithms `CRC32`, `STRICT_CRC32`, `INNODB`, `STRICT_INNODB`, `NONE`, `STRICT_NONE`.


```
$ mariabackup --backup \
      ---innodb-checksum-algorithm=strict_innodb
```

### `--innodb-data-file-path`


Defines the path to individual data files.


```
--innodb-data-file-path=/path/to/file
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option you can define the path to InnoDB data files. Each path is appended to the `[--innodb-data-home-dir](#-innodb-data-home-dir)` option.


```
$ mariabackup --backup \
     --innodb-data-file-path=ibdata1:13M:autoextend \
     --innodb-data-home-dir=/var/dbs/mysql/data
```

### `--innodb-data-home-dir`


Defines the home directory for InnoDB data files.


```
--innodb-data-home-dir=PATH
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option you can define the path to the directory containing InnoDB data files. You can specific the files using the `[--innodb-data-file-path](#-innodb-data-file-path)` option.


```
$ mariabackup --backup \
     --innodb-data-file-path=ibdata1:13M:autoextend \
     --innodb-data-home-dir=/var/dbs/mysql/data
```

### `--innodb-doublewrite`


Enables doublewrites for InnoDB tables.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. When using this option, Mariabackup improves fault tolerance on InnoDB tables with a doublewrite buffer. By default, this feature is enabled. Use this option to explicitly enable it. To disable doublewrites, use the `[--skip-innodb-doublewrite](#-skip-innodb-doublewrite)` option.


```
$ mariabackup --backup \
     --innodb-doublewrite
```

### `--innodb-encrypt-log`


Defines whether you want to encrypt InnoDB logs.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can tell Mariabackup that you want to encrypt logs from its InnoDB activity.


### `--innodb-file-io-threads`


Defines the number of file I/O threads in InnoDB.


```
--innodb-file-io-threads=#
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the number of file I/O threads Mariabackup uses on InnoDB tables.


```
$ mariabackup --backup \
     --innodb-file-io-threads=5
```

### `--innodb-file-per-table`


Defines whether you want to store each InnoDB table as an `.ibd` file.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option causes Mariabackup to store each InnoDB table as an `.ibd` file in the target directory.


### `--innodb-flush-method`


Defines the data flush method. Ignored from [MariaDB 11.0](../../../../release-notes/mariadb-community-server/what-is-mariadb-110.md).


```
--innodb-flush-method=fdatasync 
                     | O_DSYNC 
                     | O_DIRECT 
                     | O_DIRECT_NO_FSYNC 
                     | ALL_O_DIRECT
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the data flush method Mariabackup uses with InnoDB tables.


```
$ mariabackup --backup \
      --innodb-flush-method==_DIRECT_NO_FSYNC
```

### `--innodb-io-capacity`


Defines the number of IOP's the utility can perform.


```
--innodb-io-capacity=#
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can limit the I/O activity for InnoDB background tasks. It should be set around the number of I/O operations per second that the system can handle, based on drive or drives being used.


```
$ mariabackup --backup \
     --innodb-io-capacity=200
```

### `--innodb-log-checksums`


Defines whether to include checksums in the InnoDB logs.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can explicitly set Mariabackup to include checksums in the InnoDB logs. The feature is enabled by default. To disable it, use the `[--skip-innodb-log-checksums](#-skip-innodb-log-checksums)` option.


```
$ mariabackup --backup \
      --innodb-log-checksums
```

### `--innodb-log-buffer-size`


This option has no functionality in Mariabackup. It exists for MariaDB Server compatibility.


### `--innodb-log-files-in-group`


This option has no functionality in Mariabackup. It exists for MariaDB Server compatibility.


### `--innodb-log-group-home-dir`


Defines the path to InnoDB log files.


```
--innodb-log-group-home-dir=PATH
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the path to InnoDB log files.


```
$ mariabackup --backup \
     --innodb-log-group-home-dir=/path/to/logs
```

### `--innodb-max-dirty-pages-pct`


Defines the percentage of dirty pages allowed in the InnoDB buffer pool.


```
--innodb-max-dirty-pages-pct=#
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the maximum percentage of dirty, (that is, unwritten) pages that Mariabackup allows in the InnoDB buffer pool.


```
$ mariabackup --backup \
     --innodb-max-dirty-pages-pct=80
```

### `--innodb-open-files`


Defines the number of files kept open at a time.


```
--innodb-open-files=#
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set the maximum number of files InnoDB keeps open at a given time during backups.


```
$ mariabackup --backup \
      --innodb-open-files=10
```

### `--innodb-page-size`


Defines the universal page size.


```
--innodb-page-size=#
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the universal page size in bytes for Mariabackup.


```
$ mariabackup --backup \
     --innodb-page-size=16k
```

### `--innodb-read-io-threads`


Defines the number of background read I/O threads in InnoDB.


```
--innodb-read-io-threads=#
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set the number of I/O threads MariaDB uses when reading from InnoDB.


```
$ mariabackup --backup \
      --innodb-read-io-threads=4
```

### `--innodb-undo-directory`


Defines the directory for the undo tablespace files.


```
--innodb-undo-directory=PATH
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the path to the directory where you want MariaDB to store the undo tablespace on InnoDB tables. The path can be absolute.


```
$ mariabackup --backup \
     --innodb-undo-directory=/path/to/innodb_undo
```

### `--innodb-undo-tablespaces`


Defines the number of undo tablespaces to use.


```
--innodb-undo-tablespaces=#
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the number of undo tablespaces you want to use during the backup.


```
$ mariabackup --backup \
      --innodb-undo-tablespaces=10
```

### `--innodb-use-native-aio`


Defines whether you want to use native AI/O.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can enable the use of the native asynchronous I/O subsystem. It is only available on Linux operating systems.


```
$ mariabackup --backup \
      --innodb-use-native-aio
```

### `--innodb-write-io-threads`


Defines the number of background write I/O threads in InnoDB.


```
--innodb-write-io-threads=#
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set the number of background write I/O threads Mariabackup uses.


```
$ mariabackup --backup \
     --innodb-write-io-threads=4
```

### `--kill-long-queries-timeout`


Defines the timeout for blocking queries.


```
--kill-long-queries-timeout=#
```

When Mariabackup runs, it issues a `FLUSH TABLES WITH READ LOCK` statement. It then identifies blocking queries. Using this option you can set a timeout in seconds for these blocking queries. When the time runs out, Mariabackup kills the queries.


The default value is 0, which causes Mariabackup to not attempt killing any queries.


```
$ mariabackup --backup \
      --kill-long-queries-timeout=10
```

### `--kill-long-query-type`


Defines the query type the utility can kill to unblock the global lock.


```
--kill-long-query-type=ALL | UPDATE | SELECT
```

When Mariabackup encounters a query that sets a global lock, it can kill the query in order to free up MariaDB Server for the backup. Using this option, you can choose the types of query it kills: `[SELECT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)`, `[UPDATE](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md)`, or both set with `ALL`. The default is `ALL`.


```
$ mariabackup --backup \
      --kill-long-query-type=UPDATE
```

### `--lock-ddl-per-table`


Prevents DDL for each table to be backed up by acquiring MDL lock on that.
NOTE: Unless --no-lock option was also specified, conflicting DDL queries , will be killed at the end of backup This is done avoid deadlock between "FLUSH TABLE WITH READ LOCK", user's DDL query (ALTER, RENAME), and MDL lock on table.


### `--log`


This option has no functionality. It is set to ensure compatibility with MySQL.


### `--log-bin`


Defines the base name for the log sequence.


```
--log-bin[=name]
```

Using this option you, you can set the base name for Mariabackup to use in log sequences.


### `--log-copy-interval`


Defines the copy interval between checks done by the log copying thread.


```
--log-copy-interval=#
```

Using this option, you can define the copy interval Mariabackup uses between checks done by the log copying thread. The given value is in milliseconds.


```
$ mariabackup --backup \
      --log-copy-interval=50
```

### `--log-innodb-page-corruption`


Continue backup if InnoDB corrupted pages are found. The pages are logged in `innodb_corrupted_pages` and backup is finished with error. [--prepare](#-prepare) will try to fix corrupted pages. If `innodb_corrupted_pages` exists after [--prepare](#-prepare) in base backup directory, backup still contains corrupted pages and can not be considered as consistent.


Added in [MariaDB 10.5.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1059-release-notes.md)


### `--move-back`


Restores the backup to the data directory.


Using this command, Mariabackup moves the backup from the target directory to the data directory, as defined by the `[--datadir](#-h-datadir)` option. You must stop the MariaDB Server before running this command. The data directory must be empty. If you want to overwrite the data directory with the backup, use the `[--force-non-empty-directories](#-force-non-empty-directories)` option.


Bear in mind, before you can restore a backup, you first need to run Mariabackup with the `[--prepare](#-prepare)` option. In the case of full backups, this makes the files point-in-time consistent. With incremental backups, this applies the deltas to the base backup. Once the backup is prepared, you can run `--move-back` to apply it to MariaDB Server.


```
$ mariabackup --move-back \
      --datadir=/var/mysql
```

Running the `--move-back` command moves the backup files to the data directory. Use this command if you don't want to save the backup for later. If you do want to save the backup for later, use the `[--copy-back](#-copy-back)` command.


### `--mysqld`


Used internally to prepare a backup.


### `--no-backup-locks`


Mariabackup locks the database by default when it runs. This option disables support for Percona Server's backup locks.


When backing up Percona Server, Mariabackup would use backup locks by default. To be specific, backup locks refers to the `LOCK TABLES FOR BACKUP` and `LOCK BINLOG FOR BACKUP` statements. This option can be used to disable support for Percona Server's backup locks. This option has no effect when the server does not support Percona's backup locks.


Deprecated and has no effect from [MariaDB 10.11.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-8-release-notes.md), [MariaDB 11.0.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes.md), [MariaDB 11.1.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes.md) and [MariaDB 11.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes.md) as MariaDB will now always use backup locks for better performance. See [MDEV-32932](https://jira.mariadb.org/browse/MDEV-32932).


```
$ mariabackup --backup --no-backup-locks
```

### `--no-lock`


Disables table locks with the `FLUSH TABLE WITH READ LOCK` statement.


Using this option causes Mariabackup to disable table locks with the `FLUSH TABLE WITH READ LOCK` statement. Only use this option if:


* You are not executing DML statements on non-InnoDB tables during the backup. This includes the `mysql` database system tables (which are MyISAM).
* You are not executing any DDL statements during the backup.
* You are _not_ using the file "xtrabackup_binlog_info", which is not consistent with the data when --no-lock is used. Use the file "xtrabackup_binlog_pos_innodb" [link] instead.
* All tables you're backing up use the InnoDB storage engine.


```
$ mariabackup --backup --no-lock
```

If you're considering `--no-lock` due to backups failing to acquire locks, this may be due to incoming replication events preventing the lock. Consider using the [--safe-slave-backup](#-safe-slave-backup) option to momentarily stop the replica thread. This alternative may help the backup to succeed without resorting to `--no-lock`.


The --no-lock option only provides a consistent backup if the user ensures that no DDL or non-transactional table updates occur during the backup. The --no-lock option is not supported by MariaDB plc.


### `--no-timestamp`


This option prevents creation of a time-stamped subdirectory of the BACKUP-ROOT-DIR given on the command line. When it is specified, the backup is done in BACKUP-ROOT-DIR instead. This is only valid in `innobackupex` mode, which can be enabled with the `[--innobackupex](#-innobackupex)` option.


### `--no-version-check`


Disables version check.


Using this option, you can disable Mariabackup version check.


```
$ mariabackup --backup --no-version-check
```

### `--open-files-limit`


Defines the maximum number of file descriptors.


```
--open-files-limit=#
```

Using this option, you can define the maximum number of file descriptors Mariabackup reserves with `setrlimit()`.


```
$ mariabackup --backup \
      --open-files-limit=
```

### `--parallel`


Defines the number of threads to use for parallel data file transfer.


```
--parallel=#
```

Using this option, you can set the number of threads Mariabackup uses for parallel data file transfers. By default, it is set to 1.


### `-p, --password`


Defines the password to use to connect to MariaDB Server.


```
--password=passwd
```

When you run Mariabackup, it connects to MariaDB Server in order to access and back up the databases and tables. Using this option, you can set the password Mariabackup uses to access the server. To set the user, use the `[--user](#-u-user)` option.


```
$ mariabackup --backup \
      --user=root \
      --password=root_password
```

### `--plugin-dir`


Defines the directory for server plugins.


```
--plugin-dir=PATH
```

Using this option, you can define the path Mariabackup reads for MariaDB Server plugins. It only uses it during the `[--prepare](#-prepare)` phase to load the encryption plugin. It defaults to the `[plugin_dir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#plugin_dir)` server system variable.


```
$ mariabackup --backup \
      --plugin-dir=/var/mysql/lib/plugin
```

### `--plugin-load`


Defines the encryption plugins to load.


```
--plugin-load=name
```

Using this option, you can define the encryption plugin you want to load. It is only used during the `[--prepare](#-prepare)` phase to load the encryption plugin. It defaults to the server `--plugin-load` option.


The option was removed.


### `-P, --port`


Defines the server port to connect to.


```
--port=#
```

When you run Mariabackup, it connects to MariaDB Server in order to access and back up your databases and tables. Using this option, you can set the port the utility uses to access the server over TCP/IP. To set the host, see the `[--host](#-h-host)` option. Use `mysql --help` for more details.


```
$ mariabackup --backup \
      --host=192.168.11.1 \
      --port=3306
```

### `--prepare`


Prepares an existing backup to restore to the MariaDB Server.


Files that Mariabackup generates during `[--backup](#-backup)` operations in the target directory are not ready for use on the Server. Before you can restore the data to MariaDB, you first need to prepare the backup.


In the case of full backups, the files are not point in time consistent, since they were taken at different times. If you try to restore the database without first preparing the data, InnoDB rejects the new data as corrupt. Running Mariabackup with the `--prepare` command readies the data so you can restore it to MariaDB Server. When working with incremental backups, you need to use the `--prepare` command and the `[--incremental-dir](#-incremental-dir)` option to update the base backup with the deltas from an incremental backup.


```
$ mariabackup --prepare
```

Once the backup is ready, you can use the `[--copy-back](#-copy-back)` or the `[--move-back](#-move-back)` commands to restore the backup to the server.


### `--print-defaults`


Prints the utility argument list, then exits.


Using this argument, MariaDB prints the argument list to stdout and then exits. You may find this useful in debugging to see how the options are set for the utility.


```
$ mariabackup --print-defaults
```

### `--print-param`


Prints the MariaDB Server options needed for copyback.


Using this option, Mariabackup prints to stdout the MariaDB Server options that the utility requires to run the `[--copy-back](#-copy-back)` command option.


```
$ mariabackup --print-param
```

### `--rollback-xa`


By default, Mariabackup will not commit or rollback uncommitted XA transactions, and when the backup is restored, any uncommitted XA transactions must be manually committed using `XA COMMIT` or manually rolled back using `XA ROLLBACK`.



##### MariaDB starting with [10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)
Mariabackup's `--rollback-xa` option is not present because the server has more robust ways of handling uncommitted XA transactions.


This is an experimental option. Do not use this option in older versions. Older implementation can cause corruption of InnoDB data.


### `--rsync`


Defines whether to use rsync.


During normal operation, Mariabackup transfers local non-InnoDB files using a separate call to `cp` for each file. Using this option, you can optimize this process by performing this transfer with rsync, instead.


```
$ mariabackup --backup --rsync
```

This option is not compatible with the `[--stream](#-stream)` option.


Deprecated and has no effect from [MariaDB 10.11.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-8-release-notes.md), [MariaDB 11.0.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes.md), [MariaDB 11.1.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes.md) and [MariaDB 11.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes.md) as rsync will not work on tables that are in use. See [MDEV-32932](https://jira.mariadb.org/browse/MDEV-32932).


### `--safe-slave-backup`


Stops replica SQL threads for backups.


When running Mariabackup on a server that uses replication, you may occasionally encounter locks that block backups. Using this option, it stops replica SQL threads and waits until the `Slave_open_temp_tables` in the `SHOW STATUS` statement is zero. If there are no open temporary tables, the backup runs, otherwise the SQL thread starts and stops until there are no open temporary tables.


```
$ mariabackup --backup \
      --safe-slave-backup \
      --safe-slave-backup-timeout=500
```

The backup fails if the `Slave_open_temp_tables` doesn't reach zero after the timeout period set by the [--safe-slave-backup-timeout](#-safe-slave-backup-timeout) option.


### `--safe-slave-backup-timeout`


Defines the timeout for replica backups.


```
--safe-slave-backup-timeout=#
```

When running Mariabackup on a server that uses replication, you may occasionally encounter locks that block backups. With the [--safe-slave-backup](#-safe-slave-backup) option, it waits until the `Slave_open_temp_tables` in the `SHOW STATUS` statement reaches zero. Using this option, you set how long it waits. It defaults to 300.


```
$ mariabackup --backup \
      --safe-slave-backup \
      --safe-slave-backup-timeout=500
```

### `--secure-auth`


Refuses client connections to servers using the older protocol.


Using this option, you can set it explicitly to refuse client connections to the server when using the older protocol, from before 4.1.1. This feature is enabled by default. Use the [--skip-secure-auth](#-skip-secure-auth) option to disable it.


```
$ mariabackup --backup --secure-auth
```

### `--skip-innodb-adaptive-hash-index`


Disables InnoDB Adaptive Hash Index.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option you can explicitly disable the InnoDB Adaptive Hash Index. This feature is enabled by default for Mariabackup. If you want to explicitly enable it, use `[--innodb-adaptive-hash-index](#-innodb-adaptive-hash-index)`.


```
$ mariabackup --backup \
      --skip-innodb-adaptive-hash-index
```

### `--skip-innodb-doublewrite`


Disables doublewrites for InnoDB tables.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. When doublewrites are enabled, InnoDB improves fault tolerance with a doublewrite buffer. By default this feature is turned on. Using this option you can disable it for Mariabackup. To explicitly enable doublewrites, use the `[--innodb-doublewrite](#-innodb-doublewrite)` option.


```
$ mariabackup --backup \
     --skip-innodb-doublewrite
```

### `--skip-innodb-log-checksums`


Defines whether to exclude checksums in the InnoDB logs.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set Mariabackup to exclude checksums in the InnoDB logs. The feature is enabled by default. To explicitly enable it, use the `[--innodb-log-checksums](#-innodb-log-checksums)` option.


### `--skip-secure-auth`


Refuses client connections to servers using the older protocol.


Using this option, you can set it accept client connections to the server when using the older protocol, from before 4.1.1. By default, it refuses these connections. Use the `[--secure-auth](#-secure-auth)` option to explicitly enable it.


```
$ mariabackup --backup --skip-secure-auth
```

### `--slave-info`


Prints the binary log position and the name of the primary server.


If the server is a [replica](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md), then this option causes Mariabackup to print the hostname of the replica's replication primary and the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) file and position of the [replica's SQL thread](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#replica-sql-thread) to `stdout`.


This option also causes Mariabackup to record this information as a [CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) command that can be used to set up a new server as a replica of the original server's primary after the backup has been restored. This information will be written to to the [xtrabackup_slave_info](files-created-by-mariabackup.md#xtrabackup_slave_info) file.


Mariabackup does **not** check if [GTIDs](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) are being used in replication. It takes a shortcut and assumes that if the [gtid_slave_pos](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md#gtid_slave_pos) system variable is non-empty, then it writes the [CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) command with the [MASTER_USE_GTID](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_use_gtid) option set to `slave_pos`. Otherwise, it writes the [CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) command with the [MASTER_LOG_FILE](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_log_file) and [MASTER_LOG_POS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_log_pos) options using the primary's [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) file and position. See [MDEV-19264](https://jira.mariadb.org/browse/MDEV-19264) for more information.


```
$ mariabackup --slave-info
```

### `-S, --socket`


Defines the socket for connecting to local database.


```
--socket=name
```

Using this option, you can define the UNIX domain socket you want to use when connecting to a local database server. The option accepts a string argument. For more information, see the `mysql --help` command.


```
$ mariabackup --backup \
      --socket=/var/mysql/mysql.sock
```

### `--ssl`


Enables [TLS](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/README.md). By using this option, you can explicitly configure Mariabackup to to encrypt its connection with [TLS](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/README.md) when communicating with the server. You may find this useful when performing backups in environments where security is extra important or when operating over an insecure network.


TLS is also enabled even without setting this option when certain other TLS options are set. For example, see the descriptions of the following options:


* `[--ssl-ca](#-ssl-ca)`
* `[--ssl-capath](#-ssl-capath)`
* `[--ssl-cert](#-ssl-cert)`
* `[--ssl-cipher](#-ssl-cipher)`
* `[--ssl-key](#-ssl-key)`


### `--ssl-ca`


Defines a path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for [TLS](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/README.md). This option requires that you use the absolute path, not a relative path. For example:


```
--ssl-ca=/etc/my.cnf.d/certificates/ca.pem
```

This option is usually used with other TLS options. For example:


```
$ mariabackup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem
```

See [Secure Connections Overview: Certificate Authorities (CAs)](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information.


This option implies the [--ssl](#-ssl) option.


### `--ssl-capath`


Defines a path to a directory that contains one or more PEM files that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for [TLS](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/README.md). This option requires that you use the absolute path, not a relative path. For example:


```
--ssl-capath=/etc/my.cnf.d/certificates/ca/
```

This option is usually used with other TLS options. For example:


```
$ mariabackup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --ssl-capath=/etc/my.cnf.d/certificates/ca/
```

The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command.


See [Secure Connections Overview: Certificate Authorities (CAs)](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information


This option implies the [--ssl](#-ssl) option.


### `--ssl-cert`


Defines a path to the X509 certificate file to use for [TLS](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/README.md). This option requires that you use the absolute path, not a relative path. For example:


```
--ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem
```

This option is usually used with other TLS options. For example:


```
$ mariabackup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem
```

This option implies the [--ssl](#-ssl) option.


### `--ssl-cipher`


Defines the list of permitted ciphers or cipher suites to use for [TLS](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/README.md). For example:


```
--ssl-cipher=name
```

This option is usually used with other TLS options. For example:


```
$ mariabackup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem
   --ssl-cipher=TLSv1.2
```

To determine if the server restricts clients to specific ciphers, check the [ssl_cipher](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md#ssl_cipher) system variable.


This option implies the [--ssl](#-ssl) option.


### `--ssl-crl`


Defines a path to a PEM file that should contain one or more revoked X509 certificates to use for [TLS](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/README.md). This option requires that you use the absolute path, not a relative path. For example:


```
--ssl-crl=/etc/my.cnf.d/certificates/crl.pem
```

This option is usually used with other TLS options. For example:


```
$ mariabackup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --ssl-crl=/etc/my.cnf.d/certificates/crl.pem
```

See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information.


This option is only supported if Mariabackup was built with OpenSSL. If Mariabackup was built with yaSSL, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.


### `--ssl-crlpath`


Defines a path to a directory that contains one or more PEM files that should each contain one revoked X509 certificate to use for [TLS](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/README.md). This option requires that you use the absolute path, not a relative path. For example:


```
--ssl-crlpath=/etc/my.cnf.d/certificates/crl/
```

This option is usually used with other TLS options. For example:


```
$ mariabackup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --ssl-crlpath=/etc/my.cnf.d/certificates/crl/
```

The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command.


See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information.


This option is only supported if Mariabackup was built with OpenSSL. If Mariabackup was built with yaSSL, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.


### `--ssl-key`


Defines a path to a private key file to use for [TLS](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/README.md). This option requires that you use the absolute path, not a relative path. For example:


```
--ssl-key=/etc/my.cnf.d/certificates/client-key.pem
```

This option is usually used with other TLS options. For example:


```
$ mariabackup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem
```

This option implies the [--ssl](#-ssl) option.


### `--ssl-verify-server-cert`


Enables [server certificate verification](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification). This option is disabled by default.


This option is usually used with other TLS options. For example:


```
$ mariabackup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --ssl-verify-server-cert
```

### `--stream`


Streams backup files to stdout.


```
--stream=xbstream
```

Using this command option, you can set Mariabackup to stream the backup files to stdout in the given format. Currently, the supported format is `xbstream`.


```
$ mariabackup --stream=xbstream > backup.xb
```

To extract all files from the xbstream archive into a directory use the `mbstream` utility


```
$ mbstream  -x < backup.xb
```

If a backup is streamed, then Mariabackup will record the format in the [xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info) file.


### `--tables`


Defines the tables you want to include in the backup.


```
--tables=REGEX
```

Using this option, you can define what tables you want Mariabackup to back up from the database. The table values are defined using Regular Expressions. To define the tables you want to exclude from the backup, see the [--tables-exclude](#-tables-exclude) option.


```
$ mariabackup --backup \
     --databases=example
     --tables=nodes_* \
     --tables-exclude=nodes_tmp
```

If a backup is a [partial backup](partial-backup-and-restore-with-mariabackup.md), then Mariabackup will record that detail in the [xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info) file.


### `--tables-exclude`


Defines the tables you want to exclude from the backup.


```
--tables-exclude=REGEX
```

Using this option, you can define what tables you want Mariabackup to exclude from the backup. The table values are defined using Regular Expressions. To define the tables you want to include from the backup, see the [--tables](#-tables) option.


```
$ mariabackup --backup \
     --databases=example
     --tables=nodes_* \
     --tables-exclude=nodes_tmp
```

If a backup is a [partial backup](partial-backup-and-restore-with-mariabackup.md), then Mariabackup will record that detail in the [xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info) file.


### `--tables-file`


Defines path to file with tables for backups.


```
--tables-file=/path/to/file
```

Using this option, you can set a path to a file listing the tables you want to back up. Mariabackup iterates over each line in the file. The format is `database.table`.


```
$ mariabackup --backup \
     --databases=example \
     --tables-file=/etc/mysql/backup-file
```

If a backup is a [partial backup](partial-backup-and-restore-with-mariabackup.md), then Mariabackup will record that detail in the [xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info) file.


### `--target-dir`


Defines the destination directory.


```
--target-dir=/path/to/target
```

Using this option you can define the destination directory for the backup. Mariabackup writes all backup files to this directory. Mariabackup will create the directory, if it does not exist (but it will not create the full path recursively, i.e. at least parent directory if the --target-dir must exist=


```
$ mariabackup --backup \
       --target-dir=/data/backups
```

### `--throttle`


Defines the limit for I/O operations per second in IOS values.


```
--throttle=#
```

Using this option, you can set a limit on the I/O operations Mariabackup performs per second in IOS values. It is only used during the [--backup](#-backup) command option.


### `--tls-version`


This option accepts a comma-separated list of TLS protocol versions. A TLS protocol version will only be enabled if it is present in this list. All other TLS protocol versions will not be permitted. For example:


```
--tls-version="TLSv1.2,TLSv1.3"
```

This option is usually used with other TLS options. For example:


```
$ mariabackup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --tls-version="TLSv1.2,TLSv1.3"
```

See [Secure Connections Overview: TLS Protocol Versions](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#tls-protocol-versions) for more information.


### `-t, --tmpdir`


Defines path for temporary files.


```
--tmpdir=/path/tmp[;/path/tmp...]
```

Using this option, you can define the path to a directory Mariabackup uses in writing temporary files. If you want to use more than one, separate the values by a semicolon (that is, `;`). When passing multiple temporary directories, it cycles through them using round-robin.


```
$ mariabackup --backup \
     --tmpdir=/data/tmp;/tmp
```

### `--use-memory`


Defines the buffer pool size that is used during the prepare stage.


```
--use-memory=124M
```

Using this option, you can define the buffer pool size for Mariabackup. Use it instead of `buffer_pool_size`.


```
$ mariabackup --prepare \
      --use-memory=124M
```

### `--user`


Defines the username for connecting to the MariaDB Server.


```
--user=name
-u name
```

When Mariabackup runs, it connects to the specified MariaDB Server to get its backups. Using this option, you can define the database user used for authentication. Starting from [MariaDB 10.5.24](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10-5-24-release-notes.md), [MariaDB 10.6.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md), [MariaDB 10.11.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md), [MariaDB 11.0.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes.md), [MariaDB 11.1.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes.md), [MariaDB 11.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes.md), [MariaDB 11.3.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes.md), [MariaDB 11.4.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-1-release-notes.md), if the `--user` option is ommited, the user name is detected from the OS.


```
$ mariabackup --backup \
      --user=root \
      --password=root_passwd
```

### `--verbose`


Displays verbose output


```
$ mariabackup --verbose
```

### `--version`


Prints version information.


Using this option, you can print the Mariabackup version information to stdout.


```
$ mariabackup --version
```
<span></span>
