
# InnoDB Recovery Modes

The InnoDB recovery mode is a mode used for recovering from emergency situations. You should ensure you have a backup of your database before making changes in case you need to restore it. The [innodb_force_recovery](../innodb-system-variables.md#innodb_force_recovery) server system variable sets the recovery mode. A mode of 0 is normal use, while the higher the mode, the more stringent the restrictions. Higher modes incorporate all limitations of the lower modes.


The recovery mode should never be set to a value other than zero except in an emergency situation.


Please note that recovery mode does not repair corruption. The corrupted files remain corrupted regardless of recovery mode. The sole purpose of recovery mode is to allow read access to the data, if at all possible.


Generally, it is best to start with a recovery mode of 1, and increase in single increments if needs be. With a recovery mode < 4, only corrupted pages should be lost. With 4, secondary indexes could be corrupted. With 5, results could be inconsistent and secondary indexes could be corrupted (even if they were not with 4). A value of 6 leaves pages in an obsolete state, which might cause more corruption.


Until [MariaDB 10.2.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1027-release-notes.md), mode `<code>0</code>` was the only mode permitting changes to the data. From [MariaDB 10.2.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1027-release-notes.md), write transactions are permitted with mode `<code>3</code>` or less.


To recover the tables, you can execute [SELECTs](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) to dump data, and [DROP TABLE](../../../sql-statements-and-structure/sql-statements/data-definition/drop/drop-tablespace.md) (when write transactions are permitted) to remove corrupted tables.


The following modes are available:


## Recovery Modes


Recovery mode behaviour differs per version (server/storage/innobase/include/srv0srv.h)


[MariaDB 10.4](../../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md) and before:



| Mode | Description |
| --- | --- |
| Mode | Description |
| 0 | The default mode while InnoDB is running normally. Until [MariaDB 10.2.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1027-release-notes.md), it was the only mode permitting changes to the data. From [MariaDB 10.2.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1027-release-notes.md), write transactions are permitted with innodb_force_recovery<=3. |
| 1 | (SRV_FORCE_IGNORE_CORRUPT) allows the the server to keep running even if corrupt pages are detected. It does so by making redo log based recovery ignore certain errors, such as missing data files or corrupted data pages. Any redo log for affected files or pages will be skipped. You can facilitate dumping tables by getting the SELECT * FROM table_name statement to jump over corrupt indexes and pages. |
| 2 | (SRV_FORCE_NO_BACKGROUND) stops the master thread from running, preventing a crash that occurs during a purge. No purge will be performed, so the undo logs will keep growing. |
| 3 | (SRV_FORCE_NO_TRX_UNDO) does not roll back transactions after the crash recovery. Does not affect rollback of currently active transactions. Starting with [MariaDB 10.2.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1027-release-notes.md), will also prevent some undo-generating background tasks from running. These tasks could hit a lock wait due to the recovered incomplete transactions whose rollback is being prevented. |
| 4 | (SRV_FORCE_NO_IBUF_MERGE) does not calculate tables statistics and prevents insert buffer merges. |
| 5 | (SRV_FORCE_NO_UNDO_LOG_SCAN) treats incomplete transactions as committed, and does not look at the [undo logs](../innodb-undo-log.md) when starting. |
| 6 | (SRV_FORCE_NO_LOG_REDO) does not perform redo log roll-forward as part of recovery. Running queries that require indexes are likely to fail with this mode active. However, if a table dump still causes a crash, you can try using a SELECT * FROM tab ORDER BY primary_key DESC to dump all the data portion after the corrupted part. |



From [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md) to [MariaDB 10.6.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1064-release-notes.md):



| Mode | Description |
| --- | --- |
| Mode | Description |
| 0 | The default mode while InnoDB is running normally. Write transactions are permitted with innodb_force_recovery<=4. |
| 1 | (SRV_FORCE_IGNORE_CORRUPT) allows the the server to keep running even if corrupt pages are detected. It does so by making redo log based recovery ignore certain errors, such as missing data files or corrupted data pages. Any redo log for affected files or pages will be skipped. You can facilitate dumping tables by getting the SELECT * FROM table_name statement to jump over corrupt indexes and pages. |
| 2 | (SRV_FORCE_NO_BACKGROUND) stops the master thread from running, preventing a crash that occurs during a purge. No purge will be performed, so the undo logs will keep growing. |
| 3 | (SRV_FORCE_NO_TRX_UNDO) does not roll back transactions after the crash recovery. Does not affect rollback of currently active transactions. Will also prevent some undo-generating background tasks from running. These tasks could hit a lock wait due to the recovered incomplete transactions whose rollback is being prevented. |
| 4 | (SRV_FORCE_NO_IBUF_MERGE) The same as 3. |
| 5 | (SRV_FORCE_NO_UNDO_LOG_SCAN) treats incomplete transactions as committed, and does not look at the [undo logs](../innodb-undo-log.md) when starting. |
| 6 | (SRV_FORCE_NO_LOG_REDO) does not perform redo log roll-forward as part of recovery. Running queries that require indexes are likely to fail with this mode active. However, if a table dump still causes a crash, you can try using a SELECT * FROM tab ORDER BY primary_key DESC to dump all the data portion after the corrupted part. |



From [MariaDB 10.6.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1065-release-notes.md)



| Mode | Description |
| --- | --- |
| Mode | Description |
| 0 | The default mode while InnoDB is running normally. Write transactions are permitted with innodb_force_recovery<=4. |
| 1 | (SRV_FORCE_IGNORE_CORRUPT) allows the the server to keep running even if corrupt pages are detected. It does so by making redo log based recovery ignore certain errors, such as missing data files or corrupted data pages. Any redo log for affected files or pages will be skipped. You can facilitate dumping tables by getting the SELECT * FROM table_name statement to jump over corrupt indexes and pages. |
| 2 | (SRV_FORCE_NO_BACKGROUND) stops the master thread from running, preventing a crash that occurs during a purge. No purge will be performed, so the undo logs will keep growing. |
| 3 | (SRV_FORCE_NO_TRX_UNDO) does not roll back DML transactions after the crash recovery. Does not affect rollback of currently active DML transactions. Will also prevent some undo-generating background tasks from running. These tasks could hit a lock wait due to the recovered incomplete transactions whose rollback is being prevented. |
| 4 | (SRV_FORCE_NO_DDL_UNDO) does not roll back transactions after the crash recovery. Does not affect rollback of currently active transactions. Will also prevent some undo-generating background tasks from running. These tasks could hit a lock wait due to the recovered incomplete transactions whose rollback is being prevented. |
| 5 | (SRV_FORCE_NO_UNDO_LOG_SCAN) treats incomplete transactions as committed, and does not look at the [undo logs](../innodb-undo-log.md) when starting. Any DDL log for InnoDB tables will be essentially ignored by InnoDB, but the server will start up |
| 6 | (SRV_FORCE_NO_LOG_REDO) does not perform redo log roll-forward as part of recovery. Running queries that require indexes are likely to fail with this mode active. However, if a table dump still causes a crash, you can try using a SELECT * FROM tab ORDER BY primary_key DESC to dump all the data portion after the corrupted part. |



Note also that XtraDB (<= [MariaDB 10.2.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1026-release-notes.md)) by default will crash the server when it detects corrupted data in a single-table tablespace. This behaviour can be changed - see the [innodb_corrupt_table_action](../innodb-system-variables.md) system variable.


## Fixing Things


Try to set innodb_force_recovery to 1 and start mariadb. If that fails, try a value of "2". If a value of 2 works, then there is a chance the only corruption you have experienced is within the innodb "undo logs". If that gets mariadb started, you should be able to dump your database with [mariadb-dump](../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md). You can verify any other issues with any tables by running [mariadb-check --all-databases](../../../../clients-and-utilities/mariadb-check.md).


If you were able to successfully dump your databases, or had previously known good backups, drop your database(s) from the mariadb command line like "[DROP DATABASE](../../../sql-statements-and-structure/sql-statements/data-definition/drop/drop-database.md) yourdatabase". Stop mariadb. Go to /var/lib/mysql (or whereever your mysql data directory is located) and "rm -i ib*". Start mariadb, create the database(s) you dropped ("[CREATE DATABASE](../../../sql-statements-and-structure/sql-statements/data-definition/create/create-database.md) yourdatabase"), and then import your most recent dumps: "mysql < mydatabasedump.sql"

