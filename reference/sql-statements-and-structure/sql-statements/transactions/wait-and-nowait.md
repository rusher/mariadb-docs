# WAIT and NOWAIT

Extended syntax so that it is possible to set [innodb_lock_wait_timeout](../../../storage-engines/innodb/innodb-system-variables.md#innodb_lock_wait_timeout) and [lock_wait_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lock_wait_timeout) for the following statements:

#

# Syntax

```
ALTER TABLE tbl_name [WAIT n|NOWAIT] ...
CREATE ... INDEX ON tbl_name (index_col_name, ...) [WAIT n|NOWAIT] ...
DROP INDEX ... [WAIT n|NOWAIT]
DROP TABLE tbl_name [WAIT n|NOWAIT] ...
LOCK TABLE ... [WAIT n|NOWAIT]
OPTIMIZE TABLE tbl_name [WAIT n|NOWAIT]
RENAME TABLE tbl_name [WAIT n|NOWAIT] ...
SELECT ... FOR UPDATE [WAIT n|NOWAIT]
SELECT ... LOCK IN SHARE MODE [WAIT n|NOWAIT]
TRUNCATE TABLE tbl_name [WAIT n|NOWAIT]
```

#

# Description

The lock wait timeout can be explicitly set in the statement by using either `WAIT n` (to set the wait in seconds) or `NOWAIT`, in which case the statement will immediately fail if the lock cannot be obtained. `WAIT 0` is equivalent to `NOWAIT`.

#

# See Also

* [Query Limits and Timeouts](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/query-limits-and-timeouts.md)
* [ALTER TABLE](../data-definition/alter/alter-table.md)
* [CREATE INDEX](../data-definition/create/create-index.md)
* [DROP INDEX](../data-definition/drop/drop-index.md)
* [DROP TABLE](../data-definition/drop/drop-tablespace.md)
* [LOCK TABLES and UNLOCK TABLES](/en/lock-tables-and-unlock-tables/)
* [OPTIMIZE TABLE](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/optimize-table.md)
* [RENAME TABLE](../data-definition/rename-table.md)
* [SELECT](../../../../server-usage/replication-cluster-multi-master/standard-replication/selectively-skipping-replication-of-binlog-events.md)
* [TRUNCATE TABLE](../table-statements/truncate-table.md)