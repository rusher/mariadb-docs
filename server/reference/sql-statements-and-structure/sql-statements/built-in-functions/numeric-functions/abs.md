
# ABS

## Syntax


```
ABS(X)
```


## Description


Returns the absolute (non-negative) value of `<code>X</code>`. If `<code>X</code>` is not a number, it is converted to a numeric type.


## Examples


```
SELECT ABS(42);
+---------+
| ABS(42) |
+---------+
|      42 |
+---------+

SELECT ABS(-42);
+----------+
| ABS(-42) |
+----------+
|       42 |
+----------+

SELECT ABS(DATE '1994-01-01');
+------------------------+
| ABS(DATE '1994-01-01') |
+------------------------+
|               19940101 |
+------------------------+
```

## See Also


* [SIGN()](sign.md)

