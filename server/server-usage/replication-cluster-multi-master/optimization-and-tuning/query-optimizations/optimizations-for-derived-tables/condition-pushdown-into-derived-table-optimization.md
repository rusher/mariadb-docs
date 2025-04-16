
# Condition Pushdown into Derived Table Optimization

If a query uses a derived table (or a view), the first action that the query optimizer will attempt is to apply the [derived-table-merge-optimization](derived-table-merge-optimization.md) and merge the derived table into its parent select. However, that optimization is only applicable when the select inside the derived table has a join as the top-level operation. If it has a [GROUP-BY](../../../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/group-by.md), [DISTINCT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#distinct), or uses [window functions](../../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/window-functions/window-functions-overview.md), then [derived-table-merge-optimization](derived-table-merge-optimization.md) is not applicable.


In that case, the Condition Pushdown optimization is applicable.


## Introduction to Condition Pushdown


Consider an example


```
create view OCT_TOTALS as
select
  customer_id,
  SUM(amount) as TOTAL_AMT
from orders
where  order_date BETWEEN '2017-10-01' and '2017-10-31'
group by customer_id;

select * from OCT_TOTALS where customer_id=1
```

The naive way to execute the above is to


1. Compute the OCT_TOTALS contents (for all customers).
1. The, select the line with customer_id=1


This is obviously inefficient, if there are 1000 customers, then one will be doing up to 1000 times more work than necessary.


However, the optimizer can take the condition `customer_id=1` and push it down into the OCT_TOTALS view.


(TODO: elaborate here)


## Condition Pushdown Properties


* Condition Pushdown has been available since [MariaDB 10.2](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md).
* The Jira task for it was [MDEV-9197](https://jira.mariadb.org/browse/MDEV-9197).
* The optimization is enabled by default. One can disable it by setting `@@optimizer_switch` flag `condition_pushdown_for_derived` to OFF.


## See Also


* Condition Pushdown through Window Functions (since [MariaDB 10.3](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md))
* [Condition Pushdown into IN Subqueries](../subquery-optimizations/condition-pushdown-into-in-subqueries.md) (since [MariaDB 10.4](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md))

