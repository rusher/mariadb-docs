
# DBT3 Benchmark Queries

Known things about DBT-3 benchmark and its queries



## Q1


A simple, one-table query.


```
select
        l_returnflag,
        l_linestatus,
        sum(l_quantity) as sum_qty,
        sum(l_extendedprice) as sum_base_price,
        sum(l_extendedprice * (1 - l_discount)) as sum_disc_price,
        sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) as sum_charge,
        avg(l_quantity) as avg_qty,
        avg(l_extendedprice) as avg_price,
        avg(l_discount) as avg_disc,
        count(*) as count_order
from
        lineitem
where
        l_shipdate <= date_sub('1998-12-01', interval 79 day)
group by
        l_returnflag,
        l_linestatus
order by
        l_returnflag,
        l_linestatus;
```

Query plan:


```
+------+-------------+----------+------+---------------+------+---------+------+----------+----------------------------------------------+
| id   | select_type | table    | type | possible_keys | key  | key_len | ref  | rows     | Extra                                        |
+------+-------------+----------+------+---------------+------+---------+------+----------+----------------------------------------------+
|    1 | SIMPLE      | lineitem | ALL  | i_l_shipdate  | NULL | NULL    | NULL | 59711977 | Using where; Using temporary; Using filesort |
+------+-------------+----------+------+---------------+------+---------+------+----------+----------------------------------------------+
```

* l_shipdate < date_sub('1998-12-01', interval 79 day) is satisifed by 59,334,576
rows.
* The table has 59,986,052 rows in total.
* There are a total of 4 different values of `(l_returnflag,l_linestatus)`. This means, sorting doesn't matter, and temporary table is a very small heap table.


## Q2


plans starting with table "part" ... - 8sec on cold cache. scale=10 (scale=30 ETA 1min)


## Q3


```
select
       l_orderkey, sum(l_extendedprice*(1-l_discount)) as revenue,
       o_orderdate, o_shippriority
from 
      customer, 
      orders, 
      lineitem
where 
      c_mktsegment = 'BUILDING' and c_custkey = o_custkey
      and l_orderkey = o_orderkey and o_orderdate < date '1995-03-15'
      and l_shipdate > date '1995-03-15'
group by l_orderkey, o_orderdate, o_shippriority
order by revenue desc, o_orderdate
limit 10;
```

There seems to be an improvement in mysql-5.6: [dbt-3-q3-6-x-performance-in-mysql-5610.html](https://jorgenloland.blogspot.ru/2013/02/dbt-3-q3-6-x-performance-in-mysql-5610.html)


(speedup can be observed only when the query is in the form like the above (TODO: figure out where do different forms of queries come from?))


EXPLAINs (scale=10):


```
+------+-------------+----------+--------+---------------------------------------------------------+---------+---------+----------------------------+----------+----------------------------------------------+
| id   | select_type | table    | type   | possible_keys                                           | key     | key_len | ref                        | rows     | Extra                                        |
+------+-------------+----------+--------+---------------------------------------------------------+---------+---------+----------------------------+----------+----------------------------------------------+
|    1 | SIMPLE      | orders   | ALL    | NULL                                                    | NULL    | NULL    | NULL                       | 15115145 | Using where; Using temporary; Using filesort |
|    1 | SIMPLE      | customer | eq_ref | PRIMARY                                                 | PRIMARY | 4       | dbt3sf10.orders.o_custkey  |        1 | Using where                                  |
|    1 | SIMPLE      | lineitem | ref    | PRIMARY,i_l_shipdate,i_l_orderkey,i_l_orderkey_quantity | PRIMARY | 4       | dbt3sf10.orders.o_orderkey |        2 | Using where                                  |
+------+-------------+----------+--------+---------------------------------------------------------+---------+---------+----------------------------+----------+----------------------------------------------+
```

```
+------+-------------+----------+--------+---------------------------------------------------------+----------------+---------+----------------------------+---------+---------------------------------------------------------------------+
| id   | select_type | table    | type   | possible_keys                                           | key            | key_len | ref                        | rows    | Extra                                                               |
+------+-------------+----------+--------+---------------------------------------------------------+----------------+---------+----------------------------+---------+---------------------------------------------------------------------+
|    1 | SIMPLE      | orders   | range  | PRIMARY,i_o_date_clerk                                  | i_o_date_clerk | 4       | NULL                       | 7557572 | Using index condition; Using where; Using temporary; Using filesort |
|    1 | SIMPLE      | customer | eq_ref | PRIMARY                                                 | PRIMARY        | 4       | dbt3sf10.orders.o_custkey  |       1 | Using where                                                         |
|    1 | SIMPLE      | lineitem | ref    | PRIMARY,i_l_shipdate,i_l_orderkey,i_l_orderkey_quantity | PRIMARY        | 4       | dbt3sf10.orders.o_orderkey |       2 | Using where                                                         |
+------+-------------+----------+--------+---------------------------------------------------------+----------------+---------+----------------------------+---------+---------------------------------------------------------------------+
```

With statistics on 'building': we get a plan of customer, orders, lineitem. It is 5% worse. There seems to be no other possibilities.


## Q5


Nothing good so far.


watch the "c_nationkey = s_nationkey" condition. It is a "side" condition (ie it is not from the "natural" relationships between tables). It is not clear whether accounting for its selectivity will give anything)


