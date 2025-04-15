
# TIMESTAMP FUNCTION

This page is about the TIMESTAMP function. For the timestamp data type, see [TIMESTAMP](timestamp-function.md).


## Syntax


```
TIMESTAMP(expr), TIMESTAMP(expr1,expr2)
```

## Description


With a single argument, this function returns the date or datetime
expression `<code>expr</code>` as a datetime value. With two arguments, it adds the
time expression `<code>expr2</code>` to the date or datetime expression `<code>expr1</code>` and
returns the result as a datetime value.


## Examples


```
SELECT TIMESTAMP('2003-12-31');
+-------------------------+
| TIMESTAMP('2003-12-31') |
+-------------------------+
| 2003-12-31 00:00:00     |
+-------------------------+

SELECT TIMESTAMP('2003-12-31 12:00:00','6:30:00');
+--------------------------------------------+
| TIMESTAMP('2003-12-31 12:00:00','6:30:00') |
+--------------------------------------------+
| 2003-12-31 18:30:00                        |
+--------------------------------------------+
```
