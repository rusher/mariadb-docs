
# LEFT

## Syntax


```
LEFT(str,len)
```

## Description


Returns the leftmost `<code>len</code>` characters from the string `<code>str</code>`, or NULL if
any argument is NULL.


## Examples


```
SELECT LEFT('MariaDB', 5);
+--------------------+
| LEFT('MariaDB', 5) |
+--------------------+
| Maria              |
+--------------------+
```
