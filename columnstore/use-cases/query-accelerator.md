# Query Accelerator

{% hint style="warning" %}
MariaDB Query Accelerator is an **Alpha release**. Do not use it in production environments.\
Query Accelerator works only in **ColumnStore 25.10.0** and with **MariaDB Enterprise Server**.
{% endhint %}

## What is Query Accelerator

Query Accelerator allows MariaDB to use ColumnStore to execute queries that are otherwise executed by InnoDB. Under the hood, Columnstore:

* receives a query;
* searches for applicable Engine Independent statistics for InnoDB table index column;
* applies RBO[^1] rule to transform its InnoDB tables into a number of `UNION` queries over non-overlapping ranges of a suitable InnoDB table index;
* retrieves the data in parallel from MariaDB, and runs it using Columnstore runtime.

## Queries Benefitting From Query Accelerator

Query Accelerator improves the performance of queries that use aggregation functions, for instance `SUM`, `AVG`, `MIN`, `MAX`, and `GROUP BY`, where the performance overhead of pulling the data out of InnoDB can be overcome by the performance optimization of running in the ColumnStore engine.

This avoids the bottleneck/pipeline of having to move data out of InnoDB and into ColumnStore. Query Accelerator strives to parallelize data out of InnoDB, by utilizing table statistics to optimize multiple threads to data ranges on disk. If the InnoDB table in question uses an index, Query Accelerator is able to get the data much faster.

Example of a query benefitting from Query Accelerator (assuming `column_a` is indexed):

```sql
SELECT column_a, SUM(column_b) FROM innodb_table GROUP BY column_a
```

The effectiveness of Query Accelerator can vary depending on the type of queries you run and the specific characteristics of your database schema. Certain types of queries or configurations may not benefit from Query Accelerator, or could potentially experience decreased performance. It's essential to understand when Query Accelerator is most advantageous and when traditional InnoDB operations might be more efficient. Consider the following points to optimize query performance with Query Accelerator:

* To minimize performance overhead of pulling data, make sure your query uses an indexed or partitioned column.
* Also, run `ANALYZE TABLE` before running Query Accelerator.

## Queries not to run in Query Accelerator

### Performance Issues

Performance issues occur for queries like this:

```sql
 SELECT column_a FROM tbl WHERE column_a = column_b 
```

InnoDB handles such comparison much better than ColumnStore in general, and in Query Accelerator, that would be even worse.

* Generally, if you don’t use aggregation functions in a query, InnoDB will be better than ColumnStore in general and Query Accelerator in particular.
* This is also true for multi-table joins.
* Query Accelerator takes a minimum of time (between 0.05 and 0.5 seconds) to run a query. So if your queries are fast already in InnoDB, they’re not likely to benefit from Query Accelerator.

### Queries not Working in Query Accelerator

Query Accelerator has the same limitations as ColumnStore in general, in that it has a limited set of [functions](../reference/columnstore-distributed-functions.md) and [data types](../reference/columnstore-data-types.md) it can handle. Therefore, be aware of

* syntax or functions that Columnstore does not support;
* data types ColumnStore does not support (unsupported data types are silently converted to strings, which in turn means that functions relying on the data type might not work either).

## How to Enable Query Accelerator

{% stepper %}
{% step %}
**Edit the MariaDB configuration file (my.cnf or my.ini)**

Locate (or create) the mariadb section, and add a line enabling Query Accelerator, like this:

```ini
[mariadb]
columnstore_innodb_queries_use_mcs = on
```

Restart MariaDB Server for the change to take effect.
{% endstep %}

{% step %}
**Run queries to turn on Query Accelerator**

Set these parameters in a client session:

```sql
SET columnstore_unstable_optimizer=ON;
SET optimizer_switch="index_merge=off,index_merge_union=off,index_merge_sort_union=off,
                      index_merge_intersection=off,index_merge_sort_intersection=off,
                      index_condition_pushdown=off,derived_merge=off,
                      derived_with_keys=off,firstmatch=off,loosescan=off,
                      materialization=on,in_to_exists=off,semijoin=off,
                      partial_match_rowid_merge=off,partial_match_table_scan=off,
                      subquery_cache=off,mrr=off,mrr_cost_based=off,mrr_sort_keys=off,
                      outer_join_with_cache=off,semijoin_with_cache=off,
                      join_cache_incremental=off,join_cache_hashed=off,
                      join_cache_bka=off,optimize_join_buffer_size=off,
                      table_elimination=off,extended_keys=off,exists_to_in=off,
                      orderby_uses_equalities=off,condition_pushdown_for_derived=on,
                      split_materialized=off,condition_pushdown_for_subquery=off,
                      rowid_filter=off,condition_pushdown_from_having=on,
                      not_null_range_scan=off,hash_join_cardinality=off,
                      cset_narrowing=off,sargable_casefold=off";
```

{% hint style="info" %}
In future versions of Query Accelerator, those `SET` statements will be in stored procedures, allowing to turn Query Accelerator on and off with simpler commands.
{% endhint %}

{% hint style="warning" %}
To use Query Accelerator just for one query, you have to run those `SET` statements per query, not per session. Setting them per session effectively disables the MariaDB Optimizer for subsequent queries that ColumnStore cannot execute.
{% endhint %}
{% endstep %}
{% endstepper %}

## Enable ColumnStore Processing for InnoDB Tables

There must be Engine Independent statistics for InnoDB table index column to be used for Query Accelerator.

```sql
analyze table <table_name> persistent for columns (<column_name>) indexes();
```

## Control Client Session Variables and Parameters

* `columnstore_unstable_optimizer`: enables unstable optimizer that is required for Query Accelerator RBO rule
* `columnstore_select_handler`: enables/disables ColumnStore processing for InnoDB tables
* `columnstore_query_accel_parallel_factor`: controls the number of parallel ranges to be used for Query Accelerator

Watch out `max_connections`. If you set `columnstore_query_accel_parallel_factor` to a high value, you may need to increase `max_connections` to avoid connection pool exhaustion.

## How to Verify Query Accelerator is Being Used

There are two ways to verify Query Accelerator is being used:

1. Use `select mcs_get_plan('rules')` to get a list of the rules that were applied to the query.
2. Look for patterns like `derived table - $added_sub_#db_name_#table_name_X` in the optimized plan using `select mcs_get_plan('optimized')`.

[^1]: Rule-based optimizer
