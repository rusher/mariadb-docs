
# Binary Literals

Binary literals can be written in one of the following formats: `<code>b'value'</code>`, `<code>B'value'</code>` or `<code>0bvalue</code>`, where `<code>value</code>` is a string composed by `<code>0</code>` and `<code>1</code>` digits.


Binary literals are interpreted as binary strings, and are convenient to represent [VARBINARY](../../data-types/string-data-types/varbinary.md), [BINARY](../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) or [BIT](../temporal-tables/bitemporal-tables.md) values.


To convert a binary literal into an integer, just add 0.


## Examples


Printing the value as a binary string:


```
SELECT 0b1000001;
+-----------+
| 0b1000001 |
+-----------+
| A         |
+-----------+
```

Converting the same value into a number:


```
SELECT 0b1000001+0;
+-------------+
| 0b1000001+0 |
+-------------+
|          65 |
+-------------+
```

## See Also


* [BIN()](../../../../maxscale/mariadb-maxscale-14/maxscale-14-routers/binlogrouter.md)

