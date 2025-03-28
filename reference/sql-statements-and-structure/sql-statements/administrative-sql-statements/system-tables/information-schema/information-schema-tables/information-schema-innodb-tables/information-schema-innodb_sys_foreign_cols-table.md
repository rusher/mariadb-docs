# Information Schema INNODB_SYS_FOREIGN_COLS Table

The [Information Schema](/en/information_schema/) `INNODB_SYS_FOREIGN_COLS` table contains information about InnoDB [foreign key](../../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) columns.

The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.

It has the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| ID | Foreign key index associated with this column, matching the [INNODB_SYS_FOREIGN.ID](information-schema-innodb_sys_foreign-table.md) field. |
| FOR_COL_NAME | Child column name. |
| REF_COL_NAME | Parent column name. |
| POS | Ordinal position of the column in the table, starting from 0. |