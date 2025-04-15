
# Subqueries and JOINs

A [subquery](subqueries-and-all.md) can quite often, but not in all cases, be rewritten as a [JOIN](../../../../../../../../general-resources/learning-and-training/training-and-tutorials/basic-mariadb-articles/joining-tables-with-join-clauses.md).



## Rewriting Subqueries as JOINS


A subquery using `<code>IN</code>` can be rewritten with the `<code>DISTINCT</code>` keyword, for example:


```
SELECT * FROM table1 WHERE col1 IN (SELECT col1 FROM table2);
```

can be rewritten as:


```
SELECT DISTINCT table1.* FROM table1, table2 WHERE table1.col1=table2.col1;
```

`<code>NOT IN</code>` or `<code>NOT EXISTS</code>` queries can also be rewritten. For example, these two queries returns the same result:


```
SELECT * FROM table1 WHERE col1 NOT IN (SELECT col1 FROM table2);
SELECT * FROM table1 WHERE NOT EXISTS (SELECT col1 FROM table2 WHERE table1.col1=table2.col1);
```

and both can be rewritten as:


```
SELECT table1.* FROM table1 LEFT JOIN table2 ON table1.id=table2.id WHERE table2.id IS NULL;
```

Subqueries that can be rewritten as a LEFT JOIN are sometimes more efficient.


## Using Subqueries instead of JOINS


There are some scenarios, though, which call for subqueries rather than joins:


* When you want duplicates, but not false duplicates. Suppose `<code>Table_1</code>`
 has three rows — {`<code>1</code>`,`<code>1</code>`,`<code>2</code>`}
 — and `<code>Table_2</code>` has two rows
 — {`<code>1</code>`,`<code>2</code>`,`<code>2</code>`}. If you need to list the rows
 in `<code>Table_1</code>` which are also in `<code>Table_2</code>`, only this
 subquery-based `<code>SELECT</code>` statement will give the right answer
 (`<code>1</code>`,`<code>1</code>`,`<code>2</code>`):


```
SELECT Table_1.column_1 
FROM   Table_1 
WHERE  Table_1.column_1 IN 
  (SELECT Table_2.column_1 
    FROM   Table_2);
```

* This SQL statement won't work:


```
SELECT Table_1.column_1 
FROM   Table_1,Table_2 
WHERE  Table_1.column_1 = Table_2.column_1;
```

* because the result will be {`<code>1</code>`,`<code>1</code>`,`<code>2</code>`,`<code>2</code>`}
 — and the duplication of 2 is an error. This SQL
 statement won't work either:


```
SELECT DISTINCT Table_1.column_1 
FROM   Table_1,Table_2 
WHERE  Table_1.column_1 = Table_2.column_1;
```

* because the result will be {`<code>1</code>`,`<code>2</code>`} — and
 the removal of the duplicated 1 is an error too.


* When the outermost statement is not a query. The SQL statement:


```
UPDATE Table_1 SET column_1 = (SELECT column_1 FROM Table_2);
```

* can't be expressed using a join unless some rare SQL3 features are used.


* When the join is over an expression. The SQL statement:


```
SELECT * FROM Table_1 
WHERE column_1 + 5 =
  (SELECT MAX(column_1) FROM Table_2);
```

* is hard to express with a join. In fact, the only way we can think of is
 this SQL statement:


```
SELECT Table_1.*
FROM   Table_1, 
      (SELECT MAX(column_1) AS max_column_1 FROM Table_2) AS Table_2
WHERE  Table_1.column_1 + 5 = Table_2.max_column_1;
```

* which still involves a parenthesized query, so nothing is gained from the
 transformation.


* When you want to see the exception. For example, suppose the question is:
 what books are longer than Das Kapital? These two queries are effectively
 almost the same:


```
SELECT DISTINCT Bookcolumn_1.*                     
FROM   Books AS Bookcolumn_1 JOIN Books AS Bookcolumn_2 USING(page_count) 
WHERE  title = 'Das Kapital';

SELECT DISTINCT Bookcolumn_1.* 
FROM   Books AS Bookcolumn_1 
WHERE  Bookcolumn_1.page_count > 
  (SELECT DISTINCT page_count 
  FROM   Books AS Bookcolumn_2 
  WHERE  title = 'Das Kapital');
```

* The difference is between these two SQL statements is, if there are two
 editions of Das Kapital (with different page counts), then the self-join
 example will return the books which are longer than the shortest edition
 of Das Kapital. That might be the wrong answer, since the original
 question didn't ask for "... longer than `<code>ANY</code>` book named Das Kapital"
 (it seems to contain a false assumption that there's only one edition).

