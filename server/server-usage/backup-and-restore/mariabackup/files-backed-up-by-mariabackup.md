# Files Backed Up By Mariabackup

## Files Included in Backup

Mariabackup backs up the files listed below.

### InnoDB Data Files

Mariabackup backs up the following InnoDB data files:

* [InnoDB system tablespace](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md)
* [InnoDB file-per-table tablespaces](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md)

### MyRocks Data Files

Starting with [MariaDB 10.2.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10216-release-notes) and [MariaDB 10.3.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1038-release-notes), Mariabackup will back up tables that use the [MyRocks](../../../reference/storage-engines/myrocks/) storage engine. This data data is located in the directory defined by the `[rocksdb_datadir](../../../reference/storage-engines/myrocks/myrocks-system-variables.md#rocksdb_datadir)` system variable. Mariabackup backs this data up by performing a checkpoint using the `[rocksdb_create_checkpoint](../../../reference/storage-engines/myrocks/myrocks-system-variables.md#rocksdb_create_checkpoint)` system variable.

Mariabackup does not currently support [partial backups](broken-reference) for MyRocks.

### Other Data Files

Mariabackup also backs up files with the following extensions:

* `frm`
* `isl`
* `MYD`
* `MYI`
* `MAD`
* `MAI`
* `MRG`
* `TRG`
* `TRN`
* `ARM`
* `ARZ`
* `CSM`
* `CSV`
* `opt`
* `par`

## Files Excluded From Backup

Mariabackup does **not** back up the files listed below.

* [InnoDB Temporary Tablespaces](../../../reference/storage-engines/innodb/innodb-tablespaces/innodb-temporary-tablespaces.md)
* [Binary logs](../../../server-management/server-monitoring-logs/binary-log/)
* [Relay logs](../../../server-management/server-monitoring-logs/binary-log/relay-log.md)

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
