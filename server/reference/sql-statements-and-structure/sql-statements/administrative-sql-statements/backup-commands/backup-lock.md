
# BACKUP LOCK


BACKUP LOCK blocks a table from DDL statements. This is mainly intended to be used by tools like [mariabackup](../../../../../server-management/backing-up-and-restoring-databases/mariabackup/mariabackup-and-backup-stage-commands.md) that need to ensure there are no DDLs on a table while the table files are opened. For example, for an Aria table that stores data in 3 files with extensions .frm, .MAI and .MAD.
Normal read/write operations can continue as normal.


## Syntax


To lock a table:


```
BACKUP LOCK table_name
```

To unlock a table:


```
BACKUP UNLOCK
```

## Usage in a Backup Tool


```
BACKUP LOCK [database.]table_name;
 - Open all files related to a table (for example, t.frm, t.MAI and t.MYD)
BACKUP UNLOCK;
- Copy data
- Close files
```

This ensures that all files are from the same generation, that is created at the same time by the MariaDB server.
This works, because the open files will point to the original table files which will not be affected if there is
any ALTER TABLE while copying the files.


## Privileges


Prior to [MariaDB 10.5.24](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10-5-24-release-notes.md), [MariaDB 10.6.17](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md), [MariaDB 10.11.7](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md), [MariaDB 11.0.5](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes.md), [MariaDB 11.1.4](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes.md), [MariaDB 11.2.3](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes.md), [MariaDB 11.3.2](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes.md) and [MariaDB 11.4.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-1-release-notes.md), BACKUP LOCK requires the [RELOAD](../../account-management-sql-commands/grant.md#reload) privilege.


From [MariaDB 10.5.24](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10-5-24-release-notes.md), [MariaDB 10.6.17](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md), [MariaDB 10.11.7](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md), [MariaDB 11.0.5](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes.md), [MariaDB 11.1.4](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes.md), [MariaDB 11.2.3](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes.md), [MariaDB 11.3.2](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes.md) and [MariaDB 11.4.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-1-release-notes.md), BACKUP LOCK is also accessible to those with [database LOCK TABLES](../../account-management-sql-commands/grant.md#database-privileges) privileges.


## Notes


* The idea is that the `<code>BACKUP LOCK</code>` should be held for as short a time as possible by the backup tool. The time to take an uncontested lock is very short! One can easily do 50,000 locks/unlocks per second on low end hardware.
* One should use different connections for [BACKUP STAGE](backup-stage.md) commands and `<code>BACKUP LOCK</code>`.


## Implementation


* Internally, BACKUP LOCK is implemented by taking an `<code>MDLSHARED_HIGH_PRIO</code>` MDL lock on the table object, which protects the table from any DDL operations.


## See Also


* [BACKUP STAGE](backup-stage.md)
* [MDEV-17309](https://jira.mariadb.org/browse/MDEV-17309) - BACKUP LOCK: DDL locking of tables during backup

