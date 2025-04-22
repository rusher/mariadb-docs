
# Numeric Data Type Overview


There are a number of numeric data types:


* [TINYINT](tinyint.md)
* [BOOLEAN](boolean.md) - Synonym for TINYINT(1)
* [INT1](int1.md) - Synonym for TINYINT
* [SMALLINT](smallint.md)
* [INT2](int2.md) - Synonym for SMALLINT
* [MEDIUMINT](mediumint.md)
* [INT3](int3.md) - Synonym for MEDIUMINT
* [INT](int.md), INTEGER
* [INT4](int4.md) - Synonym for INT
* [BIGINT](bigint.md)
* [INT8](int8.md) - Synonym for BIGINT
* [DECIMAL](decimal.md), DEC, NUMERIC, FIXED
* [FLOAT](float.md)
* [DOUBLE](double.md), DOUBLE PRECISION, REAL
* [BIT](bit.md)
* [VECTOR](vector.md)


See the specific articles for detailed information on each.


## SIGNED, UNSIGNED and ZEROFILL


Most numeric types can be defined as `SIGNED`, `UNSIGNED` or `ZEROFILL`, for example:


```
TINYINT[(M)] [SIGNED | UNSIGNED | ZEROFILL]
```

If `SIGNED`, or no attribute, is specified, a portion of the numeric type will be reserved for the sign (plus or minus). For example, a TINYINT SIGNED can range from -128 to 127.


If `UNSIGNED` is specified, no portion of the numeric type is reserved for the sign, so for integer types range can be larger. For example, a TINYINT UNSIGNED can range from 0 to 255. Floating point and fixed-point types also can be `UNSIGNED`, but this only prevents negative values from being stored and doesn't alter the range.


If `ZEROFILL` is specified, the column will be set to UNSIGNED and the spaces used by default to pad the field are replaced with zeros. `ZEROFILL` is ignored in expressions or as part of a [UNION](../../sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/joins-subqueries/union.md). `ZEROFILL` is a non-standard MySQL and MariaDB enhancement.


Note that although the preferred syntax indicates that the attributes are exclusive, more than one attribute can be specified.


Until [MariaDB 10.2.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1027-release-notes) ([MDEV-8659](https://jira.mariadb.org/browse/MDEV-8659)), any combination of the attributes could be used in any order, with duplicates. In this case:


* the presence of `ZEROFILL` makes the column `UNSIGNED ZEROFILL`.
* the presence of `UNSIGNED` makes the column `UNSIGNED`.


From [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes), only the following combinations are supported:


* `SIGNED`
* `UNSIGNED`
* `ZEROFILL`
* `UNSIGNED ZEROFILL`
* `ZEROFILL UNSIGNED`


The latter two should be replaced with simply `ZEROFILL`, but are still accepted by the parser.


### Examples


```
CREATE TABLE zf (
  i1 TINYINT SIGNED,
  i2 TINYINT UNSIGNED,
  i3 TINYINT ZEROFILL
);

INSERT INTO zf VALUES (2,2,2);

SELECT * FROM zf;
+------+------+------+
| i1   | i2   | i3   |
+------+------+------+
|    2 |    2 |  002 |
+------+------+------+
```

## Range


When attempting to add a value that is out of the valid range for the numeric type, MariaDB will react depending on the [strict SQL_MODE](../../../server-management/variables-and-modes/sql-mode.md#strict-mode) setting.


If [strict_mode](../../../server-management/variables-and-modes/sql-mode.md#strict-mode) has been set (the default from [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes)), MariaDB will return an error.


If [strict_mode](../../../server-management/variables-and-modes/sql-mode.md#strict-mode) has not been set (the default until [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes)), MariaDB will adjust the number to fit in the field, returning a warning.


### Examples


With strict_mode set:


```
SHOW VARIABLES LIKE 'sql_mode';
+---------------+-------------------------------------------------------------------------------------------+
| Variable_name | Value                                                                                     |
+---------------+-------------------------------------------------------------------------------------------+
| sql_mode      | STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+---------------+-------------------------------------------------------------------------------------------+

CREATE TABLE ranges (i1 TINYINT, i2 SMALLINT, i3 TINYINT UNSIGNED);

INSERT INTO ranges VALUES (257,257,257);
ERROR 1264 (22003): Out of range value for column 'i1' at row 1

SELECT * FROM ranges;
Empty set (0.10 sec)
```

With strict_mode unset:


```
SHOW VARIABLES LIKE 'sql_mode%';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| sql_mode      |       |
+---------------+-------+

CREATE TABLE ranges (i1 TINYINT, i2 SMALLINT, i3 TINYINT UNSIGNED);

INSERT INTO ranges VALUES (257,257,257);
Query OK, 1 row affected, 2 warnings (0.00 sec)

SHOW WARNINGS;
+---------+------+---------------------------------------------+
| Level   | Code | Message                                     |
+---------+------+---------------------------------------------+
| Warning | 1264 | Out of range value for column 'i1' at row 1 |
| Warning | 1264 | Out of range value for column 'i3' at row 1 |
+---------+------+---------------------------------------------+
2 rows in set (0.00 sec)

SELECT * FROM ranges;
+------+------+------+
| i1   | i2   | i3   |
+------+------+------+
|  127 |  257 |  255 |
+------+------+------+
```

## Auto_increment


The `AUTO_INCREMENT` attribute can be used to generate a unique identity for new rows. For more details, see [auto_increment](../auto_increment.md).

