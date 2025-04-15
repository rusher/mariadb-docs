
# Mariabackup Options


There are a number of options available in `<code>Mariabackup</code>`.


## List of Options


### `<code>--apply-log</code>`


Prepares an existing backup to restore to the MariaDB Server. This is only valid in `<code>innobackupex</code>` mode, which can be enabled with the `<code>[--innobackupex](#-innobackupex)</code>` option.


Files that Mariabackup generates during `<code>[--backup](#-backup)</code>` operations in the target directory are not ready for use on the Server. Before you can restore the data to MariaDB, you first need to prepare the backup.


In the case of full backups, the files are not point in time consistent, since they were taken at different times. If you try to restore the database without first preparing the data, InnoDB rejects the new data as corrupt. Running Mariabackup with the `<code>--prepare</code>` command readies the data so you can restore it to MariaDB Server. When working with incremental backups, you need to use the `<code>--prepare</code>` command and the `<code>[--incremental-dir](#-incremental-dir)</code>` option to update the base backup with the deltas from an incremental backup.


```
$ mariabackup --innobackupex --apply-log
```

Once the backup is ready, you can use the `<code>[--copy-back](#-copy-back)</code>` or the `<code>[--move-back](#-move-back)</code>` commands to restore the backup to the server.


### `<code>--apply-log-only</code>`


If this option is used when preparing a backup, then only the redo log apply stage will be performed, and other stages of crash recovery will be ignored. This option is used with [incremental backups](incremental-backup-and-restore-with-mariabackup.md).



#### Note

This option is not needed or supported anymore. 


### `<code>--backup</code>`


Backs up your databases.


Using this command option, Mariabackup performs a backup operation on your database or databases. The backups are written to the target directory, as set by the `<code>[--target-dir](#-target-dir)</code>` option.


```
$ mariabackup --backup 
      --target-dir /path/to/backup \
      --user user_name --password user_passwd
```

Mariabackup can perform full and incremental backups. A full backup creates a snapshot of the database in the target directory. An incremental backup checks the database against a previously taken full backup, (defined by the `<code>[--incremental-basedir](#-incremental-basedir)</code>` option) and creates delta files for these changes.


In order to restore from a backup, you first need to run Mariabackup with the `<code>[--prepare](#-prepare)</code>` command option, to make a full backup point-in-time consistent or to apply incremental backup deltas to base. Then you can run Mariabackup again with either the `<code>[--copy-back](#-copy-back)</code>` or `<code>[--move-back](#-move-back)</code>` commands to restore the database.


For more information, see [Full Backup and Restore](full-backup-and-restore-with-mariabackup.md) and [Incremental Backup and Restore](incremental-backup-and-restore-with-mariabackup.md).


### `<code>--binlog-info</code>`


Defines how Mariabackup retrieves the binary log coordinates from the server.


```
--binlog-info[=OFF | ON | LOCKLESS | AUTO]
```

The `<code>--binlog-info</code>` option supports the following retrieval methods. When no retrieval method is provided, it defaults to `<code>AUTO</code>`.



| Option | Description |
| --- | --- |
| Option | Description |
| OFF | Disables the retrieval of binary log information |
| ON | Enables the retrieval of binary log information, performs locking where available to ensure consistency |
| LOCKLESS | Unsupported option |
| AUTO | Enables the retrieval of binary log information using ON or LOCKLESS where supported |



Using this option, you can control how Mariabackup retrieves the server's binary log coordinates corresponding to the backup.


When enabled, whether using `<code>ON</code>` or `<code>AUTO</code>`, Mariabackup retrieves information from the binlog during the backup process. When disabled with `<code>OFF</code>`, Mariabackup runs without attempting to retrieve binary log information. You may find this useful when you need to copy data without metadata like the binlog or replication coordinates.


```
$ mariabackup --binlog-info --backup
```

Currently, the `<code>LOCKLESS</code>` option depends on features unsupported by MariaDB Server. See the description of the `<code>[xtrabackup_binlog_pos_innodb](files-created-by-mariabackup.md#xtrabackup_binlog_pos_innodb)</code>` file for more information. If you attempt to run Mariabackup with this option, then it causes the utility to exit with an error.


### `<code>--close-files</code>`


Defines whether you want to close file handles.


Using this option, you can tell Mariabackup that you want to close file handles. Without this option, Mariabackup keeps files open in order to manage DDL operations. When working with particularly large tablespaces, closing the file can make the backup more manageable. However, it can also lead to inconsistent backups. Use at your own risk.


```
$ mariabackup --close-files --prepare
```

### `<code>--compress</code>`


