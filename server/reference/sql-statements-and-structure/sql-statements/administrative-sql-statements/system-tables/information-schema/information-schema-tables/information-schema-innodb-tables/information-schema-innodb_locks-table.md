# Information Schema INNODB_LOCKS Table

The [Information Schema](/en/information_schema/) `INNODB_LOCKS` table stores information about locks that InnoDB transactions have requested but not yet acquired, or that are blocking another transaction.

It has the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| LOCK_ID | Lock ID number - the format is not fixed, so do not rely upon the number for information. |
| LOCK_TRX_ID | Lock's transaction ID. Matches the [INNODB_TRX.TRX_ID](information-schema-innodb_trx-table.md) column. |
| LOCK_MODE | [Lock mode](/en/xtradbinnodb-lock-modes/). One of S (shared), X (exclusive), IS (intention shared), IX (intention exclusive row lock), S_GAP (shared gap lock), X_GAP (exclusive gap lock), IS_GAP (intention shared gap lock), IX_GAP (intention exclusive gap lock) or AUTO_INC ([auto-increment table level lock](/en/auto_increment-handling-in-xtradbinnodb/)). |
| LOCK_TYPE | Whether the lock is RECORD (row level) or TABLE level. |
| LOCK_TABLE | Name of the locked table,or table containing locked rows. |
| LOCK_INDEX | Index name if a RECORD LOCK_TYPE, or NULL if not. |
| LOCK_SPACE | Tablespace ID if a RECORD LOCK_TYPE, or NULL if not. |
| LOCK_PAGE | Locked record page number if a RECORD LOCK_TYPE, or NULL if not. |
| LOCK_REC | Locked record heap number if a RECORD LOCK_TYPE, or NULL if not. |
| LOCK_DATA | Locked record primary key as an SQL string if a RECORD LOCK_TYPE, or NULL if not. If no primary key exists, the internal InnoDB row_id number is instead used. To avoid unnecessary IO, also NULL if the locked record page is not in the [buffer pool](/en/xtradbinnodb-buffer-pool/) |

The table is often used in conjunction with the [INNODB_LOCK_WAITS](information-schema-innodb_lock_waits-table.md) and [INNODB_TRX](information-schema-innodb_trx-table.md) tables to diagnose problematic locks and transactions

#

# Example

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

.