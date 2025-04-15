
# VARBINARY


## Syntax


```
VARBINARY(M)
```

## Description


The VARBINARY type is similar to the [VARCHAR](varchar.md) type, but stores binary byte strings rather than non-binary character strings. `<code>M</code>` represents the maximum column length in bytes.


It contains no [character set](character-sets/README.md), and comparison and sorting are based on the numeric value of the bytes.


If the maximum length is exceeded, and [SQL strict mode](../../../server-management/variables-and-modes/sql-mode.md) is not enabled , the extra characters will be dropped with a warning. If strict mode is enabled, an error will occur.


Unlike [BINARY](../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) values, VARBINARYs are not right-padded when inserting.


### Oracle Mode


In [Oracle mode](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md), `<code>RAW</code>` is a synonym for `<code>VARBINARY</code>`.


## Examples


Inserting too many characters, first with strict mode off, then with it on:


```
CREATE TABLE varbins (a VARBINARY(10));

INSERT INTO varbins VALUES('12345678901');
Query OK, 1 row affected, 1 warning (0.04 sec)

SELECT * FROM varbins;
+------------+
| a          |
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
| a    |
+------+
| A    |
| B    |
| a    |
| b    |
+------+
```

Using [CAST](../../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/cast.md) to sort as a [CHAR](../../sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/charset.md) instead:


```
SELECT * FROM varbins ORDER BY CAST(a AS CHAR);
+------+
| a    |
+------+
| a    |
| A    |
| b    |
| B    |
+------+
```

### VARBINARY


For our example of VARBINARY we picked a maximum size that avoids overflowing the maximum row size (65535). Keep in mind that a multi-byte character set would need more space in the row than a single-byte character set. We also avoid the auto-conversion of a VARBINARY into a BLOB, MEDIUMBLOB, or LONGBLOB that can happen when STRICT_TRANS_TABLES is not set in the SQL_MODE.


The example:


```
CREATE TABLE varbinary_example (
   description VARCHAR(20),
   example VARBINARY(65511)
) DEFAULT CHARSET=latin1; -- One byte per char makes the examples clearer
```

```
INSERT INTO varbinary_example VALUES
   ('Normal foo', 'foo'),
   ('Trailing spaces foo', 'foo      '),
   ('NULLed', NULL),
   ('Empty', ''),
   ('Maximum', RPAD('', 65511, CHAR(7)));
```

```
SELECT description, LENGTH(example) AS length
   FROM varbinary_example;
```

```
+---------------------+--------+
| description         | length |
+---------------------+--------+
| Normal foo          |      3 |
| Trailing spaces foo |      9 |
| NULLed              |   NULL |
| Empty               |      0 |
| Maximum             |  65511 |
+---------------------+--------+
```

### Data Too Long


When SQL_MODE is strict (the default) a value is considered "too long" when its length exceeds the size of the data type, and an error is generated.


Example of data too long behavior for VARBINARY:


```
TRUNCATE varbinary_example;

INSERT INTO varbinary_example VALUES
   ('Overflow', RPAD('', 65512, CHAR(7)));
```

```
ERROR 1406 (22001): Data too long for column 'example' at row 1
```

## See Also


* [VARCHAR](varchar.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)
* [Oracle mode from MariaDB 10.3](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)

