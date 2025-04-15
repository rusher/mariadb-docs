
# CONVERT

## Syntax


```
CONVERT(expr,type), CONVERT(expr USING transcoding_name)
```


## Description


The	`<code>CONVERT()</code>` and [CAST()](cast.md) functions take a value of one type and produce a value of another type.


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


Note that in MariaDB, `<code>INT</code>` and `<code>INTEGER</code>` are the same thing.


`<code>BINARY</code>` produces a string with the [BINARY](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) data type. If the optional length is given, `<code>BINARY(N)</code>` causes the cast to use no more than `<code>N</code>` bytes of the argument. Values shorter than the given number in bytes are padded with 0x00 bytes to make them equal the length value.


`<code>CHAR(N)</code>` causes the cast to use no more than the number of characters given in the argument.


The main difference between the [CAST()](cast.md) and `<code>CONVERT()</code>` is that `<code>CONVERT(expr,type)</code>` is ODBC syntax while [CAST(expr as type)](cast.md) and `<code>CONVERT(... USING ...)</code>` are SQL92 syntax.


`<code>CONVERT()</code>` with `<code>USING</code>` is used to convert data between different [character sets](../../../../data-types/string-data-types/character-sets/README.md). In MariaDB, transcoding names are the same as the
corresponding character set names. For example, this statement
converts the string 'abc' in the default character set to the
corresponding string in the utf8 character set:


```
SELECT CONVERT('abc' USING utf8);
```

## Examples


```
SELECT enum_col FROM tbl_name 
ORDER BY CAST(enum_col AS CHAR);
```

Converting a [BINARY](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) to string to permit the [LOWER](lower.md) function to work:


```
SET @x = 'AardVark';

SET @x = BINARY 'AardVark';

SELECT LOWER(@x), LOWER(CONVERT (@x USING latin1));
+-----------+----------------------------------+
| LOWER(@x) | LOWER(CONVERT (@x USING latin1)) |
+-----------+----------------------------------+
| AardVark  | aardvark                         |
+-----------+----------------------------------+
```

## See Also


* [Character Sets and Collations](../../../../data-types/string-data-types/character-sets/README.md)

