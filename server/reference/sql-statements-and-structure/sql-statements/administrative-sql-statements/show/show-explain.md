
# SHOW EXPLAIN


## Syntax


```
SHOW EXPLAIN [FORMAT=JSON] FOR <connection_id>;
EXPLAIN [FORMAT=JSON] FOR CONNECTION <connection_id>;
```

## Description


The `<code>SHOW EXPLAIN</code>` command allows one to get an [EXPLAIN](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/outdated-pages/explain-formatjson-in-mysql.md) (that is, a
description of a query plan) of a query running in a certain connection.


```
SHOW EXPLAIN FOR <connection_id>;
```

will produce an `<code>EXPLAIN</code>` output for the query that connection number `<code>connection_id</code>` is running. The connection id can be obtained with [SHOW PROCESSLIST](show-processlist.md).


```
SHOW EXPLAIN FOR 1;
+------+-------------+-------+-------+---------------+------+---------+------+---------+-------------+
| id   | select_type | table | type  | possible_keys | key  | key_len | ref  | rows    | Extra       |
+------+-------------+-------+-------+---------------+------+---------+------+---------+-------------+
|    1 | SIMPLE      | tbl   | index | NULL          | a    | 5       | NULL | 1000107 | Using index |
+------+-------------+-------+-------+---------------+------+---------+------+---------+-------------+
1 row in set, 1 warning (0.00 sec)
```

The output is always accompanied with a warning which shows the query the
target connection is running (this shows what the `<code>EXPLAIN</code>` is for):


```
SHOW WARNINGS;
+-------+------+------------------------+
| Level | Code | Message                |
+-------+------+------------------------+
| Note  | 1003 | select sum(a) from tbl |
+-------+------+------------------------+
1 row in set (0.00 sec)
```

### EXPLAIN FOR CONNECTION



##### MariaDB starting with [10.9](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-109.md)
The `<code>EXPLAIN FOR CONNECTION</code>` syntax was added for MySQL compatibility.


### FORMAT=JSON



##### MariaDB starting with [10.9](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-109.md)
`<code>SHOW EXPLAIN [FORMAT=JSON] FOR &lt;connection_id&gt;</code>` extends `<code>SHOW EXPLAIN</code>` to return more detailed JSON output. 


### Possible Errors


The output can be only produced if the target connection is *currently* running a
query, which has a ready query plan. If this is not the case, the output will
be:


```
SHOW EXPLAIN FOR 2;
ERROR 1932 (HY000): Target is not running an EXPLAINable command
```

You will get this error when:


* the target connection is not running a command for which one can run `<code>EXPLAIN</code>`
* the target connection is running a command for which one can run `<code>EXPLAIN</code>`, but

  * there is no query plan yet (for example, tables are open and locks are
 acquired before the query plan is produced)


### Differences Between SHOW EXPLAIN and EXPLAIN Outputs


#### Background


In MySQL, `<code>EXPLAIN</code>` execution takes a slightly different route from the way
the real query (typically the `<code>SELECT</code>`) is optimized. This is unfortunate,
and has caused a number of bugs in `<code>EXPLAIN</code>`. (For example, see
[MDEV-326](https://jira.mariadb.org/browse/MDEV-326), [MDEV-410](https://jira.mariadb.org/browse/MDEV-410), and
[lp:1013343](https://bugs.launchpad.net/maria/+bug/1013343).
[lp:992942](https://bugs.launchpad.net/maria/+bug/992942) is not directly
about `<code>EXPLAIN</code>`, but it also would not have existed if MySQL didn't try to delete
parts of a query plan in the middle of the query)


`<code>SHOW EXPLAIN</code>` examines a running `<code>SELECT</code>`, and hence its output may be
slightly different from what `<code>EXPLAIN SELECT</code>` would produce. We did our best
to make sure that either the difference is negligible, or `<code>SHOW EXPLAIN</code>`'s
output is closer to reality than `<code>EXPLAIN</code>`'s output.


#### List of Recorded Differences


* `<code>SHOW EXPLAIN</code>` may have Extra='`<code>no matching row in const table</code>`', where `<code>EXPLAIN</code>` would produce Extra='`<code>Impossible WHERE ...</code>`'
* For queries with subqueries, `<code>SHOW EXPLAIN</code>` may print `<code>select_type==PRIMARY</code>` where regular `<code>EXPLAIN</code>` used to print `<code>select_type==SIMPLE</code>`, or vice versa.


#### Required Permissions


Running `<code>SHOW EXPLAIN</code>` requires the same permissions as running [SHOW PROCESSLIST](show-processlist.md) would.


## See Also


* [EXPLAIN](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/outdated-pages/explain-formatjson-in-mysql.md)
* [EXPLAIN ANALYZE](../analyze-and-explain-statements/explain-analyze.md), which will perform a query and outputs enhanced `<code>EXPLAIN</code>` results.
* [SHOW ANALYZE](show-analyze.md)
* It is also possible to [save EXPLAIN into the slow query log](../../../../../server-management/server-monitoring-logs/slow-query-log/explain-in-the-slow-query-log.md).

