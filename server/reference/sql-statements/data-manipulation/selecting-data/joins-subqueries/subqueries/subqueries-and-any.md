---
description: >-
  Compare a value against any result from a subquery. The ANY (or SOME) operator
  returns TRUE if the comparison holds for at least one row. IN can be used for
  =ANY.
---

# Subqueries With ANY, SOME, and IN

## Syntax

`SOME` is a synonym for `ANY`.  `IN` is a synonym for `= ANY`.

```sql
scalar_expression comparison_operator ANY <Table subquery>
scalar_expression comparison_operator SOME <Table subquery>
scalar_expression IN <Table subquery>
```

* `scalar_expression` may be any expression that evaluates to a single value.
* `comparison_operator` may be any one of `=`, `>`, `<`, `>=`, `<=`, `<>` or `!=`.

`ANY` or `SOME` returns:

* `TRUE` if the comparison operator returns `TRUE` for at least one row returned by the table subquery.
* `FALSE` if the comparison operator returns `FALSE` for all rows returned by the table subquery, or if the table subquery has no rows.
* `NULL` if the comparison operator returns `NULL` for at least one row returned by the table subquery and doesn't returns `TRUE` for any of them, or if `scalar_expression` returns `NULL`.

## Examples

The subsequent examples use these tables:

```sql
CREATE TABLE sq1 (num1 TINYINT);
CREATE TABLE sq2 (num2 TINYINT);
INSERT INTO sq1 VALUES(100);
INSERT INTO sq2 VALUES(40),(50),(120);
```

### Subquery With `ANY`

```sql
SELECT * FROM sq1 WHERE num1 > ANY (SELECT * FROM sq2);
+------+
| num1 |
+------+
|  100 |
+------+
```

`100` is greater than two of the three values, and so the expression evaluates to `true`.

### Subquery With `SOME`

`SOME` is a synonym for `ANY`.

```sql
SELECT * FROM sq1 WHERE num1 > SOME (SELECT * FROM sq2);
+------+
| num1 |
+------+
|  100 |
+------+
```

`100` is greater than two of the three values, and so the expression evaluates to `true`.

### Subquery With `IN`

`IN` is a synonym for `= ANY`.

```sql
SELECT * FROM sq1 WHERE num1 IN (SELECT * FROM sq2);
Empty set (0.00 sec)
```

The only value of `100` in `sq1` is not in the list of values of `sq2`.

Adding a value to `sq1` that matches one of the values in `sq2` gives a match, though:

```sql
INSERT INTO sq1 VALUES(50);
SELECT * FROM sq1 WHERE num1 IN (SELECT * FROM sq2);
+------+
| num1 |
+------+
|   50 |
+------+
```

Since they're synonyms, `=ALL` returns the same result:

```sql
SELECT * FROM sq1 WHERE num1 = ANY (SELECT * FROM sq2);
+------+
| num1 |
+------+
|   50 |
+------+
```

### Subquery With `NOT IN`

After inserting `50` into `sq1`, the tables contain these values now:

* `sq1` in the `num1` column: `50`, `100`.
* `sq2` in the `num2` column: `40`, `50`, `120`.

```sql
SELECT * FROM sq1 WHERE num1 NOT IN (SELECT * FROM sq2);
+------+
| num1 |
+------+
|  100 |
+------+
```

The value of `100` is not present in `sq2`.

```sql
SELECT * FROM sq2 WHERE num2 NOT IN (SELECT * FROM sq1);
+------+
| num2 |
+------+
|   40 |
|  120 |
+------+
```

The values of `40` and `120` are not present in `sq1`.

### Subquery With `NOT IN` Versus `<> ANY`

`IN` and `=ANY` are synonyms, but `NOT IN` and `<>ANY` aren't. Compare these queries:

```sql
SELECT * FROM sq2 WHERE num2 NOT IN (SELECT * FROM sq1);
+------+
| num2 |
+------+
|   40 |
|  120 |
+------+
SELECT * FROM sq2 WHERE num2 <> ANY (SELECT * FROM sq1);
+------+
| num2 |
+------+
|   40 |
|   50 |
|  120 |
+------+
```

The first query returns all values in `sq2` that are **not present in `sq1`**.

The second query returns all values in `sq2` unless they're **only present in `sq1` but not in `sq2`**.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