This option was deprecated as it relies on the no longer maintained [QuickLZ](https://github.com/RT-Thread-packages/quicklz/) library. It will be removed in a future release - versions supporting this function will not be affected. It is recommended to instead backup to a stream (stdout), and use a 3rd party compression library to compress the stream, as described in 
[Using Encryption and Compression Tools With Mariabackup](using-encryption-and-compression-tools-with-mariabackup.md).


Defines the compression algorithm for backup files.


```
--compress[=compression_algorithm]
```

The `<code>--compress</code>` option only supports the now deprecated `<code>quicklz</code>` algorithm.



| Option | Description |
| --- | --- |
| Option | Description |
| quicklz | Uses the QuickLZ compression algorithm |



```
$ mariabackup --compress --backup
```

If a backup is compressed using this option, then Mariabackup will record that detail in the `<code>[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)</code>` file.


### `<code>--compress-chunk-size</code>`


Deprecated, for details see the `<code>[--compress](#compress)</code>` option.


Defines the working buffer size for compression threads.


```
--compress-chunk-size=#
```

Mariabackup can perform compression operations on the backup files before writing them to disk. It can also use multiple threads for parallel data compression during this process. Using this option, you can set the chunk size each thread uses during compression. It defaults to 64K.


```
$ mariabackup --backup --compress \
     --compress-threads=12 --compress-chunk-size=5M
```

To further configure backup compression, see the `<code>[--compress](#-compress)</code>` and `<code>[--compress-threads](#-compress-threads)</code>` options.


### `<code>--compress-threads</code>`


Deprecated, for details see the `<code>[--compress](#compress)</code>` option.


Defines the number of threads to use in compression.


```
--compress-threads=#
```

Mariabackup can perform compression operations on the backup files before writing them to disk. Using this option, you can define the number of threads you want to use for this operation. You may find this useful in speeding up the compression of particularly large databases. It defaults to single-threaded.


```
$ mariabackup --compress --compress-threads=12 --backup
```

To further configure backup compression, see the `<code>[--compress](#-compress)</code>` and `<code>[--compress-chunk-size](#-compress-chunk-size)</code>` options.


### `<code>--copy-back</code>`


Restores the backup to the data directory.


Using this command, Mariabackup copies the backup from the target directory to the data directory, as defined by the `<code>[--datadir](#-h-datadir)</code>` option. You must stop the MariaDB Server before running this command. The data directory must be empty. If you want to overwrite the data directory with the backup, use the `<code>[--force-non-empty-directories](#-force-non-empty-directories)</code>` option.


Bear in mind, before you can restore a backup, you first need to run Mariabackup with the `<code>[--prepare](#-prepare)</code>` option. In the case of full backups, this makes the files point-in-time consistent. With incremental backups, this applies the deltas to the base backup. Once the backup is prepared, you can run `<code>--copy-back</code>` to apply it to MariaDB Server.


```
$ mariabackup --copy-back --force-non-empty-directories
```

Running the `<code>--copy-back</code>` command copies the backup files to the data directory. Use this command if you want to save the backup for later. If you don't want to save the backup for later, use the `<code>[--move-back](#-move-back)</code>` command.


### `<code>--core-file</code>`


Defines whether to write a core file.


Using this option, you can configure Mariabackup to dump its core to file in the event that it encounters fatal signals. You may find this useful for review and debugging purposes.


```
$ mariabackup --core-file --backup
```

### `<code>--databases</code>`


Defines the databases and tables you want to back up.


```
--databases="database[.table][ database[.table] ...]"
```

Using this option, you can define the specific database or databases you want to back up. In cases where you have a particularly large database or otherwise only want to back up a portion of it, you can optionally also define the tables on the database.


```
$ mariabackup --backup \
      --databases="example.table1 example.table2"
```

In cases where you want to back up most databases on a server or tables on a database, but not all, you can set the specific databases or tables you don't want to back up using the `<code>[--databases-exclude](#-databases-exclude)</code>` option.


If a backup is a [partial backup](partial-backup-and-restore-with-mariabackup.md), then Mariabackup will record that detail in the `<code>[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)</code>` file.


In `<code>innobackupex</code>` mode, which can be enabled with the `<code>[--innobackupex](#-innobackupex)</code>` option, the `<code>--databases</code>` option can be used as described above, or it can be used to refer to a file, just as the `<code>[--databases-file](https://mariadb.com/kb/en/-databases-file)</code>` option can in the normal mode.


### `<code>--databases-exclude</code>`


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

To include databases in the backup, see the `<code>[--databases](#-databases)</code>` option option


If a backup is a [partial backup](partial-backup-and-restore-with-mariabackup.md), then Mariabackup will record that detail in the `<code>[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)</code>` file.


### `<code>--databases-file</code>`


Defines the path to a file listing databases and/or tables you want to back up.


```
--databases-file="/path/to/database-file"
```

Format the databases file to list one element per line, with the following syntax:


```
database[.table]
```

In cases where you need to back up a number of databases or specific tables in a database, you may find the syntax for the `<code>[--databases](#-databases)</code>` and `<code>[--databases-exclude](#-databases-exclude)</code>` options a little cumbersome. Using this option you can set the path to a file listing the databases or databases and tables you want to back up.


For instance, imagine you list the databases and tables for a backup in a file called `<code>main-backup</code>`.


```
$ cat main-backup
example1
example2.table1
example2.table2

$ mariabackup --backup --databases-file=main-backup
```

If a backup is a [partial backup](partial-backup-and-restore-with-mariabackup.md), then Mariabackup will record that detail in the `<code>[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)</code>` file.


### `<code>-h, --datadir</code>`


Defines the path to the database root.


```
--datadir=PATH
```

Using this option, you can define the path to the source directory. This is the directory that Mariabackup reads for the data it backs up. It should be the same as the MariaDB Server `<code>[datadir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir)</code>` system variable.


```
$ mariabackup --backup -h /var/lib64/mysql
```

### `<code>--debug-sleep-before-unlock</code>`


This is a debug-only option used by the Xtrabackup test suite.


### `<code>--decompress</code>`


Deprecated, for details see the `<code>[--compress](#compress)</code>` option.


This option requires that you have the `<code>qpress</code>` utility installed on your system.


Defines whether you want to decompress previously compressed backup files.


When you run Mariabackup with the `<code>[--compress](#-compress)</code>` option, it compresses the subsequent backup files, using the QuickLZ algorithm. Using this option, Mariabackup decompresses the compressed files from a previous backup.


For instance, run a backup with compression,


```
$ mariabackup --compress --backup
```

Then decompress the backup,


```
$ mariabackup --decompress
```

You can enable the decryption of multiple files at a time using the `<code>[--parallel](#-parallel)</code>` option. By default, Mariabackup does not remove the compressed files from the target directory. If you want to delete these files, use the `<code>[--remove-original](#-remove-original)</code>` option.


### `<code>--debug-sync</code>`


Defines the debug sync point. This option is only used by the Mariabackup test suite.


### `<code>--defaults-extra-file</code>`


Defines the path to an extra default [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md).


```
--defaults-extra-file=/path/to/config
```

Using this option, you can define an extra default [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) for Mariabackup. Unlike `<code>[--defaults-file](#-defaults-file)</code>`, this file is read after the default [option files](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) are read, allowing you to only overwrite the existing defaults.


```
$ mariabackup --backup \
      --defaults-file-extra=addition-config.cnf \
      --defaults-file=config.cnf
```

### `<code>--defaults-file</code>`


Defines the path to the default [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md).


```
--defaults-file=/path/to/config
```

Using this option, you can define a default [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) for Mariabackup. Unlike the `<code>[--defaults-extra-file](#-defaults-extra-file)</code>` option, when this option is provided, it completely replaces all default [option files](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md).


```
$ mariabackup --backup \
     --defaults-file="config.cnf
```

### `<code>--defaults-group</code>`


Defines the [option group](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) to read in the [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md).


```
--defaults-group="name"
```

In situations where you find yourself using certain Mariabackup options consistently every time you call it, you can set the options in an [option file](../../getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). The `<code>--defaults-group</code>` option defines what option group Mariabackup reads for its options.


Options you define from the command-line can be set in the configuration file using minor formatting changes. For instance, if you find yourself perform compression operations frequently, you might set `<code>[--compress-threads](#-compress-threads)</code>` and `<code>[--compress-chunk-size](#-compress-chunk-size)</code>` options in this way:


```
[mariabackup]
compress_threads = 12
compress_chunk_size = 64K
```

Now whenever you run a backup with the `<code>[--compress](#-compress)</code>` option, it always performs the compression using 12 threads and 64K chunks.


```
$ mariabackup --compress --backup
```

See [Mariabackup Overview: Server Option Groups](mariabackup-overview.md#server-option-groups) and [Mariabackup Overview: Client Option Groups](mariabackup-overview.md#client-option-groups) for a list of the option groups read by Mariabackup by default.


### `<code>--encrypted-backup</code>`


When this option is used with `<code>--backup</code>`, if Mariabackup encounters a page that has a non-zero `<code>key_version</code>` value, then Mariabackup assumes that the page is encrypted.


Use `<code>--skip-encrypted-backup</code>` instead to allow Mariabackup to copy unencrypted tables that were originally created before MySQL 5.1.48.


### `<code>--export</code>`


If this option is provided during the `<code>--prepare</code>` stage, then it tells Mariabackup to create `<code>.cfg</code>` files for each [InnoDB file-per-table tablespace](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md). These `<code>.cfg</code>` files are used to [import transportable tablespaces](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces) in the process of [restoring partial backups](partial-backup-and-restore-with-mariabackup.md) and [restoring individual tables and partitions](restoring-individual-tables-and-partitions-with-mariabackup.md).


The `<code>--export</code>` option could require rolling back incomplete transactions that had modified the table. This will likely create a "new branch of history" that does not correspond to the server that had been backed up, which makes it impossible to apply another incremental backup on top of such additional changes. The option should only be applied when doing a `<code>--prepare</code>` of the last incremental.


```
$ mariabackup --prepare --export
```

Mariabackup did not support the `<code>[--export](mariabackup-options.md#-export)</code>` option. See [MDEV-13466](https://jira.mariadb.org/browse/MDEV-13466) about that. In earlier versions of MariaDB, this means that Mariabackup could not create `<code>.cfg</code>` files for [InnoDB file-per-table tablespaces](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md) during the `<code>--prepare</code>` stage. You can still [import file-per-table tablespaces](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces) without the `<code>.cfg</code>` files in many cases, so it may still be possible in those versions to [restore partial backups](partial-backup-and-restore-with-mariabackup.md) or to [restore individual tables and partitions](restoring-individual-tables-and-partitions-with-mariabackup.md) with just the `<code>.ibd</code>` files. If you have a [full backup](full-backup-and-restore-with-mariabackup.md) and you need to create `<code>.cfg</code>` files for [InnoDB file-per-table tablespaces](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md), then you can do so by preparing the backup as usual without the `<code>--export</code>` option, and then restoring the backup, and then starting the server. At that point, you can use the server's built-in features to [copy the transportable tablespaces](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces).


### `<code>--extra-lsndir</code>`


Saves an extra copy of the `<code>[xtrabackup_checkpoints](files-created-by-mariabackup.md#xtrabackup_checkpoints)</code>` and `<code>[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)</code>` files into the given directory.


```
--extra-lsndir=PATH
```

When using the `<code>[--backup](#-backup)</code>` command option, Mariabackup produces a number of backup files in the target directory. Using this option, you can have Mariabackup produce additional copies of the `<code>[xtrabackup_checkpoints](files-created-by-mariabackup.md#xtrabackup_checkpoints)</code>` and `<code>[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)</code>` files in the given directory.


```
$ mariabackup --extra-lsndir=extras/ --backup
```

This is especially usefull when using `<code>[--stream](#-stream)</code>` for streaming output, e.g. for [compression and/or encryption using external tools](using-encryption-and-compression-tools-with-mariabackup.md) in combination with [incremental backups](incremental-backup-and-restore-with-mariabackup.md), as the `<code>[xtrabackup_checkpoints](files-created-by-mariabackup.md#xtrabackup_checkpoints)</code>` file necessary to determine the LSN to continue the incremental backup from is still accessible without uncompressing / decrypting the backup file first. Simply pass in the `<code>--extra-lsndir</code>` of the previous backup as 
`<code>[--incremental-basedir](#-incremental-basedir)</code>`


### `<code>--force-non-empty-directories</code>`


Allows `<code>[--copy-back](#-copy-back)</code>` or `<code>[--move-back](#-move-back)</code>` command options to use non-empty target directories.


When using Mariabackup with the `<code>[--copy-back](#-copy-back)</code>` or `<code>[--move-back](#-move-back)</code>` command options, they normally require a non-empty target directory to avoid conflicts. Using this option with either of command allows Mariabackup to use a non-empty directory.


```
$ mariabackup --force-non-empty-directories --copy-back
```

Bear in mind that this option does not enable overwrites. When copying or moving files into the target directory, if Mariabackup finds that the target file already exists, it fails with an error.


### `<code>--ftwrl-wait-query-type</code>`


Defines the type of query allowed to complete before Mariabackup issues the global lock.


```
--ftwrl-wait-query-type=[ALL | UPDATE | SELECT]
```

The `<code>--ftwrl-wait-query-type</code>` option supports the following query types. The default value is `<code>ALL</code>`.



| Option | Description |
| --- | --- |
| Option | Description |
| ALL | Waits until all queries complete before issuing the global lock |
| SELECT | Waits until [SELECT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statements complete before issuing the global lock |
| UPDATE | Waits until [UPDATE](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md) statements complete before issuing the global lock |



When Mariabackup runs, it issues a global lock to prevent data from changing during the backup process. When it encounters a statement in the process of executing, it waits until the statement is finished before issuing the global lock. Using this option, you can modify this default behavior to ensure that it waits only for certain query types, such as for `<code>[SELECT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)</code>` and `<code>[UPDATE](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md)</code>` statements.


```
$ mariabackup --backup  \
      --ftwrl-wait-query-type=UPDATE
```

### `<code>--ftwrl-wait-threshold</code>`


Defines the minimum threshold for identifying long-running queries for FTWRL.


```
--ftwrl-wait-threshold=#
```

When Mariabackup runs, it issues a global lock to prevent data from changing during the backup process and ensure a consistent record. If it encounters statements still in the process of executing, it waits until they complete before setting the lock. Using this option, you can set the threshold at which Mariabackup engages FTWRL. When it `<code>[--ftwrl-wait-timeout](#-ftwrl-wait-timeout)</code>` is not 0 and a statement has run for at least the amount of time given this argument, Mariabackup waits until the statement completes or until
the `<code>[--ftwrl-wait-timeout](#-ftwrl-wait-timeout)</code>` expires before setting the global lock and starting the backup.


```
$ mariabackup --backup \
     --ftwrl-wait-timeout=90 \
     --ftwrl-wait-threshold=30
```

### `<code>--ftwrl-wait-timeout</code>`


Defines the timeout to wait for queries before trying to acquire the global lock. The global lock refers to `<code>[BACKUP STAGE BLOCK_COMMIT](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/backup-commands/backup-stage.md#backup-stage-block_commit)</code>`. The global lock refers to `<code>[FLUSH TABLES WITH READ LOCK (FTWRL)](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md#the-purpose-of-flush-tables-table_list-with-read-lock)</code>`.


```
--ftwrl-wait-timeout=#
```

When Mariabackup runs, it acquires a global lock to prevent data from changing during the backup process and ensure a consistent record. If it encounters statements still in the process of executing, it can be configured to wait until the statements complete before trying to acquire the global lock.


If the `<code>--ftwrl-wait-timeout</code>` is set to 0, then Mariabackup tries to acquire the global lock immediately without waiting. This is the default value.


If the `<code>--ftwrl-wait-timeout</code>` is set to a non-zero value, then Mariabackup waits for the configured number of seconds until trying to acquire the global lock.


Starting in [MariaDB 10.5.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1053-release-notes.md), Mariabackup will exit if it can't acquire the global lock after waiting for the configured number of seconds. In earlier versions, it could wait for the global lock indefinitely, even if `<code>--ftwrl-wait-timeout</code>` was set to a non-zero value.


```
$ mariabackup --backup \
      --ftwrl-wait-query-type=UPDATE \
      --ftwrl-wait-timeout=5
```

### `<code>--galera-info</code>`


Defines whether you want to back up information about a [Galera Cluster](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md) node's state.


When this option is used, Mariabackup creates an additional file called `<code>[xtrabackup_galera_info](files-created-by-mariabackup.md#xtrabackup_galera_info)</code>`, which records information about a [Galera Cluster](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md) node's state. It records the values of the `<code>[wsrep_local_state_uuid](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-status-variables.md#wsrep_local_state_uuid)</code>` and `<code>[wsrep_last_committed](../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-cluster-status-variables.md#wsrep_last_committed)</code>` status variables.


You should only use this option when backing up a [Galera Cluster](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md) node. If the server is not a [Galera Cluster](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md) node, then this option has no effect.


This option, when enabled and used with [GTID replication](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md), will rotate the binary logs at backup time.


```
$ mariabackup --backup --galera-info
```

### `<code>--history</code>`


Defines whether you want to track backup history in the `<code>PERCONA_SCHEMA.xtrabackup_history</code>` table.


```
--history[=name]
```

When using this option, Mariabackup records its operation in a table on the MariaDB Server. Passing a name to this option allows you group backups under arbitrary terms for later processing and analysis.


```
$ mariabackup --backup --history=backup_all
```

Currently, the table it uses by default is named `<code>mysql.mariadb_backup_history</code>`. Prior to [MariaDB 10.11](../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md), the default table was `<code>PERCONA_SCHEMA.xtrabackup_history</code>`.


Mariabackup will also record this in the `<code>[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)</code>` file.


### `<code>-H, --host</code>`


Defines the host for the MariaDB Server you want to backup.


```
--host=name
```

Using this option, you can define the host to use when connecting to a MariaDB Server over TCP/IP. By default, Mariabackup attempts to connect to the local host.


```
$ mariabackup --backup \
      --host="example.com"
```

### `<code>--include</code>`


This option is a regular expression to be matched against table names in databasename.tablename format. It is
equivalent to the `<code>[--tables](#-tables)</code>` option. This is only valid in `<code>innobackupex</code>` mode, which can be enabled with the `<code>[--innobackupex](#-innobackupex)</code>` option.


### `<code>--incremental</code>`


Defines whether you want to take an increment backup, based on another backup. This is only valid in `<code>innobackupex</code>` mode, which can be enabled with the `<code>[--innobackupex](#-innobackupex)</code>` option.


```
mariabackup --innobackupex --incremental
```

Using this option with the `<code>[--backup](#-backup)</code>` command option makes the operation incremental rather than a complete overwrite. When this option is specified, either the `<code>[--incremental-lsn](#-incremental-lsn) or </code>`[--incremental-basedir](#-incremental-basedir)`<code> options can also be given. If neither option is given, option </code>`[--incremental-basedir](#-incremental-basedir)`<code> is used by default, set to the first timestamped backup directory in the backup base directory.</code>`


```
$ mariabackup --innobackupex --backup --incremental \
     --incremental-basedir=/data/backups \
     --target-dir=/data/backups
```

If a backup is a [incremental backup](incremental-backup-and-restore-with-mariabackup.md), then Mariabackup will record that detail in the `<code>[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)</code>` file.


### `<code>--incremental-basedir</code>`


Defines whether you want to take an incremental backup, based on another backup.


```
--incremental-basedir=PATH
```

Using this option with the `<code>[--backup](#-backup)</code>` command option makes the operation incremental rather than a complete overwrite. Mariabackup will only copy pages from `<code>.ibd</code>` files if they are newer than the backup in the specified directory.


```
$ mariabackup --backup \
     --incremental-basedir=/data/backups \
     --target-dir=/data/backups
```

If a backup is a [incremental backup](incremental-backup-and-restore-with-mariabackup.md), then Mariabackup will record that detail in the `<code>[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)</code>` file.


### `<code>--incremental-dir</code>`


Defines whether you want to take an incremental backup, based on another backup.


```
--increment-dir=PATH
```

Using this option with `<code>[--prepare](#-prepare)</code>` command option makes the operation incremental rather than a complete overwrite. Mariabackup will apply `<code>.delta</code>` files and log files into the target directory.


```
$ mariabackup --prepare \
      --increment-dir=backups/
```

If a backup is a [incremental backup](incremental-backup-and-restore-with-mariabackup.md), then Mariabackup will record that detail in the `<code>[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)</code>` file.


### `<code>--incremental-force-scan</code>`


Defines whether you want to force a full scan for incremental backups.


When using Mariabackup to perform an incremental backup, this option forces it to also perform a full scan of the data pages being backed up, even when there's bitmap data on the changes. MariaDB does not support changed page bitmaps, so this option is useless in those versions. See [MDEV-18985](https://jira.mariadb.org/browse/MDEV-18985) for more information.


```
$ mariabackup --backup \
     --incremental-basedir=/path/to/target \
     --incremental-force-scan
```

### `<code>--incremental-history-name</code>`


Defines a logical name for the backup.


```
--incremental-history-name=name
```

Mariabackup can store data about its operations on the MariaDB Server. Using this option, you can define the logical name it uses in identifying the backup.


```
$ mariabackup --backup \
     --incremental-history-name=morning_backup
```

Currently, the table it uses by default is named `<code>mysql.mariadb_backup_history</code>`. Prior to [MariaDB 10.11](../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md), the default table was `<code>PERCONA_SCHEMA.xtrabackup_history</code>`.


Mariabackup will also record this in the `<code>[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)</code>` file.


### `<code>--incremental-history-uuid</code>`


Defines a UUID for the backup.


```
--incremental-history-uuid=name
```

Mariabackup can store data about its operations on the MariaDB Server. Using this option, you can define the UUID it uses in identifying a previous backup to increment from. It checks `<code>[--incremental-history-name](#-incremental-history-name)</code>`, `<code>[--incremental-basedir](#-incremental-basedir)</code>`, and `<code>[--incremental-lsn](#-incremental-lsn)</code>`. If Mariabackup fails to find a valid lsn, it generates an error.


```
$ mariabackup --backup \
      --incremental-history-uuid=main-backup012345678
```

Currently, the table it uses is named `<code>PERCONA_SCHEMA.xtrabackup_history</code>`, but expect that name to change in future releases. See [MDEV-19246](https://jira.mariadb.org/browse/MDEV-19246) for more information.


Mariabackup will also record this in the `<code>[xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info)</code>` file.


### `<code>--incremental-lsn</code>`


Defines the sequence number for incremental backups.


```
--incremental-lsn=name
```

Using this option, you can define the sequence number (LSN) value for `<code>[--backup](#-backup)</code>` operations. During backups, Mariabackup only copies `<code>.ibd</code>` pages newer than the specified values.


**WARNING**: Incorrect LSN values can make the backup unusable. It is impossible to diagnose this issue.


### `<code>--innobackupex</code>`


Deprecated


Enables `<code>innobackupex</code>` mode, which is a compatibility mode.


```
$ mariabackup --innobackupex
```

In `<code>innobackupex</code>` mode, Mariabackup has the following differences:


* To prepare a backup, the `<code>[--apply-log](#-apply-log)</code>` option is used instead of the `<code>[--prepare](#-prepare)</code>` option.
* To create an [incremental backup](incremental-backup-and-restore-with-mariabackup.md), the `<code>[--incremental](#-incremental)</code>` option is supported.
* The `<code>[--no-timestamp](#-no-timestamp)</code>` option is supported.
* To create a [partial backup](partial-backup-and-restore-with-mariabackup.md), the `<code>[--include](#--include)</code>` option is used instead of the `<code>[--tables](#-tables)</code>` option.
* To create a [partial backup](partial-backup-and-restore-with-mariabackup.md), the `<code>[--databases](#--databases)</code>` option can still be used, but it's behavior changes slightly.
* The `<code>[--target-dir](#-target-dir)</code>` option is not used to specify the backup directory. The backup directory should instead be specified as a standalone argument.


The primary purpose of `<code>innobackupex</code>` mode is to allow scripts and tools to more easily migrate to Mariabackup if they were originally designed to use the `<code>innobackupex</code>` utility that is included with [Percona XtraBackup](../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md). It is not recommended to use this mode in new scripts, since it is not guaranteed to be supported forever. See [MDEV-20552](https://jira.mariadb.org/browse/MDEV-20552) for more information.


### `<code>--innodb</code>`


This option has no effect. Set only for MySQL option compatibility.


### `<code>--innodb-adaptive-hash-index</code>`


Enables InnoDB Adaptive Hash Index.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option you can explicitly enable the InnoDB Adaptive Hash Index. This feature is enabled by default for Mariabackup. If you want to disable it, use `<code>[--skip-innodb-adaptive-hash-index](#-skip-innodb-adaptive-hash-index)</code>`.


```
$ mariabackup --backup \
      --innodb-adaptive-hash-index
```

### `<code>--innodb-autoextend-increment</code>`


Defines the increment in megabytes for auto-extending the size of tablespace file.


```
--innodb-autoextend-increment=36
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set the increment in megabytes for automatically extending the size of tablespace data file in InnoDB.


```
$ mariabackup --backup \
     --innodb-autoextend-increment=35
```

### `<code>--innodb-buffer-pool-filename</code>`


Using this option has no effect. It is available to provide compatibility with the MariaDB Server.


### `<code>--innodb-buffer-pool-size</code>`


Defines the memory buffer size InnoDB uses the cache data and indexes of the table.


```
--innodb-buffer-pool-size=124M
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can configure the buffer pool for InnoDB operations.


```
$ mariabackup --backup \
      --innodb-buffer-pool-size=124M
```

### `<code>--innodb-checksum-algorithm</code>`


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

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can specify the algorithm Mariabackup uses when checksumming on InnoDB tables. Currently, MariaDB supports the following algorithms `<code>CRC32</code>`, `<code>STRICT_CRC32</code>`, `<code>INNODB</code>`, `<code>STRICT_INNODB</code>`, `<code>NONE</code>`, `<code>STRICT_NONE</code>`.


```
$ mariabackup --backup \
      ---innodb-checksum-algorithm=strict_innodb
```

### `<code>--innodb-data-file-path</code>`


Defines the path to individual data files.


```
--innodb-data-file-path=/path/to/file
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option you can define the path to InnoDB data files. Each path is appended to the `<code>[--innodb-data-home-dir](#-innodb-data-home-dir)</code>` option.


```
$ mariabackup --backup \
     --innodb-data-file-path=ibdata1:13M:autoextend \
     --innodb-data-home-dir=/var/dbs/mysql/data
```

### `<code>--innodb-data-home-dir</code>`


Defines the home directory for InnoDB data files.


```
--innodb-data-home-dir=PATH
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option you can define the path to the directory containing InnoDB data files. You can specific the files using the `<code>[--innodb-data-file-path](#-innodb-data-file-path)</code>` option.


```
$ mariabackup --backup \
     --innodb-data-file-path=ibdata1:13M:autoextend \
     --innodb-data-home-dir=/var/dbs/mysql/data
```

### `<code>--innodb-doublewrite</code>`


Enables doublewrites for InnoDB tables.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. When using this option, Mariabackup improves fault tolerance on InnoDB tables with a doublewrite buffer. By default, this feature is enabled. Use this option to explicitly enable it. To disable doublewrites, use the `<code>[--skip-innodb-doublewrite](#-skip-innodb-doublewrite)</code>` option.


```
$ mariabackup --backup \
     --innodb-doublewrite
```

### `<code>--innodb-encrypt-log</code>`


Defines whether you want to encrypt InnoDB logs.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can tell Mariabackup that you want to encrypt logs from its InnoDB activity.


### `<code>--innodb-file-io-threads</code>`


Defines the number of file I/O threads in InnoDB.


```
--innodb-file-io-threads=#
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the number of file I/O threads Mariabackup uses on InnoDB tables.


```
$ mariabackup --backup \
     --innodb-file-io-threads=5
```

### `<code>--innodb-file-per-table</code>`


Defines whether you want to store each InnoDB table as an `<code>.ibd</code>` file.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option causes Mariabackup to store each InnoDB table as an `<code>.ibd</code>` file in the target directory.


### `<code>--innodb-flush-method</code>`


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

### `<code>--innodb-io-capacity</code>`


Defines the number of IOP's the utility can perform.


```
--innodb-io-capacity=#
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can limit the I/O activity for InnoDB background tasks. It should be set around the number of I/O operations per second that the system can handle, based on drive or drives being used.


```
$ mariabackup --backup \
     --innodb-io-capacity=200
```

### `<code>--innodb-log-checksums</code>`


Defines whether to include checksums in the InnoDB logs.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can explicitly set Mariabackup to include checksums in the InnoDB logs. The feature is enabled by default. To disable it, use the `<code>[--skip-innodb-log-checksums](#-skip-innodb-log-checksums)</code>` option.


```
$ mariabackup --backup \
      --innodb-log-checksums
```

### `<code>--innodb-log-buffer-size</code>`


This option has no functionality in Mariabackup. It exists for MariaDB Server compatibility.


### `<code>--innodb-log-files-in-group</code>`


This option has no functionality in Mariabackup. It exists for MariaDB Server compatibility.


### `<code>--innodb-log-group-home-dir</code>`


Defines the path to InnoDB log files.


```
--innodb-log-group-home-dir=PATH
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the path to InnoDB log files.


```
$ mariabackup --backup \
     --innodb-log-group-home-dir=/path/to/logs
```

### `<code>--innodb-max-dirty-pages-pct</code>`


Defines the percentage of dirty pages allowed in the InnoDB buffer pool.


```
--innodb-max-dirty-pages-pct=#
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the maximum percentage of dirty, (that is, unwritten) pages that Mariabackup allows in the InnoDB buffer pool.


```
$ mariabackup --backup \
     --innodb-max-dirty-pages-pct=80
```

### `<code>--innodb-open-files</code>`


Defines the number of files kept open at a time.


```
--innodb-open-files=#
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set the maximum number of files InnoDB keeps open at a given time during backups.


```
$ mariabackup --backup \
      --innodb-open-files=10
```

### `<code>--innodb-page-size</code>`


Defines the universal page size.


```
--innodb-page-size=#
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the universal page size in bytes for Mariabackup.


```
$ mariabackup --backup \
     --innodb-page-size=16k
```

### `<code>--innodb-read-io-threads</code>`


Defines the number of background read I/O threads in InnoDB.


```
--innodb-read-io-threads=#
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set the number of I/O threads MariaDB uses when reading from InnoDB.


```
$ mariabackup --backup \
      --innodb-read-io-threads=4
```

### `<code>--innodb-undo-directory</code>`


Defines the directory for the undo tablespace files.


```
--innodb-undo-directory=PATH
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the path to the directory where you want MariaDB to store the undo tablespace on InnoDB tables. The path can be absolute.


```
$ mariabackup --backup \
     --innodb-undo-directory=/path/to/innodb_undo
```

### `<code>--innodb-undo-tablespaces</code>`


Defines the number of undo tablespaces to use.


```
--innodb-undo-tablespaces=#
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the number of undo tablespaces you want to use during the backup.


```
$ mariabackup --backup \
      --innodb-undo-tablespaces=10
```

### `<code>--innodb-use-native-aio</code>`


Defines whether you want to use native AI/O.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can enable the use of the native asynchronous I/O subsystem. It is only available on Linux operating systems.


```
$ mariabackup --backup \
      --innodb-use-native-aio
```

### `<code>--innodb-write-io-threads</code>`


Defines the number of background write I/O threads in InnoDB.


```
--innodb-write-io-threads=#
```

Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set the number of background write I/O threads Mariabackup uses.


```
$ mariabackup --backup \
     --innodb-write-io-threads=4
```

### `<code>--kill-long-queries-timeout</code>`


Defines the timeout for blocking queries.


```
--kill-long-queries-timeout=#
```

When Mariabackup runs, it issues a `<code>FLUSH TABLES WITH READ LOCK</code>` statement. It then identifies blocking queries. Using this option you can set a timeout in seconds for these blocking queries. When the time runs out, Mariabackup kills the queries.


The default value is 0, which causes Mariabackup to not attempt killing any queries.


```
$ mariabackup --backup \
      --kill-long-queries-timeout=10
```

### `<code>--kill-long-query-type</code>`


Defines the query type the utility can kill to unblock the global lock.


```
--kill-long-query-type=ALL | UPDATE | SELECT
```

When Mariabackup encounters a query that sets a global lock, it can kill the query in order to free up MariaDB Server for the backup. Using this option, you can choose the types of query it kills: `<code>[SELECT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)</code>`, `<code>[UPDATE](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md)</code>`, or both set with `<code>ALL</code>`. The default is `<code>ALL</code>`.


```
$ mariabackup --backup \
      --kill-long-query-type=UPDATE
```

### `<code>--lock-ddl-per-table</code>`


Prevents DDL for each table to be backed up by acquiring MDL lock on that.
NOTE: Unless --no-lock option was also specified, conflicting DDL queries , will be killed at the end of backup This is done avoid deadlock between "FLUSH TABLE WITH READ LOCK", user's DDL query (ALTER, RENAME), and MDL lock on table.


### `<code>--log</code>`


This option has no functionality. It is set to ensure compatibility with MySQL.


### `<code>--log-bin</code>`


Defines the base name for the log sequence.


```
--log-bin[=name]
```

Using this option you, you can set the base name for Mariabackup to use in log sequences.


### `<code>--log-copy-interval</code>`


Defines the copy interval between checks done by the log copying thread.


```
--log-copy-interval=#
```

Using this option, you can define the copy interval Mariabackup uses between checks done by the log copying thread. The given value is in milliseconds.


```
$ mariabackup --backup \
      --log-copy-interval=50
```

### `<code>--log-innodb-page-corruption</code>`


Continue backup if InnoDB corrupted pages are found. The pages are logged in `<code>innodb_corrupted_pages</code>` and backup is finished with error. [--prepare](#-prepare) will try to fix corrupted pages. If `<code>innodb_corrupted_pages</code>` exists after [--prepare](#-prepare) in base backup directory, backup still contains corrupted pages and can not be considered as consistent.


Added in [MariaDB 10.5.9](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1059-release-notes.md)


### `<code>--move-back</code>`


Restores the backup to the data directory.


Using this command, Mariabackup moves the backup from the target directory to the data directory, as defined by the `<code>[--datadir](#-h-datadir)</code>` option. You must stop the MariaDB Server before running this command. The data directory must be empty. If you want to overwrite the data directory with the backup, use the `<code>[--force-non-empty-directories](#-force-non-empty-directories)</code>` option.


Bear in mind, before you can restore a backup, you first need to run Mariabackup with the `<code>[--prepare](#-prepare)</code>` option. In the case of full backups, this makes the files point-in-time consistent. With incremental backups, this applies the deltas to the base backup. Once the backup is prepared, you can run `<code>--move-back</code>` to apply it to MariaDB Server.


```
$ mariabackup --move-back \
      --datadir=/var/mysql
```

Running the `<code>--move-back</code>` command moves the backup files to the data directory. Use this command if you don't want to save the backup for later. If you do want to save the backup for later, use the `<code>[--copy-back](#-copy-back)</code>` command.


### `<code>--mysqld</code>`


Used internally to prepare a backup.


### `<code>--no-backup-locks</code>`


Mariabackup locks the database by default when it runs. This option disables support for Percona Server's backup locks.


When backing up Percona Server, Mariabackup would use backup locks by default. To be specific, backup locks refers to the `<code>LOCK TABLES FOR BACKUP</code>` and `<code>LOCK BINLOG FOR BACKUP</code>` statements. This option can be used to disable support for Percona Server's backup locks. This option has no effect when the server does not support Percona's backup locks.


Deprecated and has no effect from [MariaDB 10.11.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-8-release-notes.md), [MariaDB 11.0.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes.md), [MariaDB 11.1.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes.md) and [MariaDB 11.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes.md) as MariaDB will now always use backup locks for better performance. See [MDEV-32932](https://jira.mariadb.org/browse/MDEV-32932).


```
$ mariabackup --backup --no-backup-locks
```

### `<code>--no-lock</code>`


Disables table locks with the `<code>FLUSH TABLE WITH READ LOCK</code>` statement.


Using this option causes Mariabackup to disable table locks with the `<code>FLUSH TABLE WITH READ LOCK</code>` statement. Only use this option if:


* You are not executing DML statements on non-InnoDB tables during the backup. This includes the `<code>mysql</code>` database system tables (which are MyISAM).
* You are not executing any DDL statements during the backup.
* You are _not_ using the file "xtrabackup_binlog_info", which is not consistent with the data when --no-lock is used. Use the file "xtrabackup_binlog_pos_innodb" [link] instead.
* All tables you're backing up use the InnoDB storage engine.


```
$ mariabackup --backup --no-lock
```

If you're considering `<code>--no-lock</code>` due to backups failing to acquire locks, this may be due to incoming replication events preventing the lock. Consider using the [--safe-slave-backup](#-safe-slave-backup) option to momentarily stop the replica thread. This alternative may help the backup to succeed without resorting to `<code>--no-lock</code>`.


The --no-lock option only provides a consistent backup if the user ensures that no DDL or non-transactional table updates occur during the backup. The --no-lock option is not supported by MariaDB plc.


### `<code>--no-timestamp</code>`


This option prevents creation of a time-stamped subdirectory of the BACKUP-ROOT-DIR given on the command line. When it is specified, the backup is done in BACKUP-ROOT-DIR instead. This is only valid in `<code>innobackupex</code>` mode, which can be enabled with the `<code>[--innobackupex](#-innobackupex)</code>` option.


### `<code>--no-version-check</code>`


Disables version check.


Using this option, you can disable Mariabackup version check.


```
$ mariabackup --backup --no-version-check
```

### `<code>--open-files-limit</code>`


Defines the maximum number of file descriptors.


```
--open-files-limit=#
```

Using this option, you can define the maximum number of file descriptors Mariabackup reserves with `<code>setrlimit()</code>`.


```
$ mariabackup --backup \
      --open-files-limit=
```

### `<code>--parallel</code>`


Defines the number of threads to use for parallel data file transfer.


```
--parallel=#
```

Using this option, you can set the number of threads Mariabackup uses for parallel data file transfers. By default, it is set to 1.


### `<code>-p, --password</code>`


Defines the password to use to connect to MariaDB Server.


```
--password=passwd
```

When you run Mariabackup, it connects to MariaDB Server in order to access and back up the databases and tables. Using this option, you can set the password Mariabackup uses to access the server. To set the user, use the `<code>[--user](#-u-user)</code>` option.


```
$ mariabackup --backup \
      --user=root \
      --password=root_password
```

### `<code>--plugin-dir</code>`


Defines the directory for server plugins.


```
--plugin-dir=PATH
```

Using this option, you can define the path Mariabackup reads for MariaDB Server plugins. It only uses it during the `<code>[--prepare](#-prepare)</code>` phase to load the encryption plugin. It defaults to the `<code>[plugin_dir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#plugin_dir)</code>` server system variable.


```
$ mariabackup --backup \
      --plugin-dir=/var/mysql/lib/plugin
```

### `<code>--plugin-load</code>`


Defines the encryption plugins to load.


```
--plugin-load=name
```

Using this option, you can define the encryption plugin you want to load. It is only used during the `<code>[--prepare](#-prepare)</code>` phase to load the encryption plugin. It defaults to the server `<code>--plugin-load</code>` option.


The option was removed.


### `<code>-P, --port</code>`


Defines the server port to connect to.


```
--port=#
```

When you run Mariabackup, it connects to MariaDB Server in order to access and back up your databases and tables. Using this option, you can set the port the utility uses to access the server over TCP/IP. To set the host, see the `<code>[--host](#-h-host)</code>` option. Use `<code>mysql --help</code>` for more details.


```
$ mariabackup --backup \
      --host=192.168.11.1 \
      --port=3306
```

### `<code>--prepare</code>`


Prepares an existing backup to restore to the MariaDB Server.


Files that Mariabackup generates during `<code>[--backup](#-backup)</code>` operations in the target directory are not ready for use on the Server. Before you can restore the data to MariaDB, you first need to prepare the backup.


In the case of full backups, the files are not point in time consistent, since they were taken at different times. If you try to restore the database without first preparing the data, InnoDB rejects the new data as corrupt. Running Mariabackup with the `<code>--prepare</code>` command readies the data so you can restore it to MariaDB Server. When working with incremental backups, you need to use the `<code>--prepare</code>` command and the `<code>[--incremental-dir](#-incremental-dir)</code>` option to update the base backup with the deltas from an incremental backup.


```
$ mariabackup --prepare
```

Once the backup is ready, you can use the `<code>[--copy-back](#-copy-back)</code>` or the `<code>[--move-back](#-move-back)</code>` commands to restore the backup to the server.


### `<code>--print-defaults</code>`


Prints the utility argument list, then exits.


Using this argument, MariaDB prints the argument list to stdout and then exits. You may find this useful in debugging to see how the options are set for the utility.


```
$ mariabackup --print-defaults
```

### `<code>--print-param</code>`


Prints the MariaDB Server options needed for copyback.


Using this option, Mariabackup prints to stdout the MariaDB Server options that the utility requires to run the `<code>[--copy-back](#-copy-back)</code>` command option.


```
$ mariabackup --print-param
```

### `<code>--rollback-xa</code>`


By default, Mariabackup will not commit or rollback uncommitted XA transactions, and when the backup is restored, any uncommitted XA transactions must be manually committed using `<code>XA COMMIT</code>` or manually rolled back using `<code>XA ROLLBACK</code>`.



##### MariaDB starting with [10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)
Mariabackup's `<code>--rollback-xa</code>` option is not present because the server has more robust ways of handling uncommitted XA transactions.


This is an experimental option. Do not use this option in older versions. Older implementation can cause corruption of InnoDB data.


### `<code>--rsync</code>`


Defines whether to use rsync.


During normal operation, Mariabackup transfers local non-InnoDB files using a separate call to `<code>cp</code>` for each file. Using this option, you can optimize this process by performing this transfer with rsync, instead.


```
$ mariabackup --backup --rsync
```

This option is not compatible with the `<code>[--stream](#-stream)</code>` option.


Deprecated and has no effect from [MariaDB 10.11.8](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-8-release-notes.md), [MariaDB 11.0.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes.md), [MariaDB 11.1.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes.md) and [MariaDB 11.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes.md) as rsync will not work on tables that are in use. See [MDEV-32932](https://jira.mariadb.org/browse/MDEV-32932).


### `<code>--safe-slave-backup</code>`


Stops replica SQL threads for backups.


When running Mariabackup on a server that uses replication, you may occasionally encounter locks that block backups. Using this option, it stops replica SQL threads and waits until the `<code>Slave_open_temp_tables</code>` in the `<code>SHOW STATUS</code>` statement is zero. If there are no open temporary tables, the backup runs, otherwise the SQL thread starts and stops until there are no open temporary tables.


```
$ mariabackup --backup \
      --safe-slave-backup \
      --safe-slave-backup-timeout=500
```

The backup fails if the `<code>Slave_open_temp_tables</code>` doesn't reach zero after the timeout period set by the [--safe-slave-backup-timeout](#-safe-slave-backup-timeout) option.


### `<code>--safe-slave-backup-timeout</code>`


Defines the timeout for replica backups.


```
--safe-slave-backup-timeout=#
```

When running Mariabackup on a server that uses replication, you may occasionally encounter locks that block backups. With the [--safe-slave-backup](#-safe-slave-backup) option, it waits until the `<code>Slave_open_temp_tables</code>` in the `<code>SHOW STATUS</code>` statement reaches zero. Using this option, you set how long it waits. It defaults to 300.


```
$ mariabackup --backup \
      --safe-slave-backup \
      --safe-slave-backup-timeout=500
```

### `<code>--secure-auth</code>`


Refuses client connections to servers using the older protocol.


Using this option, you can set it explicitly to refuse client connections to the server when using the older protocol, from before 4.1.1. This feature is enabled by default. Use the [--skip-secure-auth](#-skip-secure-auth) option to disable it.


```
$ mariabackup --backup --secure-auth
```

### `<code>--skip-innodb-adaptive-hash-index</code>`


Disables InnoDB Adaptive Hash Index.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option you can explicitly disable the InnoDB Adaptive Hash Index. This feature is enabled by default for Mariabackup. If you want to explicitly enable it, use `<code>[--innodb-adaptive-hash-index](#-innodb-adaptive-hash-index)</code>`.


```
$ mariabackup --backup \
      --skip-innodb-adaptive-hash-index
```

### `<code>--skip-innodb-doublewrite</code>`


Disables doublewrites for InnoDB tables.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. When doublewrites are enabled, InnoDB improves fault tolerance with a doublewrite buffer. By default this feature is turned on. Using this option you can disable it for Mariabackup. To explicitly enable doublewrites, use the `<code>[--innodb-doublewrite](#-innodb-doublewrite)</code>` option.


```
$ mariabackup --backup \
     --skip-innodb-doublewrite
```

### `<code>--skip-innodb-log-checksums</code>`


Defines whether to exclude checksums in the InnoDB logs.


Mariabackup initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set Mariabackup to exclude checksums in the InnoDB logs. The feature is enabled by default. To explicitly enable it, use the `<code>[--innodb-log-checksums](#-innodb-log-checksums)</code>` option.


### `<code>--skip-secure-auth</code>`


Refuses client connections to servers using the older protocol.


Using this option, you can set it accept client connections to the server when using the older protocol, from before 4.1.1. By default, it refuses these connections. Use the `<code>[--secure-auth](#-secure-auth)</code>` option to explicitly enable it.


```
$ mariabackup --backup --skip-secure-auth
```

### `<code>--slave-info</code>`


Prints the binary log position and the name of the primary server.


If the server is a [replica](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md), then this option causes Mariabackup to print the hostname of the replica's replication primary and the [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) file and position of the [replica's SQL thread](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-threads.md#replica-sql-thread) to `<code>stdout</code>`.


This option also causes Mariabackup to record this information as a [CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) command that can be used to set up a new server as a replica of the original server's primary after the backup has been restored. This information will be written to to the [xtrabackup_slave_info](files-created-by-mariabackup.md#xtrabackup_slave_info) file.


Mariabackup does **not** check if [GTIDs](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) are being used in replication. It takes a shortcut and assumes that if the [gtid_slave_pos](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md#gtid_slave_pos) system variable is non-empty, then it writes the [CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) command with the [MASTER_USE_GTID](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_use_gtid) option set to `<code>slave_pos</code>`. Otherwise, it writes the [CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) command with the [MASTER_LOG_FILE](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_log_file) and [MASTER_LOG_POS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_log_pos) options using the primary's [binary log](../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) file and position. See [MDEV-19264](https://jira.mariadb.org/browse/MDEV-19264) for more information.


```
$ mariabackup --slave-info
```

### `<code>-S, --socket</code>`


Defines the socket for connecting to local database.


```
--socket=name
```

Using this option, you can define the UNIX domain socket you want to use when connecting to a local database server. The option accepts a string argument. For more information, see the `<code>mysql --help</code>` command.


```
$ mariabackup --backup \
      --socket=/var/mysql/mysql.sock
```

### `<code>--ssl</code>`


Enables [TLS](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/README.md). By using this option, you can explicitly configure Mariabackup to to encrypt its connection with [TLS](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/README.md) when communicating with the server. You may find this useful when performing backups in environments where security is extra important or when operating over an insecure network.


TLS is also enabled even without setting this option when certain other TLS options are set. For example, see the descriptions of the following options:


* `<code>[--ssl-ca](#-ssl-ca)</code>`
* `<code>[--ssl-capath](#-ssl-capath)</code>`
* `<code>[--ssl-cert](#-ssl-cert)</code>`
* `<code>[--ssl-cipher](#-ssl-cipher)</code>`
* `<code>[--ssl-key](#-ssl-key)</code>`


### `<code>--ssl-ca</code>`


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


### `<code>--ssl-capath</code>`


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


### `<code>--ssl-cert</code>`


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


### `<code>--ssl-cipher</code>`


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


### `<code>--ssl-crl</code>`


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


### `<code>--ssl-crlpath</code>`


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


### `<code>--ssl-key</code>`


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


### `<code>--ssl-verify-server-cert</code>`


Enables [server certificate verification](../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification). This option is disabled by default.


This option is usually used with other TLS options. For example:


```
$ mariabackup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --ssl-verify-server-cert
```

### `<code>--stream</code>`


Streams backup files to stdout.


```
--stream=xbstream
```

Using this command option, you can set Mariabackup to stream the backup files to stdout in the given format. Currently, the supported format is `<code>xbstream</code>`.


```
$ mariabackup --stream=xbstream > backup.xb
```

To extract all files from the xbstream archive into a directory use the `<code>mbstream</code>` utility


```
$ mbstream  -x < backup.xb
```

If a backup is streamed, then Mariabackup will record the format in the [xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info) file.


### `<code>--tables</code>`


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


### `<code>--tables-exclude</code>`


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


### `<code>--tables-file</code>`


Defines path to file with tables for backups.


```
--tables-file=/path/to/file
```

Using this option, you can set a path to a file listing the tables you want to back up. Mariabackup iterates over each line in the file. The format is `<code>database.table</code>`.


```
$ mariabackup --backup \
     --databases=example \
     --tables-file=/etc/mysql/backup-file
```

If a backup is a [partial backup](partial-backup-and-restore-with-mariabackup.md), then Mariabackup will record that detail in the [xtrabackup_info](files-created-by-mariabackup.md#xtrabackup_info) file.


### `<code>--target-dir</code>`


Defines the destination directory.


```
--target-dir=/path/to/target
```

Using this option you can define the destination directory for the backup. Mariabackup writes all backup files to this directory. Mariabackup will create the directory, if it does not exist (but it will not create the full path recursively, i.e. at least parent directory if the --target-dir must exist=


```
$ mariabackup --backup \
       --target-dir=/data/backups
```

### `<code>--throttle</code>`


Defines the limit for I/O operations per second in IOS values.


```
--throttle=#
```

Using this option, you can set a limit on the I/O operations Mariabackup performs per second in IOS values. It is only used during the [--backup](#-backup) command option.


### `<code>--tls-version</code>`


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


### `<code>-t, --tmpdir</code>`


Defines path for temporary files.


```
--tmpdir=/path/tmp[;/path/tmp...]
```

Using this option, you can define the path to a directory Mariabackup uses in writing temporary files. If you want to use more than one, separate the values by a semicolon (that is, `<code>;</code>`). When passing multiple temporary directories, it cycles through them using round-robin.


```
$ mariabackup --backup \
     --tmpdir=/data/tmp;/tmp
```

### `<code>--use-memory</code>`


Defines the buffer pool size that is used during the prepare stage.


```
--use-memory=124M
```

Using this option, you can define the buffer pool size for Mariabackup. Use it instead of `<code>buffer_pool_size</code>`.


```
$ mariabackup --prepare \
      --use-memory=124M
```

### `<code>--user</code>`


Defines the username for connecting to the MariaDB Server.


```
--user=name
-u name
```

When Mariabackup runs, it connects to the specified MariaDB Server to get its backups. Using this option, you can define the database user used for authentication. Starting from [MariaDB 10.5.24](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10-5-24-release-notes.md), [MariaDB 10.6.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md), [MariaDB 10.11.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md), [MariaDB 11.0.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes.md), [MariaDB 11.1.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes.md), [MariaDB 11.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes.md), [MariaDB 11.3.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes.md), [MariaDB 11.4.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-1-release-notes.md), if the `<code>--user</code>` option is ommited, the user name is detected from the OS.


```
$ mariabackup --backup \
      --user=root \
      --password=root_passwd
```

### `<code>--verbose</code>`


Displays verbose output


```
$ mariabackup --verbose
```

### `<code>--version</code>`


Prints version information.


Using this option, you can print the Mariabackup version information to stdout.


```
$ mariabackup --version
```