## Q8


```
Timour is analyzing this query.
```

## Q9


```
Timour is analyzing this query.
```

```
+------+-------------+----------+--------+----------------------------------------------------------------------------------------+---------------------+---------+--------------------------------------------------+------+----------+---------------------------------------------------------------------------+
| id   | select_type | table    | type   | possible_keys                                                                          | key                 | key_len | ref                                              | rows | filtered | Extra                                                                     |
+------+-------------+----------+--------+----------------------------------------------------------------------------------------+---------------------+---------+--------------------------------------------------+------+----------+---------------------------------------------------------------------------+
|    1 | SIMPLE      | nation   | ALL    | PRIMARY                                                                                | NULL                | NULL    | NULL                                             |   25 |   100.00 | Using temporary; Using filesort                                           |
|    1 | SIMPLE      | supplier | ref    | PRIMARY,i_s_nationkey                                                                  | i_s_nationkey       | 5       | dbt3.nation.n_nationkey                          | 4077 |   100.00 | Using index                                                               |
|    1 | SIMPLE      | partsupp | ref    | PRIMARY,i_ps_partkey,i_ps_suppkey                                                      | i_ps_suppkey        | 4       | dbt3.supplier.s_suppkey                          |   38 |   100.00 | Using join buffer (flat, BKA join); Key-ordered Rowid-ordered scan        |
|    1 | SIMPLE      | part     | eq_ref | PRIMARY                                                                                | PRIMARY             | 4       | dbt3.partsupp.ps_partkey                         |    1 |   100.00 | Using where; Using join buffer (incremental, BKA join); Key-ordered scan  |
|    1 | SIMPLE      | lineitem | ref    | PRIMARY,i_l_suppkey_partkey,i_l_partkey,i_l_suppkey,i_l_orderkey,i_l_orderkey_quantity | i_l_suppkey_partkey | 10      | dbt3.partsupp.ps_partkey,dbt3.supplier.s_suppkey |    3 |   100.00 | Using join buffer (incremental, BKA join); Key-ordered Rowid-ordered scan |
|    1 | SIMPLE      | orders   | eq_ref | PRIMARY                                                                                | PRIMARY             | 4       | dbt3.lineitem.l_orderkey                         |    1 |   100.00 | Using join buffer (incremental, BKA join); Key-ordered scan               |
+------+-------------+----------+--------+----------------------------------------------------------------------------------------+---------------------+---------+--------------------------------------------------+------+----------+---------------------------------------------------------------------------+
```

Watch for "p_name like ..." condition.
What if we force table part to be the 1st.


