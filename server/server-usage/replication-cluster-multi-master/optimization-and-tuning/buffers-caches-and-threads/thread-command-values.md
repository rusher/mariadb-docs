
# Thread Command Values

A thread can have any of the following `COMMAND` values (displayed by the `COMMAND` field listed by the [SHOW PROCESSLIST](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-processlist.md) statement or in the [Information Schema PROCESSLIST Table](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md), as well as the `PROCESSLIST_COMMAND` value listed in the [Performance Schema threads Table](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-threads-table.md)). These indicate the nature of the thread's activity.



| Value | Description |
| --- | --- |
| Value | Description |
| Binlog Dump | Master thread for sending [binary log](../../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) contents to a slave. |
| Change user | Executing a change user operation. |
| Close stmt | Closing a [prepared statement](../../../../reference/sql-statements-and-structure/sql-statements/prepared-statements/README.md). |
| Connect | [Replication](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/README.md) slave is connected to its master. |
| Connect Out | Replication slave is in the process of connecting to its master. |
| Create DB | Executing an operation to create a database. |
| Daemon | Internal server thread rather than for servicing a client connection. |
| Debug | Generating debug information. |
| Delayed insert | A delayed-insert handler. |
| Drop DB | Executing an operation to drop a database. |
| Error | Error. |
| Execute | Executing a [prepared statement](../../../../reference/sql-statements-and-structure/sql-statements/prepared-statements/README.md). |
| Fetch | Fetching the results of an executed [prepared statement](../../../../reference/sql-statements-and-structure/sql-statements/prepared-statements/README.md). |
| Field List | Retrieving table column information. |
| Init DB | Selecting default database. |
| Kill | Killing another thread. |
| Long Data | Retrieving long data from the result of executing a [prepared statement](../../../../reference/sql-statements-and-structure/sql-statements/prepared-statements/README.md). |
| Ping | Handling a server ping request. |
| Prepare | Preparing a [prepared statement](../../../../reference/sql-statements-and-structure/sql-statements/prepared-statements/README.md). |
| Processlist | Preparing processlist information about server threads. |
| Query | Executing a statement. |
| Quit | In the process of terminating the thread. |
| Refresh | [Flushing](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) a table, logs or caches, or refreshing replication server or [status variable](../system-variables/server-status-variables.md) information. |
| Register Slave | Registering a slave server. |
| Reset stmt | Resetting a [prepared statement](../../../../reference/sql-statements-and-structure/sql-statements/prepared-statements/README.md). |
| Set option | Setting or resetting a client statement execution option. |
| Sleep | Waiting for the client to send a new statement. |
| Shutdown | Shutting down the server. |
| Statistics | Preparing status information about the server. |
| Table Dump | Sending the contents of a table to a slave. |
| Time | Not used. |


<span></span>
