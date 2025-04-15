
# InnoDB Redo Log


Directly editing or moving the redo logs can cause corruption, and should never normally be attempted.


## Overview


The redo log is used by [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) during crash recovery and background flushing of transactions to the tablespaces. The redo log files have names like `<code>ib_logfileN</code>`, where `<code>N</code>` is an integer. From [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), there is only one redo log, so the file will always be named `<code>ib_logfile0</code>`. If the [innodb_log_group_home_dir](innodb-system-variables.md#innodb_log_group_home_dir) system variable is configured, then the redo log files will be created in that directory. Otherwise, they will be created in the directory defined by the [datadir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir) system variable.


## Flushing Effects on Performance and Consistency


The [innodb_flush_log_at_trx_commit](innodb-system-variables.md#innodb_flush_log_at_trx_commit) system variable determines how often the transactions are flushed to the redo log, and it is important to achieve a good balance between speed and reliability.


### Binary Log Group Commit and Redo Log Flushing


When both [innodb_flush_log_at_trx_commit=1](innodb-system-variables.md#innodb_flush_log_at_trx_commit) (the default) is set and the [binary log](binary-log-group-commit-and-innodb-flushing-performance.md) is enabled, there is one less sync to disk inside InnoDB during commit (2 syncs shared between a group of transactions instead of 3). See [Binary Log Group Commit and InnoDB Flushing Performance](binary-log-group-commit-and-innodb-flushing-performance.md) for more information.


## Redo Log Group Capacity


The redo log group capacity is the total combined size of all InnoDB redo logs. The relevant factors are:


* From [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), there is 1 redo log.
* The size of each redo log file is configured by the [innodb_log_file_size](innodb-system-variables.md#innodb_log_file_size) system variable. This can safely be set to a much higher value from [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md). Before [MariaDB 10.9](../../../../release-notes/mariadb-community-server/what-is-mariadb-109.md), resizing required the server to be restarted. From [MariaDB 10.9](../../../../release-notes/mariadb-community-server/what-is-mariadb-109.md) the variable can be set dynamically.


The redo log group capacity is determined by the following calculation:


`<code>innodb_log_group_capacity</code>` = `<code>[innodb_log_file_size](innodb-system-variables.md#innodb_log_file_size)</code>` * `<code>[innodb_log_files_in_group](innodb-system-variables.md#innodb_log_files_in_group)</code>`


For example, if [innodb_log_file_size](innodb-system-variables.md#innodb_log_file_size) is set to `<code>2G</code>` and [innodb_log_files_in_group](innodb-system-variables.md#innodb_log_files_in_group) is set to `<code>2</code>`, then we would have the following:


* `<code>innodb_log_group_capacity</code>` = `<code>[innodb_log_file_size](innodb-system-variables.md#innodb_log_file_size)</code>` * `<code>[innodb_log_files_in_group](innodb-system-variables.md#innodb_log_files_in_group)</code>`
* = `<code>2G</code>` * `<code>2</code>`
* = `<code>4G</code>`


### Changing the Redo Log Group Capacity



##### MariaDB starting with [10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)
The number of redo log files is fixed.


The size of redo log files can be changed with the following process:


* Stop the server.
* To change the log file size, configure [innodb_log_file_size](innodb-system-variables.md#innodb_log_file_size).
* Start the server.


## Log Sequence Number (LSN)


Records within the InnoDB redo log are identified via a log sequence number (LSN).


## Checkpoints


When InnoDB performs a checkpoint, it writes the LSN of the oldest dirty page in the [InnoDB buffer pool](innodb-buffer-pool.md) to the InnoDB redo log. If a page is the oldest dirty page in the [InnoDB buffer pool](innodb-buffer-pool.md), then that means that all pages with lower LSNs have been flushed to the physical InnoDB tablespace files. If the server were to crash, then InnoDB would perform crash recovery by only applying log records with LSNs that are greater than or equal to the LSN of the oldest dirty page written in the last checkpoint.


Checkpoints are one of the tasks performed by the InnoDB master background thread. This thread schedules checkpoints 7 seconds apart when the server is very active, but checkpoints can happen more frequently when the server is less active.


Dirty pages are not actually flushed from the buffer pool to the physical InnoDB tablespace files during a checkpoint. That process happens asynchronously on a continuous basis by InnoDB's write I/O background threads configured by the [innodb_write_io_threads](innodb-system-variables.md#innodb_write_io_threads) system variable. If you want to make this process more aggressive, then you can decrease the value of the [innodb_max_dirty_pages_pct](innodb-system-variables.md#innodb_max_dirty_pages_pct) system variable. You may also need to better tune InnoDB's I/O capacity on your system by setting the [innodb_io_capacity](innodb-system-variables.md#innodb_io_capacity) system variable.


### Determining the Checkpoint Age


The checkpoint age is the amount of data written to the InnoDB redo log since the last checkpoint.


#### Determining the Checkpoint Age in InnoDB



##### MariaDB starting with [10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md)
[MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md) reintroduced the [Innodb_checkpoint_age](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_checkpoint_age) status variable for determining the checkpoint age.


The checkpoint age can also be determined by the process shown below.


To determine the InnoDB checkpoint age, do the following:


* Query [SHOW ENGINE INNODB STATUS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md).
* Find the `<code>LOG</code>` section. For example:


```
---
LOG
---
Log sequence number 252794398789379
Log flushed up to 252794398789379
Pages flushed up to 252792767756840
Last checkpoint at 252792767756840
0 pending log flushes, 0 pending chkp writes
23930412 log i/o's done, 2.03 log i/o's/second
```

* Perform the following calculation:


`<code>innodb_checkpoint_age</code>` = `<code>Log sequence number</code>` - `<code>Last checkpoint at</code>`


In the example above, that would be:


* `<code>innodb_checkpoint_age</code>` = `<code>Log sequence number</code>` - `<code>Last checkpoint at</code>`
* = 252794398789379 - 252792767756840
* = 1631032539 bytes
* = 1631032539 byes / (1024 * 1024 * 1024) (GB/bytes)
* = 1.5 GB of redo log written since last checkpoint


## Determining the Redo Log Occupancy


The redo log occupancy is the percentage of the InnoDB redo log capacity that is taken up by dirty pages that have not yet been flushed to the physical InnoDB tablespace files in a checkpoint. Therefore, it's determined by the following calculation:


`<code>innodb_log_occupancy</code>` = `<code>[innodb_checkpoint_age](#determining-the-checkpoint-age)</code>` / `<code>[innodb_log_group_capacity](#redo-log-group-capacity)</code>`


For example, if `<code>[innodb_checkpoint_age](#determining-the-checkpoint-age)</code>` is `<code>1.5G</code>` and `<code>[innodb_log_group_capacity](#redo-log-group-capacity)</code>` is `<code>4G</code>`, then we would have the following:


* `<code>innodb_log_occupancy</code>` = `<code>[innodb_checkpoint_age](#determining-the-checkpoint-age)</code>` / `<code>[innodb_log_group_capacity](#redo-log-group-capacity)</code>`
* = `<code>1.5G</code>` / `<code>4G</code>`
* = `<code>0.375</code>`


If the calculated value for redo log occupancy is too close to `<code>1.0</code>`, then the InnoDB redo log capacity may be too small for the current workload.


## [MariaDB 10.8](../../../../release-notes/mariadb-community-server/what-is-mariadb-108.md) Updates


A number of redo log improvements were made in [MariaDB 10.8](../../../../release-notes/mariadb-community-server/what-is-mariadb-108.md):


* Autosize innodb_buffer_pool_chunk_size ([MDEV-25342](https://jira.mariadb.org/browse/MDEV-25342)).
* Improve the redo log for concurrency ([MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425)).
* Remove FIL_PAGE_FILE_FLUSH_LSN ([MDEV-27199](https://jira.mariadb.org/browse/MDEV-27199)).


Before [MariaDB 10.8.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1081-release-notes.md), [mariadb-backup --prepare](../../../server-management/backing-up-and-restoring-databases/mariabackup/mariabackup-options.md#-prepare) created a zero-length ib_logfile0 as a dummy placeholder. From [MariaDB 10.8.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1081-release-notes.md) ([MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425)), the size of that dummy file was increased to 12304 (0x3010) bytes, and all updates of FIL_PAGE_FILE_FLUSH_LSN in the first page of the system tablespace are removed.


From [MariaDB 10.8.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1081-release-notes.md), if the server is started up with a zero-sized ib_logfile0, it is assumed that an upgrade is being performed after a backup had been prepared. The start LSN will then be read from FIL_PAGE_FILE_FLUSH_LSN, and a new log file will be created starting from exactly that LSN.


Manually creating a zero-sized ib_logfile0 without manually updating the FIL_PAGE_FILE_FLUSH_LSN in the system tablespace to a recent enough LSN may result in error messages such as "page LSN is in the future". If a log was discarded while some changes had already been written to data pages, all sort of corruption may occur.


If the database was initialized with a server that never updates the FIL_PAGE_FILE_FLUSH_LSN field, then any server startup attempts with a zero-size ib_logfile0 will be refused because of an invalid LSN. If that field was ever updated with a valid LSN by an older server, this safety mechanism cannot work, and the server may "rewind" to an earlier LSN.

