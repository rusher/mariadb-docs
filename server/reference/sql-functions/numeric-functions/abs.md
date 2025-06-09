
# ABS

## Syntax


```
ABS(X)
```


## Description


Returns the absolute (non-negative) value of `X`. If `X` is not a number, it is converted to a numeric type.


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


GPLv2 fill_help_tables.sql


{% @marketo/form formId="4316" %}
