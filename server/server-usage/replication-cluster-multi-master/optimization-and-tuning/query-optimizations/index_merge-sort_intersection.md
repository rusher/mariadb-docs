
# index_merge sort_intersection

Prior to [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md), the `<code>index_merge</code>` access method supported `<code>union</code>`,
`<code>sort-union</code>`, and `<code>intersection</code>` operations. Starting from [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md), the
`<code>sort-intersection</code>` operation is also supported. This allows the use of
`<code>index_merge</code>` in a broader number of cases.


This feature is disabled by default. To enable it, turn on the optimizer switch
`<code>index_merge_sort_intersection</code>` like so:


```
SET optimizer_switch='index_merge_sort_intersection=on'
```

## Limitations of index_merge/intersection


Prior to [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md), the `<code>index_merge</code>` access method had one intersection
strategy called `<code>intersection</code>`. That strategy can only be used when merged
index scans produced rowid-ordered streams. In practice this means that an
`<code>intersection</code>` could only be constructed from equality (=) conditions.


For example, the following query will use `<code>intersection</code>`:


```
MySQL [ontime]> EXPLAIN SELECT AVG(arrdelay) FROM ontime WHERE depdel15=1 AND OriginState ='CA';
+--+-----------+------+-----------+--------------------+--------------------+-------+----+-----+-------------------------------------------------+
|id|select_type|table |type       |possible_keys       |key                 |key_len|ref |rows |Extra                                            |
+--+-----------+------+-----------+--------------------+--------------------+-------+----+-----+-------------------------------------------------+
| 1|SIMPLE     |ontime|index_merge|OriginState,DepDel15|OriginState,DepDel15|3,5    |NULL|76952|Using intersect(OriginState,DepDel15);Using where|
+--+-----------+------+-----------+--------------------+--------------------+-------+----+-----+-------------------------------------------------+
```

but if you replace `<code>OriginState ='CA'</code>` with `<code>OriginState IN ('CA', 'GB')</code>`
(which matches the same number of records), then `<code>intersection</code>` is not usable
anymore:


```
MySQL [ontime]> explain select avg(arrdelay) from ontime where depdel15=1 and OriginState IN ('CA', 'GB');
+--+-----------+------+----+--------------------+--------+-------+-----+-----+-----------+
|id|select_type|table |type|possible_keys       |key     |key_len|ref  |rows |Extra      |
+--+-----------+------+----+--------------------+--------+-------+-----+-----+-----------+
| 1|SIMPLE     |ontime|ref |OriginState,DepDel15|DepDel15|5      |const|36926|Using where|
+--+-----------+------+----+--------------------+--------+-------+-----+-----+-----------+
```

The latter query would also run 5.x times slower (from 2.2 to 10.8 seconds) in
our experiments.


## How index_merge/sort_intersection improves the situation


In [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md), when `<code>index_merge_sort_intersection</code>` is enabled,
`<code>index_merge</code>` intersection plans can be constructed from non-equality
conditions:


```
MySQL [ontime]> explain select avg(arrdelay) from ontime where depdel15=1 and OriginState IN ('CA', 'GB');
+--+-----------+------+-----------+--------------------+--------------------+-------+----+-----+--------------------------------------------------------+
|id|select_type|table |type       |possible_keys       |key                 |key_len|ref |rows |Extra                                                   |
+--+-----------+------+-----------+--------------------+--------------------+-------+----+-----+--------------------------------------------------------+
| 1|SIMPLE     |ontime|index_merge|OriginState,DepDel15|DepDel15,OriginState|5,3    |NULL|60754|Using sort_intersect(DepDel15,OriginState); Using where |
+--+-----------+------+-----------+--------------------+--------------------+-------+----+-----+--------------------------------------------------------+
```

In our tests, this query ran in 3.2 seconds, which is not as good as the case
with two equalities, but still much better than 10.8 seconds we were getting
without `<code>sort_intersect</code>`.


The `<code>sort_intersect</code>` strategy has higher overhead than `<code>intersect</code>` but is
able to handle a broader set of `<code>WHERE</code>` conditions.


![intersect-vs-sort-intersect](../../../../.gitbook/assets/index_merge-sort_intersection/+image/intersect-vs-sort-intersect.png "intersect-vs-sort-intersect")


## When to Use


`<code>index_merge/sort_intersection</code>` works best on tables with lots of records and
where intersections are sufficiently large (but still small enough to make a
full table scan overkill).


The benefit is expected to be bigger for io-bound loads.


## See Also


* [What is MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md)

