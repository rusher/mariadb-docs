
# Subqueries and ALL

[Subqueries](subqueries-and-all.md) using the ALL keyword will return `<code>true</code>` if the comparison returns `<code>true</code>` for each row returned by the subquery, or the subquery returns no rows.


## Syntax


```
scalar_expression comparison_operator ALL <Table subquery>
```

* `<code>scalar_expression</code>` may be any expression that evaluates to a single
value
* `<code>comparison_operator</code>` may be any one of: `<code>=</code>`, `<code>></code>`, `<code><</code>`, `<code>>=</code>`, `<code><=</code>`, `<code><></code>` or `<code>!=</code>`


`<code>ALL</code>` returns:


* `<code>NULL</code>` if the comparison operator returns `<code>NULL</code>` for at least one row returned by the Table subquery or scalar_expression returns `<code>NULL</code>`.
* `<code>FALSE</code>` if the comparison operator returns `<code>FALSE</code>` for at least one row returned by the Table subquery.
* `<code>TRUE</code>` if the comparison operator returns `<code>TRUE</code>` for all rows returned by the Table subquery, or if Table subquery returns no rows.


`<code>NOT IN</code>` is an alias for `<code><> ALL</code>`.


## Examples


```
CREATE TABLE sq1 (num TINYINT);

CREATE TABLE sq2 (num2 TINYINT);

INSERT INTO sq1 VALUES(100);

INSERT INTO sq2 VALUES(40),(50),(60);

SELECT * FROM sq1 WHERE num > ALL (SELECT * FROM sq2);
+------+
| num  |
+------+
|  100 |
+------+
```

Since `<code>100</code>` > all of `<code>40</code>`,`<code>50</code>` and `<code>60</code>`, the evaluation is true and the row is returned


Adding a second row to sq1, where the evaluation for that record is false:


```
INSERT INTO sq1 VALUES(30);

SELECT * FROM sq1 WHERE num > ALL (SELECT * FROM sq2);
+------+
| num  |
+------+
|  100 |
+------+
```

Adding a new row to sq2, causing all evaluations to be false:


```
INSERT INTO sq2 VALUES(120);

SELECT * FROM sq1 WHERE num > ALL (SELECT * FROM sq2);
Empty set (0.00 sec)
```

When the subquery returns no results, the evaluation is still true:


```
SELECT * FROM sq1 WHERE num > ALL (SELECT * FROM sq2 WHERE num2 > 300);
+------+
| num  |
+------+
|  100 |
|   30 |
+------+
```

Evaluating against a NULL will cause the result to be unknown, or not true, and therefore return no rows:


```
INSERT INTO sq2 VALUES (NULL);

SELECT * FROM sq1 WHERE num > ALL (SELECT * FROM sq2);
```
