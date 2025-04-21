
# Performance Schema events_transactions_history_long Table


##### MariaDB starting with [10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)
The events_transactions_history_long table was introduced in [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes).


The `events_transactions_history_long` table contains the most recent completed transaction events that have ended globally, across all threads.


The number of records stored in the table is determined by the [performance_schema_events_transactions_history_long_size](../performance-schema-system-variables.md#performance_schema_events_transactions_history_long_size) system variable, which is autosized on startup.


If adding a completed transaction would cause the table to exceed this limit, the oldest row, regardless of thread, is discarded.


The table contains the following columns:



| Column | Type | Description |
| --- | --- | --- |
| Column | Type | Description |
| THREAD_ID | bigint(20) unsigned | The thread associated with the event. |
| EVENT_ID | bigint(20) unsigned | The event id associated with the event. |
| END_EVENT_ID | bigint(20) unsigned | This column is set to NULL when the event starts and updated to the thread current event number when the event ends. |
| EVENT_NAME | varchar(128) | The name of the instrument from which the event was collected. This is a NAME value from the setup_instruments table. |
| STATE | enum('ACTIVE', 'COMMITTED',' ROLLED BACK') | The current transaction state. The value is ACTIVE (after START TRANSACTION or BEGIN), COMMITTED (after COMMIT), or ROLLED BACK (after ROLLBACK). |
| TRX_ID | bigint(20) unsigned | Unused. |
| GTID | varchar(64) | Transaction [GTID](../../../../../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md), using the format DOMAIN-SERVER_ID-SEQUENCE_NO. |
| XID_FORMAT_ID | int(11) | XA transaction format ID for GTRID and BQUAL values. |
| XID_GTRID | varchar(130) | XA global transaction ID. |
| XID_BQUAL | varchar(130) | XA transaction branch qualifier. |
| XA_STATE | varchar(64) | The state of the XA transaction. The value is ACTIVE (after XA START), IDLE (after XA END), PREPARED (after XA PREPARE), ROLLED BACK (after XA ROLLBACK), or COMMITTED (after XA COMMIT). |
| SOURCE | varchar(64) | The name of the source file containing the instrumented code that produced the event and the line number in the file at which the instrumentation occurs. |
| TIMER_START | bigint(20) unsigned | The unit is picoseconds. When event timing started. NULL if event has no timing information. |
| TIMER_END | bigint(20) unsigned | The unit is picoseconds. When event timing ended. NULL if event has no timing information. |
| TIMER_WAIT | bigint(20) unsigned | The unit is picoseconds. Event duration. NULL if event has not timing information. |
| ACCESS_MODE | enum('READ ONLY', 'READ WRITE') | Transaction access mode. |
| ISOLATION_LEVEL | varchar(64) | Transaction isolation level. One of: REPEATABLE READ, READ COMMITTED, READ UNCOMMITTED, or SERIALIZABLE. |
| AUTOCOMMIT | enum('YES', 'NO') | NO |
| NUMBER_OF_SAVEPOINTS | bigint(20) unsigned | The number of SAVEPOINT statements issued during the transaction. |
| NUMBER_OF_ROLLBACK_TO_SAVEPOINT | bigint(20) unsigned | The number of ROLLBACK_TO_SAVEPOINT statements issued during the transaction. |
| NUMBER_OF_RELEASE_SAVEPOINT | bigint(20) unsigned | The number of RELEASE_SAVEPOINT statements issued during the transaction. |
| OBJECT_INSTANCE_BEGIN | bigint(20) unsigned | Unused. |
| NESTING_EVENT_ID | bigint(20) unsigned | The EVENT_ID value of the event within which this event is nested. |
| NESTING_EVENT_TYPE | enum('TRANSACTION',' STATEMENT', 'STAGE', 'WAIT') | The nesting event type. |


