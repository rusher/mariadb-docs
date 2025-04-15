
# INSTR

## Syntax


```
INSTR(str,substr)
```


## Description


Returns the position of the first occurrence of substring *substr* in
string *str*. This is the same as the two-argument form of [LOCATE()](locate.md),
except that the order of the arguments is reversed.


`<code>INSTR()</code>` performs a case-insensitive search.


If any argument is `<code>NULL</code>`, returns `<code>NULL</code>`.


## Examples


```
SELECT INSTR('foobarbar', 'bar');
+---------------------------+
| INSTR('foobarbar', 'bar') |
+---------------------------+
|                         4 |
+---------------------------+

SELECT INSTR('My', 'Maria');
+----------------------+
| INSTR('My', 'Maria') |
+----------------------+
|                    0 |
+----------------------+
```

## See Also


* [LOCATE()](locate.md) ; Returns the position of a string within a string
* [SUBSTRING_INDEX()](substring_index.md) ; Returns the substring from string before count occurrences of a delimiter

