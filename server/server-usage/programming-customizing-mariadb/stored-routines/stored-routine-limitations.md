
# Stored Routine Limitations

The following SQL statements are not permitted inside any [stored routines](README.md) ([stored functions](stored-functions/README.md), [stored procedures](stored-procedures/README.md), [events](../triggers-events/event-scheduler/events.md) or [triggers](../triggers-events/triggers/triggers-and-implicit-locks.md)).


* [ALTER VIEW](../views/alter-view.md); you can use [CREATE OR REPLACE VIEW](../views/create-view.md) instead.
* [LOAD DATA](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) and [LOAD TABLE](../../replication-cluster-multi-master/standard-replication/obsolete-replication-information/load-table-from-master-removed.md).
* [CHANGE MASTER TO](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md)
* [INSERT DELAYED](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md) is permitted, but the statement is handled as a regular [INSERT](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/insert-function.md).
* [LOCK TABLES](../../../reference/sql-statements-and-structure/sql-statements/transactions/lock-tables.md) and [UNLOCK TABLES](../../../reference/sql-statements-and-structure/sql-statements/transactions/lock-tables.md).
* References to [local variables](../programmatic-compound-statements/declare-variable.md) within prepared statements inside a stored routine (use [user-defined variables](../../../reference/sql-statements-and-structure/sql-language-structure/user-defined-variables.md) instead).
* [BEGIN (WORK)](../../../reference/sql-statements-and-structure/sql-statements/transactions/start-transaction.md) is treated as the beginning of a [BEGIN END](../programmatic-compound-statements/begin-end.md) block, not a transaction, so [START TRANSACTION](../../../reference/sql-statements-and-structure/sql-statements/transactions/start-transaction.md) needs to be used instead.
* The number of permitted recursive calls is limited to [max_sp_recursion_depth](../../replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_sp_recursion_depth). If this variable is 0 (default), recursivity is disabled. The limit does not apply to stored functions.
* Most statements that are not permitted in prepared statements are not permitted in stored programs. See [Prepare Statement:Permitted statements](../../../reference/sql-statements-and-structure/sql-statements/prepared-statements/prepare-statement.md#permitted-statements) for a list of statements that can be used. [SIGNAL](../programmatic-compound-statements/signal.md), [RESIGNAL](../programmatic-compound-statements/resignal.md) and [GET DIAGNOSTICS](../programmatic-compound-statements/programmatic-compound-statements-diagnostics/get-diagnostics.md) are exceptions, and may be used in stored routines.


There are also further limitations specific to the kind of stored routine.


Note that, if a stored program calls another stored program, the latter will inherit the caller's limitations. So, for example, if a stored procedure is called by a stored function, that stored procedure will not be able to produce a result set, because stored functions can't do this.


## See Also


* [Stored Function Limitations](stored-functions/stored-function-limitations.md)
* [Trigger Limitations](../triggers-events/triggers/trigger-limitations.md)
* [Event Limitations](../triggers-events/event-scheduler/event-limitations.md)

<span></span>
