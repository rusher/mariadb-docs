# Information Schema INNODB_BUFFER_POOL_PAGES_BLOB Table

The [Information Schema](/en/information_schema/) `INNODB_BUFFER_POOL_PAGES_BLOB` table is a Percona enchancement, and is only available for XtraDB, not InnoDB (see [XtraDB and InnoDB](/en/xtradb-and-innodb/)). It contains information about [buffer pool](/en/xtradbinnodb-memory-buffer/) blob pages.

It has the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| SPACE_ID | Tablespace ID. |
| PAGE_NO | Page offset within tablespace. |
| COMPRESSED | 1 if the blob contains compressed data, 0 if not. |
| PART_LEN | Page data length. |
| NEXT_PAGE_NO | Next page number. |
| LRU_POSITION | Page position in the LRU (least-recently-used) list. |
| FIX_COUNT | Page reference count, incremented each time the page is accessed. 0 if the page is not currently being accessed. |
| FLUSH_TYPE | Flush type of the most recent flush.0 (LRU), 2 (flush_list) |