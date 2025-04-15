
# CHARSET

## Syntax


```
CHARSET(str)
```

## Description


Returns the [character set](../../../../../data-types/string-data-types/character-sets/README.md) of the string argument. If `<code>str</code>` is not a string, it is considered as a binary string (so the function returns 'binary'). This applies to `<code>NULL</code>`, too. The return value is a string in the utf8 [character set](../../../../../data-types/string-data-types/character-sets/README.md).


## Examples


```
SELECT CHARSET('abc');
+----------------+
| CHARSET('abc') |
+----------------+
| latin1         |
+----------------+

SELECT CHARSET(CONVERT('abc' USING utf8));
+------------------------------------+
| CHARSET(CONVERT('abc' USING utf8)) |
+------------------------------------+
| utf8                               |
+------------------------------------+

SELECT CHARSET(USER());
+-----------------+
| CHARSET(USER()) |
+-----------------+
| utf8            |
+-----------------+
```
