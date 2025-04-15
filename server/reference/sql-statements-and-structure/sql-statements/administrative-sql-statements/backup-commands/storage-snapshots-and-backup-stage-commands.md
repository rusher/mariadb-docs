
# Storage Snapshots and BACKUP STAGE Commands


The [BACKUP STAGE](backup-stage.md) commands are a set of commands to make it possible to make an efficient external backup tool. These commands could even be used by tools that perform backups by taking a snapshot of a file system, SAN, or some other kind of storage device.


## Generic Backup Process with Storage Snapshots


A tool that backs up MariaDB by taking a snapshot of a file system, SAN, or some other kind of storage device could use each `<code>BACKUP STAGE</code>` command in the following way:


* First, execute the following:


```
BACKUP STAGE START
BACKUP STAGE BLOCK_COMMIT
```

* Then, take the snapshot.


* Then, execute the following:


```
BACKUP STAGE END
```

The above ensures that all non-transactional tables are properly flushed to disk before the snapshot is done.
Using `<code>BACKUP STAGE</code>` commands is also more efficient than using the [FLUSH TABLES WITH READ LOCK](../flush-commands/flush-tables-for-export.md) command as the above set of commands will not block or be blocked by write operations to transactional tables.


Note that when the backup is completed, one should delete all files with the "#sql" prefix, as these are files used by concurrent running `<code>ALTER TABLE</code>`. Note that InnoDB will on server restart automatically delete any tables with the "#sql" prefix.

