
# Concurrent Inserts

The [MyISAM](../../../../storage-engines/myisam-storage-engine/myisam-system-variables.md) storage engine supports concurrent inserts. This feature allows [SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statements to be executed during [INSERT](../../built-in-functions/string-functions/insert-function.md) operations, reducing contention.


Whether concurrent inserts can be used or not depends on the value of the [concurrent_insert](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#concurrent_insert) server system variable:


* `NEVER` (0) disables concurrent inserts.
* `AUTO` (1) allows concurrent inserts only when the target table has no free blocks (no data in the middle of the table has been deleted after the last [OPTIMIZE TABLE](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/optimize-table.md)). This is the default.
* `ALWAYS` (2) always enables concurrent inserts, in which case new rows are added at the end of a table if the table is being used by another thread.


If the [binary log](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) is used, [CREATE TABLE ... SELECT](../../../vectors/create-table-with-vectors.md#create-table-select) and [INSERT ... SELECT](insert-select.md) statements cannot use concurrent inserts. These statements acquire a read lock on the table, so concurrent inserts will need to wait. This way the log can be safely used to restore data.


Concurrent inserts are not used by replicas with the row based [replication](../../administrative-sql-statements/replication-statements/README.md) (see [binary log formats](../../../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md)).


If an [INSERT](../../built-in-functions/string-functions/insert-function.md) statement contain the [HIGH_PRIORITY](../changing-deleting-data/high_priority-and-low_priority.md) clause, concurrent inserts cannot be used. [INSERT ... DELAYED](insert-delayed.md) is usually unneeded if concurrent inserts are enabled.


[LOAD DATA INFILE](load-data-into-tables-or-index/load-data-infile.md) uses concurrent inserts if the `CONCURRENT` keyword is specified and [concurrent_insert](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#concurrent_insert) is not `NEVER`. This makes the statement slower (even if no other sessions access the table) but reduces contention.


[LOCK TABLES](../../transactions/lock-tables.md) allows non-conflicting concurrent inserts if a `READ LOCAL` lock is used. Concurrent inserts are not allowed if the `LOCAL` keyword is omitted.


## Notes


The decision to enable concurrent insert for a table is done when the table is opened. If you change the value of [concurrent_insert](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#concurrent_insert) it will only affect new opened tables. If you want it to work for also for tables in use or cached, you should do [FLUSH TABLES](../../administrative-sql-statements/flush-commands/flush-tables-for-export.md) after setting the variable.


## See Also


* [INSERT](../../built-in-functions/string-functions/insert-function.md)
* [INSERT DELAYED](insert-delayed.md)
* [INSERT SELECT](insert-select.md)
* [HIGH_PRIORITY and LOW_PRIORITY](../changing-deleting-data/high_priority-and-low_priority.md)
* [INSERT - Default & Duplicate Values](insert-default-duplicate-values.md)
* [INSERT IGNORE](insert-ignore.md)
* [INSERT ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md)

