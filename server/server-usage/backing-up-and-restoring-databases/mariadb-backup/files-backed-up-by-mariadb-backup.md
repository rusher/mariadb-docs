# Files Backed Up By mariadb-backup

## Files Backed Up By mariadb-backup

### Files Included in Backup

mariadb-backup backs up the files listed below.

#### InnoDB Data Files

mariadb-backup backs up the following InnoDB data files:

* InnoDB system tablespace
* InnoDB file-per-table tablespaces

#### MyRocks Data Files

<<<<<<< HEAD\
Starting with [MariaDB 10.2.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10216-release-notes) and [MariaDB 10.3.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1038-release-notes), mariadb-backup will back up tables that use the MyRocks storage engine. This data data is located in the directory defined by the `[rocksdb_datadir](../../../reference/storage-engines/myrocks/myrocks-system-variables.md#rocksdb_datadir)` system variable. mariadb-backup backs this data up by performing a checkpoint using the `[rocksdb_create_checkpoint](../../../reference/storage-engines/myrocks/myrocks-system-variables.md#rocksdb_create_checkpoint)` system variable.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Starting with [MariaDB 10.2.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10216-release-notes) and [MariaDB 10.3.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1038-release-notes), mariadb-backup will back up tables that use the MyRocks storage engine. This data data is located in the directory defined by the rocksdb\_datadir system variable. mariadb-backup backs this data up by performing a checkpoint using the rocksdb\_create\_checkpoint system variable.

> > > > > > > 2f4a7af992d60113345320299a7c689ee31815c1

mariadb-backup does not currently support partial backups for MyRocks.

#### Other Data Files

mariadb-backup also backs up files with the following extensions:

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

### Files Excluded From Backup

mariadb-backup does **not** back up the files listed below.

* InnoDB Temporary Tablespaces
* Binary logs
* Relay logs

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
