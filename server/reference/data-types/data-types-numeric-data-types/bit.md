# BIT

## Syntax

```
BIT[(M)]
```

## Description

A bit-field type. `M` indicates the number of bits per value, from `1` to`64`. The default is `1` if `M` is omitted.

Bit values can be inserted with `b'value'` notation, where `value` is the bit value in 0's and 1's.

Bit fields are automatically zero-padded from the left to the full length of the bit, so for example in a BIT(4) field, '10' is equivalent to '0010'.

Bits are returned as binary, so to display them, either add 0, or use a function such as [HEX](../../sql-statements/built-in-functions/string-functions/hex.md), [OCT](../../sql-statements/built-in-functions/numeric-functions/oct.md) or [BIN](../../sql-statements/built-in-functions/string-functions/bin.md) to convert them.

## Examples

Example of BIT:

```
CREATE TABLE bit_example (
  description VARCHAR(20),
  b1 BIT,
  b4 BIT(4),
  b16 BIT(16)
);
```

```
INSERT INTO bit_example VALUES
  ('Zero', 0, 0, 0),
  ('One', 1, 1, 1),
  ('Two', 0, 2, 2),
  ('Eight', 0, 8, b'1000'),
  ('All on', 1, 15, b'1111111111111111');
SELECT description, b1+0, LPAD(BIN(b4), 4, 0) AS b4, HEX(b16)
  FROM bit_example;

+-------------+------+------+----------+
| description | b1+0 | b4   | HEX(b16) |
+-------------+------+------+----------+
| Zero        |    0 | 0000 | 0        |
| One         |    1 | 0001 | 1        |
| Two         |    0 | 0010 | 2        |
| Eight       |    0 | 1000 | 8        |
| All on      |    1 | 1111 | FFFF     |
+-------------+------+------+----------+
```

### With [strict\_mode](../../../server-management/variables-and-modes/sql-mode.md#strict-mode) set

```
CREATE TABLE b ( b1 BIT(8) );
```

```
INSERT INTO b VALUES (b'11111111');

INSERT INTO b VALUES (b'01010101');

INSERT INTO b VALUES (b'1111111111111');
ERROR 1406 (22001): Data too long for column 'b1' at row 1

SELECT b1+0, HEX(b1), OCT(b1), BIN(b1) FROM b;
+------+---------+---------+----------+
| b1+0 | HEX(b1) | OCT(b1) | BIN(b1)  |
+------+---------+---------+----------+
|  255 | FF      | 377     | 11111111 |
|   85 | 55      | 125     | 1010101  |
+------+---------+---------+----------+
```

GPLv2 fill\_help\_tables.sql
