
# Information Schema INNODB_SYS_VIRTUAL Table

The [Information Schema](../../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>INNODB_SYS_VIRTUAL</code>` table contains information about base columns of [virtual columns](../../../../../data-definition/create/generated-columns.md). The `<code>PROCESS</code>` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


It contains the following columns:



|   |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| TABLE_ID | bigint(21) unsigned | NO |  | 0 |  |
| POS | int(11) unsigned | NO |  | 0 |  |
| BASE_POS | int(11) unsigned | NO |  | 0 |  |


