
# InnoDB Asynchronous I/O

From [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) uses asynchronous I/O to read from and write to disk asynchronously. This forms part of the InnoDB Background Thread Pool.


### Stages


Each asynchronous IO operation goes through multiple stages:


1. SUBMITTED – The IO operation is initiated.

  * For asynchronous writes, this typically occurs in the buffer pool flushing code.
  * For asynchronous reads, this may happen during buffer pool loading at startup or in prefetching logic.
1. COMPLETED_IN_OS – The operating system notifies InnoDB that the I/O operation is complete.

  * If using libaio or io_uring, a dedicated thread handles this notification.
  * The completed IO operation is then submitted to InnoDB’s internal thread pool (tpool).
1. EXECUTING_COMPLETION_TASK – A tpool thread processes the completion task for the IO operation.
1. COMPLETED – The IO operation is fully handled.


### Resource Constraints and Queuing Mechanisms


#### Waiting for IO Slots


The total number of pending asynchronous IO operations is limited by:


```
total_count = number_of_IO_threads * 256
```

where number_of_IO_threads refers to either [innodb_io_read_threads](innodb-system-variables.md#innodb_read_io_threads) or [innodb_io_write_threads](innodb-system-variables.md#innodb_write_io_threads).


Each IO operation is associated with an IO slot, which contains necessary metadata such as the file handle, operation type, offset, length, and any OS error codes. Initially, all total_count slots are free, but as pending IO requests accumulate, slots get occupied. If all slots are in use, additional IO requests must wait for a free slot.


#### Queuing Mechanism


The number of completion tasks (EXECUTING_COMPLETION_TASK stage) that can run in parallel is also limited by [innodb_io_read_threads](innodb-system-variables.md#innodb_read_io_threads) or [innodb_io_write_threads](innodb-system-variables.md#innodb_write_io_threads). If too many IO operations complete simultaneously, they cannot all be processed in parallel and must be queued, respecting the thread limit.


### Variables


From [MariaDB 11.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md), a number of status variables were added to give insight into the above operations:


* [innodb_async_reads_pending](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_reads_pending) – Number of read IO operations currently in progress (from SUBMITTED to COMPLETED).
* [innodb_async_reads_tasks_running](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_reads_tasks_running) – Number of read IO operations currently in the EXECUTING_COMPLETION_TASK state.
* [innodb_async_reads_total_count](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_reads_total_count) – Total number of read completion tasks that have finished execution.
* [innodb_async_reads_queue_size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_reads_queue_size) – Current size of the queue (see [Queuing Mechanism](#queuing-mechanism)).
* [innodb_async_reads_wait_slot_sec](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_reads_wait_slot_sec) – Total wait time for a free IO slot (see Waiting for IO Slots).
* [innodb_async_reads_total_enqueues](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_reads_total_enqueues) – Total number of read operations that were queued (see [Queuing Mechanism](#queuing-mechanism)). Includes those still waiting and making up `<code>innodb_async_reads_queue_size</code>`.


Similar variables exist for write operations:


* [innodb_async_writes_pending](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_writes_pending)
* [innodb_async_writes_tasks_running](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_writes_tasks_running)
* [innodb_async_reads_total_count](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_writes_total_count)
* [innodb_async_writes_queue_size](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_writes_queue_size)
* [innodb_async_writes_wait_slot_sec](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_writes_wait_slot_sec)
* [innodb_async_writes_total_enqueues](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_writes_total_enqueues)

