
# DISTINCT removal in aggregate functions

## Basics


One can use `<code>DISTINCT</code>` keyword to de-duplicate the arguments of an aggregate function. For example:


```
SELECT COUNT(DISTINCT col1) FROM tbl1;
```

In order to compute this, MariaDB has to collect the values of `<code>col1</code>` and remove the duplicates. This may be computationally expensive.


After the fix for [MDEV-30660](https://jira.mariadb.org/browse/MDEV-30660) (available from [MariaDB 10.5.25](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10-5-25-release-notes.md), [MariaDB 10.6.18](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-18-release-notes.md), [MariaDB 10.11.8](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-8-release-notes.md), [MariaDB 11.0.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes.md), [MariaDB 11.1.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes.md), [MariaDB 11.2.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes.md), [MariaDB 11.4.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-2-release-notes.md)), the optimizer can detect certain
cases when argument of aggregate function will not have duplicates and so de-duplication can be skipped.


## When one can skip de-duplication


A basic example: if we're doing a select from one table, then the values of `<code>primary_key</code>` are already distinct:


```
SELECT aggregate_func(DISTINCT tbl.primary_key, ...) FROM tbl;
```

If the SELECT has other constant tables, that's also ok, as they will not create duplicates.


The next step: a part of the primary key can be "bound" by the GROUP BY clause. Consider a query:


```
SELECT aggregate_func(DISTINCT t1.pk1, ...) FROM t1 GROUP BY t1.pk2;
```

Suppose the table has `<code>PRIMARY KEY(pk1, pk2)</code>`. Grouping by `<code>pk2</code>` fixes the value of `<code>pk2</code>` within each group. Then, the values of `<code>pk1</code>` must be unique within each group, and de-duplication is not necessary.


## Observability


`<code>EXPLAIN</code>` or `<code>EXPLAIN FORMAT=JSON</code>` do not show any details about how aggregate functions are computed. One has to look at the Optimizer Trace. Search for `<code>aggregator_type</code>`:


When de-duplication is necessary, it will show:


```
{
            "prepare_sum_aggregators": {
              "function": "count(distinct t1.col1)",
              "aggregator_type": "distinct"
            }
          }
```

When de-duplication is not necessary, it will show:


```
{
            "prepare_sum_aggregators": {
              "function": "count(distinct t1.pk1)",
              "aggregator_type": "simple"
            }
          }
```
