# Binary Literals

Binary literals can be written in one of the following formats: `b'value'`, `B'value'` or `0bvalue`, where `value` is a string composed by `0` and `1` digits.

Binary literals are interpreted as binary strings, and are convenient to represent [VARBINARY](../../data-types/string-data-types/varbinary.md), [BINARY](../../data-types/string-data-types/binary.md) or [BIT](../../data-types/numeric-data-types/bit.md) values.

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

* [BIN()](../../sql-functions/string-functions/bin.md)

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
