# BACKUP TABLE (removed)

BACKUP TABLE was removed and is no longer a part of MariaDB

#

# Syntax

```
BACKUP TABLE tbl_name [, tbl_name] ... TO '/path/to/backup/directory'
```

#

# Description

**Note:** Like [RESTORE TABLE](restore-table-removed.md), this command was not reliable and has been removed in current versions of MariaDB.

For doing a backup of MariaDB use [mysqldump](../../../../../clients-and-utilities/legacy-clients-and-utilities/mysqldumpslow.md) or [MariaDB Backup](../../../../../server-management/getting-installing-and-upgrading-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-sql-server/mariadb-backups-overview-for-sql-server-users.md). See [Backing Up and Restoring](/en/backing-up-and-restoring/).