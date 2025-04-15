
# ANALYZE: Interpreting rows and filtered members

This article describes how to interpret `<code>r_rows</code>` and `<code>r_filtered</code>` members in ANALYZE FORMAT=JSON when an index-based access method is used.



## Index-based access method


Index-based access method may employ some or all of the following:


* [Index Condition Pushdown](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/index-condition-pushdown.md)
* [Rowid Filtering](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/rowid-filtering-optimization.md)
* attached_condition checking


Consider a table access which does all three:


```
"table": {
    "table_name": "t1",
    "access_type": "range",
    "possible_keys": ...,
    "key": "INDEX1",
    ...
    "rowid_filter": {
      ...
      "r_selectivity_pct": n.nnn,
    },
    ...
    "rows": 123,
    "r_rows": 125,
    ...
    "filtered": 8.476269722,
    "r_filtered": 100,
    "index_condition": "cond1",
    "attached_condition": "cond2"
  }
```

The access is performed as follows:


### Access diagram


![index-read-diagram-3](../../../../../../.gitbook/assets/analyze-interpreting-rows-and-filtered-members/+image/index-read-diagram-3.png "index-read-diagram-3")


## Statistics values in MariaDB before 11.5


In MariaDB versions before 11.5, the counters were counted as follows:


![index-read-stats-old](../../../../../../.gitbook/assets/analyze-interpreting-rows-and-filtered-members/+image/index-read-stats-old.png "index-read-stats-old")


that is,


* `<code>r_rows</code>` is counted after Index Condition Pushdown check and Rowid Filter check.
* `<code>r_filtered</code>` only counts selectivity of the `<code>attached_condition</code>`.
* selectivity of the Rowid Filter is in `<code>rowid_filter.r_selectivity_pct</code>`.


## Statistics values in [MariaDB 11.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md) and later versions


Starting from [MariaDB 11.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md) ([MDEV-18478](https://jira.mariadb.org/browse/MDEV-18478)), the row counters are:


* `<code>r_index_rows</code>` counts the number of enumerated index tuples, before any checks are made
* `<code>r_rows</code>` is the same as before - number of rows after index checks.


The selectivity counters are:


* `<code>r_icp_filtered</code>` is the percentage of records left after pushed index condition check.
* `<code>rowid_filter.r_selectivity_pct</code>` shows selectivity of Rowid Filter, as before.
* `<code>r_filtered</code>` is the selectivity of `<code>attached_condition</code>` check, as before.
* `<code>r_total_filtered</code>` is the combined selectivity of all checks.


![index-read-stats-new](../../../../../../.gitbook/assets/analyze-interpreting-rows-and-filtered-members/+image/index-read-stats-new.png "index-read-stats-new")


### ANALYZE output members


in ANALYZE FORMAT=JSON output these members are placed as follows:


```
"table": {
    "table_name": ...,

    "rows": 426,
    "r_index_rows": 349,
    "r_rows": 34,
```

Whenever applicable, `<code>r_index_rows</code>` is shown. It is comparable with `<code>rows</code>` - both are numbers of rows to enumerate before any filtering is done. 
If `<code>r_index_rows</code>` is not shown, `<code>r_rows</code>` shows the number of records enumerated.


Then, filtering members:


```
...
    "filtered": 8.476269722,
    "r_total_filtered": 9.742120344,
```

`<code>filtered</code>` is comparable with `<code>r_total_filtered</code>`: both show total amount of filtering.


```
...
    "index_condition": "lineitem.l_quantity > 47",
    "r_icp_filtered": 100,
```

ICP and its observed filtering. The optimizer doesn't compute an estimate for this currently.


```
...
    "attached_condition": "lineitem.l_shipDATE between '1997-01-01' and '1997-06-30'",
    "r_filtered": 100
```

`<code>attached_condition</code>` and its observed filtering.

