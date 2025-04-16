
# BIN

## Syntax


```
BIN(N)
```

## Description


Returns a string representation of the binary value of the given longlong (that is, `[BIGINT](../../../../data-types/data-types-numeric-data-types/bigint.md)`) number. This is equivalent to `[CONV(N,10,2)](../../../../storage-engines/converting-tables-from-myisam-to-innodb.md)`. The argument should be positive. If it is a `FLOAT`, it will be truncated. Returns `NULL` if the argument is `NULL`.


## Examples


```
SELECT BIN(12);
+---------+
| BIN(12) |
+---------+
| 1100    |
+---------+
```

## See Also


* [Binary literals](../../../sql-language-structure/binary-literals.md)
* [CONV()](../../../../storage-engines/converting-tables-from-myisam-to-innodb.md)
* [OCT()](../numeric-functions/oct.md)
* [HEX()](../../../sql-language-structure/hexadecimal-literals.md)

