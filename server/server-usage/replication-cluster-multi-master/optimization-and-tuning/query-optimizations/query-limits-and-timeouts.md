
# Query Limits and Timeouts

This article describes the different methods MariaDB provides to limit/timeout a query:


## [LIMIT](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/select.md#limit)


```
SELECT ... LIMIT row_count
or
SELECT ... LIMIT offset, row_count
or
SELECT ... LIMIT row_count OFFSET offset
```

The [LIMIT](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/select.md#limit) clause restricts the number of returned rows.


## [LIMIT ROWS EXAMINED](limit-rows-examined.md)


```
SELECT ... LIMIT ROWS EXAMINED rows_limit;
```

Stops the query after 'rows_limit' number of rows have been examined.


## sql_safe_updates


If the [sql_safe_updates](../system-variables/server-system-variables.md#sql_safe_updates) variable is set, one can't execute an [UPDATE](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/update.md) or [DELETE](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/delete.md)
statement unless one specifies a key constraint in the `WHERE` clause or provide a `LIMIT` clause (or both).


```
SET @@SQL_SAFE_UPDATES=1
UPDATE tbl_name SET not_key_column=val;
-> ERROR 1175 (HY000): You are using safe update mode 
  and you tried to update a table without a WHERE that uses a KEY column
```

## sql_select_limit


[sql_select_limit](../system-variables/server-system-variables.md#sql_select_limit) acts as an automatic `LIMIT row_count` to any [SELECT](../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/select.md) query.


```
SET @@SQL_SELECT_LIMIT=1000
SELECT * from big_table;
```

The above is the same as:


```
SELECT * from big_table LIMIT 1000;
```

## max_join_size


If the [max_join_size](../system-variables/server-system-variables.md#max_join_size) variable (also called `sql_max_join_size`) is set, then it will limit
any SELECT statements that probably need to examine more than 
`MAX_JOIN_SIZE` rows.


```
SET @@MAX_JOIN_SIZE=1000;
SELECT count(null_column) from big_table;
->ERROR 1104 (42000): The SELECT would examine more than MAX_JOIN_SIZE rows; 
  check your WHERE and use SET SQL_BIG_SELECTS=1 or SET MAX_JOIN_SIZE=# if the SELECT is okay
```

## max_statement_time


If the [max_statement_time](../system-variables/server-system-variables.md#max_statement_time) variable is set, any query (excluding stored procedures) taking longer than the value of `max_statement_time` (specified in seconds) to execute will be aborted. This can be set globally, by session, as well as per user and per query. See [Aborting statements that take longer than a certain time to execute](aborting-statements.md).


## See Also


* [WAIT and NOWAIT](../../../../reference/sql-statements-and-structure/sql-statements/transactions/wait-and-nowait.md)
* [Aborting statements that take longer than a certain time to execute](aborting-statements.md)
* [lock_wait_timeout](../system-variables/server-system-variables.md#lock_wait_timeout) variable

