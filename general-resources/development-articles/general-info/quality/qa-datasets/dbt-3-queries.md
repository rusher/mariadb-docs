
# DBT-3 Queries

## Q1


See [MDEV-4309](https://jira.mariadb.org/browse/MDEV-4309) (just speeding up temptable-based GROUP BY execution).
Optimizer seems to make a good choice here.


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
        l_shipdate <= date_sub('1998-12-01', interval 63 day)
group by
        l_returnflag,
        l_linestatus
order by
        l_returnflag,
        l_linestatus
```

## Q4


See [MDEV-6015](https://jira.mariadb.org/browse/MDEV-6015).


Applicable optimizations:


* subquery cache brings no benefit because subquery refers to outer_table.pk, which is different for each row
* EXISTS-to-IN is applicable

  * After that, BKA brings slight speedup


Comments on query plan choice


* It seems, we're using the best possible query plan here.


```
select
	o_orderpriority,
	count(*) as order_count
from
	orders
where
	o_orderdate >= '1995-06-06'
	and o_orderdate < date_add('1995-06-06', interval 3 month)
	and exists (
		select
			*
		from
			lineitem
		where
			l_orderkey = o_orderkey
			and l_commitdate < l_receiptdate
	)
group by
	o_orderpriority
order by
	o_orderpriority;
```

.


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
