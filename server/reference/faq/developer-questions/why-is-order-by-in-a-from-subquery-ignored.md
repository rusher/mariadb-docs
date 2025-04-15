
# Why is ORDER BY in a FROM Subquery Ignored?

Query with ORDER BY in a FROM subquery produces unordered result. Is this a bug?
Below is an example of this:


```
SELECT field1, field2 FROM ( SELECT field1, field2 FROM table1 ORDER BY field2 ) alias
```

returns a result set that is not necessarily ordered by field2. This is not a bug.


A "table" (and subquery in the `<code>FROM</code>` clause too) is - according to the SQL standard - an unordered set of rows. Rows in a table (or in a subquery in the `<code>FROM</code>` clause) do not come in any specific order. That's why the optimizer can ignore the [ORDER BY](../../sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/order-by.md) clause that you have specified. In fact, the SQL standard does not even allow the `<code>ORDER BY</code>` clause to appear in this subquery (we allow it, because `<code>ORDER BY ... LIMIT ...</code>` changes the result, the set of rows, not only their order).


You need to treat the subquery in the `<code>FROM</code>` clause, as a set of rows in some unspecified and undefined order, and put the `<code>ORDER BY</code>` on the top-level `<code>SELECT</code>`.


Source: [MDEV-3926, Comment by Sergei Golubchik](https://jira.mariadb.org/browse/MDEV-3926?focusedCommentId=28800&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-28800)


## See also


* [MDEV-3926](https://jira.mariadb.org/browse/MDEV-3926), [MDEV-5007](https://jira.mariadb.org/browse/MDEV-5007), [MDEV-3795](https://jira.mariadb.org/browse/MDEV-3795).
* [SELECT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)
* [ORDER BY](../../sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/order-by.md)

