
# Optimizer Quality


## Generating the Queries


As of Nov 2010, there are 5 primary SQL grammars available for testing the Optimizer:


* `<code>optimizer_nosubquery.yy</code>` generates random queries with no subselects, with
 up to 3-way join and with various SQL clauses such as aggregates, GROUP BY ,
 HAVING, LIMIT;
* `<code>optimizer_subquery.yy</code>` generates queries with subselects with up to 2
 levels of nesting. Subqueries are placed in various locations, such as in
 the `<code>SELECT</code>` list, in the `<code>ON</code>` clause, etc. Aggregates, LIMIT, HAVING,
 etc. are used if allowed by the server;
* `<code>optimizer_subquery.yy</code>` generates outer joins of various depths;
* `<code>range_optimizer.yy</code>` tests the range optimizer by joinging several tables
 and generating various conditions on which range optimization is likely to be
 applied;
* `<code>range_optimizer2.yy</code>` tests the range optimizer by generating single-table
 queries that contain a lot of range-optimizable clauses. Avoiding joins
 allows the single table to be arbitrarily large, this allowing for more
 interesting range overlaps;


## Validating the Results


As of Nov 2010, the RQG has two primary modes for validating the results:


* by using a reference implementation. This can be a PostgreSQL, JavaDB or
 another version or flavor of MySQL/Maria/Drizzle. Testing this way requires
 trusting external software that is not under our control. Also, it is
 sometimes difficult to determine which implementation has returned the
 correct result. Technically, 3 implementations can "vote" as to which is the
 correct result, but this is not reliable if the implementations all derive
 from one another.
* by executing the generated query using a different execution plan. This is
 usually achieved by disabling particular optimizations and thus "downgrading"
 the plan to a more basic, presumed stable one. It is assumed that a
 nested-loop-join that takes no advantage of indexes would always provide the
 correct result. The advantage of this approach is that there is no need for a
 reference implementation and the source of the wrong result can be obtained
 by diffing the original and the downgraded execution plan.


In addition to result set validation, there is a module which executes each
generated `<code>SELECT</code>` in various contexts, such as as part of a union, stored
procedure, trigger, etc. and makes sure that the query returns a correct
result. This is most often used for testing subselects.


## Running a Complete Test Cycle


A test cycle is described in a configuration file called the CC file. The CC
file contains a list of mysqld options to use, the list of grammars to use and
other settings (e.g. Engines, table sizes, etc.). The testing framework will
then take a random permutation from the settings described in the file and run
them as a RQG test for a predefined time, such as 10 minutes. This is repeated
up to 100 times, each with a different random permutation. The PRNG seed for
each run will also be different, so different queries will be generated for
each run, in addition to using different mysqld options, engine, etc.


By default, all cycles include MyISAM, Aria and InnoDB, and some percentage are
run under Valgrind. Cycles run with both NULL and NOT NULL fields and with and
without simple views.


### Configuration for Join Cache Testing


`<code>outer_join_with_cache</code>` is always ON.
`<code><code>--</code>join_cache_level</code>` varies from 0 to 8.
`<code><code>--</code>join_buffer_size</code>` varies between 1, 100, 1K, 10K and 100K.
The `<code>optimizer_no_subquery.yy</code>`, `<code>outer_join.yy</code>` and `<code>range_access.yy</code>`
grammars are used. Once semijoin is stable, join_cache + semijoin will be
tested with `<code>optimizer_subquery.yy</code>`.


### Configuration for MRR/ICP/DS-MRR-CPK Testing


`<code><code>--</code>optimizer_use_mrr</code>` is ON,
`<code>mrr_sort_keys</code>` is both ON and OFF,
`<code>index_condition_pushdown</code>` is both ON and OFF,
`<code>join_cache_level</code>` is between 0 and 8,
`<code>join_buffer_size</code>` and `<code>mrr_buffer_size</code>` are 1, 100, 1K, 10K and 100K.
`<code>optimizer_no_subquery.yy</code>`, `<code>outer_join.yy</code>`, `<code>range_access.yy</code>`
and `<code>range_access2.yy</code>` grammars are used.


### Configuration for Subquery Testing


The `<code>optimizer_no_subquery.yy</code>` grammar is used. Each individual
`<code>optimizer_switch</code>` related to subquery optimization may be disabled so that
the "second best" plan is generated.


#### Testing [MWL#89](https://askmonty.org/worklog/?tid=89)


When testing [MWL#89](https://askmonty.org/worklog/?tid=89), the following `<code>optimizer_switch</code>` are used:
`<code>in_to_exists=ON,materialization=OFF</code>`,
`<code>in_to_exists=OFF,materialization=ON</code>` and
`<code>in_to_exists=ON,materialization=ON</code>`. In addition `<code>semijoin</code>` is always OFF
to force more queries to use materialization/in_to_exists. `<code>subquery_cache</code>`
is OFF to prevent subquery cache bugs from showing up during the test.


## See Also


* [RQG Documentation](https://github.com/RQG/RQG-Documentation/wiki/Category:RandomQueryGenerator)
* [RQG Performance Comparisons](benchmarks-and-long-running-tests/benchmarks/rqg-performance-comparisons.md)
* [RQG Extensions for MariaDB Features](rqg-extensions-for-mariadb.md)
* [QA Tools](qa-tools.md)
* [Worklog Quality Checklist Template](worklog-quality-checklist-template.md)

