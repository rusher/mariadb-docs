
# BIT_AND

## Syntax


```
BIT_AND(expr) [over_clause]
```

## Description


Returns the bitwise AND of all bits in *expr*. The calculation is performed with 64-bit ([BIGINT](../../../../data-types/data-types-numeric-data-types/bigint.md)) precision. It is an [aggregate function](README.md), and so can be used with the [GROUP BY](../../data-manipulation/selecting-data/group-by.md) clause.


If no rows match, `BIT_AND` will return a value with all bits set to 1. NULL values have no effect on the result unless all results are NULL, which is treated as no match.


`BIT_AND` can be used as a [window function](../special-functions/window-functions/README.md) with the addition of the *over_clause*.


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

As an [aggregate function](README.md):


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
SELECT BIT_AND(NULL);
+----------------------+
| BIT_AND(NULL)        |
+----------------------+
| 18446744073709551615 |
+----------------------+
```

## See Also


* [BIT_OR](bit_or.md)
* [BIT_XOR](bit_xor.md)

