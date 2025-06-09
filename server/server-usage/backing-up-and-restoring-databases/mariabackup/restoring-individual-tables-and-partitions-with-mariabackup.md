# Restoring Individual Tables and Partitions with Mariabackup

When using Mariabackup, you don't necessarily need to restore every table and/or partition that was backed up. Even if you're starting from a [full backup](full-backup-and-restore-with-mariabackup.md), it is certainly possible to restore only certain tables and/or partitions from the backup, as long as the table or partition involved is in an [InnoDB file-per-table tablespace](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md). This page documents how to restore individual tables and partitions.

## Preparing the Backup

Before you can restore from a backup, you first need to **prepare** it to make the data files consistent. You can do so with the `[--prepare](mariabackup-options.md#-prepare)` command option.

The ability to restore individual tables and partitions relies on [InnoDB's transportable tablespaces](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces). For MariaDB to import tablespaces like these, [InnoDB](../../../reference/storage-engines/innodb/) looks for a file with a `.cfg` extension. For Mariabackup to create these files, you also need to add the `[--export](mariabackup-options.md#-export)` option during the prepare step.

For example, you might execute the following command:

```bash
$ mariabackup --prepare --export \
   --target-dir=/var/mariadb/backup/ \
   --user=mariabackup --password=mypassword
```

If this operation completes without error, then the backup is ready to be restored.

#### Note

Mariabackup did not support the `[--export](mariabackup-options.md#-export)` option to begin with. See [MDEV-13466](https://jira.mariadb.org/browse/MDEV-13466) about that. In earlier versions of MariaDB, this means that Mariabackup could not create `.cfg` files for [InnoDB file-per-table tablespaces](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md) during the `--prepare` stage. You can still [import file-per-table tablespaces](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces) without the `.cfg` files in many cases, so it may still be possible in those versions to [restore partial backups](partial-backup-and-restore-with-mariabackup.md) or to [restore individual tables and partitions](restoring-individual-tables-and-partitions-with-mariabackup.md) with just the `.ibd` files. If you have a [full backup](full-backup-and-restore-with-mariabackup.md) and you need to create `.cfg` files for [InnoDB file-per-table tablespaces](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md), then you can do so by preparing the backup as usual without the `--export` option, and then restoring the backup, and then starting the server. At that point, you can use the server's built-in features to [copy the transportable tablespaces](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces).

## Restoring the Backup

The restore process for restoring individual tables and/or partitions is quite different than the process for [full backups](full-backup-and-restore-with-mariabackup.md).

Rather than using the `[--copy-back](mariabackup-options.md#-copy-back)` or the `[--move-back](mariabackup-options.md#-move-back)`, each individual [InnoDB file-per-table tablespace](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md) file will have to be manually imported into the target server. The process that is used to restore the backup will depend on whether partitioning is involved.

### Restoring Individual Non-Partitioned Tables

To restore individual non-partitioned tables from a backup, find the `.ibd` and `.cfg` files for the table in the backup, and then import them using the [Importing Transportable Tablespaces for Non-partitioned Tables](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#importing-transportable-tablespaces-for-non-partitioned-tables) process.

### Restoring Individual Partitions and Partitioned Tables

To restore individual partitions or partitioned tables from a backup, find the `.ibd` and `.cfg` files for the partition(s) in the backup, and then import them using the [Importing Transportable Tablespaces for Partitioned Tables](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#importing-transportable-tablespaces-for-partitioned-tables) process.

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
