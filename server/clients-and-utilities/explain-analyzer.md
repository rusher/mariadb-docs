
# EXPLAIN Analyzer

The EXPLAIN Analyzer is no longer active.


The [EXPLAIN Analyzer](https://mariadb.org/explain_analyzer/analyze/) was an online tool for analyzing and optionally sharing the output of both [EXPLAIN](../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/outdated-pages/explain-formatjson-in-mysql.md) and `<code>EXPLAIN EXTENDED</code>`.


## Using the Analyzer


Using the analyzer is very simple.


1. In the mariadb client, run `<code>EXPLAIN</code>` on a query and copy the output. For example:


```
EXPLAIN SELECT * FROM t1 INNER JOIN t2 INNER JOIN t3 WHERE t1.a=t2.a AND t2.a=t3.a;
+------+-------------+-------+------+---------------+------+---------+------+------+--------------------------------------------------------+
| id   | select_type | table | type | possible_keys | key  | key_len | ref  | rows | Extra                                                  |
+------+-------------+-------+------+---------------+------+---------+------+------+--------------------------------------------------------+
|    1 | SIMPLE      | t1    | ALL  | NULL          | NULL | NULL    | NULL |    3 |                                                        |
|    1 | SIMPLE      | t2    | ALL  | NULL          | NULL | NULL    | NULL |    3 | Using where; Using join buffer (flat, BNL join)        |
|    1 | SIMPLE      | t3    | ALL  | NULL          | NULL | NULL    | NULL |    3 | Using where; Using join buffer (incremental, BNL join) |
+------+-------------+-------+------+---------------+------+---------+------+------+--------------------------------------------------------+
3 rows in set (0.00 sec)
```

1. Paste the output into the [EXPLAIN Analyzer input box](https://mariadb.org/explain_analyzer/analyze/) and click the "Analyze Explain" button.


1. The formatted `<code>EXPLAIN</code>` will be shown. You can now click on various part to get more information about them.


### Some Notes:


* As you can see in the example above, you don't need to chop off the query line or the command prompt.
* To save the EXPLAIN, so you can share it, or just for future reference, click the "Save Explain for analysis and sharing" button and then click the "Analyze Explain" button. You will be given a link which leads to your saved `<code>EXPLAIN</code>`. For example, the above explain can be viewed here: [](https://mariadb.org/explain_analyzer/analyze/)
* Some of the elements in the formatted `<code>EXPLAIN</code>` are clickable. Clicking on them will show pop-up help related to that element.


## Clients which integrate with the Explain Analyzer


The Analyzer has an API that client programs can use to send EXPLAINs. If you are a client application developer, see the [EXPLAIN Analyzer API](explain-analyzer-api.md) page for details.


The following clients have support for the EXPLAIN Analyzer built in:


### HeidiSQL


[HeidiSQL](https://www.heidisql.com/) has a button when viewing a query that sends the query to the explain analyzer.

