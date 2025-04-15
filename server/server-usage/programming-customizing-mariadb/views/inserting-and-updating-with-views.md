
# Inserting and Updating with Views

A [view](README.md) can be used for inserting or updating. However, there are certain limitations.


## Updating with views


A view cannot be used for updating if it uses any of the following:


* ALGORITHM=TEMPTABLE (see [View Algorithms](view-algorithms.md))
* [HAVING](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)
* [GROUP BY](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#group-by)
* [DISTINCT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#distinct)
* [UNION](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/joins-subqueries/union.md)
* [UNION ALL](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/joins-subqueries/union.md)
* An aggregate function, such as [MAX()](../../../../maxscale/mariadb-maxscale-14/maxscale-14-tutorials/maxscale-connection-routing-with-mysql-replication.md), [MIN()](../../../reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/minmax-optimization.md), [SUM()](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/aggregate-functions/sum.md) or [COUNT()](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/aggregate-functions/count.md)
* subquery in the SELECT list
* subquery in the WHERE clause referring to a table in the FROM clause
* if it has no underlying table because it refers only to literal values
* the FROM clause contains a non-updatdable view.
* multiple references to any base table column
* an outer join
* an inner join where more than one table in the view definition is being updated
* if there's a LIMIT clause, the view does not contain all primary or not null unique key columns from the underlying table and the [updatable_views_with_limit](../../replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#updatable_views_with_limit) system variable is set to `<code>0</code>`.


## Inserting with views


A view cannot be used for inserting if it fails any of the criteria for [updating](#updating-with-views), and must also meet the following conditions:


* the view contains all base table columns that don't have default values
* no base table columns are present in view select list more than once
* the view columns are all simple columns, and not derived in any way. The following are examples of derived columns

  * column_name + 25
  * LOWER(column_name)
  * (subquery)
  * 9.5
  * column1 / column2


## Checking whether a view is updatable


MariaDB stores an IS_UPDATABLE flag with each view, so it is always possible to see if MariaDB considers a view updatable (although not necessarily insertable) by querying the IS_UPDATABLE column in the INFORMATION_SCHEMA.VIEWS table.


## WITH CHECK OPTION


The WITH CHECK OPTION clause is used to prevent updates or inserts to views unless the WHERE clause in the SELECT statement is true.


There are two keywords that can be applied. WITH LOCAL CHECK OPTION restricts the CHECK OPTION to only the view being defined, while WITH CASCADED CHECK OPTION checks all underlying views as well. CASCADED is treated as default if neither keyword is given.


If a row is rejected because of the CHECK OPTION, an error similar to the following is produced:


```
ERROR 1369 (HY000): CHECK OPTION failed 'db_name.view_name'
```

A view with a WHERE which is always false (like `<code>WHERE 0</code>`) and WITH CHECK OPTION is similar to a [BLACKHOLE](../../../reference/storage-engines/blackhole.md) table: no row is ever inserted and no row is ever returned. An insertable view with a WHERE which is always false but no CHECK OPTION is a view that accepts data but does not show them.


## Examples


```
CREATE TABLE table1 (x INT);

CREATE VIEW view1 AS SELECT x, 99 AS y FROM table1;
```

Checking whether the view is updateable:


```
SELECT TABLE_NAME,IS_UPDATABLE FROM INFORMATION_SCHEMA.VIEWS;
+------------+--------------+
| TABLE_NAME | IS_UPDATABLE |
+------------+--------------+
| view1      | YES          |
+------------+--------------+
```

This query works, as the view is updateable:


```
UPDATE view1 SET x = 5;
```

This query fails, since column `<code>y</code>` is a literal.


```
UPDATE view1 SET y = 5;
ERROR 1348 (HY000): Column 'y' is not updatable
```

Here are three views to demonstrate the WITH CHECK OPTION clause.


```
CREATE VIEW view_check1 AS SELECT * FROM table1 WHERE x < 100 WITH CHECK OPTION;

CREATE VIEW view_check2 AS SELECT * FROM view_check1 WHERE x > 10 WITH LOCAL CHECK OPTION;

CREATE VIEW view_check3 AS SELECT * FROM view_check1 WHERE x > 10 WITH CASCADED CHECK OPTION;
```

This insert succeeds, as `<code>view_check2</code>` only checks the insert against `<code>view_check2</code>`, and the WHERE clause evaluates to true (`<code>150</code>` is `<code>>10</code>`).


```
INSERT INTO view_check2 VALUES (150);
```

This insert fails, as `<code>view_check3</code>` checks the insert against both `<code>view_check3</code>` and the underlying views. The WHERE clause for `<code>view_check1</code>` evaluates as false (`<code>150</code>` is `<code>>10</code>`, but `<code>150</code>` is not `<code><100</code>`), so the insert fails.


```
INSERT INTO view_check3 VALUES (150);
ERROR 1369 (HY000): CHECK OPTION failed 'test.view_check3'
```
