
# Information Schema INNODB_SYS_FIELDS Table

The [Information Schema](../../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>INNODB_SYS_FIELDS</code>` table contains information about fields that are part of an InnoDB index.


The `<code>PROCESS</code>` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


It has the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| INDEX_ID | Index identifier, matching the value from [INNODB_SYS_INDEXES.INDEX_ID](information-schema-innodb_sys_indexes-table.md). |
| NAME | Field name, matching the value from [INNODB_SYS_COLUMNS.NAME](information-schema-innodb_sys_columns-table.md). |
| POS | Ordinal position of the field within the index, starting from 0. This is adjusted as columns are removed. |



## Example


```
SELECT * FROM information_schema.INNODB_SYS_FIELDS LIMIT 3\G
*************************** 1. row ***************************
INDEX_ID: 11
    NAME: ID
     POS: 0
*************************** 2. row ***************************
INDEX_ID: 12
    NAME: FOR_NAME 
     POS: 0
*************************** 3. row ***************************
INDEX_ID: 13
    NAME: REF_NAME 
     POS: 0
3 rows in set (0.00 sec)
```
