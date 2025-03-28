# Information Schema INNODB_BUFFER_POOL_PAGES Table

The [Information Schema](/en/information_schema/) `INNODB_BUFFER_POOL_PAGES` table is a Percona enhancement, and is only available for XtraDB, not InnoDB (see [XtraDB and InnoDB](/en/xtradb-and-innodb/)). It contains a record for each page in the [buffer pool](/en/xtradbinnodb-memory-buffer/).

It has the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| PAGE_TYPE | Type of page; one of index, undo_log, inode, ibuf_free_list, allocated, bitmap, sys, trx_sys, fsp_hdr, xdes, blob, zblob, zblob2 and unknown. |
| SPACE_ID | Tablespace ID. |
| PAGE_NO | Page offset within tablespace. |
| LRU_POSITION | Page position in the LRU (least-recently-used) list. |
| FIX_COUNT | Page reference count, incremented each time the page is accessed. 0 if the page is not currently being accessed. |
| FLUSH_TYPE | Flush type of the most recent flush.0 (LRU), 2 (flush_list) |