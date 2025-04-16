
# Information Schema INNODB_BUFFER_PAGE Table

The [Information Schema](../../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `INNODB_BUFFER_PAGE` table contains information about pages in the [buffer pool](../../../../../../../storage-engines/innodb/innodb-buffer-pool.md).


Querying this table can have a noticeable performance impact on a production server.


The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


It has the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| POOL_ID | Buffer Pool identifier. From [MariaDB 10.5.1](../../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1051-release-notes.md) returns a value of 0, since multiple InnoDB buffer pool instances has been removed. |
| BLOCK_ID | Buffer Pool Block identifier. |
| SPACE | Tablespace identifier. Matches the SPACE value in the [INNODB_SYS_TABLES](information-schema-innodb_sys_tables-table.md) table. |
| PAGE_NUMBER | Buffer pool page number. |
| PAGE_TYPE | Page type; one of allocated (newly-allocated page), index (B-tree node), undo_log (undo log page), inode (index node), ibuf_free_list (insert buffer free list), ibuf_bitmap (insert buffer bitmap), system (system page), trx_system (transaction system data), file_space_header (file space header), extent_descriptor (extent descriptor page), blob (uncompressed blob page), compressed_blob (first compressed blob page), compressed_blob2 (subsequent compressed blob page) or unknown. |
| FLUSH_TYPE | Flush type. |
| FIX_COUNT | Count of the threads using this block in the buffer pool. When it is zero, the block can be evicted from the buffer pool. |
| IS_HASHED | Whether or not a hash index has been built on this page. |
| NEWEST_MODIFICATION | Most recent modification's Log Sequence Number. |
| OLDEST_MODIFICATION | Oldest modification's Log Sequence Number. |
| ACCESS_TIME | Abstract number representing the time the page was first accessed. |
| TABLE_NAME | Table that the page belongs to. |
| INDEX_NAME | Index that the page belongs to, either a clustered index or a secondary index. |
| NUMBER_RECORDS | Number of records the page contains. |
| DATA_SIZE | Size in bytes of all the records contained in the page. |
| COMPRESSED_SIZE | Compressed size in bytes of the page, or NULL for pages that aren't compressed. |
| PAGE_STATE | Page state; one of FILE_PAGE (page from a file) or MEMORY (page from an in-memory object) for valid data, or one of NULL, READY_FOR_USE, NOT_USED, REMOVE_HASH. |
| IO_FIX | Whether there is I/O pending for the page; one of IO_NONE (no pending I/O), IO_READ (read pending), IO_WRITE (write pending). |
| IS_OLD | Whether the page is old or not. |
| FREE_PAGE_CLOCK | Freed_page_clock counter, which tracks the number of blocks removed from the end of the least recently used (LRU) list, at the time the block was last placed at the head of the list. |



The related [INFORMATION_SCHEMA.INNODB_BUFFER_PAGE_LRU](information-schema-innodb_buffer_page_lru-table.md) table contains the same information, but with an LRU (least recently used) position rather than block id.


## Examples


```
DESC information_schema.innodb_buffer_page;
+---------------------+---------------------+------+-----+---------+-------+
| Field               | Type                | Null | Key | Default | Extra |
+---------------------+---------------------+------+-----+---------+-------+
| POOL_ID             | bigint(21) unsigned | NO   |     | 0       |       |
| BLOCK_ID            | bigint(21) unsigned | NO   |     | 0       |       |
| SPACE               | bigint(21) unsigned | NO   |     | 0       |       |
| PAGE_NUMBER         | bigint(21) unsigned | NO   |     | 0       |       |
| PAGE_TYPE           | varchar(64)         | YES  |     | NULL    |       |
| FLUSH_TYPE          | bigint(21) unsigned | NO   |     | 0       |       |
| FIX_COUNT           | bigint(21) unsigned | NO   |     | 0       |       |
| IS_HASHED           | varchar(3)          | YES  |     | NULL    |       |
| NEWEST_MODIFICATION | bigint(21) unsigned | NO   |     | 0       |       |
| OLDEST_MODIFICATION | bigint(21) unsigned | NO   |     | 0       |       |
| ACCESS_TIME         | bigint(21) unsigned | NO   |     | 0       |       |
| TABLE_NAME          | varchar(1024)       | YES  |     | NULL    |       |
| INDEX_NAME          | varchar(1024)       | YES  |     | NULL    |       |
| NUMBER_RECORDS      | bigint(21) unsigned | NO   |     | 0       |       |
| DATA_SIZE           | bigint(21) unsigned | NO   |     | 0       |       |
| COMPRESSED_SIZE     | bigint(21) unsigned | NO   |     | 0       |       |
| PAGE_STATE          | varchar(64)         | YES  |     | NULL    |       |
| IO_FIX              | varchar(64)         | YES  |     | NULL    |       |
| IS_OLD              | varchar(3)          | YES  |     | NULL    |       |
| FREE_PAGE_CLOCK     | bigint(21) unsigned | NO   |     | 0       |       |
+---------------------+---------------------+------+-----+---------+-------+
```

```
SELECT * FROM INFORMATION_SCHEMA.INNODB_BUFFER_PAGE\G
...
*************************** 6. row ***************************
            POOL_ID: 0
           BLOCK_ID: 5
              SPACE: 0
        PAGE_NUMBER: 11
          PAGE_TYPE: INDEX
         FLUSH_TYPE: 1
          FIX_COUNT: 0
          IS_HASHED: NO
NEWEST_MODIFICATION: 2046835
OLDEST_MODIFICATION: 0
        ACCESS_TIME: 2585566280
         TABLE_NAME: `SYS_INDEXES`
         INDEX_NAME: CLUST_IND
     NUMBER_RECORDS: 57
          DATA_SIZE: 4016
    COMPRESSED_SIZE: 0
         PAGE_STATE: FILE_PAGE
             IO_FIX: IO_NONE
             IS_OLD: NO
    FREE_PAGE_CLOCK: 0
...
```

## See Also


* [InnoDB Buffer Pool](../../../../../../../storage-engines/innodb/innodb-buffer-pool.md)
* [innodb_buffer_stats_by_schema and x$innodb_buffer_stats_by_schema Sys Schema Views](https://mariadb.com/kb/en/sys-schema-views-innodb_buffer_stats_by_schema-and-xinnodb_buffer_stats_by_/)

