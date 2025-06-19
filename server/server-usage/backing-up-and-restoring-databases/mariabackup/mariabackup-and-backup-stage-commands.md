# Mariabackup and BACKUP STAGE Commands

The [BACKUP STAGE](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/backup-commands/backup-stage.md) commands are a set of commands to make it possible to make an efficient external backup tool. How Mariabackup uses these commands depends on whether you are using the version that is bundled with MariaDB Community Server or the version that is bundled with [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-server/blob/test/en/mariadb-enterprise-server/README.md).

## Mariabackup and `BACKUP STAGE` Commands in MariaDB Community Server

The [BACKUP STAGE](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/backup-commands/backup-stage.md) commands are supported. However, the version of Mariabackup that is bundled with MariaDB Community Server does not yet use the [BACKUP STAGE](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/backup-commands/backup-stage.md) commands in the most efficient way. Mariabackup simply executes the following [BACKUP STAGE](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/backup-commands/backup-stage.md) commands to lock the database:

```sql
BACKUP STAGE START;
BACKUP STAGE BLOCK_COMMIT;
```

When the backup is complete, it executes the following [BACKUP STAGE](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/backup-commands/backup-stage.md) command to unlock the database:

```sql
BACKUP STAGE END;
```

If you would like to use a version of Mariabackup that uses the [BACKUP STAGE](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/backup-commands/backup-stage.md) commands in the most efficient way, then your best option is to use [MariaDB Backup](./) that is bundled with [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-server/blob/test/en/mariadb-enterprise-server/README.md).

### Tasks Performed Prior to `BACKUP STAGE` in MariaDB Community Server

* Copy some transactional tables.
  * [InnoDB](../../storage-engines/innodb/) (i.e. `ibdataN` and file extensions `.ibd` and `.isl`)
* Copy the tail of some transaction logs.
  * The tail of the [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md) (i.e. `ib_logfileN` files) will be copied for [InnoDB](../../storage-engines/innodb/) tables.

### `BACKUP STAGE START` in MariaDB Community Server

Mariabackup from MariaDB Community Server does not currently perform any tasks in the `START` stage.

### `BACKUP STAGE FLUSH` in MariaDB Community Server

Mariabackup from MariaDB Community Server does not currently perform any tasks in the `FLUSH` stage.

### `BACKUP STAGE BLOCK_DDL` in MariaDB Community Server

Mariabackup from MariaDB Community Server does not currently perform any tasks in the `BLOCK_DDL` stage.

### `BACKUP STAGE BLOCK_COMMIT` in MariaDB Community Server

Mariabackup from MariaDB Community Server performs the following tasks in the `BLOCK_COMMIT` stage:

* Copy other files.
  * i.e. file extensions `.frm`, `.isl`, `.TRG`, `.TRN`, `.opt`, `.par`
* Copy some transactional tables.
  * [Aria](../../storage-engines/aria/) (i.e. `aria_log_control` and file extensions `.MAD` and `.MAI`)
* Copy the non-transactional tables.
  * [MyISAM](../../storage-engines/myisam-storage-engine/) (i.e. file extensions `.MYD` and `.MYI`)
  * [MERGE](../../storage-engines/merge.md) (i.e. file extensions `.MRG`)
  * [ARCHIVE](../../storage-engines/archive.md) (i.e. file extensions `.ARM` and `.ARZ`)
  * [CSV](../../storage-engines/csv/) (i.e. file extensions `.CSM` and `.CSV`)
