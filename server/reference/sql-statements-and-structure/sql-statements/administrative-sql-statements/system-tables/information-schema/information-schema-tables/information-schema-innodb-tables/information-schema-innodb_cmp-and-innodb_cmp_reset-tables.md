
# Information Schema INNODB_CMP and INNODB_CMP_RESET Tables

The `<code>INNODB_CMP</code>` and `<code>INNODB_CMP_RESET</code>` tables contain status information on compression operations related to [compressed XtraDB/InnoDB tables](../../../../../../../storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md).


The `<code>[PROCESS](../../../../../account-management-sql-commands/grant.md#global-privileges)</code>` privilege is required to query this table.


These tables contain the following columns:



| Column Name | Description |
| --- | --- |
| Column Name | Description |
| PAGE_SIZE | Compressed page size, in bytes. This value is unique in the table; other values are totals which refer to pages of this size. |
| COMPRESS_OPS | How many times a page of the size PAGE_SIZE has been compressed. This happens when a new page is created because the compression log runs out of space. This value includes both successful operations and compression failures. |
| COMPRESS_OPS_OK | How many times a page of the size PAGE_SIZE has been successfully compressed. This value should be as close as possible to COMPRESS_OPS. If it is notably lower, either avoid compressing some tables, or increase the KEY_BLOCK_SIZE for some compressed tables. |
| COMPRESS_TIME | Time (in seconds) spent to compress pages of the size PAGE_SIZE. This value includes time spent in compression failures. |
| UNCOMPRESS_OPS | How many times a page of the size PAGE_SIZE has been uncompressed. This happens when an uncompressed version of a page is created in the buffer pool, or when a compression failure occurs. |
| UNCOMPRESS_TIME | Time (in seconds) spent to uncompress pages of the size PAGE_SIZE. |



These tables can be used to measure the effectiveness of XtraDB/InnoDB table compression. When you have to decide a value for `<code>KEY_BLOCK_SIZE</code>`, you can create more than one version of the table (one for each candidate value) and run a realistic workload on them. Then, these tables can be used to see how the operations performed with different page sizes.


`<code>INNODB_CMP</code>` and `<code>INNODB_CMP_RESET</code>` have the same columns and always contain the same values, but when `<code>INNODB_CMP_RESET</code>` is queried, both the tables are cleared. `<code>INNODB_CMP_RESET</code>` can be used, for example, if a script periodically logs the performances of compression in the last period of time. `<code>INNODB_CMP</code>` can be used to see the cumulated statistics.


## Examples


```
SELECT * FROM information_schema.INNODB_CMP\G
**************************** 1. row *****************************
      page_size: 1024
   compress_ops: 0
compress_ops_ok: 0
  compress_time: 0
 uncompress_ops: 0
uncompress_time: 0
...
```

## See Also


Other tables that can be used to monitor XtraDB/InnoDB compressed tables:


* [INNODB_CMP_PER_INDEX and INNODB_CMP_PER_INDEX_RESET](information-schema-innodb-tables-information-schema-innodb_cmp_per_index-an.md)
* [INNODB_CMPMEM and INNODB_CMPMEM_RESET](information-schema-innodb_cmpmem-and-innodb_cmpmem_reset-tables.md)

