
# Downgrading between Major Versions of MariaDB

Downgrading MariaDB is not officially supported between major versions.

For minor versions, upgrade is supported to an earlier [gamma/RC/GA](../../../release-notes/mariadb-release-criteria.md) version as we do not change the storage format after [Alpha](../../../release-notes/mariadb-release-criteria.md) and very rarely during [Beta](../../../release-notes/mariadb-release-criteria.md) (it has to be a very critical bug to require such a change).
There are a few very rare cases when incompatible changes happen on a GA version, for example [MariaDB 10.1.21](../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10121-release-notes.md) fixed a file format incompatibility bug that prevents a downgrade to earlier [MariaDB 10.1](../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md) releases. After [MariaDB 10.1.21](../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10121-release-notes.md) this has not happened in a GA release.

The main reason why downgrades between major versions do not work are:

* Changes in the privilege/status tables in the [mysql schema](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md). These changes happen between most major versions as we are continuously improving the privilege system.
* Changes that affect how data is stored on disk. This happens more rarely and is usually table specific. For example, if one has used [Instant add column](../../reference/storage-engines/innodb/innodb-online-ddl/instant-add-column-for-innodb.md) on a table in [MariaDB 10.3](../../../release-notes/mariadb-community-server/what-is-mariadb-103.md), that table cannot be opened in [MariaDB 10.2](../../../release-notes/mariadb-community-server/what-is-mariadb-102.md).
* Between major releases there are often substantial changes, even if none of the new features are used. For example, both [MariaDB 10.2](../../../release-notes/mariadb-community-server/what-is-mariadb-102.md) and [MariaDB 10.3](../../../release-notes/mariadb-community-server/what-is-mariadb-103.md) introduce new versions of the redo log.

The only reliable way to downgrade is to [restore from a full backup](../backing-up-and-restoring-databases/README.md) made before upgrading, and start the old version of MariaDB. At least one should take a backup of the [mysql](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md) schema as most upgrade changes happens in this directory. This may be of help if one needs to downgrade to an earlier MariaDB version. More about this later.

Some people have reported successfully downgrading, but there are many possible things that can go wrong, and downgrading between two major versions is not tested in any way by the MariaDB developers.

In general, one can downgrade a major version to an earlier version if one has not yet run [mariadb-upgrade](../../clients-and-utilities/mariadb-upgrade.md) on the new version. Note however that it's recommended that one always uses [mariadb-upgrade](../../clients-and-utilities/mariadb-upgrade.md) after upgrading to a new major version as otherwise some security features in the new server may not work and tables that have indexes using a character collation that has changed may not work properly.

Assuming one **must** downgrade to an earlier major version, here is a list of things one has to do:

* MariaDB must be shut down cleanly. This means that:

  * One should ensure that [innodb_fast_shutdown≠2](../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown).
  * One uses the [SHUTDOWN](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/shutdown.md) command, [mariadb-admin shutdown](../../clients-and-utilities/mariadb-admin.md) or the operating system official commands, like [systemctl stop mariadb.service](starting-and-stopping-mariadb/systemd.md#stopping-the-mariadb-server-process).
* Start the old server with [--skip-privilege-tables](starting-and-stopping-mariadb/mariadbd-options.md#-skip-grant-tables).
* Use ALTER TABLE to restore the [mysql schema tables](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md) to their original definition or drop and recreate the mysql tables. One can find the old definition by using [mariadb-install-db](mariadb-install-db-exe.md) to create a separate temporary data directory. Starting the MariaDB server on the temporary directory will allow you to use [SHOW CREATE TABLE](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-table.md) to find the old definition.
* Execute [FLUSH PRIVILEGES](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) to reload the old tables.

The cases when the above will not work are when the table format has changed in an incompatible manner. In this case the affected tables may not be usable in the earlier version.

The following is an incomplete list of when one will not be able to use a table in an earlier major version:

* [MariaDB 11.0](../../../release-notes/mariadb-community-server/what-is-mariadb-110.md) or later

  * A downgrade to [MariaDB 10.4](../../../release-notes/mariadb-community-server/what-is-mariadb-104.md) or earlier is not possible, because [MDEV-29694](https://jira.mariadb.org/browse/MDEV-29694) removed the InnoDB change buffer.
  * A downgrade to [MariaDB 10.5](../../../release-notes/mariadb-community-server/what-is-mariadb-105.md) or later is only possible if [innodb_change_buffering=none](../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_change_buffering) (the default starting with [MDEV-27734](https://jira.mariadb.org/browse/MDEV-27734)).
* [MariaDB 10.8](../../../release-notes/mariadb-community-server/what-is-mariadb-108.md) or later

  * The InnoDB redo log file `ib_logfile0` would have to be replaced with a logically equivalent file, or the shutdown LSN has to be written to the `FIL_PAGE_FILE_FLUSH_LSN` field in the system tablespace (see [MDEV-27199](https://jira.mariadb.org/browse/MDEV-27199)), or the data may be accessed read-only when using [innodb_force_recovery=6](../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_force_recovery).
* [MariaDB 10.5](../../../release-notes/mariadb-community-server/what-is-mariadb-105.md) → [MariaDB 10.4](../../../release-notes/mariadb-community-server/what-is-mariadb-104.md)

  * The InnoDB redo log file `ib_logfile0` has to be deleted between a clean shutdown of the newer version and a startup of the older version. This is *not recommended*.
* [MariaDB 10.4](../../../release-notes/mariadb-community-server/what-is-mariadb-104.md) → [MariaDB 10.3](../../../release-notes/mariadb-community-server/what-is-mariadb-103.md)

  * Any InnoDB table where one has used `ALTER TABLE ALGORITHM=INSTANT DROP COLUMN` while [innodb_instant_alter_column_allowed=add_drop_reorder](../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_instant_alter_column_allowed)
  * Any InnoDB table that was created or rebuilt while [innodb_checksum_algorithm=full_crc32](../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm)
  * In [MariaDB 10.4](../../../release-notes/mariadb-community-server/what-is-mariadb-104.md), the MariaDB mysql.user table was replaced by [mysql.global_priv table](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-user-table.md) which may cause problems if ones wants to downgrade to 10.3.
* [MariaDB 10.3](../../../release-notes/mariadb-community-server/what-is-mariadb-103.md) → [MariaDB 10.2](../../../release-notes/mariadb-community-server/what-is-mariadb-102.md)

  * Any InnoDB table where one has used `ALTER TABLE…ADD COLUMN` (unless [innodb_instant_alter_column_allowed=never](../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_instant_alter_column_allowed)).
  * A prior shutdown with [innodb_fast_shutdown=0](../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown) will be needed in order to empty the undo logs whose format changed in [MDEV-12288](https://jira.mariadb.org/browse/MDEV-12288), and even then, you might need to set [innodb_force_recovery=3](../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_force_recovery).

