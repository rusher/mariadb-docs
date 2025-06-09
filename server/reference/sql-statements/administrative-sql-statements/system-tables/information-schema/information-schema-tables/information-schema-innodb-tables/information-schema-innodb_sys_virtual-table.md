# Information Schema INNODB\_SYS\_VIRTUAL Table

The [Information Schema](../../) `INNODB_SYS_VIRTUAL` table contains information about base columns of [virtual columns](../../../../../data-definition/create/generated-columns.md). The `PROCESS` [privilege](../../../../../account-management-sql-statements/grant.md) is required to view the table.

It contains the following columns:

|           |                     |      |     |         |             |
| --------- | ------------------- | ---- | --- | ------- | ----------- |
| Field     | Type                | Null | Key | Default | Description |
| TABLE\_ID | bigint(21) unsigned | NO   |     | 0       |             |
| POS       | int(11) unsigned    | NO   |     | 0       |             |
| BASE\_POS | int(11) unsigned    | NO   |     | 0       |             |

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
