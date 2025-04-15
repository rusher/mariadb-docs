
# Incremental Backup and Restore with Mariabackup

When using Mariabackup, you have the option of performing a full or incremental backup. Full backups create a complete copy in an empty directory while incremental backups update a previous backup with new data. This page documents incremental backups.


InnoDB pages contain log sequence numbers, or LSN's. Whenever you modify a row on any InnoDB table on the database, the storage engine increments this number. When performing an incremental backup, Mariabackup checks the most recent LSN for the backup against the LSN's contained in the database. It then updates any of the backup files that have fallen behind.


## Backing up the Database Server


In order to take an incremental backup, you first need to take a [full backup](full-backup-and-restore-with-mariabackup.md). In order to back up the database, you need to run Mariabackup with the `<code>[--backup](mariabackup-options.md#-backup)</code>` option to tell it to perform a backup and with the `<code>[--target-dir](mariabackup-options.md#-target-dir)</code>` option to tell it where to place the backup files. When taking a full backup, the target directory must be empty or it must not exist.


To take a backup, run the following command:


```
$ mariabackup --backup \
   --target-dir=/var/mariadb/backup/ \
   --user=mariabackup --password=mypassword
```

This backs up all databases into the target directory `<code>/var/mariadb/backup</code>`. If you look in that directory at the `<code>[xtrabackup_checkpoints](files-created-by-mariabackup.md#xtrabackup_checkpoints)</code>` file, you can see the LSN data provided by InnoDB.


For example:


```
backup_type = full-backuped
from_lsn = 0
to_lsn = 1635102
last_lsn = 1635102
recover_binlog_info = 0
```

## Backing up the Incremental Changes


Once you have created a full backup on your system, you can also back up the incremental changes as often as you would like.


In order to perform an incremental backup, you need to run Mariabackup with the `<code>[--backup](mariabackup-options.md#-backup)</code>` option to tell it to perform a backup and with the `<code>[--target-dir](mariabackup-options.md#-target-dir)</code>` option to tell it where to place the incremental changes. The target directory must be empty. You also need to run it with the `<code>[--incremental-basedir](mariabackup-options.md#-incremental-basedir)</code>` option to tell it the path to the full backup taken above. For example:


```
$ mariabackup --backup \
   --target-dir=/var/mariadb/inc1/ \
   --incremental-basedir=/var/mariadb/backup/ \
   --user=mariabackup --password=mypassword
```

This command creates a series of delta files that store the incremental changes in `<code>/var/mariadb/inc1</code>`. You can find a similar `<code>[xtrabackup_checkpoints](files-created-by-mariabackup.md#xtrabackup_checkpoints)</code>` file in this directory, with the updated LSN values.


For example:


```
backup_type = incremental
from_lsn = 1635102
to_lsn = 1635114
last_lsn = 1635114
recover_binlog_info = 0
```

To perform additional incremental backups, you can then use the target directory of the previous incremental backup as the incremental base directory of the next incremental backup. For example:


```
$ mariabackup --backup \
   --target-dir=/var/mariadb/inc2/ \
   --incremental-basedir=/var/mariadb/inc1/ \
   --user=mariabackup --password=mypassword
```

## Combining with `<code>--stream</code>` output


When using `<code>[--stream](mariabackup-options.md#-stream)</code>`, e.g for [compression or encryption using external tools](using-encryption-and-compression-tools-with-mariabackup.md), the `<code>[xtrabackup_checkpoints](files-created-by-mariabackup.md#xtrabackup_checkpoints)</code>` file containing the information where to continue from on the next incremental backup will also be part of the compressed/encrypted backup file, and so not directly accessible by default.


A directory containing an extra copy of the file can be created using the `<code>[--extra-lsndir=...](mariabackup-options.md#-extra-lsndir)</code>` option though, and this directory can then be passed to the next incremental backup `<code>[--incremental-basedir=...](mariabackup-options.md#-incremental-basedir)</code>`, for example:


```
# initial full backup
$ mariabackup --backup --stream=mbstream \
  --user=mariabackup --password=mypassword \
  --extra-lsndir=backup_base | gzip > backup_base.gz

# incremental backup
$ mariabackup --backup --stream=mbstream \
  --incremental-basedir=backup_base \
  --user=mariabackup --password=mypassword \
  --extra-lsndir=backup_inc1 | gzip > backup-inc1.gz
```

## Preparing the Backup


Following the above steps, you have three backups in `<code>/var/mariadb</code>`: The first is a full backup, the others are increments on this first backup. In order to restore a backup to the database, you first need to apply the incremental backups to the base full backup. This is done using the `<code>[--prepare](mariabackup-options.md#-prepare)</code>` command option. In [MariaDB 10.1](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md), you would also have to use the the `<code>[--apply-log-only](mariabackup-options.md#-apply-log-only)</code>` option.


In [MariaDB 10.2](../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md) and later, perform the following process:


First, prepare the base backup:


```
$ mariabackup --prepare \
   --target-dir=/var/mariadb/backup
```

Running this command brings the base full backup, that is, `<code>/var/mariadb/backup</code>`, into sync with the changes contained in the [InnoDB redo log](../../../reference/storage-engines/innodb/innodb-redo-log.md) collected while the backup was taken.


Then, apply the incremental changes to the base full backup:


```
$ mariabackup --prepare \
   --target-dir=/var/mariadb/backup \
   --incremental-dir=/var/mariadb/inc1
```

Running this command brings the base full backup, that is, `<code>/var/mariadb/backup</code>`, into sync with the changes contained in the first incremental backup.


For each remaining incremental backup, repeat the last step to bring the base full backup into sync with the changes contained in that incremental backup.


## Restoring the Backup


Once you've applied all incremental backups to the base, you can restore the backup using either the `<code>[--copy-back](mariabackup-options.md#-copy-back)</code>` or the `<code>[--move-back](mariabackup-options.md#-move-back)</code>` options. The `<code>[--copy-back](mariabackup-options.md#-copy-back)</code>` option allows you to keep the original backup files. The `<code>[--move-back](mariabackup-options.md#-move-back)</code>` option actually moves the backup files to the `<code>[datadir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir)</code>`, so the original backup files are lost.


* First, [stop the MariaDB Server process](https://mariadb.com/kb/en/).


* Then, ensure that the `<code>[datadir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir)</code>` is empty.


* Then, run Mariabackup with one of the options mentioned above:


```
$ mariabackup --copy-back \
   --target-dir=/var/mariadb/backup/
```

* Then, you may need to fix the file permissions.


When Mariabackup restores a database, it preserves the file and directory privileges of the backup. However, it writes the files to disk as the user and group restoring the database. As such, after restoring a backup, you may need to adjust the owner of the data directory to match the user and group for the MariaDB Server, typically `<code>mysql</code>` for both. For example, to recursively change ownership of the files to the `<code>mysql</code>` user and group, you could execute:


```
$ chown -R mysql:mysql /var/lib/mysql/
```

* Finally, [start the MariaDB Server process](https://mariadb.com/kb/en/).

