
# SET STATEMENT


`<code>SET STATEMENT</code>` can be used to set the value of a system variable for the duration of the statement. It is also possible to set multiple variables.


## Syntax


```
SET STATEMENT var1=value1 [, var2=value2, ...] 
  FOR <statement>
```

where `<code>varN</code>` is a system variable (list of allowed variables is provided below), and `<code>valueN</code>` is a constant literal.


## Description


`<code>SET STATEMENT var1=value1 FOR stmt</code>`


is roughly equivalent to


```
SET @save_value=@@var1;
SET SESSION var1=value1;
stmt;
SET SESSION var1=@save_value;
```

The server parses the whole statement before executing it, so any variables set in this fashion that affect the parser may not have the expected effect. Examples include the charset variables, sql_mode=ansi_quotes, etc.


## Examples


One can limit statement execution time `<code>[max_statement_time](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_statement_time)</code>`:


```
SET STATEMENT max_statement_time=1000 FOR SELECT ... ;
```

One can switch on/off individual optimizations:


```
SET STATEMENT optimizer_switch='materialization=off' FOR SELECT ....;
```

It is possible to enable MRR/BKA for a query:


```
SET STATEMENT  join_cache_level=6, optimizer_switch='mrr=on'  FOR SELECT ...
```

Note that it makes no sense to try to set a session variable inside a `<code>SET STATEMENT</code>`:


```
#USELESS STATEMENT
SET STATEMENT sort_buffer_size = 100000 for SET SESSION sort_buffer_size = 200000;
```

For the above, after setting sort_buffer_size to 200000 it will be reset to its original state (the state before the `<code>SET STATEMENT</code>` started) after the statement execution.


## Limitations


There are a number of variables that cannot be set on per-query basis. These include:


* `<code>autocommit</code>`
* `<code>character_set_client</code>`
* `<code>character_set_connection</code>`
* `<code>character_set_filesystem</code>`
* `<code>collation_connection</code>`
* `<code>default_master_connection</code>`
* `<code>debug_sync</code>`
* `<code>interactive_timeout</code>`
* `<code>gtid_domain_id</code>`
* `<code>last_insert_id</code>`
* `<code>log_slow_filter</code>`
* `<code>log_slow_rate_limit</code>`
* `<code>log_slow_verbosity</code>`
* `<code>long_query_time</code>`
* `<code>min_examined_row_limit</code>`
* `<code>profiling</code>`
* `<code>profiling_history_size</code>`
* `<code>query_cache_type</code>`
* `<code>rand_seed1</code>`
* `<code>rand_seed2</code>`
* `<code>skip_replication</code>`
* `<code>slow_query_log</code>`
* `<code>sql_log_off</code>`
* `<code>tx_isolation</code>`
* `<code>wait_timeout</code>`


## Source


* The feature was originally implemented as a Google Summer of Code 2009 project by Joseph Lukas.
* Percona Server 5.6 included it as [Per-query variable statement](https://www.percona.com/doc/percona-server/5.6/flexibility/per_query_variable_statement.html)
* MariaDB ported the patch and fixed many bugs. The task in MariaDB Jira is [MDEV-5231](https://jira.mariadb.org/browse/MDEV-5231).

