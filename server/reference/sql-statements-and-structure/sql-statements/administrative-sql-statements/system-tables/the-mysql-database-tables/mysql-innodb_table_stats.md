
# mysql.innodb_table_stats

The `<code>mysql.innodb_table_stats</code>` table stores data related to [InnoDB Persistent Statistics](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md), and contains one row per table.


This table, along with the related [mysql.innodb_index_stats](mysql-innodb_index_stats.md) table, can be manually updated in order to force or test differing query optimization plans. After updating, [FLUSH TABLE innodb_table_stats](../../flush-commands/flush-tables-for-export.md) is required to load the changes.


`<code>mysql.innodb_table_stats</code>` is not replicated, although any [ANALYZE TABLE](../../../table-statements/analyze-table.md) statements on the table will be by default.


It contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| database_name | varchar(64) | NO | PRI | NULL | Database name. |
| table_name | varchar(64) | NO | PRI | NULL | Table, partition or subpartition name. |
| last_update | timestamp | NO |  | current_timestamp() | Time that this row was last updated. |
| n_rows | bigint(20) unsigned | NO |  | NULL | Number of rows in the table. |
| clustered_index_size | bigint(20) unsigned | NO |  | NULL | Size, in pages, of the primary index. |
| sum_of_other_index_sizes | bigint(20) unsigned | NO |  | NULL | Size, in pages, of non-primary indexes. |



## Example


```
SELECT * FROM mysql.innodb_table_stats\G
*************************** 1. row ***************************
           database_name: mysql
              table_name: gtid_slave_pos
             last_update: 2017-08-19 20:38:34
                  n_rows: 0
    clustered_index_size: 1
sum_of_other_index_sizes: 0
*************************** 2. row ***************************
           database_name: test
              table_name: ft
             last_update: 2017-09-15 12:58:39
                  n_rows: 0
    clustered_index_size: 1
sum_of_other_index_sizes: 2
...
```

## See Also


* [InnoDB Persistent Statistics](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md)
* [mysql.innodb_index_stats](mysql-innodb_index_stats.md)
* [ANALYZE TABLE](../../../table-statements/analyze-table.md)

