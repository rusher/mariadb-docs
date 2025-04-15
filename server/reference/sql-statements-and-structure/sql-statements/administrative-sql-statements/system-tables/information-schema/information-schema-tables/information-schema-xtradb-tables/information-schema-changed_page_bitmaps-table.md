
# Information Schema CHANGED_PAGE_BITMAPS Table

The [Information Schema](../../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>CHANGED_PAGE_BITMAPS</code>` table is a dummy table added to [XtraDB](../../../../../../../../server-usage/replication-cluster-multi-master/standard-replication/obsolete-replication-information/xtradb-option-innodb-release-locks-early.md) with reset_table callback to allow `<code>FLUSH NO_WRITE_TO_BINLOG CHANGED_PAGE_BITMAPS</code>` to be called from `<code>innobackupex</code>`. It contains only one column, *dummy*.


For more information, see [MDEV-7472](https://jira.mariadb.org/browse/MDEV-7472).


The `<code>PROCESS</code>` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.

