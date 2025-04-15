
# SUBSTRING_INDEX

## Syntax


```
SUBSTRING_INDEX(str,delim,count)
```


## Description


Returns the substring from string *`<code>str</code>`* before count occurrences of the
delimiter *`<code>delim</code>`*. If *`<code>count</code>`* is positive, everything to the left
of the final delimiter (counting from the left) is returned. If *`<code>count</code>`*
is negative, everything to the right of the final delimiter (counting from the
right) is returned. `<code>SUBSTRING_INDEX()</code>` performs a case-sensitive match when
searching for *`<code>delim</code>`*.


If any argument is `<code>NULL</code>`, returns `<code>NULL</code>`.


For example


```
SUBSTRING_INDEX('www.mariadb.org', '.', 2)
```

means "Return all of the characters up to the 2nd occurrence of ."


## Examples


```
SELECT SUBSTRING_INDEX('www.mariadb.org', '.', 2);
+--------------------------------------------+
| SUBSTRING_INDEX('www.mariadb.org', '.', 2) |
+--------------------------------------------+
| www.mariadb                                |
+--------------------------------------------+

SELECT SUBSTRING_INDEX('www.mariadb.org', '.', -2);
+---------------------------------------------+
| SUBSTRING_INDEX('www.mariadb.org', '.', -2) |
+---------------------------------------------+
| mariadb.org                                 |
+---------------------------------------------+
```

## See Also


* [INSTR()](instr.md) - Returns the position of a string within a string
* [LOCATE()](locate.md) - Returns the position of a string within a string
* [SUBSTRING()](substring.md) - Returns a string based on position

