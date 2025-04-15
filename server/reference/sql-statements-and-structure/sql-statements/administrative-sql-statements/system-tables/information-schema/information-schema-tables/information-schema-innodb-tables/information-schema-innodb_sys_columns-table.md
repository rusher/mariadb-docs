# Information Schema INNODB_SYS_COLUMNS Table

The [Information Schema](/en/information_schema/) `INNODB_SYS_COLUMNS` table contains information about InnoDB fields.

The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.

It has the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| TABLE_ID | Table identifier, matching the value from [INNODB_SYS_TABLES.TABLE_ID](information-schema-innodb_sys_tables-table.md). |
| NAME | Column name. |
| POS | Ordinal position of the column in the table, starting from 0. This value is adjusted when columns are added or removed. |
| MTYPE | Numeric column type identifier, (see the table below for an explanation of its values). |
| PRTYPE | Binary value of the InnoDB precise type, representing the data type, character set code and nullability. |
| LEN | Column length. For multi-byte character sets, represents the length in bytes. |

The column `MTYPE` uses a numeric column type identifier, which has the following values:

| Column Type Identifier | Description |
| --- | --- |
| Column Type Identifier | Description |
| 1 | [VARCHAR](../../../../../../../data-types/string-data-types/varchar.md) |
| 2 | [CHAR](../../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/charset-narrowing-optimization.md) |
| 3 | FIXBINARY |
| 4 | [BINARY](../../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) |
| 5 | [BLOB](../../../../../../../data-types/string-data-types/blob.md) |
| 6 | [INT](../../../../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/intvar_event.md) |
| 7 | SYS_CHILD |
| 8 | SYS |
| 9 | [FLOAT](../../../../../../../data-types/data-types-numeric-data-types/floating-point-accuracy.md) |
| 10 | [DOUBLE](../../../../../../../data-types/data-types-numeric-data-types/double.md) |
| 11 | [DECIMAL](../../../../../../../data-types/data-types-numeric-data-types/decimal.md) |
| 12 | VARMYSQL |
| 13 | MYSQL |

#

# Example

```
SELECT * FROM information_schema.INNODB_SYS_COLUMNS LIMIT 3\G
*************************** 1. row ***************************
TABLE_ID: 11
 NAME: ID
 POS: 0
 MTYPE: 1
 PRTYPE: 524292
 LEN: 0
*************************** 2. row ***************************
TABLE_ID: 11
 NAME: FOR_NAME 
 POS: 0
 MTYPE: 1
 PRTYPE: 524292
 LEN: 0
*************************** 3. row ***************************
TABLE_ID: 11
 NAME: REF_NAME 
 POS: 0
 MTYPE: 1
 PRTYPE: 524292
 LEN: 0
3 rows in set (0.00 sec)
```