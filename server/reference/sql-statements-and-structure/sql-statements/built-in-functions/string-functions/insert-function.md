
# INSERT Function

## Syntax


```
INSERT(str,pos,len,newstr)
```

## Description


Returns the string `<code>str</code>`, with the substring beginning at position `<code>pos</code>`
and `<code>len</code>` characters long replaced by the string `<code>newstr</code>`. Returns the
original string if `<code>pos</code>` is not within the length of the string.
Replaces the rest of the string from position `<code>pos</code>` if `<code>len</code>` is not within
the length of the rest of the string. Returns NULL if any argument is
NULL.


## Examples


```
SELECT INSERT('Quadratic', 3, 4, 'What');
+-----------------------------------+
| INSERT('Quadratic', 3, 4, 'What') |
+-----------------------------------+
| QuWhattic                         |
+-----------------------------------+

SELECT INSERT('Quadratic', -1, 4, 'What');
+------------------------------------+
| INSERT('Quadratic', -1, 4, 'What') |
+------------------------------------+
| Quadratic                          |
+------------------------------------+

SELECT INSERT('Quadratic', 3, 100, 'What');
+-------------------------------------+
| INSERT('Quadratic', 3, 100, 'What') |
+-------------------------------------+
| QuWhat                              |
+-------------------------------------+
```
