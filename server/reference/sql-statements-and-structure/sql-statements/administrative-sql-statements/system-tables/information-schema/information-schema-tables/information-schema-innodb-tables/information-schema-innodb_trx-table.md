
# Information Schema INNODB_TRX Table

The [Information Schema](../../README.md) `INNODB_TRX` table stores information about all currently executing InnoDB transactions.


It has the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| TRX_ID | Unique transaction ID number. |
| TRX_STATE | Transaction execution state; one of RUNNING, LOCK WAIT, ROLLING BACK or COMMITTING. |
| TRX_STARTED | Time that the transaction started. |
| TRX_REQUESTED_LOCK_ID | If TRX_STATE is LOCK_WAIT, the [INNODB_LOCKS.LOCK_ID](information-schema-innodb_locks-table.md) value of the lock being waited on. NULL if any other state. |
| TRX_WAIT_STARTED | If TRX_STATE is LOCK_WAIT, the time the transaction started waiting for the lock, otherwise NULL. |
| TRX_WEIGHT | Transaction weight, based on the number of locked rows and the number of altered rows. To resolve deadlocks, lower weighted transactions are rolled back first. Transactions that have affected non-transactional tables are always treated as having a heavier weight. |
| TRX_MYSQL_THREAD_ID | Thread ID from the [PROCESSLIST](../information-schema-processlist-table.md) table (note that the locking and transaction information schema tables use a different snapshot from the processlist, so records may appear in one but not the other). |
| TRX_QUERY | SQL that the transaction is currently running. |
| TRX_OPERATION_STATE | Transaction's current state, or NULL. |
| TRX_TABLES_IN_USE | Number of InnoDB tables currently being used for processing the current SQL statement. |
| TRX_TABLES_LOCKED | Number of InnoDB tables that that have row locks held by the current SQL statement. |
| TRX_LOCK_STRUCTS | Number of locks reserved by the transaction. |
| TRX_LOCK_MEMORY_BYTES | Total size in bytes of the memory used to hold the lock structures for the current transaction in memory. |
| TRX_ROWS_LOCKED | Number of rows the current transaction has locked. locked by this transaction. An approximation, and may include rows not visible to the current transaction that are delete-marked but physically present. |
| TRX_ROWS_MODIFIED | Number of rows added or changed in the current transaction. |
| TRX_CONCURRENCY_TICKETS | Indicates how much work the current transaction can do before being swapped out, see the [innodb_concurrency_tickets](../../../../../../../storage-engines/innodb/innodb-system-variables.md) system variable. |
| TRX_ISOLATION_LEVEL | [Isolation level](../../../../../transactions/set-transaction.md#isolation-levels) of the current transaction. |
| TRX_UNIQUE_CHECKS | Whether unique checks are on or off for the current transaction. Bulk data are a case where unique checks would be off. |
| TRX_FOREIGN_KEY_CHECKS | Whether foreign key checks are on or off for the current transaction. Bulk data are a case where foreign keys checks would be off. |
| TRX_LAST_FOREIGN_KEY_ERROR | Error message for the most recent foreign key error, or NULL if none. |
| TRX_ADAPTIVE_HASH_LATCHED | Whether the adaptive hash index is locked by the current transaction or not. One transaction at a time can change the adaptive hash index. |
| TRX_ADAPTIVE_HASH_TIMEOUT | Whether the adaptive hash index search latch shoild be relinquished immediately or reserved across all MariaDB calls. 0 if there is no contention on the adaptive hash index, in which case the latch is reserved until completion, otherwise counts down to zero and the latch is released after each row lookup. |
| TRX_IS_READ_ONLY | 1 if a read-only transaction, otherwise 0. |
| TRX_AUTOCOMMIT_NON_LOCKING | 1 if the transaction only contains this one statement, that is, a [SELECT](../../../../../data-manipulation/selecting-data/select.md) statement not using FOR UPDATE or LOCK IN SHARED MODE, and with autocommit on. If this and TRX_IS_READ_ONLY are both 1, the transaction can be optimized by the storrage engine to reduce some overheads |



The table is often used in conjunction with the [INNODB_LOCKS](information-schema-innodb_locks-table.md) and [INNODB_LOCK_WAITS](information-schema-innodb_lock_waits-table.md) tables to diagnose problematic locks and transactions.


[XA transactions](../../../../../transactions/xa-transactions.md) are not stored in this table. To see them, `XA RECOVER` can be used.


## Example


```
-- session 1
START TRANSACTION;
UPDATE t SET id = 15 WHERE id = 10;

-- session 2
DELETE FROM t WHERE id = 10;

-- session 1
USE information_schema;
SELECT l.*, t.*
    FROM information_schema.INNODB_LOCKS l
    JOIN information_schema.INNODB_TRX t
        ON l.lock_trx_id = t.trx_id
    WHERE trx_state = 'LOCK WAIT' \G
*************************** 1. row ***************************
                   lock_id: 840:40:3:2
               lock_trx_id: 840
                 lock_mode: X
                 lock_type: RECORD
                lock_table: `test`.`t`
                lock_index: PRIMARY
                lock_space: 40
                 lock_page: 3
                  lock_rec: 2
                 lock_data: 10
                    trx_id: 840
                 trx_state: LOCK WAIT
               trx_started: 2019-12-23 18:43:46
     trx_requested_lock_id: 840:40:3:2
          trx_wait_started: 2019-12-23 18:43:46
                trx_weight: 2
       trx_mysql_thread_id: 46
                 trx_query: DELETE FROM t WHERE id = 10
       trx_operation_state: starting index read
         trx_tables_in_use: 1
         trx_tables_locked: 1
          trx_lock_structs: 2
     trx_lock_memory_bytes: 1136
           trx_rows_locked: 1
         trx_rows_modified: 0
   trx_concurrency_tickets: 0
       trx_isolation_level: REPEATABLE READ
         trx_unique_checks: 1
    trx_foreign_key_checks: 1
trx_last_foreign_key_error: NULL
          trx_is_read_only: 0
trx_autocommit_non_locking: 0
```
