
# View Algorithms


## Description


The [CREATE VIEW](create-view.md) statement accepts an optional ALGORITHM clause, an extension to standard SQL for [Views](README.md).


It can contain one of three values: MERGE, TEMPTABLE or UNDEFINED, and affects how MariaDB will process the view.


With MERGE, the view definition and the related portion of the statement referring to the view are merged. If TEMPTABLE is selected, the view results are stored in a temporary table.


MERGE is usually more efficient, and a view can only be updated with this algorithm. TEMPTABLE can be useful in certain situations, as locks on the underlying tables can be released before the statement is finished processing.


If it's UNDEFINED (or the ALGORITHM clause is not used), MariaDB will choose what it thinks is the best algorithm. An algorithm can also be UNDEFINED if its defined as MERGE, but the view requires a temporary table.


Views with definition ALGORITHM=MERGE or ALGORITHM=TEMPTABLE got accidentally swapped between MariaDB and MySQL. When upgrading, you have to re-create views created with either of these definitions (see [MDEV-6916](https://jira.mariadb.org/browse/MDEV-6916)).


## MERGE Limitations


A view cannot be of type ALGORITHM=MERGE if it uses any of the following:


* [HAVING](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)
* [LIMIT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#limit)
* [GROUP BY](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#group-by)
* [DISTINCT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#distinct)
* [UNION](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/joins-subqueries/union.md)
* [UNION ALL](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/joins-subqueries/union.md)
* An aggregate function, such as [MAX()](../../../../maxscale/mariadb-maxscale-14/maxscale-14-tutorials/maxscale-connection-routing-with-mysql-replication.md), [MIN()](../../../reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/minmax-optimization.md), [SUM()](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/aggregate-functions/sum.md) or [COUNT()](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/aggregate-functions/count.md)
* subquery in the SELECT list
* if it has no underlying table because it refers only to literal values


## MERGE Examples


### Example 1


Here's an example of how MariaDB handles a view with a MERGE algorithm. Take a view defined as follows:


```
CREATE ALGORITHM = MERGE VIEW view_name (view_field1, view_field2) AS
SELECT field1, field2 FROM table_name WHERE field3 > '2013-06-01';
```

Now, if we run a query on this view, as follows:


```
SELECT * FROM view_name;
```

to execute the view `view_name` becomes the underlying table, `table_name`, the `*` becomes the fields `view_field1` and `view_field2`, corresponding to `field1` and `field2` and the WHERE clause, `WHERE field3 > 100` is added, so the actual query executed is:


```
SELECT field1, field2 FROM table_name WHERE field3 > '2013-06-01'
```

### Example 2


Given the same view as above, if we run the query:


```
SELECT * FROM view_name WHERE view_field < 8000;
```

everything occurs as it does in the previous example, but `view_field < 8000` takes the corresponding field name and becomes `field1 < 8000`, connected with `AND` to the `field3 > '2013-06-01'` part of the query.


So the resulting query is:


```
SELECT field1, field2 FROM table_name WHERE (field3 > '2013-06-01') AND (field1 < 8000);
```

When connecting with `AND`, parentheses are added to make sure the correct precedence is used.

