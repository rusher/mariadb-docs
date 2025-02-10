# BACKUP STAGE

The `BACKUP STAGE` commands are a set of commands to make it possible to make an efficient external backup tool.

{% hint style="info" %}
BACKUP STAGE commands are available from MariaDB 10.4.1.
{% endhint %}

### Syntax <a href="#syntax" id="syntax"></a>

```
BACKUP STAGE [START | FLUSH | BLOCK_DDL | BLOCK_COMMIT | END ]
```

In the following text, a transactional table means InnoDB or "InnoDB-like engine with redo log that can lock redo purges and can be copied without locks by an outside process".

### Syntax <a href="#syntax" id="syntax"></a>

```
BACKUP STAGE [START | FLUSH | BLOCK_DDL | BLOCK_COMMIT | END ]
```

In the following text, a transactional table means InnoDB or "InnoDB-like engine with redo log that can lock redo purges and can be copied without locks by an outside process".

### Goals with BACKUP STAGE Commands <a href="#goals-with-backup-stage-commands" id="goals-with-backup-stage-commands"></a>

* To be able to do a majority of the backup with the minimum possible server locks. Especially for transactional tables (InnoDB, MyRocks etc) there is only need for a very short block of new commits while copying statistics and log tables.
* DDL are only needed to be blocked for a very short duration of the backup while [mariabackup](https://mariadb.com/kb/en/mariabackup/) is copying the tables affected by DDL during the initial part of the backup.
* Most non transactional tables (those that are not in use) will be copied during `BACKUP STAGE START`. The exceptions are system statistic and log tables that are not blocked during the backup until `BLOCK_COMMIT`.
* Should work efficiently with backup tools that use disk snapshots.
* Should work as efficiently as possible for all table types that store data on the local disks.
* As little copying as possible under higher level stages/locks. For example, .frm (dictionary) and .trn (trigger) files should be copying while copying the table data.

### `BACKUP STAGE` Commands <a href="#backup-stage-commands" id="backup-stage-commands"></a>

#### `BACKUP STAGE START` <a href="#backup-stage-start" id="backup-stage-start"></a>

The `START` stage is designed for the following tasks:

* Blocks purge of redo files for storage engines that needs this (Aria)
* Start logging of DDL commands into 'datadir'/ddl.log. This may take a short time as the command has to wait until there are no active DDL commands.

#### `BACKUP STAGE FLUSH` <a href="#backup-stage-flush" id="backup-stage-flush"></a>

The `FLUSH` stage is designed for the following tasks:

* FLUSH all changes for inactive non-transactional tables, except for statistics and log tables.
* Close all tables that are not in use, to ensure they are marked as closed for the backup.
* BLOCK all new write locks for all non transactional tables (except statistics and log tables). The command will not wait for tables that are in use by read-only transactions.

DDLs don't have to be blocked at this stage as they can't cause the table to be in an inconsistent state. This is true also for non-transactional tables.

#### `BACKUP STAGE BLOCK_DDL` <a href="#backup-stage-block_ddl" id="backup-stage-block_ddl"></a>

The `BLOCK_DDL` stage is designed for the following tasks:

* Wait for all statements using write locked non-transactional tables to end.
* Blocks [CREATE TABLE](https://mariadb.com/kb/en/create-table/), [DROP TABLE](https://mariadb.com/kb/en/drop-table/), [TRUNCATE TABLE](https://mariadb.com/kb/en/truncate-table/), and [RENAME TABLE](https://mariadb.com/kb/en/rename-table/).
* Blocks also start off a **new** [ALTER TABLE](https://mariadb.com/kb/en/alter-table/) and the **final rename phase** of [ALTER TABLE](https://mariadb.com/kb/en/alter-table/). Running ALTER TABLES are not blocked.

#### `BACKUP STAGE BLOCK_COMMIT` <a href="#backup-stage-block_commit" id="backup-stage-block_commit"></a>

The `BLOCK_COMMIT` stage is designed for the following tasks:

* Lock the binary log and commit/rollback to ensure that no changes are committed to any tables. If there are active commits or data to be copied to the binary log this will be allowed to finish. Active transactions will not affect `BLOCK_COMMIT`.
* This doesn't lock temporary tables that are not used by replication. However these will be blocked when it's time to write to the binary log.
* Lock system log tables and statistics tables, flush them and mark them closed.

When the `BLOCK_COMMIT`'s stages return, this is the 'backup time'. Everything committed will be in the backup and everything not committed will roll back.

Transactional engines will continue to do changes to the redo log during the `BLOCK COMMIT` stage, but this is not important as all of these will roll back later as the changes will not be committed.

#### `BACKUP STAGE END` <a href="#backup-stage-end" id="backup-stage-end"></a>

The `END` stage is designed for the following tasks:

* End DDL logging
* Free resources

### Using `BACKUP STAGE` Commands with Backup Tools <a href="#using-backup-stage-commands-with-backup-tools" id="using-backup-stage-commands-with-backup-tools"></a>

#### Using `BACKUP STAGE` Commands with Mariabackup <a href="#using-backup-stage-commands-with-mariabackup" id="using-backup-stage-commands-with-mariabackup"></a>

The `BACKUP STAGE` commands are a set of commands that enable you to create an efficient external backup tool. How [Mariabackup](https://mariadb.com/kb/en/mariabackup/) uses these commands depends on which version you are using. Prior to [MariaDB 10.11.8](https://mariadb.com/kb/en/mariadb-10-11-8-release-notes/), [MariaDB 11.0.6](https://mariadb.com/kb/en/mariadb-11-0-6-release-notes/), [MariaDB 11.1.5](https://mariadb.com/kb/en/mariadb-11-1-5-release-notes/) and [MariaDB 11.2.4](https://mariadb.com/kb/en/mariadb-11-2-4-release-notes/), this depended on whether you are using the version that is bundled with MariaDB Community Server or the version that is bundled with [MariaDB Enterprise Server](https://mariadb.com/docs/products/mariadb-enterprise-server/). See [Mariabackup and BACKUP STAGE Commands](https://mariadb.com/kb/en/mariabackup-and-backup-stage-commands/) for some examples on how [Mariabackup](https://mariadb.com/kb/en/mariabackup/) uses these commands. From [MariaDB 10.11.8](https://mariadb.com/kb/en/mariadb-10-11-8-release-notes/), [MariaDB 11.0.6](https://mariadb.com/kb/en/mariadb-11-0-6-release-notes/), [MariaDB 11.1.5](https://mariadb.com/kb/en/mariadb-11-1-5-release-notes/) and [MariaDB 11.2.4](https://mariadb.com/kb/en/mariadb-11-2-4-release-notes/), these features were ported from MariaDB Enterprise Server ([MDEV-32932](https://jira.mariadb.org/browse/MDEV-32932)).

{% tabs %}
{% tab title="Current" %}
BACKUP STAGE is available to Mariabackup for MariaDB Enterprise Server and MariaDB Community Server.
{% endtab %}

{% tab title="MariaDB < 11.2.4" %}
BACKUP STAGE is available depending on the Mariabackup version that is bundled with the MariaDB Server, which can be MariaDB Enterprise Server or MariaDB Community Server.
{% endtab %}

{% tab title="MariaDB < 11.1.5" %}
BACKUP STAGE is available depending on the Mariabackup version that is bundled with the MariaDB Server, which can be MariaDB Enterprise Server or MariaDB Community Server.
{% endtab %}

{% tab title="MariaDB < 11.0.6" %}
BACKUP STAGE is available depending on the Mariabackup version that is bundled with the MariaDB Server, which can be MariaDB Enterprise Server or MariaDB Community Server.
{% endtab %}

{% tab title="MariaDB < 10.11.8" %}
BACKUP STAGE is available depending on the Mariabackup version that is bundled with the MariaDB Server, which can be MariaDB Enterprise Server or MariaDB Community Server.
{% endtab %}
{% endtabs %}

#### Using `BACKUP STAGE` Commands with Storage Snapshots <a href="#using-backup-stage-commands-with-storage-snapshots" id="using-backup-stage-commands-with-storage-snapshots"></a>

The `BACKUP STAGE` commands are a set of commands to make it possible to make an efficient external backup tool. These commands could even be used by tools that perform backups by taking a snapshot of a file system, SAN, or some other kind of storage device. See [Storage Snapshots and BACKUP STAGE Commands](https://mariadb.com/kb/en/storage-snapshots-and-backup-stage-commands/) for some examples on how to use each `BACKUP STAGE` command in an efficient way.

### Privileges <a href="#privileges" id="privileges"></a>

`BACKUP STAGE` requires the [RELOAD](https://mariadb.com/kb/en/grant/) privilege.

### Notes <a href="#notes" id="notes"></a>

* Only one connection can run `BACKUP STAGE START`. If a second connection tries, it will wait until the first one has executed `BACKUP STAGE END`.
* If the user skips a `BACKUP STAGE`, then all intermediate backup stages will automatically be run. This will allow us to add new stages within the `BACKUP STAGE` hierarchy in the future with even more precise locks without causing problems for tools using an earlier version of the `BACKUP STAGE` implementation.
* One can use the [max\_statement\_time](https://mariadb.com/kb/en/server-system-variables/#max_statement_time) or [lock\_wait\_timeout](https://mariadb.com/kb/en/server-system-variables/#lock_wait_timeout) system variables to ensure that a `BACKUP STAGE` command doesn't block the server too long.
* DDL logging is only be available from [MariaDB 10.11.8](https://mariadb.com/kb/en/mariadb-10-11-8-release-notes/), [MariaDB 11.0.6](https://mariadb.com/kb/en/mariadb-11-0-6-release-notes/), [MariaDB 11.1.5](https://mariadb.com/kb/en/mariadb-11-1-5-release-notes/) and [MariaDB 11.2.4](https://mariadb.com/kb/en/mariadb-11-2-4-release-notes/), or in [MariaDB Enterprise Server](https://mariadb.com/docs/products/mariadb-enterprise-server/).
* A disconnect will automatically release backup stages.
* There is no easy way to see which is the current stage.



