# Operators

Operators can be used for comparing values or for assigning values. There are several operators and they may be used in different SQL statements and clauses. Some can be used somewhat on their own, not within an SQL statement clause.

For comparing values—string or numeric—you can use symbols such as the equal-sign (i.e., `=`) or the exclamation point and the equal-sign together (i.e., `!=`). You might use these in `WHERE` clauses or within a flow-control statement or function (e.g., [IF( )](../sql-statements/built-in-functions/control-flow-functions/if-function.md)). You can also use basic regular expressions with the `LIKE ` operator.

For assigning values, you can also use the equal-sign or other arithmetic symbols (e.g. plus-sign). You might do this with the [SET](../../../server-usage/replication-cluster-multi-master/standard-replication/setting-up-replication.md) statement or in a `SET` clause in an [UPDATE](../sql-statements/data-manipulation/changing-deleting-data/update.md) statement.