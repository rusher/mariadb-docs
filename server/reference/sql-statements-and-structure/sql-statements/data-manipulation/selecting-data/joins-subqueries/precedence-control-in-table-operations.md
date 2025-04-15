
# Precedence Control in Table Operations

You can control the ordering of execution on table operations using parentheses.


## Syntax


```
(  expression )
[ORDER BY [column[, column...]]]
[LIMIT {[offset,] row_count | row_count OFFSET offset}]
```


## Description


Using parentheses in your SQL allows you to control the order of execution for `<code>[SELECT](../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)</code>` statements and [Table Value Constructor](../../../../sql-language-structure/table-value-constructors.md), including `<code>[UNION](union.md)</code>`, `<code>[EXCEPT](except.md)</code>`, and `<code>[INTERSECT](../../../../geographic-geometric-features/geometry-relations/intersects.md)</code>` operations. MariaDB executes the parenthetical expression before the rest of the statement. You can then use `<code>[ORDER BY](../order-by.md)</code>` and `<code>[LIMIT](../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/limitationsdifferences-with-a-mariadb-server-compiled-for-debugging.md)</code>` clauses the further organize the result-set.


**Note**: In practice, the Optimizer may rearrange the exact order in which MariaDB executes different parts of the statement.  When it calculates the result-set, however, it returns values as though the parenthetical expression were executed first.


## Example


```
CREATE TABLE test.t1 (num INT);

INSERT INTO test.t1 VALUES (1),(2),(3);

(SELECT * FROM test.t1 
 UNION 
 VALUES (10)) 
INTERSECT 
VALUES (1),(3),(10),(11);
+------+
| num  |
+------+
|    1 |
|    3 |
|   10 |
+------+

((SELECT * FROM test.t1 
  UNION 
  VALUES (10)) 
 INTERSECT 
 VALUES (1),(3),(10),(11)) 
ORDER BY 1 DESC;
+------+
| num  |
+------+
|   10 |
|    3 |
|    1 |
+------+
```
