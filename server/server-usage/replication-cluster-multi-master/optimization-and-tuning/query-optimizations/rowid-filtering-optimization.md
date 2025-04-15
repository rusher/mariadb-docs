
# Rowid Filtering Optimization


The target use case for rowid filtering is as follows:


* a table uses ref access on index IDX1
* but it also has a fairly restrictive range predicate on another index IDX2.


In this case, it is advantageous to:


* Do an index-only scan on index IDX2 and collect rowids of index records into a data structure that allows filtering (let's call it $FILTER).
* When doing ref access on IDX1, check $FILTER before reading the full record.


## Example


Consider a query


```
SELECT ...
FROM orders JOIN lineitem ON o_orderkey=l_orderkey
WHERE
  l_shipdate BETWEEN '1997-01-01' AND '1997-01-31' AND
  o_totalprice between 200000 and 230000;
```

Suppose the condition on `<code>l_shipdate</code>` is very restrictive, which means lineitem table should go first in the join order. Then, the optimizer can use `<code>o_orderkey=l_orderkey</code>` equality to do an index lookup to get the order the line item is from. On the other hand `<code>o_totalprice between ...</code>` can also be rather selective.


With filtering, the query plan would be:


```
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: lineitem
         type: range
possible_keys: PRIMARY,i_l_shipdate,i_l_orderkey,i_l_orderkey_quantity
          key: i_l_shipdate
      key_len: 4
          ref: NULL
         rows: 98
        Extra: Using index condition
*************************** 2. row ***************************
           id: 1
  select_type: SIMPLE
        table: orders
         type: eq_ref|filter
possible_keys: PRIMARY,i_o_totalprice
          key: PRIMARY|i_o_totalprice
      key_len: 4|9
          ref: dbt3_s001.lineitem.l_orderkey
         rows: 1 (5%)
        Extra: Using where; Using rowid filter
```

Note that table `<code>orders</code>` has "Using rowid filter". The `<code>type</code>` column has `<code>"|filter"</code>`, the `<code>key</code>` column shows the index that is used to construct the filter. `<code>rows</code>` column shows the expected filter selectivity, it is 5%.


ANALYZE FORMAT=JSON output for table orders will show


```
"table": {
      "table_name": "orders",
      "access_type": "eq_ref",
      "possible_keys": ["PRIMARY", "i_o_totalprice"],
      "key": "PRIMARY",
      "key_length": "4",
      "used_key_parts": ["o_orderkey"],
      "ref": ["dbt3_s001.lineitem.l_orderkey"],
      "rowid_filter": {
        "range": {
          "key": "i_o_totalprice",
          "used_key_parts": ["o_totalprice"]
        },
        "rows": 69,
        "selectivity_pct": 4.6,
        "r_rows": 71,
        "r_selectivity_pct": 10.417,
        "r_buffer_size": 53,
        "r_filling_time_ms": 0.0716
      }
```

Note the `<code>rowid_filter</code>` element. It has a `<code>range</code>` element inside it. `<code>selectivity_pct</code>` is the expected selectivity, accompanied by the `<code>r_selectivity_pct</code>` showing the actual observed selectivity.


## Details


* The optimizer makes a cost-based decision about when the filter should be used.
* The filter data structure is currently an ordered array of rowids. (a Bloom filter would be better here and will probably be introduced in the future versions).
* The optimization needs to be supported by the storage engine. At the moment, it is supported by [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) and [MyISAM](../../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md). It is not supported in [partitioned tables](../../../../server-management/partitioning-tables/README.md).


## Limitations


* Rowid Filtering can't be used with a backward-ordered index scan. When the optimizer needs to execute an ORDER BY ... DESC query and decides to handle it with a backward-ordered index scan, it will disable Rowid Filtering.


## Control


Rowid filtering can be switched on/off using `<code>rowid_filter</code>` flag in the [optimizer_switch](../system-variables/server-system-variables.md#optimizer_switch) variable. By default, the optimization is enabled.

