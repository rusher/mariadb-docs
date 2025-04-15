
# BIT_XOR

## Syntax


```
BIT_XOR(expr) [over_clause]
```


## Description


Returns the bitwise XOR of all bits in `<code>expr</code>`. The calculation is performed with 64-bit ([BIGINT](../../../../data-types/data-types-numeric-data-types/bigint.md)) precision. It is an [aggregate function](../special-functions/window-functions/aggregate-functions-as-window-functions.md), and so can be used with the [GROUP BY](../../data-manipulation/selecting-data/group-by.md) clause.


If no rows match, `<code>BIT_XOR</code>` will return a value with all bits set to `<code>0</code>`. NULL values have no effect on the result unless all results are NULL, which is treated as no match.


`<code>BIT_XOR</code>` can be used as a [window function](../special-functions/window-functions/window-functions-overview.md) with the addition of the *over_clause*.


## Examples


```
CREATE TABLE vals (x INT);

INSERT INTO vals VALUES(111),(110),(100);

SELECT BIT_AND(x), BIT_OR(x), BIT_XOR(x) FROM vals;
+------------+-----------+------------+
| BIT_AND(x) | BIT_OR(x) | BIT_XOR(x) |
+------------+-----------+------------+
|        100 |       111 |        101 |
+------------+-----------+------------+
```

As an [aggregate function](../special-functions/window-functions/aggregate-functions-as-window-functions.md):


```
CREATE TABLE vals2 (category VARCHAR(1), x INT);

INSERT INTO vals2 VALUES
  ('a',111),('a',110),('a',100),
  ('b','000'),('b',001),('b',011);

SELECT category, BIT_AND(x), BIT_OR(x), BIT_XOR(x) 
  FROM vals GROUP BY category;
+----------+------------+-----------+------------+
| category | BIT_AND(x) | BIT_OR(x) | BIT_XOR(x) |
+----------+------------+-----------+------------+
| a        |        100 |       111 |        101 |
| b        |          0 |        11 |         10 |
+----------+------------+-----------+------------+
```

No match:


```
SELECT BIT_XOR(NULL);
+---------------+
| BIT_XOR(NULL) |
+---------------+
|             0 |
+---------------+
```

## See Also


* [BIT_AND](bit_and.md)
* [BIT_OR](bit_or.md)

