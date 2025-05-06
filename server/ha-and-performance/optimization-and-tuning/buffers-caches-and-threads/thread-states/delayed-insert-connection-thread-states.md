# Delayed Insert Connection Thread States

This article documents thread states that are related to the connection thread that processes [INSERT DELAYED](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md) statements.

These correspond to the `STATE` values listed by the [SHOW PROCESSLIST](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-processlist.md) statement or in the [Information Schema PROCESSLIST Table](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) as well as the `PROCESSLIST_STATE` value listed in the [Performance Schema threads Table](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-threads-table.md).

| Value                      | Description                                                                                                                                                      |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Value                      | Description                                                                                                                                                      |
| allocating local table     | Preparing to allocate rows to the delayed-insert handler thread. Follows from the got handler lock state.                                                        |
| Creating delayed handler   | Creating a handler for the delayed-inserts.                                                                                                                      |
| got handler lock           | Lock to access the delayed-insert handler thread has been received. Follows from the waiting for handler lock state and before the allocating local table state. |
| got old table              | The initialization phase is over. Follows from the waiting for handler open state.                                                                               |
| storing row into queue     | Adding new row to the list of rows to be inserted by the delayed-insert handler thread.                                                                          |
| waiting for delay\_list    | Initializing (trying to find the delayed-insert handler thread).                                                                                                 |
| waiting for handler insert | Waiting for new inserts, as all inserts have been processed.                                                                                                     |
| waiting for handler lock   | Waiting for delayed insert-handler lock to access the delayed-insert handler thread.                                                                             |
| waiting for handler open   | Waiting for the delayed-insert handler thread to initialize. Follows from the Creating delayed handler state and before the got old table state.                 |

CC BY-SA / Gnu FDL
