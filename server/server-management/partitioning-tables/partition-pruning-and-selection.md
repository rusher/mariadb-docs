
# Partition Pruning and Selection

When a WHERE clause is related to the partitioning expression, the optimizer knows which partitions are relevant for the query. Other partitions will not be read. This optimization is called *partition pruning*.


[EXPLAIN PARTITIONS](../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/outdated-pages/explain-formatjson-in-mysql.md) can be used to know which partitions will be read for a given query. A column called `partitions` will contain a comma-separated list of the accessed partitions. For example:


```
EXPLAIN PARTITIONS SELECT * FROM orders WHERE id < 15000000;
+------+-------------+--------+------------+-------+---------------+---------+---------+------+------+-------------+
| id   | select_type | table  | partitions | type  | possible_keys | key     | key_len | ref  | rows | Extra       |
+------+-------------+--------+------------+-------+---------------+---------+---------+------+------+-------------+
|    1 | SIMPLE      | orders | p0,p1      | range | PRIMARY       | PRIMARY | 4       | NULL |    2 | Using where |
+------+-------------+--------+------------+-------+---------------+---------+---------+------+------+-------------+
```

Sometimes the WHERE clause does not contain the necessary information to use partition pruning, or the optimizer cannot infer this information. However, we may know which partitions are relevant for the query. Since [MariaDB 10.0](../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md), we can force MariaDB to only access the specified partitions by adding a PARTITION clause. This feature is called *partition selection*. For example:


```
SELECT * FROM orders PARTITION (p3) WHERE user_id = 50;
SELECT * FROM orders PARTITION (p2,p3) WHERE user_id >= 40;
```

The PARTITION clause is supported for all DML statements:


* [SELECT](../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)
* [INSERT](../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/insert-function.md)
* [UPDATE](../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md)
* [DELETE](../../reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/delete.md)
* [REPLACE](../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/replace-function.md)


## Partition Pruning and Triggers


In general, partition pruning is applied to statements contained in [triggers](../../server-usage/programming-customizing-mariadb/triggers-events/triggers/triggers-and-implicit-locks.md).


However, note that if a `BEFORE INSERT` or `BEFORE UPDATE` trigger is defined on a table, MariaDB doesn't know in advance if the columns used in the partitioning expression will be changed. For this reason, it is forced to lock all partitions.

<span></span>
