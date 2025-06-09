# Information Schema INNODB\_SYS\_FOREIGN Table

The [Information Schema](../../) `INNODB_SYS_FOREIGN` table contains information about InnoDB [foreign keys](../../../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md).

The `PROCESS` [privilege](../../../../../account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Column    | Description                                           |
| --------- | ----------------------------------------------------- |
| Column    | Description                                           |
| ID        | Database name and foreign key name.                   |
| FOR\_NAME | Database and table name of the foreign key child.     |
| REF\_NAME | Database and table name of the foreign key parent.    |
| N\_COLS   | Number of foreign key index columns.                  |
| TYPE      | Bit flag providing information about the foreign key. |

The `TYPE` column provides a bit flag with information about the foreign key. This information is `OR`'ed together to read:

| Bit Flag | Description         |
| -------- | ------------------- |
| Bit Flag | Description         |
| 1        | ON DELETE CASCADE   |
| 2        | ON UPDATE SET NULL  |
| 4        | ON UPDATE CASCADE   |
| 8        | ON UPDATE SET NULL  |
| 16       | ON DELETE NO ACTION |
| 32       | ON UPDATE NO ACTION |

## Example

```
SELECT * FROM INNODB_SYS_FOREIGN\G
*************************** 1. row ***************************
      ID: mysql/innodb_index_stats_ibfk_1
FOR_NAME: mysql/innodb_index_stats
REF_NAME: mysql/innodb_table_stats
  N_COLS: 2
    TYPE: 0
...
```

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
