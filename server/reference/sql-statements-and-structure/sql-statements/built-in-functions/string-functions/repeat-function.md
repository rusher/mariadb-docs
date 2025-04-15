
# REPEAT Function

## Syntax


```
REPEAT(str,count)
```

## Description


Returns a string consisting of the string `<code>str</code>` repeated `<code>count</code>` times. If
`<code>count</code>` is less than 1, returns an empty string. Returns NULL if `<code>str</code>` or
`<code>count</code>` are NULL.


## Examples


```
SELECT QUOTE(REPEAT('MariaDB ',4));
+------------------------------------+
| QUOTE(REPEAT('MariaDB ',4))        |
+------------------------------------+
| 'MariaDB MariaDB MariaDB MariaDB ' |
+------------------------------------+
```
