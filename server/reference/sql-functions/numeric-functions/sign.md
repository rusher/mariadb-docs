
# SIGN

## Syntax


```
SIGN(X)
```

## Description


Returns the sign of the argument as -1, 0, or 1, depending on whether
X is negative, zero, or positive.


## Examples


```
SELECT SIGN(-32);
+-----------+
| SIGN(-32) |
+-----------+
|        -1 |
+-----------+

SELECT SIGN(0);
+---------+
| SIGN(0) |
+---------+
|       0 |
+---------+

SELECT SIGN(234);
+-----------+
| SIGN(234) |
+-----------+
|         1 |
+-----------+
```

## See Also


* [ABS()](abs.md)


GPLv2 fill_help_tables.sql


{% @marketo/form formId="4316" %}
