# VARBINARY

#

# Syntax

```
VARBINARY(M)
```

#

# Description

The VARBINARY type is similar to the [VARCHAR](/kb/en/sql_language-data_types-varchar/) type, but stores binary byte strings rather than non-binary character strings. `M` represents the maximum column length in bytes.

It contains no [character set](/kb/en/data-types-character-sets-and-collations/), and comparison and sorting are based on the numeric value of the bytes.

If the maximum length is exceeded, and [SQL strict mode](../../../server-management/variables-and-modes/sql-mode.md) is not enabled , the extra characters will be dropped with a warning. If strict mode is enabled, an error will occur.

Unlike [BINARY](../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) values, VARBINARYs are not right-padded when inserting.

#

## Oracle Mode

In [Oracle mode from MariaDB 10.3](/kb/en/sql_modeoracle-from-mariadb-103/#synonyms-for-basic-sql-types), `RAW` is a synonym for `VARBINARY`.

#

# Examples

Inserting too many characters, first with strict mode off, then with it on:

```
CREATE TABLE varbins (a VARBINARY(10));

INSERT INTO varbins VALUES('12345678901');
Query OK, 1 row affected, 1 warning (0.04 sec)

SELECT * FROM varbins;
+------------+
| a |
+------------+
| 1234567890 |
+------------+

SET sql_mode='STRICT_ALL_TABLES';

INSERT INTO varbins VALUES('12345678901');
ERROR 1406 (22001): Data too long for column 'a' at row 1
```

Sorting is performed with the byte value:

```
TRUNCATE varbins;

INSERT INTO varbins VALUES('A'),('B'),('a'),('b');

SELECT * FROM varbins ORDER BY a;
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
SELECT * FROM varbins ORDER BY CAST(a AS CHAR);
+------+
| a |
+------+
| a |
| A |
| b |
| B |
+------+
```

#

# See Also

* [VARCHAR](varchar.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)
* [Oracle mode from MariaDB 10.3](/kb/en/sql_modeoracle-from-mariadb-103/#synonyms-for-basic-sql-types)