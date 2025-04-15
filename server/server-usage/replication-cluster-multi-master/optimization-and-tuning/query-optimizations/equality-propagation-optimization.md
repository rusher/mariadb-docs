
# Equality propagation optimization


## Basic idea


Consider a query with a WHERE clause:


```
WHERE col1=col2 AND ...
```

the WHERE clause will compute to true only if `<code>col1=col2</code>`. This means that in the rest of the WHERE clause occurrences of `<code>col1</code>` can be substituted with `<code>col2</code>` (with some limitations which are discussed in the next section). This allows the optimizer to infer additional restrictions.


For example:


```
WHERE col1=col2 AND col1=123
```

allows to infer a new equality: `<code>col2=123</code>`


```
WHERE col1=col2 AND col1 < 10
```

allows to infer that `<code>col2<10</code>`.


## Identity and comparison substitution


There are some limitations to where one can do the substitution, though.


The first and obvious example is the string datatype and collations. Most commonly-used collations in SQL are "case-insensitive", that is `<code>'A'='a'</code>`. Also, most collations have a "PAD SPACE" attribute, which means that comparison ignores the spaces at the end of the value, `<code>'a'='a '</code>`.


Now, consider a query:


```
INSERT INTO t1 (col1, col2) VALUES ('ab', 'ab   ');
SELECT * FROM t1 WHERE col1=col2 AND LENGTH(col1)=2
```

Here, `<code>col1=col2</code>`, the values are "equal". At the same time `<code>LENGTH(col1)=2</code>`, while `<code>LENGTH(col2)=4</code>`, which means one can't perform the substiution for the argument of LENGTH(...).


It's not only collations. There are similar phenomena when equality compares columns of different datatypes. The exact criteria of when thy happen are rather convoluted.


The take-away is: **sometimes, X=Y does not mean that one can replace any reference to X with Y**. 
What one CAN do is still replace the occurrence in the comparisons `<code><</code>`, `<code>></code>`, `<code>>=</code>`, `<code><=</code>`, etc.


This is how we get two kinds of substitution:


* Identity substitution: X=Y, and any occurrence of X can be replaced with Y.
* Comparison substitution: X=Y, and an occurrence of X in a comparison (X<Z) can be replaced with Y (Y<Z).


## Place in query optimization


(A draft description): 
Let's look at how Equality Propagation is integrated with the rest of the query optimization process.


* First, multiple-equalities are built (TODO example from optimizer trace)

  * If multiple-equality includes a constant, fields are substituted with a constant if possible.


* From this point, all optimizations like range optimization, ref access, etc make use of multiple equalities: when they see a reference to `<code>tableX.columnY</code>` somewhere, they also look at all the columns that tableX.columnY is equal to.


* After the join order is picked, the optimizer walks through the WHERE clause and substitutes each field reference with the "best" one - the one that can be checked as soon as possible.

  * Then, the parts of the WHERE condition are attached to the tables where they can be checked.


### Interplay with ORDER BY optimization


Consider a query:


```
SELECT ... FROM ... WHERE col1=col2 ORDER BY col2
```

Suppose, there is an `<code>INDEX(col1)</code>`. MariaDB optimizer is able to figure out that it can use an index on `<code>col1</code>` (or sort by the value of `<code>col1</code>`) in order to resolve `<code>ORDER BY col2</code>`.


## Optimizer trace


Look at these elements:


* `<code>condition_processing</code>`
* `<code>attaching_conditions_to_tables</code>`


## More details


Equality propagation doesn't just happen at the top of the WHERE clause. It is done "at all levels" where a level is:


* A top level of the WHERE clause.
* If the WHERE clause has an OR clause, each branch of the OR clause.
* The top level of any ON expression
* (the same as above about OR-levels)

