
# TINYINT


## Syntax


```
TINYINT[(M)] [SIGNED | UNSIGNED | ZEROFILL]
```

## Description


A very small [integer](int.md). The signed range is -128 to 127. The unsigned range is 0 to 255. For details on the attributes, see [Numeric Data Type Overview](numeric-data-type-overview.md).


[INT1](int1.md), [BOOL, and BOOLEAN](boolean.md) are synonyms for `TINYINT`.


## Examples


```
CREATE TABLE tinyints (a TINYINT,b TINYINT UNSIGNED,c TINYINT ZEROFILL);
```

### With [strict_mode](../../../server-management/variables-and-modes/sql-mode.md#strict-mode) set


```
INSERT INTO tinyints VALUES (-10,-10,-10);
ERROR 1264 (22003): Out of range value for column 'b' at row 1

INSERT INTO tinyints VALUES (-10,10,-10);
ERROR 1264 (22003): Out of range value for column 'c' at row 1

INSERT INTO tinyints VALUES (-10,10,10);

SELECT * FROM tinyints;
+------+------+------+
| a    | b    | c    |
+------+------+------+
|  -10 |   10 |  010 |
+------+------+------+

INSERT INTO tinyints VALUES (128,128,128);
ERROR 1264 (22003): Out of range value for column 'a' at row 1

INSERT INTO tinyints VALUES (127,128,128);

SELECT * FROM tinyints;
+------+------+------+
| a    | b    | c    |
+------+------+------+
|  -10 |   10 |  010 |
|  127 |  128 |  128 |
+------+------+------+
```

### SIGNED and UNSIGNED


The `TINYINT` data type may be `SIGNED` (allowing negative values) or `UNSIGNED` (not allowing negative values).


Example of TINYINT SIGNED (the default):


```
CREATE TABLE tinyint_signed_example (
   description VARCHAR(20),
   example TINYINT SIGNED
);
```

```
INSERT INTO tinyint_signed_example VALUES
   ('Zero', 0),
   ('Forty-Two', 42),
   ('Minimum', -128),
   ('Maximum', 127);
```

Example of TINYINT UNSIGNED:


```
CREATE TABLE tinyint_unsigned_example (
   description VARCHAR(20),
   example TINYINT UNSIGNED
);
```

```
INSERT INTO tinyint_unsigned_example VALUES
   ('Zero', 0),
   ('Forty-Two', 42),
   ('Minimum', 0),
   ('Maximum', 255);
```

### Out-of-Range


A value is considered "out-of-range" when it is too small or too large to be stored in a data type. When `sql_mode=STRICT_TRANS_TABLES` (the default) is set, an out-of-range value generates an error. If strict mode is not in effect, the value is rounded to the nearest valid value and a warning is generated (which might be hidden, depending on your warning settings).


An example of non-strict out-of-range behavior:


```
TRUNCATE tinyint_signed_example;

-- Disable strict mode or the inserts will fail
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));

INSERT INTO tinyint_signed_example VALUES
   ('Underflow', -129),
   ('Overflow', 128);
```

```
Warning (sql 1264): Out of range value for column 'example' at row 1
Warning (sql 1264): Out of range value for column 'example' at row 2
```

```
SELECT * FROM tinyint_signed_example;
```

```
+-------------+---------+
| description | example |
+-------------+---------+
| Underflow   |    -128 |
| Overflow    |     127 |
+-------------+---------+
```

```
TRUNCATE tinyint_unsigned_example;

-- Disable strict mode or the inserts will fail
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));

INSERT INTO tinyint_unsigned_example VALUES
   ('Underflow', -1),
   ('Overflow', 256);
```

```
Warning (sql 1264): Out of range value for column 'example' at row 1
Warning (sql 1264): Out of range value for column 'example' at row 2
```

```
SELECT * FROM tinyint_unsigned_example;
```

```
+-------------+---------+
| description | example |
+-------------+---------+
| Underflow   |       0 |
| Overflow    |     255 |
+-------------+---------+
```

### TINYINT ZEROFILL


A special type of `TINYINT UNSIGNED` is `TINYINT ZEROFILL`, which pads out the values with leading zeros in SELECT results. The number of leading zeros are just enough to pad the field out to the length of the type's maximum unsigned value, but the zeros are not included in an expression result or in a UNION `SELECT` column.


Using `TINYINT ZEROFILL` works the same way as `TINYINT UNSIGNED` for most operations except a simple `SELECT`. For example, with the following test table setup:


```
CREATE TABLE tinyint_zerofill_example (
   description VARCHAR(20),
   example TINYINT ZEROFILL
);
INSERT INTO tinyint_zerofill_example VALUES
   ('Zero', 0),
   ('Forty-Two', 42),
   ('Minimum', 0),
   ('Maximum', 255);
```

```
-- Turn off strict mode or the inserts will fail
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));
```

```
INSERT INTO tinyint_zerofill_example VALUES
   ('Underflow', -1),
   ('Overflow', 256);
```

```
Warning (sql 1264): Out of range value for column 'example' at row 1
Warning (sql 1264): Out of range value for column 'example' at row 2
```

The resulting data would look like this:


```
SELECT *, example + 0 FROM tinyint_zerofill_example;
```

```
+-------------+---------+-------------+
| description | example | example + 0 |
+-------------+---------+-------------+
| Zero        |     000 |           0 |
| Forty-Two   |     042 |          42 |
| Minimum     |     000 |           0 |
| Maximum     |     255 |         255 |
| Underflow   |     000 |           0 |
| Overflow    |     255 |         255 |
+-------------+---------+-------------+
```

## See Also


* [Numeric Data Type Overview](numeric-data-type-overview.md)
* [SMALLINT](smallint.md)
* [MEDIUMINT](mediumint.md)
* [INTEGER](int.md)
* [BIGINT](bigint.md)
* [BOOLEAN](boolean.md)

