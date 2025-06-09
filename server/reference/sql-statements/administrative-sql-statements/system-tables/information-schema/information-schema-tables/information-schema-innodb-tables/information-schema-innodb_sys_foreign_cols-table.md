# Information Schema INNODB\_SYS\_FOREIGN\_COLS Table

The [Information Schema](../../) `INNODB_SYS_FOREIGN_COLS` table contains information about InnoDB [foreign key](../../../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) columns.

The `PROCESS` [privilege](../../../../../account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Column         | Description                                                                                                                                  |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Column         | Description                                                                                                                                  |
| ID             | Foreign key index associated with this column, matching the [INNODB\_SYS\_FOREIGN.ID](information-schema-innodb_sys_foreign-table.md) field. |
| FOR\_COL\_NAME | Child column name.                                                                                                                           |
| REF\_COL\_NAME | Parent column name.                                                                                                                          |
| POS            | Ordinal position of the column in the table, starting from 0.                                                                                |

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
