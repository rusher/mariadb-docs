# InnoDB Architecture for MariaDB Enterprise Server

## Overview

| Component                                                                                                            | Description                                                                                   |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Component                                                                                                            | Description                                                                                   |
| [Background Thread Pool](mariadb-enterprise-server-innodb-background-thread-pool.md)                                 | An internal thread pool used by InnoDB to perform tasks in the background.                    |
| [Buffer Pool](https://mariadb.com/kb/en/mariadb-enterprise-server-innodb-buffer-pool)                                | An in-memory cache that is used to improve performance of queries against InnoDB tables.      |
| [I/O Threads](mariadb-enterprise-server-innodb-io-threads.md)                                                        | Read pages from disk into the buffer pool and flush dirty pages from the buffer pool to disk. |
| [Purge Threads](https://mariadb.com/kb/en/mariadb-enterprise-server-innodb-purge-threads)                            | Perform garbage collection of undo log.                                                       |
| [Redo Log](https://mariadb.com/kb/en/mariadb-enterprise-server-innodb-redo-log)                                      | Transaction log for durability.                                                               |
| [Row Formats](https://mariadb.com/kb/en/innodb-architecture-for-mariadb-enterprise-server-mariadb-enterprise-server) | The format used for data on disk.                                                             |
| [Undo Log](mariadb-enterprise-server-innodb-undo-log/)                                                               | Transaction log for MVCC.                                                                     |
