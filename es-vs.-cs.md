---
description: >-
  Test page for marking up bigger portions (or a complete page) so that ES
  (Enterprise Server) is in the default tab block, and CS (Community Server) in
  another tab block.
---

# ES vs. CS

## Backing up <a href="#overview_h2" id="overview_h2"></a>

{% tabs %}
{% tab title="Enterprise Server" %}
### MariaDB Enterprise Backup <a href="#overview_h2" id="overview_h2"></a>

### Overview <a href="#overview_h2" id="overview_h2"></a>

Regular and reliable backups are essential to successful recovery of mission critical applications. [MariaDB Enterprise Server](https://mariadb.com/docs/server/products/mariadb-enterprise-server/) backup and restore operations are performed using [MariaDB Enterprise Backup](https://mariadb.com/docs/server/ref/mdb/cli/mariadb-backup/), an [enterprise-build](https://mariadb.com/docs/server/products/mariadb-enterprise-server/lifecycle/) of [MariaDB Backup](https://mariadb.com/docs/server/data-operations/backups/community-server/mariadb-backup/).

[MariaDB Enterprise Backup](https://mariadb.com/docs/server/ref/mdb/cli/mariadb-backup/) is compatible with MariaDB Enterprise Server 10.2, 10.3, 10.4, 10.5, and 10.6.

* [Storage Engines and Backup Types](https://mariadb.com/docs/server/data-operations/backups/enterprise-server/mariadb-enterprise-backup/#Storage_Engines_and_Backup_Types)
* [Non-blocking Backups](https://mariadb.com/docs/server/data-operations/backups/enterprise-server/mariadb-enterprise-backup/#Non-blocking_Backups)
* [Understanding Recovery](https://mariadb.com/docs/server/data-operations/backups/enterprise-server/mariadb-enterprise-backup/#Understanding_Recovery)
* [Creating the Backup User](https://mariadb.com/docs/server/data-operations/backups/enterprise-server/mariadb-enterprise-backup/#Creating_the_Backup_User)
* [Full Backup and Restore](https://mariadb.com/docs/server/data-operations/backups/enterprise-server/mariadb-enterprise-backup/#Full_Backup_and_Restore)
* [Incremental Backup and Restore](https://mariadb.com/docs/server/data-operations/backups/enterprise-server/mariadb-enterprise-backup/#Incremental_Backup_and_Restore)
* [Partial Backup and Restore](https://mariadb.com/docs/server/data-operations/backups/enterprise-server/mariadb-enterprise-backup/#Partial_Backup_and_Restore)
* [Point-in-Time Recoveries](https://mariadb.com/docs/server/data-operations/backups/enterprise-server/mariadb-enterprise-backup/#Point-in-Time_Recoveries)

### Storage Engines and Backup Types

MariaDB Enterprise Backup creates a file-level backup of data from the MariaDB Enterprise Server data directory. This backup includes [temporal data](https://mariadb.com/docs/server/sql/features/temporal-tables/), and the encrypted and unencrypted tablespaces of supported storage engines (e.g., [InnoDB](https://mariadb.com/docs/server/storage-engines/innodb/), [MyRocks](https://mariadb.com/docs/server/storage-engines/myrocks/), [Aria](https://mariadb.com/docs/server/storage-engines/aria/)).

MariaDB Enterprise Server implements:

* Full backups, which contain all data in the database.
* Incremental backups, which contain modifications since the last backup.
* Partial backups, which contain a subset of the tables in the database.

Backup support is specific to storage engines. All supported storage engines enable full backup. The InnoDB storage engine additionally supports incremental backup.
{% endtab %}

{% tab title="Community Server" %}
### Logical vs Physical Backups <a href="#logical-vs-physical-backups" id="logical-vs-physical-backups"></a>

Logical backups consist of the SQL statements necessary to restore the data, such as [CREATE DATABASE](https://mariadb.com/kb/en/create-database/), [CREATE TABLE](https://mariadb.com/kb/en/create-table/) and [INSERT](https://mariadb.com/kb/en/insert/).

Physical backups are performed by copying the individual data files or directories.

The main differences are as follows:

* logical backups are more flexible, as the data can be restored on other hardware configurations, MariaDB versions or even on another DBMS, while physical backups cannot be imported on significantly different hardware, a different DBMS, or potentially even a different MariaDB version.
* logical backups can be performed at the level of database and table, while physical databases are the level of directories and files. In the [MyISAM](https://mariadb.com/kb/en/myisam/) and [InnoDB](https://mariadb.com/kb/en/innodb/) storage engines, each table has an equivalent set of files. (In versions prior to [MariaDB 5.5](https://mariadb.com/kb/en/what-is-mariadb-55/), by default a number of InnoDB tables are stored in the same file, in which case it is not possible to backup by table. See [innodb\_file\_per\_table](https://mariadb.com/kb/en/xtradbinnodb-server-system-variables/#innodb_file_per_table).)
* logical backups are larger in size than the equivalent physical backup.
* logical backups takes more time to both backup and restore than the equivalent physical backup.
* log files and configuration files are not part of a logical backup

### Backup Tools <a href="#backup-tools" id="backup-tools"></a>

#### Mariadb-backup <a href="#mariadb-backup" id="mariadb-backup"></a>

[Mariadb-backup](https://mariadb.com/kb/en/mariadb-backup/) is a fork of [Percona XtraBackup](https://mariadb.com/kb/en/backup-restore-and-import-xtrabackup/) with added support for [MariaDB 10.1](https://mariadb.com/kb/en/what-is-mariadb-101/) [compression](https://mariadb.com/kb/en/backup-and-restore-overview/InnoDB_compression) and [data-at-rest encryption](https://mariadb.com/kb/en/data-at-rest-encryption/). It is included with [MariaDB 10.1.23](https://mariadb.com/kb/en/mariadb-10123-release-notes/) and later.

#### mariadb-dump <a href="#mariadb-dump" id="mariadb-dump"></a>

[mariadb-dump](https://mariadb.com/kb/en/mariadb-dump/) (previously mysqldump) performs a logical backup. It is the most flexible way to perform a backup and restore, and a good choice when the data size is relatively small.

For large datasets, the backup file can be large, and the restore time lengthy.

mariadb-dump dumps the data into SQL format (it can also dump into other formats, such as CSV or XML) which can then easily be imported into another database. The data can be imported into other versions of MariaDB, MySQL, or even another DBMS entirely, assuming there are no version or DBMS-specific statements in the dump.

mariadb-dump dumps triggers along with tables, as these are part of the table definition. However, [stored procedures](https://mariadb.com/kb/en/stored-procedures/), [views](https://mariadb.com/kb/en/views/), and [events](https://mariadb.com/kb/en/events/) are not, and need extra parameters to be recreated explicitly (for example, `--routines` and `--events`). [Procedures](https://mariadb.com/kb/en/stored-procedures/) and [functions](https://mariadb.com/kb/en/backup-and-restore-overview/functions) are however also part of the system tables (for example [mysql.proc](https://mariadb.com/kb/en/mysqlproc-table/)).

**InnoDB Logical Backups**

InnoDB uses the [buffer pool](https://mariadb.com/kb/en/xtradbinnodb-buffer-pool/), which stores data and indexes from its tables in memory. This buffer is very important for performance. If InnoDB data doesn't fit the memory, it is important that the buffer contains the most frequently accessed data. However, last accessed data is candidate for insertion into the buffer pool. If not properly configured, when a table scan happens, InnoDB may copy the whole contents of a table into the buffer pool. The problem with logical backups is that they always imply full table scans.

An easy way to avoid this is by increasing the value of the [innodb\_old\_blocks\_time](https://mariadb.com/kb/en/xtradbinnodb-server-system-variables/#innodb_old_blocks_time) system variable. It represents the number of milliseconds that must pass before a recently accessed page can be put into the "new" sublist in the buffer pool. Data which is accessed only once should remain in the "old" sublist. This means that they will soon be evicted from the buffer pool. Since during the backup process the "old" sublist is likely to store data that is not useful, one could also consider resizing it by changing the value of the [innodb\_old\_blocks\_pct](https://mariadb.com/kb/en/xtradbinnodb-server-system-variables/#innodb_old_blocks_pct) system variable.

It is also possible to explicitly dump the buffer pool on disk before starting a logical backup, and restore it after the process. This will undo any negative change to the buffer pool which happens during the backup. To dump the buffer pool, the [innodb\_buffer\_pool\_dump\_now](https://mariadb.com/kb/en/innodb-system-variables/#innodb_buffer_pool_dump_now) system variable can be set to ON. To restore it, the [innodb\_buffer\_pool\_load\_now](https://mariadb.com/kb/en/innodb-system-variables/#innodb_buffer_pool_load_now) system variable can be set to ON.

**Examples**

Backing up a single database

```
shell> mariadb-dump db_name > backup-file.sql
```

Restoring or loading the database

```
shell> mariadb db_name < backup-file.sql
```

See the [mariadb-dump](https://mariadb.com/kb/en/mariadb-dump/) page for detailed syntax and examples.

#### mariadb-hotcopy <a href="#mariadb-hotcopy" id="mariadb-hotcopy"></a>

[mariadb-hotcopy](https://mariadb.com/kb/en/mariadb-hotcopy/) performs a physical backup, and works only for backing up [MyISAM](https://mariadb.com/kb/en/myisam/) and [ARCHIVE](https://mariadb.com/kb/en/archive/) tables. It can only be run on the same machine as the location of the database directories.

**Examples**

```
shell> mariadb-hotcopy db_name [/path/to/new_directory]
shell> mariadb-hotcopy db_name_1 ... db_name_n /path/to/new_directory
```

#### Percona XtraBackup <a href="#percona-xtrabackup" id="percona-xtrabackup"></a>

Percona XtraBackup is **not supported** in MariaDB. [Mariabackup](https://mariadb.com/kb/en/mariabackup/) is the recommended backup method to use instead of Percona XtraBackup. See [Percona XtraBackup Overview: Compatibility with MariaDB](https://mariadb.com/kb/en/percona-xtrabackup-overview/#compatibility-with-mariadb) for more information.

[Percona XtraBackup](https://mariadb.com/kb/en/backup-restore-and-import-xtrabackup/) is a tool for performing fast, hot backups. It was designed specifically for [XtraDB/InnoDB](https://mariadb.com/kb/en/innodb/) databases, but can be used with any storage engine (although not with [MariaDB 10.1](https://mariadb.com/kb/en/what-is-mariadb-101/) [encryption](https://mariadb.com/kb/en/encryption/) and [compression](https://mariadb.com/kb/en/compression/)). It is not included by default with MariaDB.

#### Filesystem Snapshots <a href="#filesystem-snapshots" id="filesystem-snapshots"></a>

Some filesystems, like Veritas, support snapshots. During the snapshot, the table must be locked. The proper steps to obtain a snapshot are:

* From the mariadb client, execute [FLUSH TABLES WITH READ LOCK](https://mariadb.com/kb/en/flush/). The client must remain open.
* From a shell, execute `mount vxfs snapshot`
* The client can execute [UNLOCK TABLES](https://mariadb.com/kb/en/transactions-lock/).
* Copy the snapshot files.
* From a shell, unmount the snapshot with `umount snapshot`.

#### LVM <a href="#lvm" id="lvm"></a>

Widely-used physical backup method, using a Perl script as a wrapper. See [http://www.lenzg.net/mylvmbackup/](http://www.lenzg.net/mylvmbackup/).

#### Percona TokuBackup <a href="#percona-tokubackup" id="percona-tokubackup"></a>

For details, see:

* [TokuDB Hot Backup – Part 1](https://www.percona.com/blog/2013/09/12/tokudb-hot-backup-part-1/)
* [TokuDB Hot Backup – Part 2](https://www.percona.com/blog/2013/09/19/tokudb-hot-backup-part-2/)
* [TokuDB Hot Backup Now a MySQL Plugin](https://www.percona.com/blog/2015/02/05/tokudb-hot-backup-now-mysql-plugin/)

#### dbForge Studio for MySQL <a href="#dbforge-studio-for-mysql" id="dbforge-studio-for-mysql"></a>

Besides the system utilities, it is possible to use third-party GUI tools to perform backup and restore operations. In this context, it is worth mentioning dbForge Studio for MySQL, a feature-rich database IDE that is fully compatible with MariaDB and delivers extensive backup functionality.

The backup and restore module of the Studio allows precise [configuration and management of full and partial backups](https://mariadb.com/kb/en/backup-and-restore-via-dbforge-studio/) up to particular database objects. The feature of scheduling regular backups offers specific settings to handle errors and keep a log of them. Additionally, settings and configurations can be saved for later reuse.

These operations are wizard-aided allowing users to set up all tasks in a visual mode.
{% endtab %}
{% endtabs %}
