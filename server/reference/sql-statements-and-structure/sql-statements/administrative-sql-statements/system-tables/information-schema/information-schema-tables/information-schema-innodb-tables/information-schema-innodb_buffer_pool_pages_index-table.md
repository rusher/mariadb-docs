
# Information Schema INNODB_BUFFER_POOL_PAGES_INDEX Table

The [Information Schema](../../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `INNODB_BUFFER_POOL_PAGES` table is a Percona enhancement, and is only available for XtraDB, not InnoDB (see [XtraDB and InnoDB](../../../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md)). It contains information about [buffer pool](../../../../../../../storage-engines/innodb/innodb-buffer-pool.md) index pages.


It has the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| INDEX_ID | Index name |
| SPACE_ID | Tablespace ID |
| PAGE_NO | Page offset within tablespace. |
| N_RECS | Number of user records on the page. |
| DATA_SIZE | Total data size in bytes of records in the page. |
| HASHED | 1 if the block is in the adaptive hash index, 0 if not. |
| ACCESS_TIME | Page's last access time. |
| MODIFIED | 1 if the page has been modified since being loaded, 0 if not. |
| DIRTY | 1 if the page has been modified since it was last flushed, 0 if not |
| OLD | 1 if the page in the in the old blocks of the LRU (least-recently-used) list, 0 if not. |
| LRU_POSITION | Position in the LRU (least-recently-used) list. |
| FIX_COUNT | Page reference count, incremented each time the page is accessed. 0 if the page is not currently being accessed. |
| FLUSH_TYPE | Flush type of the most recent flush.0 (LRU), 2 (flush_list) |


