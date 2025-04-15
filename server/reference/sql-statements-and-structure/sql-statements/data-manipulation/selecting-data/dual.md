
# DUAL

## Description


You are allowed to specify `<code class="highlight fixed" style="white-space:pre-wrap">DUAL</code>` as a dummy table name in
situations where no tables are referenced, such as the following [SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) statement:


```
SELECT 1 + 1 FROM DUAL;
+-------+
| 1 + 1 |
+-------+
|     2 |
+-------+
```

`<code class="highlight fixed" style="white-space:pre-wrap">DUAL</code>` is purely for the convenience of people who require
 that all `<code class="highlight fixed" style="white-space:pre-wrap">SELECT</code>` statements should have
 `<code class="highlight fixed" style="white-space:pre-wrap">FROM</code>` and possibly other clauses. MariaDB ignores the
 clauses. MariaDB does not require `<code class="highlight fixed" style="white-space:pre-wrap">FROM DUAL</code>` if no tables
 are referenced.


FROM DUAL could be used when you only SELECT computed values, but require a WHERE clause, perhaps to test that a script correctly handles empty resultsets:


```
SELECT 1 FROM DUAL WHERE FALSE;
Empty set (0.00 sec)
```

## See Also


* [SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)

