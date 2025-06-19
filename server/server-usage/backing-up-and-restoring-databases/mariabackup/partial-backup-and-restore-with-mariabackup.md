# Partial Backup and Restore with mariadb-backup

When using mariadb-backup, you have the option of performing partial backups. Partial backups allow you to choose which databases or tables to backup, as long as the table or partition involved is in an [InnoDB file-per-table tablespace](../../storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md).This page documents how to perform partial backups.

## Backing up the Database Server

Just like with [full backups](full-backup-and-restore-with-mariabackup.md), in order to back up the database, you need to run mariadb-backup with the `[--backup](mariabackup-options.md#-backup)` option to tell it to perform a backup and with the `[--target-dir](mariabackup-options.md#-target-dir)` option to tell it where to place the backup files. The target directory must be empty or not exist.

For a partial backup, there are a few other arguments that you can provide as well:

* To tell it which databases to backup, you can provide the `[--databases](mariabackup-options.md#-databases)` option.
* To tell it which databases to exclude from the backup, you can provide the `[--databases-exclude](mariabackup-options.md#-databases-exclude)` option.
* To tell it to check a file for the databases to backup, you can provide the `[--databases-file](mariabackup-options.md#-databases-file)` option.
* To tell it which tables to backup, you can use the `[--tables](mariabackup-options.md#-tables)` option.
* To tell it which tables to exclude from the backup, you can provide the `[--tables-exclude](mariabackup-options.md#-tables-exclude)` option.
* To tell it to check a file for specific tables to backup, you can provide the `[--tables-file](mariabackup-options.md#-tables-file)` option.

The non-file partial backup options support regex in the database and table names.

For example, to take a backup of any database that starts with the string `app1_` and any table in those databases that start with the string `tab_`, run the following command:

```bash
$ mariabackup --backup \
   --target-dir=/var/mariadb/backup/ \
   --databases='app1_*' --tables='tab_*' \
   --user=mariabackup --password=mypassword
```

mariadb-backup cannot currently backup a subset of partitions from a partitioned table. Backing up a partitioned table is currently an all-or-nothing selection. See [MDEV-17132](https://jira.mariadb.org/browse/MDEV-17132) about that. If you need to backup a subset of partitions, then one possibility is that instead of using mariadb-backup, you can [export the file-per-table tablespaces of the partitions](../../storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces).

The time the backup takes depends on the size of the databases or tables you're backing up. You can cancel the backup if you need to, as the backup process does not modify the database.

mariadb-backup writes the backup files to the target directory. If the target directory doesn't exist, then it creates it. If the target directory exists and contains files, then it raises an error and aborts.

## Preparing the Backup

Just like with [full backups](full-backup-and-restore-with-mariabackup.md), the data files that mariadb-backup creates in the target directory are not point-in-time consistent, given that the data files are copied at different times during the backup operation. If you try to restore from these files, InnoDB notices the inconsistencies and crashes to protect you from corruption. In fact, for partial backups, the backup is not even a completely functional MariaDB data directory, so InnoDB would raise more errors than it would for full backups. This point will also be very important to keep in mind during the restore process.

Before you can restore from a backup, you first need to **prepare** it to make the data files consistent. You can do so with the `[--prepare](mariabackup-options.md#-prepare)` command option.

Partial backups rely on [InnoDB's transportable tablespaces](../../storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces). For MariaDB to import tablespaces like these, [InnoDB](../../storage-engines/innodb/) looks for a file with a `.cfg` extension. For mariadb-backup to create these files, you also need to add the `[--export](mariabackup-options.md#-export)` option during the prepare step.

For example, you might execute the following command:

```bash
$ mariabackup --prepare --export \
   --target-dir=/var/mariadb/backup/
```

If this operation completes without error, then the backup is ready to be restored.

mariadb-backup did not support the `[--export](mariabackup-options.md#-export)` option. See [MDEV-13466](https://jira.mariadb.org/browse/MDEV-13466) about that. This means that mariadb-backup could not create `.cfg` files for [InnoDB file-per-table tablespaces](../../storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md) during the `--prepare` stage. You can still [import file-per-table tablespaces](../../storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces) without the `.cfg` files in many cases, so it may still be possible in those versions to [restore partial backups](partial-backup-and-restore-with-mariabackup.md) or to [restore individual tables and partitions](restoring-individual-tables-and-partitions-with-mariabackup.md) with just the `.ibd` files. If you have a [full backup](full-backup-and-restore-with-mariabackup.md) and you need to create `.cfg` files for [InnoDB file-per-table tablespaces](../../storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md), then you can do so by preparing the backup as usual without the `--export` option, and then restoring the backup, and then starting the server. At that point, you can use the server's built-in features to [copy the transportable tablespaces](../../storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces).

## Restoring the Backup

The restore process for partial backups is quite different than the process for [full backups](full-backup-and-restore-with-mariabackup.md). A partial backup is not a completely functional data directory. The data dictionary in the [InnoDB system tablespace](../../storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md) will still contain entries for the databases and tables that were not included in the backup.

Rather than using the `[--copy-back](mariabackup-options.md#-copy-back)` or the `[--move-back](mariabackup-options.md#-move-back)`, each individual [InnoDB file-per-table tablespace](../../storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md) file will have to be manually imported into the target server. The process that is used to import the file will depend on whether partitioning is involved.

### Restoring Individual Non-Partitioned Tables

To restore individual non-partitioned tables from a backup, find the `.ibd` and `.cfg` files for the table in the backup, and then import them using the [Importing Transportable Tablespaces for Non-partitioned Tables](../../storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#importing-transportable-tablespaces-for-non-partitioned-tables) process.

### Restoring Individual Partitions and Partitioned Tables

To restore individual partitions or partitioned tables from a backup, find the `.ibd` and `.cfg` files for the partition(s) in the backup, and then import them using the [Importing Transportable Tablespaces for Partitioned Tables](../../storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#importing-transportable-tablespaces-for-partitioned-tables) process.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
