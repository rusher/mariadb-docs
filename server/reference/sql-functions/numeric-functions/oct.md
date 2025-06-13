# OCT

## Syntax

```
OCT(N)
```

## Description

Returns a string representation of the octal value of N, where N is a longlong ([BIGINT](../../data-types/numeric-data-types/bigint.md)) number. This is equivalent to [CONV(N,10,8)](conv.md). Returns NULL if N is NULL.

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

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
