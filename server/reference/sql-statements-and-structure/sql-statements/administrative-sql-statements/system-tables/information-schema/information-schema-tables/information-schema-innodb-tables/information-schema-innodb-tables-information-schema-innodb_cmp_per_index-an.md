
# Information Schema INNODB_CMP_PER_INDEX and INNODB_CMP_PER_INDEX_RESET Tables

The `INNODB_CMP_PER_INDEX` and `INNODB_CMP_PER_INDEX_RESET` tables contain status information on compression operations related to [compressed XtraDB/InnoDB tables](../../../../../../../storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md), grouped by individual indexes. These tables are only populated if the [innodb_cmp_per_index_enabled](../../../../../../../storage-engines/innodb/innodb-system-variables.md#innodb_cmp_per_index_enabled) system variable is set to `ON`.


The [PROCESS](../../../../../account-management-sql-commands/grant.md#global-privileges) privilege is required to query this table.


These tables contains the following columns:



| Column Name | Description |
| --- | --- |
| Column Name | Description |
| DATABASE_NAME | Database containing the index. |
| TABLE_NAME | Table containing the index. |
| INDEX_NAME | Other values are totals which refer to this index's compression. |
| COMPRESS_OPS | How many times a page of INDEX_NAME has been compressed. This happens when a new page is created because the compression log runs out of space. This value includes both successful operations and compression failures. |
| COMPRESS_OPS_OK | How many times a page of INDEX_NAME has been successfully compressed. This value should be as close as possible to COMPRESS_OPS. If it is notably lower, either avoid compressing some tables, or increase the KEY_BLOCK_SIZE for some compressed tables. |
| COMPRESS_TIME | Time (in seconds) spent to compress pages of the size PAGE_SIZE. This value includes time spent in compression failures. |
| UNCOMPRESS_OPS | How many times a page of INDEX_NAME has been uncompressed. This happens when an uncompressed version of a page is created in the buffer pool, or when a compression failure occurs. |
| UNCOMPRESS_TIME | Time (in seconds) spent to uncompress pages of INDEX_NAME. |



These tables can be used to measure the effectiveness of XtraDB/InnoDB compression, per table or per index. The values in these tables show which tables perform better with index compression, and which tables cause too many *compression failures* or perform too many compression/uncompression operations. When compression performs badly for a table, this might mean that you should change its `KEY_BLOCK_SIZE`, or that the table should not be compressed.


`INNODB_CMP_PER_INDEX` and `INNODB_CMP_PER_INDEX_RESET` have the same columns and always contain the same values, but when `INNODB_CMP_PER_INDEX_RESET` is queried, both the tables are cleared. `INNODB_CMP_PER_INDEX_RESET` can be used, for example, if a script periodically logs the performances of compression in the last period of time. `INNODB_CMP_PER_INDEX` can be used to see the cumulated statistics.


## See Also


Other tables that can be used to monitor XtraDB/InnoDB compressed tables:


* [INNODB_CMP and INNODB_CMP_RESET](information-schema-innodb_cmp-and-innodb_cmp_reset-tables.md)
* [INNODB_CMPMEM and INNODB_CMPMEM_RESET](information-schema-innodb_cmpmem-and-innodb_cmpmem_reset-tables.md)


CC BY-SA / Gnu FDL

