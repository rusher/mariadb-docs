# BINARY

This page describes the BINARY data type. For details about the operator, see [Binary Operator](../../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/binary-operator.md).

#

# Syntax

```
BINARY(M)
```

#

# Description

The `BINARY` type is similar to the `[CHAR](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/charset-narrowing-optimization.md)` type, but stores binary
byte strings rather than non-binary character strings. `M` represents the
column length in bytes.

It contains no character set, and comparison and sorting are based on the numeric value of the bytes.

If the maximum length is exceeded, and [SQL strict mode](../../../server-management/variables-and-modes/sql-mode.md) is not enabled , the extra characters will be dropped with a warning. If strict mode is enabled, an error will occur.

BINARY values are right-padded with `0x00` (the zero byte) to the specified length when inserted. The padding is *not* removed on select, so this needs to be taken into account when sorting and comparing, where all bytes are significant. The zero byte, `0x00` is less than a space for comparison purposes.

#

# Examples

Inserting too many characters, first with strict mode off, then with it on:

```
CREATE TABLE bins (a BINARY(10));

INSERT INTO bins VALUES('12345678901');
Query OK, 1 row affected, 1 warning (0.04 sec)

SELECT * FROM bins;
+------------+
| a |
+------------+
| 1234567890 |
+------------+

SET sql_mode='STRICT_ALL_TABLES';

INSERT INTO bins VALUES('12345678901');
ERROR 1406 (22001): Data too long for column 'a' at row 1
```

Sorting is performed with the byte value:

```
TRUNCATE bins;

INSERT INTO bins VALUES('A'),('B'),('a'),('b');

SELECT * FROM bins ORDER BY a;
+------+
| a |
+------+
| A |
| B |
| a |
| b |
+------+
```

Using [CAST](../../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/cast.md) to sort as a [CHAR](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/charset-narrowing-optimization.md) instead:

```
SELECT * FROM bins ORDER BY CAST(a AS CHAR);
+------+
| a |
+------+
| a |
| A |
| b |
| B |
+------+
```

The field is a BINARY(10), so padding of two '\0's are inserted, causing comparisons that don't take this into account to fail:

```
TRUNCATE bins;

INSERT INTO bins VALUES('12345678');

SELECT a = '12345678', a = '12345678\0\0' from bins;
+----------------+--------------------+
| a = '12345678' | a = '12345678\0\0' |
+----------------+--------------------+
| 0 | 1 |
+----------------+--------------------+
```

#

# See Also

* [CHAR](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/charset-narrowing-optimization.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)