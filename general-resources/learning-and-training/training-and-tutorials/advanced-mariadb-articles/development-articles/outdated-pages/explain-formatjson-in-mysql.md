
# EXPLAIN FORMAT=JSON in MySQL


There are some things that we in MariaDB are not happy with in MySQL/Oracle's implementation of EXPLAIN FORMAT=JSON.


The most important issues are already fixed in MariaDB's [EXPLAIN FORMAT=JSON](explain-format-json-differences.md) implementation. See [EXPLAIN FORMAT=JSON Differences From MySQL](explain-format-json-differences.md) for details.


This page lists things are are not fixed yet.


## Higher priority


* Better display for ORDER/GROUP BY ([MDEV-6995](https://jira.mariadb.org/browse/MDEV-6995))
* Better display for Batched Key Access plans (Plain join buffering is fixed already)


## Nice to have


### Show ranges being scanned


Currently, one can only find the ranges produced by the range optimizer by looking into optimizer_trace. It would be nice if EXPLAIN showed them, too


```
MySQL [dbt3sf1]> explain format=json select * from customer where c_acctbal < -1000 \G
*************************** 1. row ***************************
EXPLAIN: {
  "query_block": {
    "select_id": 1,
    "table": {
      "table_name": "customer",
      "access_type": "range",
      "possible_keys": [
        "c_acctbal",
        "i_c_acctbal_nationkey"
      ],
      "key": "c_acctbal",
      "used_key_parts": [
        "c_acctbal"
      ],
      "key_length": "9",
      "rows": 1,
      "filtered": 100,
      "index_condition": "(`dbt3sf1`.`customer`.`c_acctbal` < -(1000))"
    }
  }
}
```

## Low priority


### Filesort/priority queue


Neither version of EXPLAIN in 5.6 shows the "filesort with small limit" optimization. See [MDEV-6430](https://jira.mariadb.org/browse/MDEV-6430).

