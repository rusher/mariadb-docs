# ColumnStore Utility Functions

MariaDB ColumnStore Utility Functions are a set of simple functions that return useful information about the system, such as whether it is ready for queries.&#x20;

| Function            | Description                                                                                                                                                                                                                                                                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mcsSystemReady()    | Returns 1 if the system can accept queries, 0 if it's not ready yet.                                                                                                                                                                                                                                                                          |
| mcsSystemReadOnly() | Returns 1 if ColumnStore is in a write-suspended mode. That is, a user executed the SuspendDatabaseWrites.It returns 2 if in a read only state. ColumnStore puts itself into a read only state if it detects a logic error that may have corrupted data. Generally it means a ROLLBACK operation failed. Returns 0 if the system is writable. |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