* Create a [MyRocks](../../storage-engines/myrocks/) checkpoint using the [rocksdb_create_checkpoint](../../../reference/storage-engines/myrocks/myrocks-system-variables.md#rocksdb_create_checkpoint) system variable.
* Copy the tail of some transaction logs.
  * The tail of the [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md) (i.e. `ib_logfileN` files) will be copied for [InnoDB](../../storage-engines/innodb/) tables.
* Save the [binary log](../../../server-management/server-monitoring-logs/binary-log/) position to [xtrabackup_binlog_info](files-created-by-mariabackup.md#xtrabackup_binlog_info).
* Save the [Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/en/galera/README.md) state information to [xtrabackup_galera_info](files-created-by-mariabackup.md#xtrabackup_galera_info).

### `BACKUP STAGE END` in MariaDB Community Server

Mariabackup from MariaDB Community Server performs the following tasks in the `END` stage:

* Copy the [MyRocks](../../storage-engines/myrocks/) checkpoint into the backup.

## Mariabackup and `BACKUP STAGE` Commands in MariaDB Enterprise Server

The following sections describe how the [MariaDB Backup](./) version of Mariabackup that is bundled with [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-server/blob/test/en/mariadb-enterprise-server/README.md) uses each [BACKUP STAGE](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/backup-commands/backup-stage.md) command in an efficient way.

### `BACKUP STAGE START` in MariaDB Enterprise Server

Mariabackup from MariaDB Enterprise Server performs the following tasks in the `START` stage:

* Copy all transactional tables.
  * [InnoDB](../../storage-engines/innodb/) (i.e. `ibdataN` and file extensions `.ibd` and `.isl`)
  * [Aria](../../storage-engines/aria/) (i.e. `aria_log_control` and file extensions `.MAD` and `.MAI`)
* Copy the tail of all transaction logs.
  * The tail of the [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md) (i.e. `ib_logfileN` files) will be copied for [InnoDB](../../storage-engines/innodb/) tables.
  * The tail of the Aria redo log (i.e. `aria_log.N` files) will be copied for [Aria](../../storage-engines/aria/) tables.

### `BACKUP STAGE FLUSH` in MariaDB Enterprise Server

Mariabackup from MariaDB Enterprise Server performs the following tasks in the `FLUSH` stage:

* Copy all non-transactional tables that are not in use. This list of used tables is found with [SHOW OPEN TABLES](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-open-tables.md).
  * [MyISAM](../../storage-engines/myisam-storage-engine/) (i.e. file extensions `.MYD` and `.MYI`)
  * [MERGE](../../storage-engines/merge.md) (i.e. file extensions `.MRG`)
  * [ARCHIVE](../../storage-engines/archive.md) (i.e. file extensions `.ARM` and `.ARZ`)
  * [CSV](../../storage-engines/csv/) (i.e. file extensions `.CSM` and `.CSV`)
* Copy the tail of all transaction logs.
  * The tail of the [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md) (i.e. `ib_logfileN` files) will be copied for [InnoDB](../../storage-engines/innodb/) tables.
  * The tail of the Aria redo log (i.e. `aria_log.N` files) will be copied for [Aria](../../storage-engines/aria/) tables.

### `BACKUP STAGE BLOCK_DDL` in MariaDB Enterprise Server

Mariabackup from MariaDB Enterprise Server performs the following tasks in the `BLOCK_DDL` stage:

* Copy other files.
  * i.e. file extensions `.frm`, `.isl`, `.TRG`, `.TRN`, `.opt`, `.par`
* Copy the non-transactional tables that were in use during `BACKUP STAGE FLUSH`.
  * [MyISAM](../../storage-engines/myisam-storage-engine/) (i.e. file extensions `.MYD` and `.MYI`)
  * [MERGE](../../storage-engines/merge.md) (i.e. file extensions `.MRG`)
  * [ARCHIVE](../../storage-engines/archive.md) (i.e. file extensions `.ARM` and `.ARZ`)
  * [CSV](../../storage-engines/csv/) (i.e. file extensions `.CSM` and `.CSV`)
* Check `ddl.log` for DDL executed before the `BLOCK DDL` stage.
  * The file names of newly created tables can be read from `ddl.log`.
  * The file names of dropped tables can also be read from `ddl.log`.
  * The file names of renamed tables can also be read from `ddl.log`, so the files can be renamed instead of re-copying them.
* Copy changes to system log tables.
  * [mysql.general_log](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysqlgeneral_log-table.md)
  * [mysql.slow_log](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-slow_log-table.md)
  * This is easy as these are append only.
* Copy the tail of all transaction logs.
  * The tail of the [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md) (i.e. `ib_logfileN` files) will be copied for [InnoDB](../../storage-engines/innodb/) tables.
  * The tail of the Aria redo log (i.e. `aria_log.N` files) will be copied for [Aria](../../storage-engines/aria/) tables.

### `BACKUP STAGE BLOCK_COMMIT` in MariaDB Enterprise Server

Mariabackup from MariaDB Enterprise Server performs the following tasks in the `BLOCK_COMMIT` stage:

* Create a [MyRocks](../../storage-engines/myrocks/) checkpoint using the [rocksdb_create_checkpoint](../../../reference/storage-engines/myrocks/myrocks-system-variables.md#rocksdb_create_checkpoint) system variable.
* Copy changes to system log tables.
  * [mysql.general_log](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysqlgeneral_log-table.md)
  * [mysql.slow_log](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-slow_log-table.md)
  * This is easy as these are append only.
* Copy changes to statistics tables.
  * [mysql.table_stats](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-table_stats-table.md)
  * [mysql.column_stats](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-column_stats-table.md)
  * [mysql.index_stats](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-index_stats-table.md)
* Copy the tail of all transaction logs.
  * The tail of the [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md) (i.e. `ib_logfileN` files) will be copied for [InnoDB](../../storage-engines/innodb/) tables.
  * The tail of the Aria redo log (i.e. `aria_log.N` files) will be copied for [Aria](../../storage-engines/aria/) tables.
* Save the [binary log](../../../server-management/server-monitoring-logs/binary-log/) position to [xtrabackup_binlog_info](files-created-by-mariabackup.md#xtrabackup_binlog_info).
* Save the [Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/en/galera/README.md) state information to [xtrabackup_galera_info](files-created-by-mariabackup.md#xtrabackup_galera_info).

### `BACKUP STAGE END` in MariaDB Enterprise Server

Mariabackup from MariaDB Enterprise Server performs the following tasks in the `END` stage:

* Copy the [MyRocks](../../storage-engines/myrocks/) checkpoint into the backup.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
