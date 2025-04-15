
# Information Schema INNODB_SYS_SEMAPHORE_WAITS Table

The [Information Schema](../../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) INNODB_SYS_SEMAPHORE_WAITS table is meant to contain information about current semaphore waits. At present it is not correctly populated. See [MDEV-21330](https://jira.mariadb.org/browse/MDEV-21330).


The [PROCESS privilege](../../../../../account-management-sql-commands/grant.md#process) is required to view the table.


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| THREAD_ID | Thread id waiting for semaphore |
| OBJECT_NAME | Semaphore name |
| FILE | File name where semaphore was requested |
| LINE | Line number on above file |
| WAIT_TIME | Wait time |
| WAIT_OBJECT |  |
| WAIT_TYPE | Object type (mutex, rw-lock) |
| HOLDER_THREAD_ID | Holder thread id |
| HOLDER_FILE | File name where semaphore was acquired |
| HOLDER_LINE | Line number for above |
| CREATED_FILE | Creation file name |
| CREATED_LINE | Line number for above |
| WRITER_THREAD | Last write request thread id |
| RESERVATION_MODE | Reservation mode (shared, exclusive) |
| READERS | Number of readers if only shared mode |
| WAITERS_FLAG | Flags |
| LOCK_WORD | Lock word (for developers) |
| LAST_READER_FILE | Removed |
| LAST_READER_LINE | Removed |
| LAST_WRITER_FILE | Last writer file name |
| LAST_WRITER_LINE | Above line number |
| OS_WAIT_COUNT | Wait count |


