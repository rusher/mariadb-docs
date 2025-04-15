
# OCT

## Syntax


```
OCT(N)
```


## Description


Returns a string representation of the octal value of N, where N is a longlong ([BIGINT](../../../../data-types/data-types-numeric-data-types/bigint.md)) number. This is equivalent to [CONV(N,10,8)](../../../../storage-engines/converting-tables-from-myisam-to-innodb.md). Returns NULL if N is NULL.


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


* [CONV()](../../../../storage-engines/converting-tables-from-myisam-to-innodb.md)
* [BIN()](../../../../../../maxscale/mariadb-maxscale-14/maxscale-14-routers/binlogrouter.md)
* [HEX()](../../../sql-language-structure/hexadecimal-literals.md)

