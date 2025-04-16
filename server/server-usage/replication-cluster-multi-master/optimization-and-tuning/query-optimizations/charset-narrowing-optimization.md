
# Charset Narrowing Optimization

The Charset Narrowing optimization handles equality comparisons like:


```
utf8mb3_key_column=utf8mb4_expression
```

It enables the optimizer to construct `ref` access to `utf8mb3_key_column` based on this equality. The optimization supports comparisons of columns that use `utf8mb3_general_ci` to expressions that use `utf8mb4_general_ci` .


The optimization was introduced in [MariaDB 10.6.16](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md), [MariaDB 10.10.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10-10-7-release-notes.md), [MariaDB 10.11.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-6-release-notes.md), [MariaDB 11.0.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes.md), [MariaDB 11.1.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes.md) and [MariaDB 11.2.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes.md), where it is **OFF** by default. From [MariaDB 11.7](../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md), it is `ON` by default.


## Description


MariaDB supports both the UTF8MB3 and UTF8MB4 [character sets](../../../../reference/data-types/string-data-types/character-sets/README.md). It is possible to construct join queries that compare values in UTF8MB3 to UTF8MB4.


Suppose, we have the table *'users* that uses UTF8MB4:


```
create table users (
  user_name_mb4 varchar(100) collate utf8mb4_general_ci,
  ...
);
```

and table *orders* that uses UTF8MB3:


```
create table orders (
  user_name_mb3 varchar(100) collate utf8mb3_general_ci,
  ...,
  INDEX idx1(user_name_mb3)
);
```

One can join *users* to *orders* on user_name:


```
select * from orders, users where orders.user_name_mb3=users.user_name_mb4;
```

Internally the optimizer will handle the equality by converting the UTF8MB3 value into UTF8MB4 and then doing the comparison. One can see the call to `CONVERT` in EXPLAIN FORMAT=JSON output or Optimizer Trace:


```
convert(orders.user_name_mb3 using utf8mb4) = users.user_name_mb4
```

This produces the expected result but the query optimizer is not able to use the index over `orders.user_name_mb3` to find matches for values of `users.user_name_mb4`.


The EXPLAIN of the above query looks like this:


```
explain select * from orders, users where orders.user_name_mb3=users.user_name_mb4;
+------+-------------+--------+------+---------------+------+---------+------+-------+-------------------------------------------------+
| id   | select_type | table  | type | possible_keys | key  | key_len | ref  | rows  | Extra                                           |
+------+-------------+--------+------+---------------+------+---------+------+-------+-------------------------------------------------+
|    1 | SIMPLE      | users  | ALL  | NULL          | NULL | NULL    | NULL | 1000  |                                                 |
|    1 | SIMPLE      | orders | ALL  | NULL          | NULL | NULL    | NULL | 10330 | Using where; Using join buffer (flat, BNL join) |
+------+-------------+--------+------+---------------+------+---------+------+-------+-------------------------------------------------+
```

The Charset Narrowing optimization enables the optimizer to perform the comparison between UTF8MB3 and UTF8MB4 values by "narrowing" the value in UTF8MB4 to UTF8MB3. The `CONVERT` call is no longer needed, and the optimizer is able to use the equality to construct ref access:


```
set optimizer_switch='cset_narrowing=on';

explain select * from orders, users where orders.user_name_mb3=users.user_name_mb4;
+------+-------------+--------+------+---------------+------+---------+---------------------+------+-----------------------+
| id   | select_type | table  | type | possible_keys | key  | key_len | ref                 | rows | Extra                 |
+------+-------------+--------+------+---------------+------+---------+---------------------+------+-----------------------+
|    1 | SIMPLE      | users  | ALL  | NULL          | NULL | NULL    | NULL                | 1000 | Using where           |
|    1 | SIMPLE      | orders | ref  | idx1          | idx1 | 303     | users.user_name_mb4 | 1    | Using index condition |
+------+-------------+--------+------+---------------+------+---------+---------------------+------+-----------------------+
```

## Controlling the Optimization


The optimization is controlled by an [optimizer_switch](../system-variables/server-system-variables.md#optimizer_switch) flag. Specify:


```
set optimizer_switch='cset_narrowing=on';
```

to enable the optimization.


## References


* [MDEV-32113](https://jira.mariadb.org/browse/MDEV-32113): utf8mb3_key_col=utf8mb4_value cannot be used for ref access
* Blog post: [Making “tbl.utf8mb3_key_column=utf8mb4_expr” sargable](https://petrunia.net/2023/10/11/making-tbl-utf8mb3_key_columnutf8mb4_expr-sargable/)

<span></span>
