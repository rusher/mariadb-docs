
# optimizer_join_limit_pref_ratio optimization


## Basics


Off (0) by default, when enabling this optimization, MariaDB will consider a join order that may shorten query execution time based on the `<code>ORDER BY ... LIMIT n</code>` clause. For small values of `<code>n</code>`, this may improve performance.


Set the value of `<code>optimizer_join_limit_pref_ratio</code>` to a non-zero value to enable this option (higher values are more conservative, recommended value is 100), or set to 0 (the default value) to disable it.


## Detailed description


### Problem setting


By default, the MariaDB optimizer picks a join order without considering the ORDER BY ... LIMIT clause, when present.


For example, consider a query looking at latest 10 orders together with customers who made them:


```
select *
from
  customer,order
where
  customer.name=order.customer_name
order by
  order.date desc
limit 10
```

The two possible plans are:
`<code>customer->orders</code>`:


```
+------+-------------+----------+------+---------------+---------------+---------+---------------+------+----------------------------------------------+
| id   | select_type | table    | type | possible_keys | key           | key_len | ref           | rows | Extra                                        |
+------+-------------+----------+------+---------------+---------------+---------+---------------+------+----------------------------------------------+
|    1 | SIMPLE      | customer | ALL  | name          | NULL          | NULL    | NULL          | 9623 | Using where; Using temporary; Using filesort |
|    1 | SIMPLE      | orders   | ref  | customer_name | customer_name | 103     | customer.name | 1    |                                              |
+------+-------------+----------+------+---------------+---------------+---------+---------------+------+----------------------------------------------+
```

and `<code>orders->customer</code>`:


```
+------+-------------+----------+-------+---------------+------------+---------+----------------------+------+-------------+
| id   | select_type | table    | type  | possible_keys | key        | key_len | ref                  | rows | Extra       |
+------+-------------+----------+-------+---------------+------------+---------+----------------------+------+-------------+
|    1 | SIMPLE      | orders   | index | customer_name | order_date | 4       | NULL                 | 10   | Using where |
|    1 | SIMPLE      | customer | ref   | name          | name       | 103     | orders.customer_name | 1    |             |
+------+-------------+----------+-------+---------------+------------+---------+----------------------+------+-------------+
```

The `<code>customer->orders</code>` plan computes a join between all customers and orders, saves that result into a temporary table, and then uses filesort to get the 10 most recent orders. This query plan doesn't benefit from the fact that just 10 orders are needed.


However, in contrast, the `<code>orders->customers</code>` plan uses an index to read rows in the ORDER BY order. The query can stop execution once it finds 10 `<code>order-and-customer</code>` combinations. This is much faster than computing the entire join. Under this plan, and when this new optimization, we can leverage ORDER BY ... LIMIT to stop early, when we have the 10 combinations.


### Plans with LIMIT shortcuts are difficult to estimate


It is fundamentally difficult to produce a reliable estimate for ORDER BY ... LIMIT shortcuts. Let's take an example from the previous section to see why. This query searches for last 10 orders that were shipped by air:


```
select *
from
  customer,order
where
  customer.name=order.customer_name 
  and order.shipping_method='Airplane'
order by
  order.date desc
limit 10
```

Suppose we know beforehand that 50% of orders are shipped by air. 
Assuming there's no correlation between date and shipping method, `<code>orders->customer</code>` plan will need to scan 20 orders before we find 10 that are shipped by air.
But if there is correlation, then we may need to scan up to `<code>(total_orders*0.5 + 10)</code>` before we find first 10 orders that are shipped by air. Scanning about 50% of all orders can be expensive.


This situation worsens when the query has constructs whose selectivity is not known. For example, suppose the WHERE condition was


```
order.shipping_method='%Airplane%'
```

in this case, we can't reliably say whether we will be able to stop after scanning #LIMIT rows or we will need to enumerate all rows before we find #LIMIT matches.


## Providing guidelines to the optimizer


Due to these challenges, the optimization is not enabled by default.


When running a mostly OLTP workload such that query WHERE conditions have suitable
indexes or are not very selective, then any ORDER BY ... LIMIT queries will typically find matching rows
quickly. In this case, it makes sense to give the following guidance to the optimizer:


```
Do consider the query plan using LIMIT short-cutting 
and prefer it if it promises at least X times speedup.
```

The value of `<code>X</code>` is given to the optimizer via `<code>optimizer_join_limit_pref_ratio</code>` setting.
Higher values carry less risk. The recommended value is 100: prefer the LIMIT join order if it 
promises at least 100x speedup.


## References


* [MDEV-34720](https://jira.mariadb.org/browse/MDEV-34720) introduces optimizer_join_limit_pref_ratio optimization
* [MDEV-18079](https://jira.mariadb.org/browse/MDEV-18079) is about future development that would make the optimizer handle such cases without user guidance.

