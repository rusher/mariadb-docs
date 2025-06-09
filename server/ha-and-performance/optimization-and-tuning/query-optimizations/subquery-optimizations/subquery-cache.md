# Subquery Cache

The goal of the subquery cache is to optimize the evaluation of correlated\
subqueries by storing results together with correlation parameters in a cache\
and avoiding re-execution of the subquery in cases where the result is already\
in the cache.

## Administration

The cache is on by default. One can switch it off using the [optimizer\_switch](../../system-variables/server-system-variables.md#optimizer_switch) `subquery_cache` setting, like so:

```sql
SET optimizer_switch='subquery_cache=off';
```

The efficiency of the subquery cache is visible in 2 statistical variables:

* [Subquery\_cache\_hit](../../system-variables/server-status-variables.md#subquery_cache_hit) - Global counter for all subquery cache hits.
* [Subquery\_cache\_miss](../../system-variables/server-status-variables.md#subquery_cache_miss) - Global counter for all subquery cache misses.

The session variables [tmp\_table\_size](../../system-variables/server-system-variables.md#tmp_table_size) and [max\_heap\_table\_size](../../system-variables/server-system-variables.md#max_heap_table_size)\
influence the size of in-memory temporary tables in the table used\
for caching. It cannot grow more than the minimum of the above variables values\
(see the [Implementation](subquery-cache.md#implementation) section for details).

## Visibility

Your usage of the cache is visible in `EXTENDED EXPLAIN` output (warnings) as`"<expr_cache><//list of parameters//>(//cached expression//)"`.\
For example:

```sql
EXPLAIN EXTENDED SELECT * FROM t1 WHERE a IN (SELECT b FROM t2);
+----+--------------------+-------+------+---------------+------+---------+------+------+----------+-------------+
| id | select_type        | table | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra       |
+----+--------------------+-------+------+---------------+------+---------+------+------+----------+-------------+
|  1 | PRIMARY            | t1    | ALL  | NULL          | NULL | NULL    | NULL |    2 |   100.00 | Using where |
|  2 | DEPENDENT SUBQUERY | t2    | ALL  | NULL          | NULL | NULL    | NULL |    2 |   100.00 | Using where |
+----+--------------------+-------+------+---------------+------+---------+------+------+----------+-------------+
2 rows in set, 1 warning (0.00 sec)

SHOW WARNINGS;
+-------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Level | Code | Message                                                                                                                                                                                                    |
+-------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Note  | 1003 | SELECT `test`.`t1`.`a` AS `a` from `test`.`t1` WHERE <expr_cache><`test`.`t1`.`a`>(<in_optimizer>(`test`.`t1`.`a`,<exists>(SELECT 1 FROM `test`.`t2` WHERE (<cache>(`test`.`t1`.`a`) = `test`.`t2`.`b`)))) |
+-------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)
```

In the example above the presence of`"<expr_cache><`test`.`t1`.`a`>(...)"` is how you know you are\
using the subquery cache.

## Implementation

Every subquery cache creates a temporary table where the results and all\
parameters are stored. It has a unique index over all parameters. First the\
cache is created in a [MEMORY](../../../../reference/storage-engines/memory-storage-engine.md) table (if doing this is impossible the cache becomes\
disabled for that expression). When the table grows up to the minimum of`tmp_table_size` and `max_heap_table_size`, the hit rate will be checked:

* if the hit rate is really small (<0.2) the cache will be disabled.
* if the hit rate is moderate (<0.7) the table will be cleaned (all records\
  deleted) to keep the table in memory
* if the hit rate is high the table will be converted to a disk table\
  (for 5.3.0 it can only be converted to a disk table).

```
hit rate = hit / (hit + miss)
```

## Performance Impact

Here are some examples that show the performance impact of the subquery cache\
(these tests were made on a 2.53 GHz Intel Core 2 Duo MacBook Pro with dbt-3\
scale 1 data set).

| example | cache on | cache off              | gain     | hit    | miss  | hit rate | 1 | 2 | 3 | 4 |
| ------- | -------- | ---------------------- | -------- | ------ | ----- | -------- | - | - | - | - |
| example | cache on | cache off              | gain     | hit    | miss  | hit rate |   |   |   |   |
| 1       | 1.01sec  | 1 hour 31 min 43.33sec | 5445x    | 149975 | 25    | 99.98%   |   |   |   |   |
| 2       | 0.21sec  | 1.41sec                | 6.71x    | 6285   | 220   | 96.6%    |   |   |   |   |
| 3       | 2.54sec  | 2.55sec                | 1.00044x | 151    | 461   | 24.67%   |   |   |   |   |
| 4       | 1.87sec  | 1.95sec                | 0.96x    | 0      | 23026 | 0%       |   |   |   |   |

### Example 1

Dataset from DBT-3 benchmark, a query to find customers with balance near top in their nation:

```sql
select count(*) from customer 
where 
   c_acctbal > 0.8 * (select max(c_acctbal) 
                      from customer C 
                      where C.c_nationkey=customer.c_nationkey
                      group by c_nationkey);
```

### Example 2

DBT-3 benchmark, Query #17

```sql
select sum(l_extendedprice) / 7.0 as avg_yearly 
from lineitem, part 
where 
  p_partkey = l_partkey and 
  p_brand = 'Brand#42' and p_container = 'JUMBO BAG' and 
  l_quantity < (select 0.2 * avg(l_quantity) from lineitem 
                where l_partkey = p_partkey);
```

### Example 3

DBT-3 benchmark, Query #2

```sql
select
        s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
from
        part, supplier, partsupp, nation, region
where
        p_partkey = ps_partkey and s_suppkey = ps_suppkey and p_size = 33
        and p_type like '%STEEL' and s_nationkey = n_nationkey
        and n_regionkey = r_regionkey and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
                select
                        min(ps_supplycost)
                from
                        partsupp, supplier, nation, region
                where
                        p_partkey = ps_partkey and s_suppkey = ps_suppkey
                        and s_nationkey = n_nationkey and n_regionkey = r_regionkey
                        and r_name = 'MIDDLE EAST'
        )
order by
        s_acctbal desc, n_name, s_name, p_partkey;
```

### Example 4

DBT-3 benchmark, Query #20

```sql
select
        s_name, s_address
from
        supplier, nation
where
        s_suppkey in (
                select
                        distinct (ps_suppkey)
                from
                        partsupp, part
                where
                        ps_partkey=p_partkey
                        and p_name like 'indian%'
                        and ps_availqty > (
                                select
                                        0.5 * sum(l_quantity)
                                from
                                        lineitem
                                where
                                        l_partkey = ps_partkey
                                        and l_suppkey = ps_suppkey
                                        and l_shipdate >= '1995-01-01'
                                        and l_shipdate < date_ADD('1995-01-01',interval 1 year)
                                )
        )
        and s_nationkey = n_nationkey and n_name = 'JAPAN'
order by
        s_name;
```

## See Also

* [Query cache](../../buffers-caches-and-threads/query-cache.md)
* blog post describing impact of subquery cache optimization on queries used by DynamicPageList MediaWiki extension
* [mariadb-subquery-cache-in-real-use-case.html](https://varokism.blogspot.ru/2013/06/mariadb-subquery-cache-in-real-use-case.html) Another use case from the real world
* [What is MariaDB 5.3](broken-reference)

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
