# not\_null\_range\_scan Optimization

The NOT NULL range scan optimization enables the optimizer to construct range scans from NOT NULL conditions that it was able to infer from the WHERE clause.

The optimization appeared in [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-5-series/mariadb-1050-release-notes). It is not enabled by default; one needs to set an `optimizer_switch` flag to enable it.

## Description

A basic (but slightly artificial) example:

```
create table items (
  price  decimal(8,2),
  weight decimal(8,2),
  ...
  index(weight)
);
```

```
-- Find items that cost more than 1000 $currency_units per kg:
set optimizer_switch='not_null_range_scan=on';
explain
select * from items where items.price > items.weight / 1000;
```

The WHERE condition in this form cannot be used for range scans. However, one can infer that it will reject rows that NULL for `weight`. That is, infer an additional condition that

```
weight IS NOT NULL
```

and pass it to the range optimizer. The range optimizer can, in turn, evaluate whether it makes sense to construct range access from the condition:

```
+------+-------------+-------+-------+---------------+--------+---------+------+------+-------------+
| id   | select_type | table | type  | possible_keys | key    | key_len | ref  | rows | Extra       |
+------+-------------+-------+-------+---------------+--------+---------+------+------+-------------+
|    1 | SIMPLE      | items | range | NULL          | weight | 5       | NULL | 1    | Using where |
+------+-------------+-------+-------+---------------+--------+---------+------+------+-------------+
```

Here's another example that's more complex but is based on a real-world query. Consider a join query

```
-- Find orders that were returned
select * from current_orders as O, order_returns as RET
where 
  O.return_id= RET.id;
```

Here, the optimizer can infer the condition "return\_id IS NOT NULL". If most of the orders are not returned (and so have NULL for return\_id), one can use range access to scan only those orders that had a return.

## Controlling the Optimization

The optimization is not enabled by default. One can enable it like so

```
set optimizer_switch='not_null_range_scan=on';
```

## Optimizer Trace

TODO.

## See Also

* [MDEV-15777](https://jira.mariadb.org/browse/MDEV-15777) - JIRA bug report which resulted in the optimization
* [NULL Filtering Optimization](https://dev.mysql.com/doc/internals/en/optimizer-nulls-filtering.html) is a related optimization in MySQL and MariaDB. It uses inferred NOT NULL conditions to perform filtering (but not index access)

CC BY-SA / Gnu FDL
