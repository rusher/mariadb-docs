
# SQL Server and MariaDB Types Comparison


This page helps to map each SQL Server type to the matching MariaDB type.


## Numbers


In MariaDB, numeric types can be declared as `<code>SIGNED</code>` or `<code>UNSIGNED</code>`. By default, numeric columns are `<code>SIGNED</code>`, so not specifying either will not break compatibility with SQL Server.


When using `<code>UNSIGNED</code>` values, there is a potential problem with subtractions. When subtracting an `<code>UNSIGNED</code>` valued from another, the result is usually of an `<code>UNSIGNED</code>` type. But if the result is negative, this will cause an error. To solve this problem, we can enable the [NO_UNSIGNED_SUBTRACTION](../../../variables-and-modes/sql-mode.md#no_unsigned_subtraction) flag in sql_mode.


For more information see [Numeric Data Type Overview](../../../../reference/data-types/data-types-numeric-data-types/numeric-data-type-overview.md).


### Integer Numbers



| SQL Server Types | Size (bytes) | MariaDB Types | Size (bytes) | Notes |
| --- | --- | --- | --- | --- |
| SQL Server Types | Size (bytes) | MariaDB Types | Size (bytes) | Notes |
| tinyint | 1 | [TINYINT](../../../../reference/data-types/data-types-numeric-data-types/tinyint.md) | 1 |  |
| smallint | 2 | [SMALLINT](../../../../reference/data-types/data-types-numeric-data-types/smallint.md) | 2 |  |
|  |  | [MEDIUMINT](../../../../reference/data-types/data-types-numeric-data-types/mediumint.md) | 3 | Takes 3 bytes on disk, but 4 bytes in memory |
| int | 1 | [INT](../../../../../general-resources/learning-and-training/video-presentations-and-screencasts/interviews-related-to-mariadb.md) / [INTEGER](../../../../reference/data-types/data-types-numeric-data-types/integer.md) | 4 |  |
| bigint | 8 | [BIGINT](../../../../reference/data-types/data-types-numeric-data-types/bigint.md) | 8 |  |



### Real Numbers (approximated)



| SQL Server Types | Precision | Size | MariaDB Types | Size |
| --- | --- | --- | --- | --- |
| SQL Server Types | Precision | Size | MariaDB Types | Size |
| float(1-24) | 7 digits | 4 | [FLOAT(0-23)](../../../../reference/data-types/data-types-numeric-data-types/float.md) | 4 |
| float(25-53) | 15 digist | 8 | [FLOAT(24-53)](../../../../reference/data-types/data-types-numeric-data-types/float.md) | 8 |



MariaDB supports an alternative syntax: `<code>FLOAT(M, D)</code>`. M is the total number of digits, and D is the number of digits after the decimal point.


See also: [Floating-point Accuracy](../../../../reference/data-types/data-types-numeric-data-types/floating-point-accuracy.md).


#### Aliases


In SQL Server `<code>real</code>` is an alias for `<code>float(24)</code>`.


In MariaDB [DOUBLE](../../../../reference/data-types/data-types-numeric-data-types/double.md), and [DOUBLE PRECISION](../../../../reference/data-types/data-types-numeric-data-types/double-precision.md) are aliases for `<code>FLOAT(24-53)</code>`.


Normally, `<code>REAL</code>` is also a synonym for `<code>FLOAT(24-53)</code>`. However, the [sql_mode](../../../variables-and-modes/sql-mode.md) variable can be set with the `<code>REAL_AS_FLOAT</code>` flag to make `<code>REAL</code>` a synonym for `<code>FLOAT(0-23)</code>`.


### Real Numbers (Exact)



| SQL Server Types | Precision | Size (bytes) | MariaDB Types | Precision | Size (bytes) |
| --- | --- | --- | --- | --- | --- |
| SQL Server Types | Precision | Size (bytes) | MariaDB Types | Precision | Size (bytes) |
| decimal | 0 - 38 | Up to 17 | [DECIMAL](../../../../reference/data-types/data-types-numeric-data-types/decimal.md) | 0 - 38 | [See table](../../../../reference/data-types/data-type-storage-requirements.md#decimal) |



MariaDB supports this syntax: `<code>DECIMAL(M, D)</code>`. M and D are both optional. M is the total number of digits (10 by default), and D is the number of digits after the decimal point (0 by default). In SQL Server, defaults are 18 and 0, respectively. The reason for this difference is that SQL standard imposes a default of 0 for D, but it leaves the implementation free to choose any default for M.


SQL Server `<code>DECIMAL</code>` is equivalent to MariaDB `<code>DECIMAL(18)</code>`.


#### Aliases


The following [aliases](../../../../reference/data-types/data-types-numeric-data-types/dec-numeric-fixed.md) for `<code>DECIMAL</code>` are recognized in both SQL Server and MariaDB: `<code>DEC</code>`, `<code>NUMERIC</code>`. MariaDB also allows one to use `<code>FIXED</code>`.


### Money


SQL Server `<code>money</code>` and `<code>smallmoney</code>` types represent real numbers guaranteeing a very low level of approximation (five decimal digits are accurate), optionally associated with one of the supported currencies.


MariaDB doesn't have monetary types. To represent amounts of money:


* Store the currency in a separate column, if necessary. It's possible to use a foreign key to a currencies table, or the [ENUM](../../../../reference/data-types/string-data-types/enum.md) type.
* Use a non-approximated type:

  * [DECIMAL](../../../../reference/data-types/data-types-numeric-data-types/decimal.md) is very convenient, as it allows one to store the number as-is. But calculations are potentially slower.
  * An integer type is faster for calculations. It is possible to store, for example, the amount of money multiplied by 100.


There is a small incompatibility that users should be aware about. `<code>money</code>` and `<code>smallmoney</code>` are accurate to about 4 decimal digits. This means that, if you use enough decimal digits, operations on these types may produce different results than the results they would produce on MariaDB types.


### Bits


The [BIT](../../../../reference/sql-statements-and-structure/temporal-tables/bitemporal-tables.md) type is supported in MariaDB. Its maximum size is `<code>BIT(64)</code>`. The `<code>BIT</code>` type has a fixed length. If we insert a value which requires less bits than the ones that are allocated, zero-bits are padded on the left.


In MariaDB, binary values can be written in one of the following ways:


* `<code>b'value'</code>`
* `<code>0value</code>`
where `<code>value</code>` is a sequence of 0 and 1 digits. Hexadecimal syntax can also be used. For more details, see [Binary Literals](../../../../reference/sql-statements-and-structure/sql-language-structure/binary-literals.md) and [Hexadecimal Literals](../../../../reference/sql-statements-and-structure/sql-language-structure/hexadecimal-literals.md).


MariaDB and SQL Server have different sets of bitwise operators. See [Bit Functions and Operators](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/README.md).


## BOOLEAN Pseudo-Type


In SQL Server, it is common to use `<code>bit</code>` to represent boolean values. In MariaDB it is possible to do the same, but this is not a common practice.


A column can also be defined as [BOOLEAN](../../../../reference/data-types/data-types-numeric-data-types/boolean.md) or `<code>BOOL</code>`, which is just a synonym for [TINYINT](../../../../reference/data-types/data-types-numeric-data-types/tinyint.md). `<code>TRUE</code>` and `<code>FALSE</code>` keywords also exist, but they are synonyms for 1 and 0. To understand what this implies, see [Boolean Literals](../../../../reference/sql-statements-and-structure/sql-language-structure/sql-language-structure-boolean-literals.md).


In MariaDB `<code>'True'</code>` and `<code>'False'</code>` are always strings.


## Date and Time



| SQL Server Types | Range | Precision | Size (bytes) | MariaDB Types | Range | Size (bytes) | Precision | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SQL Server Types | Range | Precision | Size (bytes) | MariaDB Types | Range | Size (bytes) | Precision | Notes |
| date | 0001-01-01 - 9999-12-31 | 3 | / | [DATE](../../../../reference/sql-statements-and-structure/sql-language-structure/date-and-time-literals.md) | 0001-01-01 - 9999-12-31 | 3 | / | They cover the same range |
| datetime | 1753-01-01 - 9999-12-31 | 8 | 0 to 3, rounded | [DATETIME](../../../../reference/data-types/date-and-time-data-types/datetime.md) | 001-01-01 - 9999-12-31 | 8 | 0 to 6 | MariaDB values are not approximated, see below. |
| datetime2 | 001-01-01 - 9999-12-31 | 8 | 6 to 8 | [DATETIME](../../../../reference/data-types/date-and-time-data-types/datetime.md) | 001-01-01 - 9999-12-31 | 8 | 0 to 6 | MariaDB values are not approximated, see below. |
| smalldatetime |  |  |  | [DATETIME](../../../../reference/data-types/date-and-time-data-types/datetime.md) |  |  |  |  |
| datetimeoffset |  |  |  | [DATETIME](../../../../reference/data-types/date-and-time-data-types/datetime.md) |  |  |  |  |
| time |  |  |  | [TIME](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/time_ms-column-in-information_schemaprocesslist.md) |  |  |  |  |



You may also consider the following MariaDB types:


* [TIMESTAMP](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/timestamp-function.md) has little to do with SQL Server's `<code>timestamp</code>`. In MariaDB it is the number of seconds elapsed since the beginning of 1970-01-01, with a decimal precision up to 6 digits (0 by default). The maximum allowed value is '2038-01-19 03:14:07'. Values are always stored in UTC. A TIMESTAMP column can optionally be automatically set to the current timestamp on insert, on update, or both. It is not meant to be a unique row identifier. Also, in MariaDB the range of TIMESTAMP values is
* [YEAR](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/year.md) is a 1-byte type representing years between 1901 and 2155, as well as 0000.


### Zero Values


MariaDB allows a special value where all the parts of a date are zeroes: `<code>'0000-00-00'</code>`. This can be disallowed by setting [sql_mode=NO_ZERO_DATE](../../../variables-and-modes/sql-mode.md#no_zero_date).


It is also possible to use values where only some date parts are zeroes, for example `<code>'1994-01-00'</code>` or `<code>'1994-00-00'</code>`. These values can be disallowed by setting [sql_mode=NO_ZERO_IN_DATE](../../../variables-and-modes/sql-mode.md#no_zero_in_date). They are not affected by `<code>NO_ZERO_DATE</code>`.


### Syntax


Several different date formats are understood. Typically used formats are `<code>'YYYY-MM-DD'</code>` and `<code>YYYYMMDD</code>`. Several separators are accepted.


The syntax defined in standard SQL and ODBC are understood - for example, `<code>DATE '1994-01-01'</code>` and `<code>{d '1994-01-01'} </code>`. Using these eliminates possible ambiguities in contexts where a temporal value could be interpreted as a string or as an integer.


See [Date and Time Literals](../../../../reference/sql-statements-and-structure/sql-language-structure/date-and-time-literals.md) for the details.


### Precision


For temporal types that include a day time, MariaDB allows a precision from 0 to 6 (microseconds), 0 being the default. The subsecond part is never approximated. It adds up to 3 bytes. See [Data Type Storage Requirements](../../../../reference/data-types/data-type-storage-requirements.md#microseconds) for the details.


## String and Binary


### Binary Strings



| SQL Server Types | Size (bytes) | MariaDB Types | Notes |
| --- | --- | --- | --- |
| SQL Server Types | Size (bytes) | MariaDB Types | Notes |
| binary | 1 to 8000 | [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md) or [BLOB](../../../../reference/data-types/string-data-types/blob-and-text-data-types.md) | See below for BLOB types |
| varbinary | 1 to 8000 | [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md) or [BLOB](../../../../reference/data-types/string-data-types/blob-and-text-data-types.md) | See below for BLOB types |
| image | 2^31-1 | [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md) or [BLOB](../../../../reference/data-types/string-data-types/blob-and-text-data-types.md) | See below for BLOB types |



The `<code>VARBINARY</code>` type is similar to `<code>VARCHAR</code>`, but stores binary byte strings, just like SQL Server `<code>binary</code>` does.


For large binary strings, MariaDB has four `<code>BLOB</code>` types, with different sizes. See [BLOB and TEXT Data Types](../../../../reference/data-types/string-data-types/blob-and-text-data-types.md) for more information.


### Character Strings


One important difference between SQL Server and MariaDB is that **in MariaDB character sets do not depend on types and collations**. Character sets can be set at database, table or column level. If this is not done, the default character sets applies, which is specified by the [character_set_server](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_server) system variable.


To create a MariaDB table that is identical to a SQL Server table, **it may be necessary to specify a character set for each string column**. However, in many cases using UTF-8 will work.



| SQL Server Types | Size (bytes) | MariaDB Types | Size (bytes) | Character set |
| --- | --- | --- | --- | --- |
| SQL Server Types | Size (bytes) | MariaDB Types | Size (bytes) | Character set |
| char | 1 to 8000 | [CHAR](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/charset.md) | 0 to 255 | utf8mb4 (1, 4) |
| varchar | 1 to 8000 | [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md) | 0 to 65,532 (2) | utf8mb4 (1) |
| text | 2^31-1 | [TEXT](../../../../reference/data-types/string-data-types/blob-and-text-data-types.md) | 2^31-1 | ucs2 |
| nchar | 2 to 8000 | [CHAR](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/charset.md) | 0 to 255 | utf16 or ucs2 (3, 4) |
| nvarchar | 2 to 8000 | [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md) | 0 to 65,532 (2) (5) | utf16 or ucs2 (1) (3) |
| ntext | 2^30 - 1 | [TEXT](../../../../reference/data-types/string-data-types/blob-and-text-data-types.md) | 2^31-1 | ucs2 |



**Notes:**


1) If SQL Server uses a non-unicode collation, a subset of UTF-8 is used. So it is possible to use a smaller character set on MariaDB too.


2) [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) has a maximum row length of 65,535 bytes. [TEXT](../../../../reference/data-types/string-data-types/blob-and-text-data-types.md) columns do not contribute to the row size, because they are stored separately (except for the first 12 bytes).


3) In SQL Server, UTF-16 is used if data contains Supplementary Characters, otherwise UCS-2 is used. If not sure, use `<code>utf16</code>` in MariaDB.


4) In SQL Server, the value of `<code>ANSI_PADDING</code>` determines if `<code>char</code>` values should be padded with spaces to their maximum length. In MariaDB, this depends on the [PAD_CHAR_TO_FULL_LENGTH](../../../variables-and-modes/sql-mode.md#pad_char_to_full_length) sql_mode flag.


5) See JSON, below.


## SQL Server Special Types


### rowversion


MariaDB does not have the `<code>rowversion</code>` type.


If the only purpose is to check if a row has been modified since its last read, a [TIMESTAMP](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/timestamp-function.md) column can be used instead. Its default value should be `<code>ON UPDATE CURRENT_TIMESTAMP</code>`. In this way, the timestamp will be updated whenever the column is modified.


A way to preserve much more information is to use a [temporal table](../../../../reference/sql-statements-and-structure/temporal-tables/system-versioned-tables.md). Past versions of the row will be preserved.


### sql_variant


MariaDB does not support the `<code>sql_variant</code>` type.


MariaDB is quite flexible about implicit and explicit [type conversions](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/type-conversion.md). Therefore, for most cases storing the values as a string should be equivalent to using `<code>sql_variant</code>`.


Be aware that the maximum length of an `<code>sql_variant</code>` value is 8,000 bytes. In MariaDB, you may need to use `<code>TINYBLOB</code>`.


### uniqueidentifier


While MariaDB does not support the `<code>uniqueidentifier</code>` type, the [UUID](../../../../reference/data-types/string-data-types/uuid-data-type.md) type can typically be used for the same purpose.


`<code>uniqueidentifier</code>` columns contain 16-bit GUIDs. MariaDB UUID columns store UUIDv1 values (128 bits).


The UUID type was implemented in [MariaDB 10.7](../../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md). On older versions, you can generate unique values with the [UUID()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/miscellaneous-functions/uuid.md) or [UUID_SHORT()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/miscellaneous-functions/uuid_short.md) functions, and store them in `<code>BIT(128)</code>` or `<code>BIT(64)</code>` columns, respectively.


### xml


MariaDB does not support the `<code>xml</code>` type.


XML data can be stored in string columns. MariaDB supports several XML functions.


### JSON


With SQL Server, typically JSON documents are stored in `<code>nvarchar</code>` columns in a text form.


MariaDB has a [JSON](../../../../reference/storage-engines/connect/json-sample-files.md) pseudo-type that maps to [LONGTEXT](../../../../reference/data-types/string-data-types/longtext.md). However, from [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md) the `<code>JSON</code>` pseudo-type also checks that the value is valid a JSON document.


MariaDB supports different JSON functions than SQL Server. MariaDB currently has more functions, and SQL Server syntax will not work. See [JSON functions](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/json-functions/README.md) for more information.


## MariaDB Specific Types


The following types are supported by MariaDB and don't have a direct equivalent in SQL Server. If you are migrating your database to MariaDB, you can consider using these types.


* [INET6](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/miscellaneous-functions/inet6_aton.md) - IPv6 addresses.
* [INET4](../../../../reference/data-types/string-data-types/inet4.md) - IPv4 addresses.

