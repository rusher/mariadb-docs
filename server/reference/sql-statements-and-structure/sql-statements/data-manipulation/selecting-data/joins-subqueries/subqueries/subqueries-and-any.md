
# Subqueries and ANY

[Subqueries](subqueries-and-all.md) using the ANY keyword will return `<code>true</code>` if the comparison returns `<code>true</code>` for at least one row returned by the subquery.


## Syntax


The required syntax for an `<code>ANY</code>` or `<code>SOME</code>` quantified comparison is:


```
scalar_expression comparison_operator ANY <Table subquery>
```

Or:


```
scalar_expression comparison_operator SOME <Table subquery>
```

* `<code>scalar_expression</code>` may be any expression that evaluates to a
single value.
* `<code>comparison_operator</code>` may be any one of `<code>=</code>`, `<code>></code>`, `<code><</code>`, `<code>>=</code>`, `<code><=</code>`, `<code><></code>` or `<code>!=</code>`.


`<code>ANY</code>` returns:


* `<code>TRUE</code>` if the comparison operator returns `<code>TRUE</code>` for at least one row returned by the Table subquery.
* `<code>FALSE</code>` if the comparison operator returns `<code>FALSE</code>` for all rows returned by the Table subquery, or Table subquery has zero rows.
* `<code>NULL</code>` if the comparison operator returns `<code>NULL</code>` for at least one row returned by the Table subquery and doesn't returns `<code>TRUE</code>` for any of them, or if scalar_expression returns `<code>NULL</code>`.


`<code>SOME</code>` is a synmonym for `<code>ANY</code>`, and `<code>IN</code>` is a synonym for `<code>= ANY</code>`


## Examples


```
CREATE TABLE sq1 (num TINYINT);

CREATE TABLE sq2 (num2 TINYINT);

INSERT INTO sq1 VALUES(100);

INSERT INTO sq2 VALUES(40),(50),(120);

SELECT * FROM sq1 WHERE num > ANY (SELECT * FROM sq2);
+------+
| num  |
+------+
|  100 |
+------+
```

`<code>100</code>` is greater than two of the three values, and so the expression evaluates as true.


SOME is a synonym for ANY:


```
SELECT * FROM sq1 WHERE num < SOME (SELECT * FROM sq2);
+------+
| num  |
+------+
|  100 |
+------+
```

`<code>IN</code>` is a synonym for `<code>= ANY</code>`, and here there are no matches, so no results are returned:


```
SELECT * FROM sq1 WHERE num IN (SELECT * FROM sq2);
Empty set (0.00 sec)
```

```
INSERT INTO sq2 VALUES(100);
Query OK, 1 row affected (0.05 sec)

SELECT * FROM sq1 WHERE num <> ANY (SELECT * FROM sq2);
+------+
| num  |
+------+
|  100 |
+------+
```

Reading this query, the results may be counter-intuitive. It may seem to read as "SELECT * FROM sq1 WHERE num does not match any results in sq2. Since it does match 100, it could seem that the results are incorrect. However, the query returns a result if the match does not match any *of* sq2. Since `<code>100</code>` already does not match `<code>40</code>`, the expression evaluates to true immediately, regardless of the 100's matching. It may be more easily readable to use SOME in a case such as this:


```
SELECT * FROM sq1 WHERE num <> SOME (SELECT * FROM sq2);
+------+
| num  |
+------+
|  100 |
+------+
```
