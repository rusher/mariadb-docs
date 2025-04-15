# LOCATE

#

# Syntax

```
LOCATE(substr,str), LOCATE(substr,str,pos)
```

#

# Description

The first syntax returns the position of the first occurrence of
substring `substr` in string `str`. The second syntax returns the position
of the first occurrence of substring `substr` in string `str`, starting at
position `pos`. Returns 0 if `substr` is not in `str`.

`LOCATE()` performs a case-insensitive search.

If any argument is `NULL`, returns `NULL.`

[INSTR()](instr.md) is the same as the two-argument form of `LOCATE()`, except that the order of the arguments is reversed.

#

# Examples

```
SELECT LOCATE('bar', 'foobarbar');
+----------------------------+
| LOCATE('bar', 'foobarbar') |
+----------------------------+
| 4 |
+----------------------------+

SELECT LOCATE('My', 'Maria');
+-----------------------+
| LOCATE('My', 'Maria') |
+-----------------------+
| 0 |
+-----------------------+

SELECT LOCATE('bar', 'foobarbar', 5);
+-------------------------------+
| LOCATE('bar', 'foobarbar', 5) |
+-------------------------------+
| 7 |
+-------------------------------+
```

#

# See Also

* [INSTR()](instr.md) ; Returns the position of a string withing a string
* [SUBSTRING_INDEX()](substring_index.md) ; Returns the substring from string before count occurrences of a delimiter