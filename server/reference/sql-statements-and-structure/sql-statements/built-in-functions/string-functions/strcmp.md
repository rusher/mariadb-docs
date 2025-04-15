
# STRCMP

## Syntax


```
STRCMP(expr1,expr2)
```

## Description


`<code>STRCMP()</code>` returns `<code>0</code>` if the strings are the same, `<code>-1</code>` if the first
argument is smaller than the second according to the current sort order,
and `<code>1</code>` if the strings are otherwise not the same. Returns `<code>NULL</code>` is either argument is `<code>NULL</code>`.


## Examples


```
SELECT STRCMP('text', 'text2');
+-------------------------+
| STRCMP('text', 'text2') |
+-------------------------+
|                      -1 |
+-------------------------+

SELECT STRCMP('text2', 'text');
+-------------------------+
| STRCMP('text2', 'text') |
+-------------------------+
|                       1 |
+-------------------------+

SELECT STRCMP('text', 'text');
+------------------------+
| STRCMP('text', 'text') |
+------------------------+
|                      0 |
+------------------------+
```
