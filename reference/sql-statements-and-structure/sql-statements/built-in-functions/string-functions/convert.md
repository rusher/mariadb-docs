# CONVERT

#

# Syntax

```
CONVERT(expr,type), CONVERT(expr USING transcoding_name)
```

#

# Description

The	`CONVERT()` and [CAST()](cast.md) functions take a value of one type and produce a value of another type.

The type can be one of the following values:

* [BINARY](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md)
* [CHAR](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/charset-narrowing-optimization.md)
* [DATE](../../../../data-types/date-and-time-data-types/date.md)
* [DATETIME](../../../../data-types/date-and-time-data-types/datetime.md)
* [DECIMAL[(M[,D])](../../../../data-types/data-types-numeric-data-types/decimal.md)]
* [DOUBLE](../../../../data-types/data-types-numeric-data-types/double.md)
* [FLOAT](../../../../data-types/data-types-numeric-data-types/floating-point-accuracy.md) (from [MariaDB 10.4.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-104-series/mariadb-1045-release-notes))
* [INTEGER](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/intvar_event.md)

 * Short for `SIGNED INTEGER`
* SIGNED [INTEGER]
* UNSIGNED [INTEGER]
* [TIME](../../../../data-types/date-and-time-data-types/time.md)
* [VARCHAR](../../../../data-types/string-data-types/varchar.md) (in [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/sql_modeoracle), from [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-103))

Note that in MariaDB, `INT` and `INTEGER` are the same thing.

`BINARY` produces a string with the [BINARY](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) data type. If the optional length is given, `BINARY(N)` causes the cast to use no more than `N` bytes of the argument. Values shorter than the given number in bytes are padded with 0x00 bytes to make them equal the length value.

`CHAR(N)` causes the cast to use no more than the number of characters given in the argument.

The main difference between the [CAST()](cast.md) and `CONVERT()` is that `CONVERT(expr,type)` is ODBC syntax while [CAST(expr as type)](cast.md) and `CONVERT(... USING ...)` are SQL92 syntax.

`CONVERT()` with `USING` is used to convert data between different [character sets](/kb/en/data-types-character-sets-and-collations/). In MariaDB, transcoding names are the same as the
corresponding character set names. For example, this statement
converts the string 'abc' in the default character set to the
corresponding string in the utf8 character set:

```
SELECT CONVERT('abc' USING utf8);
```

#

# Examples

```
SELECT enum_col FROM tbl_name 
ORDER BY CAST(enum_col AS CHAR);
```

Converting a [BINARY](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) to string to permit the [LOWER](lower.md) function to work:

```
SET @x = 'AardVark';

SET @x = BINARY 'AardVark';

SELECT LOWER(@x), LOWER(CONVERT (@x USING latin1));
+-----------+----------------------------------+
| LOWER(@x) | LOWER(CONVERT (@x USING latin1)) |
+-----------+----------------------------------+
| AardVark | aardvark |
+-----------+----------------------------------+
```

#

# See Also

* [Character Sets and Collations](/kb/en/data-types-character-sets-and-collations/)