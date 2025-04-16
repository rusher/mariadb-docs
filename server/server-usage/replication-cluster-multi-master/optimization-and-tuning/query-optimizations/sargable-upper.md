
# Sargable UPPER

Starting from [MariaDB 11.3](../../../../../release-notes/mariadb-community-server/what-is-mariadb-113.md), expressions in the form


```
UPPER(key_col) = expr
UPPER(key_col) IN (constant-list)
```

are sargable if `key_col` uses either the `utf8mb3_general_ci` or `utf8mb4_general_ci` collation.


`UCASE` is a synonym for [UPPER](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/upper.md) so is covered as well.


Sargable means that the optimizer is able to use such conditions to construct access methods, estimate their selectivity, or perform partition pruning.


## Example


```
create table t1 (
  key1 varchar(32) collate utf8mb4_general_ci,
  ...
  key(key1)
);
```

```
explain select * from t1 where UPPER(key1)='ABC'
+------+-------------+-------+------+---------------+------+---------+-------+------+--------------------------+
| id   | select_type | table | type | possible_keys | key  | key_len | ref   | rows | Extra                    |
+------+-------------+-------+------+---------------+------+---------+-------+------+--------------------------+
|    1 | SIMPLE      | t1    | ref  | key1          | key1 | 131     | const | 1    | Using where; Using index |
+------+-------------+-------+------+---------------+------+---------+-------+------+--------------------------+
```

Note that `ref` access is used.


An example with join:


```
explain select * from t0,t1 where upper(t1.key1)=t0.col;
+------+-------------+-------+------+---------------+------+---------+-------------+------+-------------+
| id   | select_type | table | type | possible_keys | key  | key_len | ref         | rows | Extra       |
+------+-------------+-------+------+---------------+------+---------+-------------+------+-------------+
|    1 | SIMPLE      | t0    | ALL  | NULL          | NULL | NULL    | NULL        | 10   | Using where |
|    1 | SIMPLE      | t1    | ref  | key1          | key1 | 131     | test.t0.col | 1    | Using index |
+------+-------------+-------+------+---------------+------+---------+-------------+------+-------------+
```

Here, the optimizer was able to construct `ref` access.


## Controlling the Optimization


The [optimizer_switch](optimizer-switch.md) variable has the flag `sargable_casefold` to turn the optimization on and off. The default is ON.


## Optimizer Trace


The optimization is implemented as a rewrite for a query's WHERE/ON conditions. It uses the `sargable_casefold_removal` object name in the trace:


```
"join_optimization": {
        "select_id": 1,
        "steps": [
          {
            "sargable_casefold_removal": {
              "before": "ucase(t1.key1) = t0.col",
              "after": "t1.key1 = t0.col"
            }
          },
```

## References


* [MDEV-31496](https://jira.mariadb.org/browse/MDEV-31496): Make optimizer handle UCASE(varchar_col)=...
* An analog for [LCASE](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/lcase.md) is not possible. See [MDEV-31955](https://jira.mariadb.org/browse/MDEV-31955): Make optimizer handle LCASE(varchar_col)=... for details.

<span></span>
