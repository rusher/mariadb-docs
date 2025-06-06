# mariadb-enterprise-server-innodb-operations

## MariaDB Enterprise Server InnoDB Operations

## Overview

| Operation                                                                                                                                                        | Description                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Operation                                                                                                                                                        | Description                                                                                   |
| [Configure the Buffer Pool](configure-the-innodb-buffer-pool.md)                                                                                                 | An in-memory cache that is used to improve the performance of queries against InnoDB tables.  |
| [Configure the I/O Threads](configure-the-innodb-io-threads.md)                                                                                                  | Read pages from disk into the buffer pool and flush dirty pages from the buffer pool to disk. |
| [Configure InnoDB Page Compression](../../../../reference/storage-engines/innodb/mariadb-enterprise-server-innodb-operations/configure-innodb-page-compression/) | InnoDB supports table compression using InnoDB Page Compression.                              |
| [Configure the Purge Threads](configure-the-innodb-purge-threads.md)                                                                                             | Perform garbage collection of undo log.                                                       |
| [Configure the Redo Log](configure-the-innodb-redo-log.md)                                                                                                       | Transaction log for durability.                                                               |
| [Configure the Undo Log](configure-the-innodb-undo-log.md)                                                                                                       | Transaction log for MVCC.                                                                     |
| [Schema Changes](schema-changes/)                                                                                                                                | Changing table schemas using DDL.                                                             |
