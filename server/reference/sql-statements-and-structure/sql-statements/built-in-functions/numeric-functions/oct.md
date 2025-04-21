
# OCT

## Syntax


```
OCT(N)
```


## Description


Returns a string representation of the octal value of N, where N is a longlong ([BIGINT](../../../../data-types/data-types-numeric-data-types/bigint.md)) number. This is equivalent to [CONV(N,10,8)](conv.md). Returns NULL if N is NULL.


## Examples


```
SELECT OCT(34);
+---------+
| OCT(34) |
+---------+
| 42      |
+---------+

SELECT OCT(12);
+---------+
| OCT(12) |
+---------+
| 14      |
+---------+
```

## See Also


* [CONV()](conv.md)
* [BIN()](../string-functions/bin.md)
* [HEX()](../string-functions/hex.md)

