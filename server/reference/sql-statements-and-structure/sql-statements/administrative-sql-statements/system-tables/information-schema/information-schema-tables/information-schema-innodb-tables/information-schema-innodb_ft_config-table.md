# Information Schema INNODB_FT_CONFIG Table

The [Information Schema](/en/information_schema/) `INNODB_FT_CONFIG` table contains InnoDB [fulltext index](/en/full-text-indexes/) metadata.

The `SUPER` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table, and it also requires the [innodb_ft_aux_table](/en/xtradbinnodb-server-system-variables/#innodb_ft_aux_table) system variable to be set.

It has the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| KEY | Metadata item name. |
| VALUE | Associated value. |

#

# Example

```
SELECT * FROM INNODB_FT_CONFIG;
+---------------------------+-------+
| KEY | VALUE |
+---------------------------+-------+
| optimize_checkpoint_limit | 180 |
| synced_doc_id | 6 |
| last_optimized_word | |
| deleted_doc_count | 0 |
| total_word_count | |
| optimize_start_time | |
| optimize_end_time | |
| stopword_table_name | |
| use_stopword | 1 |
| table_state | 0 |
+---------------------------+-------+
```