
# EXPLAIN FORMAT=JSON


## Synopsis


`EXPLAIN FORMAT=JSON` is a variant of [EXPLAIN](explain.md) command that produces output in JSON form. The output always has one row which has only one column titled "`JSON`". The contents are a JSON representation of the query plan, formatted for readability:


```
EXPLAIN FORMAT=JSON SELECT * FROM t1 WHERE col1=1\G
```

```
*************************** 1. row ***************************
EXPLAIN: {
  "query_block": {
    "select_id": 1,
    "table": {
      "table_name": "t1",
      "access_type": "ALL",
      "rows": 1000,
      "filtered": 100,
      "attached_condition": "(t1.col1 = 1)"
    }
  }
}
```

## Output is different from MySQL


The output of MariaDB's `EXPLAIN FORMAT=JSON` is different from `EXPLAIN FORMAT=JSON` in MySQL.The reasons for that are:


* MySQL's output has deficiencies. Some are listed here: [EXPLAIN FORMAT=JSON in MySQL](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/training-and-tutorials/advanced-mariadb-articles/development-articles/outdated-pages/explain-formatjson-in-mysql)
* The output of MySQL's `EXPLAIN FORMAT=JSON` is not defined. Even MySQL Workbench has trouble parsing it (see this [blog post](https://s.petrunia.net/blog/?p=93)).
* MariaDB has query optimizations that MySQL does not have. Ergo, MariaDB generates query plans that MySQL does not generate.


A (as yet incomplete) list of how MariaDB's output is different from MySQL can be found here: [EXPLAIN FORMAT=JSON differences from MySQL](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/training-and-tutorials/advanced-mariadb-articles/development-articles/outdated-pages/explain-format-json-differences).


## Output Format


TODO: MariaDB's output format description.


## See Also


* [ANALYZE FORMAT=JSON](analyze-format-json.md) produces output like `EXPLAIN FORMAT=JSON`, but amended with the data from query execution.

