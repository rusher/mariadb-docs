# CAST

## Syntax

```
CAST(expr AS type)
```

## Description

The `CAST()` function takes a value of one [type](../../../data-types/) and produces a value of another type, similar to the [CONVERT()](convert.md) function.

The type can be one of the following values:

* [BINARY](../../../data-types/string-data-types/binary.md)
* [CHAR](../../../data-types/string-data-types/char.md)
* [DATE](../../../data-types/date-and-time-data-types/date.md)
* [DATETIME](../../../data-types/date-and-time-data-types/datetime.md)
* \[DECIMAL[(M\[,D\])](../../../data-types/data-types-numeric-data-types/decimal.md)]
* [DOUBLE](../../../data-types/data-types-numeric-data-types/double.md)
* [FLOAT](../../../data-types/data-types-numeric-data-types/float.md) (from [MariaDB 10.4.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1045-release-notes))
* [INTEGER](../../../data-types/data-types-numeric-data-types/int.md)
  * Short for `SIGNED INTEGER`
* SIGNED \[INTEGER]
* UNSIGNED \[INTEGER]
* [TIME](../../../data-types/date-and-time-data-types/time.md)
* [VARCHAR](../../../data-types/string-data-types/varchar.md) (in [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/sql_modeoracle), from [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103))

The main difference between `CAST` and [CONVERT()](convert.md) is that `[CONVERT(expr,type)](convert.md)` is ODBC syntax while `CAST(expr as type)` and `[CONVERT(... USING ...)](convert.md)` are SQL92 syntax.

In [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104) and later, you can use the `CAST()` function with the `INTERVAL` keyword.

Until [MariaDB 5.5.31](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/mariadb-5531-release-notes), `X'HHHH'`, the standard SQL syntax for binary string literals, erroneously worked in the same way as `0xHHHH`. In 5.5.31 it was intentionally changed to behave as a string in all contexts (and never as a number).

This introduced an incompatibility with previous versions of MariaDB, and all versions of MySQL (see the example below).

## Examples

Simple casts:

```
SELECT CAST("abc" AS BINARY);
SELECT CAST("1" AS UNSIGNED INTEGER);
SELECT CAST(123 AS CHAR CHARACTER SET utf8)
```

Note that when one casts to [CHAR](../../../data-types/string-data-types/char.md) without specifying the character set, the [collation\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) character set collation will be used. When used with `CHAR CHARACTER SET`, the default collation for that character set will be used.

```
SELECT COLLATION(CAST(123 AS CHAR));
+------------------------------+
| COLLATION(CAST(123 AS CHAR)) |
+------------------------------+
| latin1_swedish_ci            |
+------------------------------+

SELECT COLLATION(CAST(123 AS CHAR CHARACTER SET utf8));
+-------------------------------------------------+
| COLLATION(CAST(123 AS CHAR CHARACTER SET utf8)) |
+-------------------------------------------------+
| utf8_general_ci                                 |
+-------------------------------------------------+
```

If you also want to change the collation, you have to use the `COLLATE` operator:

```
SELECT COLLATION(CAST(123 AS CHAR CHARACTER SET utf8) 
  COLLATE utf8_unicode_ci);
+-------------------------------------------------------------------------+
| COLLATION(CAST(123 AS CHAR CHARACTER SET utf8) COLLATE utf8_unicode_ci) |
+-------------------------------------------------------------------------+
| utf8_unicode_ci                                                         |
+-------------------------------------------------------------------------+
```

Using `CAST()` to order an `[ENUM](../../../../data-types/string-data-types/enum.md)` field as a `[CHAR](../../../../data-types/string-data-types/char.md)` rather than the internal numerical value:

```
CREATE TABLE enum_list (enum_field enum('c','a','b'));

INSERT INTO enum_list (enum_field) 
VALUES('c'),('a'),('c'),('b');

SELECT * FROM enum_list 
ORDER BY enum_field;
+------------+
| enum_field |
+------------+
| c          |
| c          |
| a          |
| b          |
+------------+

SELECT * FROM enum_list 
ORDER BY CAST(enum_field AS CHAR);
+------------+
| enum_field |
+------------+
| a          |
| b          |
| c          |
| c          |
+------------+
```

From [MariaDB 5.5.31](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/mariadb-5531-release-notes), the following will trigger warnings, since `x'aa'` and `'X'aa'` no longer behave as a number. Previously, and in all versions of MySQL, no warnings are triggered since they did erroneously behave as a number:

```
SELECT CAST(0xAA AS UNSIGNED), CAST(x'aa' AS UNSIGNED), CAST(X'aa' AS UNSIGNED);
+------------------------+-------------------------+-------------------------+
| CAST(0xAA AS UNSIGNED) | CAST(x'aa' AS UNSIGNED) | CAST(X'aa' AS UNSIGNED) |
+------------------------+-------------------------+-------------------------+
|                    170 |                       0 |                       0 |
+------------------------+-------------------------+-------------------------+
1 row in set, 2 warnings (0.00 sec)

Warning (Code 1292): Truncated incorrect INTEGER value: '\xAA'
Warning (Code 1292): Truncated incorrect INTEGER value: '\xAA'
```

Casting to intervals:

```
SELECT CAST(2019-01-04 AS INTERVAL DAY_SECOND(2)) AS "Cast";

+-------------+
| Cast        |
+-------------+
| 00:20:14.00 |
+-------------+
```

## See Also

* [Supported data types](../../../data-types/)
* [Microseconds in MariaDB](../date-time-functions/microseconds-in-mariadb.md)
* [String literals](../../../sql-statements-and-structure/sql-language-structure/string-literals.md)
* [COLLATION()](../secondary-functions/information-functions/collation.md)
* [CONVERT()](convert.md)

GPLv2 fill\_help\_tables.sql
