
# CAST

## Syntax


```
CAST(expr AS type)
```


## Description


The `<code>CAST()</code>` function takes a value of one [type](../../../../data-types/data-types-overview/data-types-subcategory/data-types-dec.md) and produces a value of another type, similar to the [CONVERT()](../../../../storage-engines/converting-tables-from-myisam-to-innodb.md) function.


The type can be one of the following values:


* [BINARY](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md)
* [CHAR](../secondary-functions/information-functions/charset.md)
* [DATE](../../../sql-language-structure/date-and-time-literals.md)
* [DATETIME](../../../../data-types/date-and-time-data-types/datetime.md)
* [DECIMAL[(M[,D])](../../../../data-types/data-types-numeric-data-types/decimal.md)]
* [DOUBLE](../../../../data-types/data-types-numeric-data-types/double.md)
* [FLOAT](../../../../data-types/data-types-numeric-data-types/float.md) (from [MariaDB 10.4.5](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1045-release-notes.md))
* [INTEGER](../../../../../../general-resources/learning-and-training/video-presentations-and-screencasts/interviews-related-to-mariadb.md)

  * Short for `<code>SIGNED INTEGER</code>`
* SIGNED [INTEGER]
* UNSIGNED [INTEGER]
* [TIME](../../administrative-sql-statements/system-tables/information-schema/time_ms-column-in-information_schemaprocesslist.md)
* [VARCHAR](../../../../data-types/string-data-types/varchar.md) (in [Oracle mode](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md), from [MariaDB 10.3](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md))


The main difference between `<code>CAST</code>` and [CONVERT()](../../../../storage-engines/converting-tables-from-myisam-to-innodb.md) is that `<code>[CONVERT(expr,type)](../../../../storage-engines/converting-tables-from-myisam-to-innodb.md)</code>` is ODBC syntax while `<code>CAST(expr as type)</code>` and `<code>[CONVERT(... USING ...)](../../../../storage-engines/converting-tables-from-myisam-to-innodb.md)</code>` are SQL92 syntax.


In [MariaDB 10.4](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md) and later, you can use the `<code>CAST()</code>` function with the `<code>INTERVAL</code>` keyword.


Until [MariaDB 5.5.31](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5531-release-notes.md), `<code>X'HHHH'</code>`, the standard SQL syntax for binary string literals, erroneously worked in the same way as `<code>0xHHHH</code>`. In 5.5.31 it was intentionally changed to behave as a string in all contexts (and never as a number).


This introduced an incompatibility with previous versions of MariaDB, and all versions of MySQL (see the example below).


## Examples


Simple casts:


```
SELECT CAST("abc" AS BINARY);
SELECT CAST("1" AS UNSIGNED INTEGER);
SELECT CAST(123 AS CHAR CHARACTER SET utf8)
```

Note that when one casts to [CHAR](../secondary-functions/information-functions/charset.md) without specifying the character set, the [collation_connection](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) character set collation will be used. When used with `<code>CHAR CHARACTER SET</code>`, the default collation for that character set will be used.


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

If you also want to change the collation, you have to use the `<code>COLLATE</code>` operator:


```
SELECT COLLATION(CAST(123 AS CHAR CHARACTER SET utf8) 
  COLLATE utf8_unicode_ci);
+-------------------------------------------------------------------------+
| COLLATION(CAST(123 AS CHAR CHARACTER SET utf8) COLLATE utf8_unicode_ci) |
+-------------------------------------------------------------------------+
| utf8_unicode_ci                                                         |
+-------------------------------------------------------------------------+
```

Using `<code>CAST()</code>` to order an `<code>[ENUM](../../../../data-types/string-data-types/enum.md)</code>` field as a `<code>[CHAR](../secondary-functions/information-functions/charset.md)</code>` rather than the internal numerical value:


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

From [MariaDB 5.5.31](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5531-release-notes.md), the following will trigger warnings, since `<code>x'aa'</code>` and `<code>'X'aa'</code>` no longer behave as a number. Previously, and in all versions of MySQL, no warnings are triggered since they did erroneously behave as a number:


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


* [Supported data types](../../../../data-types/data-types-overview/data-types-subcategory/data-types-dec.md)
* [Microseconds in MariaDB](../date-time-functions/microseconds-in-mariadb.md)
* [String literals](../../../sql-language-structure/string-literals.md)
* [COLLATION()](../secondary-functions/information-functions/collation.md)
* [CONVERT()](../../../../storage-engines/converting-tables-from-myisam-to-innodb.md)

