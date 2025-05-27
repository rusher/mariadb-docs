# Information Schema INNODB\_FT\_CONFIG Table

The [Information Schema](../../) `INNODB_FT_CONFIG` table contains InnoDB [fulltext index](../../../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) metadata.

The `SUPER` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table, and it also requires the [innodb\_ft\_aux\_table](../../../../../../storage-engines/innodb/innodb-system-variables.md) system variable to be set.

It has the following columns:

| Column | Description         |
| ------ | ------------------- |
| Column | Description         |
| KEY    | Metadata item name. |
| VALUE  | Associated value.   |

## Example

```
SELECT * FROM INNODB_FT_CONFIG;
+---------------------------+-------+
| KEY                       | VALUE |
+---------------------------+-------+
| optimize_checkpoint_limit | 180   |
| synced_doc_id             | 6     |
| last_optimized_word       |       |
| deleted_doc_count         | 0     |
| total_word_count          |       |
| optimize_start_time       |       |
| optimize_end_time         |       |
| stopword_table_name       |       |
| use_stopword              | 1     |
| table_state               | 0     |
+---------------------------+-------+
```

CC BY-SA / Gnu FDL
