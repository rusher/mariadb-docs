
# LOCATE

## Syntax


```
LOCATE(substr,str), LOCATE(substr,str,pos)
```

## Description


The first syntax returns the position of the first occurrence of
substring `<code>substr</code>` in string `<code>str</code>`. The second syntax returns the position
of the first occurrence of substring `<code>substr</code>` in string `<code>str</code>`, starting at
position `<code>pos</code>`. Returns 0 if `<code>substr</code>` is not in `<code>str</code>`.


`<code>LOCATE()</code>` performs a case-insensitive search.


If any argument is `<code>NULL</code>`, returns `<code>NULL.</code>`


[INSTR()](instr.md) is the same as the two-argument form of `<code>LOCATE()</code>`, except that the order of the arguments is reversed.


## Examples


```
SELECT LOCATE('bar', 'foobarbar');
+----------------------------+
| LOCATE('bar', 'foobarbar') |
+----------------------------+
|                          4 |
+----------------------------+

SELECT LOCATE('My', 'Maria');
+-----------------------+
| LOCATE('My', 'Maria') |
+-----------------------+
|                     0 |
+-----------------------+

SELECT LOCATE('bar', 'foobarbar', 5);
+-------------------------------+
| LOCATE('bar', 'foobarbar', 5) |
+-------------------------------+
|                             7 |
+-------------------------------+
```

## See Also


* [INSTR()](instr.md) ; Returns the position of a string withing a string
* [SUBSTRING_INDEX()](substring_index.md) ; Returns the substring from string before count occurrences of a delimiter

