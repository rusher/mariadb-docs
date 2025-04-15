
# ASCII

## Syntax


```
ASCII(str)
```

## Description


Returns the numeric ASCII value of the leftmost character of the string argument. Returns `<code>0</code>` if the given string is empty and `<code>NULL</code>` if it is `<code>NULL</code>`.


`<code>ASCII()</code>` works for 8-bit characters.


## Examples


```
SELECT ASCII(9);
+----------+
| ASCII(9) |
+----------+
|       57 |
+----------+

SELECT ASCII('9');
+------------+
| ASCII('9') |
+------------+
|         57 |
+------------+

SELECT ASCII('abc');
+--------------+
| ASCII('abc') |
+--------------+
|           97 |
+--------------+
```
