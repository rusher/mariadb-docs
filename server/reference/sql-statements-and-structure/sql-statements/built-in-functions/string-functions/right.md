
# RIGHT

## Syntax


```
RIGHT(str,len)
```

## Description


Returns the rightmost *`<code>len</code>`* characters from the string *`<code>str</code>`*, or NULL if
any argument is NULL.


## Examples


```
SELECT RIGHT('MariaDB', 2);
+---------------------+
| RIGHT('MariaDB', 2) |
+---------------------+
| DB                  |
+---------------------+
```
