
# Read-Only Replicas

A common [replication](README.md) setup is to have the replicas
[read-only](../optimization-and-tuning/system-variables/server-system-variables.md#read_only) to ensure that no one
accidentally updates them. If the replica has [binary logging enabled](setting-up-replication.md) and [gtid_strict_mode](gtid.md#gtid_strict_mode) is used, then any update that causes changes to the [binary log](../../../server-management/server-monitoring-logs/binary-log/README.md) will stop replication.


When the variable `read_only` is set to 1, no updates are permitted except from users with the [SUPER](../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#super) privilege (<= [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes)) or [READ ONLY ADMIN](../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#read_only-admin) privilege (>= [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)) or replica servers updating from a primary. Inserting rows to log tables, updates to temporary tables and [OPTIMIZE TABLE](../optimization-and-tuning/optimizing-tables/optimize-table.md) or [ANALYZE TABLE](../../../reference/sql-statements-and-structure/sql-statements/table-statements/analyze-table.md) statements on temporary tables are excluded from this limitation.


If read_only is set to 1, then the [SET PASSWORD](../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/set-password.md) statement is limited only to users with the [SUPER](../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#super) privilege (<= [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes)) or [READ ONLY ADMIN](../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#read_only-admin) privilege (>= [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)).


Attempting to set the `read_only` variable to 1 will fail if the current session has table locks or transactions pending.


The statement will wait for other sessions that hold table locks. While the attempt to set read_only is waiting, other requests for table locks or transactions will also wait until read_only has been set.


From [MariaDB 10.3.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10319-release-notes), some issues related to read only replicas are fixed:


* [CREATE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-table.md), [DROP](../../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-table.md), [ALTER](../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md), [INSERT](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert.md) and [DELETE](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/delete.md) of temporary tables are not logged to binary log, even in [statement](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging) or [mixed](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#mixed-logging) mode. With earlier MariaDB versions, one can avoid the problem with temporary tables by using [binlog_format=ROW](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#row-based-logging) in which cases temporary tables are never logged.
* Changes to temporary tables created during `read_only` will not be logged even after `read_only` mode is disabled (for example if the replica is promoted to a primary).
* The admin statements [ANALYZE](../../../reference/sql-statements-and-structure/sql-statements/table-statements/analyze-table.md), [CHECK](../../../reference/sql-statements-and-structure/sql-statements/table-statements/check-table.md), [OPTIMIZE](../optimization-and-tuning/optimizing-tables/optimize-table.md) and [REPAIR](../../../reference/sql-statements-and-structure/sql-statements/table-statements/repair-table.md) will not be logged to the binary log under read-only.


### Older MariaDB Versions


If you are using an older MariaDB version with read-only replicas and binary logging enabled on the replica, and you need to do some changes but don't want to have them logged to the binary log, the easiest way to avoid the logging is to [disable binary logging](../../../server-management/server-monitoring-logs/binary-log/activating-the-binary-log.md) while running as root during maintenance:


```
set sql_log_bin=0;
alter table test engine=rocksdb;
```

The above changes the test table on the replica to rocksdb without registering
the change in the binary log.

