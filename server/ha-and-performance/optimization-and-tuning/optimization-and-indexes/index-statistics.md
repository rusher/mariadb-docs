# Index Statistics

## How Index Statistics Help the Query Optimizer

The MariaDB query optimizer decides how best to execute each query based largely on the details of the indexes involved.

The index statistics help inform these decisions. Imagine yourself choosing whether to look up a number in a phone book, or in your personal address book. You'd choose the personal phone book if at all possible, as it would (usually!) contain far fewer records and be quicker to search.

Now imagine getting to your personal address book and finding it has twice the number of entries as the phone book. Your search would be slower. The same process applies to the query optimizer, so having access to up-to-date and accurate statistics is critical.

## Value Groups

The statistics are mainly based on groups of index elements of the same value. In a primary key, every index is unique, so every group size is one. In a non-unique index, you may have multiple keys with the same value. A worst-case example would be having large groups with the same value, for example an index on a boolean field.

MariaDB makes heavy use of the average group size statistic. For example, if there are 100 rows, and twenty groups with the same index values, the average group size would be five.

However, averages can be skewed by extremes, and the usual culprit is NULL values. The row of 100 may have 19 groups with an average size of 1, while the other 81 values are all NULL. MariaDB may think five is a good average size and choose to use that index, and then end up having to read through 81 rows with identical keys, taking longer than an alternative.

## Dealing with NULLs

There are three main approaches to the problem of NULLs. NULL index values can be treated as a single group (nulls\_equal). This is usually fine, but if you have large numbers of NULLs the average group size is slanted higher, and the optimizer may miss using the index for ref accesses when it would be useful. This is the default used by XtraDB/InnoDB and MyISAM. Nulls\_unequal is the opposite approach, with each NULL forming its own group of one. Conversely, the average group size is slanted lower, and the optimizer may use the index for ref accesses when not suitable. This is the default used by the Aria storage engine. A third options sees NULL's ignored altogether from index group calculations.

The default approaches can be changed by setting the [aria\_stats\_method](../../../reference/storage-engines/aria/aria-system-variables.md), [myisam\_stats\_method](../../../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md) and [innodb\_stats\_method](../../../reference/storage-engines/innodb/innodb-system-variables.md) server variables.

## Null-Safe and Regular Comparisons

The comparison operator used plays an important role. If two values are compared with <=> (see the [null-safe-equal](../../../reference/sql-statements-and-structure/operators/comparison-operators/null-safe-equal.md) comparison operator), and both are null, 1 is returned. If the same values are compared with = (see the [equal](../../../reference/sql-statements-and-structure/operators/comparison-operators/equal.md) comparison operator) null is returned. For example:

```
SELECT 1 <=> 1, NULL <=> NULL, 1 <=> NULL;
+---------+---------------+------------+
| 1 <=> 1 | NULL <=> NULL | 1 <=> NULL |
+---------+---------------+------------+
|       1 |             1 |          0 |
+---------+---------------+------------+

SELECT 1 = 1, NULL = NULL, 1 = NULL;
+-------+-------------+----------+
| 1 = 1 | NULL = NULL | 1 = NULL |
+-------+-------------+----------+
|     1 |        NULL |     NULL |
+-------+-------------+----------+
```

## Engine-Independent Statistics

[MariaDB 10.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1001-release-notes) introduced a way to gather statistics independently of the storage engine. See [Engine-independent table statistics](../query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md).

## Histogram-Based Statistics

[Histogram-Based Statistics](../query-optimizations/statistics-for-optimizing-queries/histogram-based-statistics.md) were introduced in [MariaDB 10.0.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1002-release-notes), and are collected by default from [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes).

## See Also

* [User Statistics](../query-optimizations/statistics-for-optimizing-queries/user-statistics.md). This plugin provides user, client, table and index usage statistics.
* [InnoDB Persistent Statistics](../query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md)
* [Engine-independent Statistics](../query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md)
* [Histogram-based Statistics](../query-optimizations/statistics-for-optimizing-queries/histogram-based-statistics.md)
* [Ignored Indexes](ignored-indexes.md)

CC BY-SA / Gnu FDL
