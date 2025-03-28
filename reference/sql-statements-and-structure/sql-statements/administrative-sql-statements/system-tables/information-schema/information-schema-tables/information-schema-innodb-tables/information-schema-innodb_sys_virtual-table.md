# Information Schema INNODB_SYS_VIRTUAL Table

The [Information Schema](/en/information_schema/) `INNODB_SYS_VIRTUAL` table contains information about base columns of [virtual columns](../../../../../data-definition/create/generated-columns.md). The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.

It contains the following columns:

| Field | Type | Null | Key | Default | Description |
| TABLE_ID | bigint(21) unsigned | NO | | 0 | |
| POS | int(11) unsigned | NO | | 0 | |
| BASE_POS | int(11) unsigned | NO | | 0 | |