## Q10


## Q13


```
SergeyP is analyzing this query.
```

```
select
	c_count,
	count(*) as custdist
from
	(
		select
			c_custkey,
			count(o_orderkey) as c_count
		from
			customer left outer join orders on
				c_custkey = o_custkey
				and o_comment not like '%express%requests%'
		group by
			c_custkey
	) as c_orders
group by
	c_count
order by
	custdist desc,
	c_count desc;
```

## Q15


```
SergeyP is analyzing this query.
```

## Q17


```
Timour is analyzing this query.
```

* Q17 cannot benefit from [MDEV-89](https://jira.mariadb.org/browse/MDEV-89) because the '<' predicate depends on both query tables. No matter what is the join order, the subquery has to be attached to the last table in the plan.


* There are no sargable conditions for 'lineitem', and it is bigger than 'part', and
selectivity(p_brand = 'Brand#43' and p_container = 'WRAP DRUM') = 0.1%. Therefore table part should be first in the join plan.


* selectivity(p_partkey = l_partkey) << selectivity(l_quantity < (select ...)), therefore the expensive subquery will be placed correctly after the cheap join condition.


* One possible improvement for this query is to stop the execution of the subquery as soon as the selected expression becomes false. In this case stop when (l_quantity >= 0.2 * avg(l_quantity)).


```
select sum(l_extendedprice) / 7.0 as avg_yearly
from lineitem, part
where
  p_partkey = l_partkey
  and p_brand = 'Brand#43'
  and p_container = 'WRAP DRUM'
  and l_quantity < (select 0.2 * avg(l_quantity) from lineitem where l_partkey = p_partkey);
```

```
+------+--------------------+----------+------+---------------------------------+---------------------+---------+---------------------+---------+----------+------------------------------------------------------------------------------------------------+
| id   | select_type        | table    | type | possible_keys                   | key                 | key_len | ref                 | rows    | filtered | Extra                                                                                          |
+------+--------------------+----------+------+---------------------------------+---------------------+---------+---------------------+---------+----------+------------------------------------------------------------------------------------------------+
|    1 | PRIMARY            | part     | ALL  | PRIMARY                         | NULL                | NULL    | NULL                | 6000000 |     1.39 | Using where                                                                                    |
|    1 | PRIMARY            | lineitem | ref  | i_l_suppkey_partkey,i_l_partkey | i_l_suppkey_partkey | 5       | dbt3.part.p_partkey |      29 |   100.00 | Using where; Subqueries: 2; Using join buffer (flat, BKA join); Key-ordered Rowid-ordered scan |
|    2 | DEPENDENT SUBQUERY | lineitem | ref  | i_l_suppkey_partkey,i_l_partkey | i_l_suppkey_partkey | 5       | dbt3.part.p_partkey |      29 |   100.00 |                                                                                                |
+------+--------------------+----------+------+---------------------------------+---------------------+---------+---------------------+---------+----------+------------------------------------------------------------------------------------------------+
```

## Q20


* This query will benefit from [MWL#253](https://askmonty.org/worklog/?tid=253) (Exact index stats), and [MDEV-83](https://jira.mariadb.org/browse/MDEV-83) (Cost-based choice for the pushdown of subqueries to joined tables).


```
explain extended
select sql_calc_found_rows 
  s_name, s_address
from 
  supplier, nation
where s_suppkey in (select ps_suppkey from partsupp
                    where ps_partkey in (select p_partkey from part where p_name like 'g%')
                          and ps_availqty >
                              (select 0.5 * sum(l_quantity)
                               from lineitem
                               where l_partkey = ps_partkey and l_suppkey = ps_suppkey
                                     and l_shipdate >= date('1993-01-01') and l_shipdate < date('1993-01-01') + interval '1' year ))
and s_nationkey = n_nationkey
and n_name = 'UNITED STATES'
order by s_name
limit 10;
```


CC BY-SA / Gnu FDL

