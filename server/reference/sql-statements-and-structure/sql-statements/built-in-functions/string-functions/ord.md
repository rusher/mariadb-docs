
# ORD

## Syntax


```
ORD(str)
```

## Description


If the leftmost character of the string `<code>str</code>` is a multi-byte character,
returns the code for that character, calculated from the numeric
values of its constituent bytes using this formula:


```
(1st byte code)
+ (2nd byte code x 256)
+ (3rd byte code x 256 x 256) ...
```

If the leftmost character is not a multi-byte character, ORD() returns
the same value as the [ASCII()](ascii.md) function.


## Examples


```
SELECT ORD('2');
+----------+
| ORD('2') |
+----------+
|       50 |
+----------+
```

## See Also


* [ASCII()](ascii.md) - Return ASCII value of first character
* [CHAR()](char-function.md) - Create a character from an integer value

