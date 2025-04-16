
# HIGH_PRIORITY and LOW_PRIORITY

The [InnoDB](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) storage engine uses row-level locking to ensure data integrity. However some storage engines (such as [MEMORY](../../../../storage-engines/memory-storage-engine.md), [MyISAM](../../../../storage-engines/myisam-storage-engine/myisam-system-variables.md), [Aria](../../../../storage-engines/s3-storage-engine/aria_s3_copy.md) and [MERGE](../../../../storage-engines/merge.md)) lock the whole table to prevent conflicts. These storage engines use two separate queues to remember pending statements; one is for [SELECTs](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) and the other one is for write statements ([INSERT](../../built-in-functions/string-functions/insert-function.md), [DELETE](delete.md), [UPDATE](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md)). By default, the latter has a higher priority.


To give write operations a lower priority, the [low_priority_updates](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#low_priority_updates) server system variable can be set to `ON`. The option is available on both the global and session levels, and it can be set at startup or via the [SET](../../../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md) statement.


When too many table locks have been set by write statements, some pending SELECTs are executed. The maximum number of write locks that can be acquired before this happens is determined by the [max_write_lock_count](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_write_lock_count) server system variable, which is dynamic.


If write statements have a higher priority (default), the priority of individual write statements ([INSERT](../../built-in-functions/string-functions/insert-function.md), [REPLACE](../../built-in-functions/string-functions/replace-function.md), [UPDATE](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md), [DELETE](delete.md)) can be changed via the `LOW_PRIORITY` attribute, and the priority of a `SELECT` statement can be raised via the `HIGH_PRIORITY` attribute. Also, [LOCK TABLES](../../transactions/lock-tables.md) supports a `LOW_PRIORITY` attribute for `WRITE` locks.


If read statements have a higher priority, the priority of an `INSERT` can be changed via the `HIGH_PRIORITY` attribute. However, the priority of other write statements cannot be raised individually.


The use of `LOW_PRIORITY` or `HIGH_PRIORITY` for an `INSERT` prevents [Concurrent Inserts](../inserting-loading-data/concurrent-inserts.md) from being used.


## See Also


* [INSERT](../../built-in-functions/string-functions/insert-function.md)
* [INSERT DELAYED](../inserting-loading-data/insert-delayed.md)
* [INSERT SELECT](../inserting-loading-data/insert-select.md)
* [Concurrent Inserts](../inserting-loading-data/concurrent-inserts.md)
* [INSERT - Default & Duplicate Values](../inserting-loading-data/insert-default-duplicate-values.md)
* [INSERT IGNORE](../inserting-loading-data/insert-ignore.md)
* [INSERT ON DUPLICATE KEY UPDATE](../inserting-loading-data/insert-on-duplicate-key-update.md)

