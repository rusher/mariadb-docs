
# Virtual Column Support in the Optimizer


##### MariaDB starting with [11.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md)
Starting from [MariaDB 11.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md), the optimizer can recognize use of indexed virtual column expressions in the WHERE clause and use them to construct range and ref(const) accesses.



## Motivating Example


Suppose one has a table with data in JSON:


```
create table t1 (json_data JSON);
insert into t1 values('{"column1": 1234}'); 
insert into t1 ...
```

In order to do efficient queries over data in JSON, one can add a virtual column and an index on it:


```
alter table t1
  add column vcol1 int as (cast(json_value(json_data, '$.column1') as integer)),
  add index(vcol1);
```

Before [MariaDB 11.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md), one had to use `vcol1` in the WHERE clause. Now, one can use the 
virtual column expression, too:


```
-- This will use the index before 11.8:
explain select * from t1 where vcol1=100;
-- Starting from 11.8, this will use the index, too:
explain select * from t1 
where cast(json_value(json_data, '$.column1') as integer)=100;
```

```
+------+-------------+-------+------+---------------+-------+---------+-------+------+-------+
| id   | select_type | table | type | possible_keys | key   | key_len | ref   | rows | Extra |
+------+-------------+-------+------+---------------+-------+---------+-------+------+-------+
|    1 | SIMPLE      | t1    | ref  | vcol1         | vcol1 | 5       | const | 1    |       |
+------+-------------+-------+------+---------------+-------+---------+-------+------+-------+
```

## General Considerations


* In MariaDB, one has to create a virtual column and then create an index over it. Other databases allow to create an index directly over expression: `create index on t1((col1+col2))`. This is not yet supported in MariaDB ([MDEV-35853](https://jira.mariadb.org/browse/MDEV-35853)).


* The `WHERE` clause must use the exact same expression as in the virtual column definition.


* The optimization is implemented in a similar way to MySQL: the optimizer finds potentially useful occurrences of `vcol_expr` in the WHERE clause and replaces them with `vcol_name`.


* In the optimizer trace, the rewrites are shown like so:


```
"virtual_column_substitution": {
              "condition": "WHERE",
              "resulting_condition": "t1.vcol1 = 100"
            }
```

## Accessing JSON fields


### Cast the value to the desired type


SQL is strongly-typed language while JSON is weakly-typed. This means one must specify the desired datatype when accessing JSON data from SQL. In the above example, we declared `vcol1` as `INT` and then used `(CAST ... AS INTEGER)` (both in the ALTER TABLE and in the `WHERE` clause in SELECT query:):


```
alter table t1
  add column vcol1 INT as (CAST(json_value(json_data, '$.column1') AS INTEGER)) ...
```

```
select ...  where ... CAST(json_value(json_data, '$.column1') AS INTEGER) ...;
```

### Specify collation for strings


When extracting string values, `CAST` is not necessary, as `JSON_VALUE` returns strings.


However, one must take into account collations. If one declares the column as `JSON`:


```
create table t1 ( 
  json_data JSON 
  ...
```

the collation of `json_data` will be `utf8mb4_bin`. The collation of 
 `JSON_VALUE(json_data, ...)` will also be `utf8mb4_bin`.


Most use cases require a more commonly-used collation. It is possible to achieve that using the `COLLATE` clause:


```
alter table t1
  add col1 varchar(100) collate utf8mb4_uca1400_ai_ci as
  (json_value(js1, '$.string_column') collate utf8mb4_uca1400_ai_ci),
  add index(col1);
...
select  ... 
where
  json_value(js1, '$.string_column') collate utf8mb4_uca1400_ai_ci='string-value';
```

## References


* [MDEV-35616](https://jira.mariadb.org/browse/MDEV-35616): Add basic optimizer support for virtual columns

