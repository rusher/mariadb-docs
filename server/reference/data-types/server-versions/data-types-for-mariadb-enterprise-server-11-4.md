# data-types-for-mariadb-enterprise-server-11-4

## Data Types for MariaDB Enterprise Server 11.4

## Overview

Each column in a table has a specified data type that defines what kind of data can be stored in the column.

## Integer Numeric Types

| Data Type                                       | Class                                            | Description                                                                                                           |
| ----------------------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| Data Type                                       | Class                                            | Description                                                                                                           |
| [BIGINT](../numeric-data-types/bigint.md)       | Integer                                          | Integer from -9223372036854775808 to 9223372036854775807 when signed, or from 0 to 18446744073709551615 when unsigned |
| [BIT](../numeric-data-types/bit.md)             | Bit                                              | Bit data                                                                                                              |
| [BOOL](../numeric-data-types/bool.md)           | Integer                                          | See [TINYINT](../numeric-data-types/tinyint.md)                                                                       |
| [BOOLEAN](../numeric-data-types/boolean.md)     | Integer                                          | See [TINYINT](../numeric-data-types/tinyint.md)                                                                       |
| [INT](../numeric-data-types/int.md)             | Integer                                          | Integer from -2147483648 to 2147483647 when signed, or from 0 to 4294967295 when unsigned                             |
| [INT1](../numeric-data-types/int1.md)           | Integer                                          | See [TINYINT](../numeric-data-types/tinyint.md)                                                                       |
| [INT2](../numeric-data-types/int2.md)           | Integer                                          | See [SMALLINT](../numeric-data-types/smallint.md)                                                                     |
| \[                                              | INT3]\(../data-types-numeric-data-types/int3.md) | Integer                                                                                                               |
| [INT4](../numeric-data-types/int4.md)           | Integer                                          | See [INT](../numeric-data-types/int.md)                                                                               |
| [INT8](../numeric-data-types/int8.md)           | Integer                                          | See [BIGINT](../numeric-data-types/bigint.md)                                                                         |
| [INTEGER](../numeric-data-types/integer.md)     | Integer                                          | See [INT](../numeric-data-types/int.md)                                                                               |
| [MEDIUMINT](../numeric-data-types/mediumint.md) | Integer                                          | Integer from -8388608 to 8388607 when signed, or from 0 to 16777215 when unsigne                                      |
| [MIDDLEINT](../numeric-data-types/middleint.md) | Integer                                          | See [MEDIUMINT](../numeric-data-types/mediumint.md)                                                                   |
| [SERIAL](../serial.md)                          | Alias                                            | This is an alias for BIGINT UNSIGNED NOT NULL AUTO\_INCREMENT UNIQUE                                                  |
| [SMALLINT](../numeric-data-types/smallint.md)   | Integer                                          | Integer from -32768 to 32767 when signed, or from 0 to 65535 when unsigned                                            |
| [TINYINT](../numeric-data-types/tinyint.md)     | Integer                                          | Integer from -128 to 127 when signed, or from 0 to 255 when unsigned                                                  |

## Non-integer Numeric Types

| Data Type                                                     | Class     | Description                                     |
| ------------------------------------------------------------- | --------- | ----------------------------------------------- |
| Data Type                                                     | Class     | Description                                     |
| [DEC](../numeric-data-types/dec-numeric-fixed.md)             | Fixed Num | See [DECIMAL](../numeric-data-types/decimal.md) |
| [DECIMAL](../numeric-data-types/decimal.md)                   | Fixed Num | Fixed-point number                              |
| [DOUBLE](../numeric-data-types/double.md)                     | Float     | Double-precision floating-point number          |
| [DOUBLE PRECISION](../numeric-data-types/double-precision.md) | Float     | See [DOUBLE](../numeric-data-types/double.md)   |
| [FIXED](../numeric-data-types/fixed.md)                       | Fixed Num | See [DECIMAL](../numeric-data-types/decimal.md) |
| [FLOAT](../numeric-data-types/float.md)                       | Float     | Single-precision floating-point number          |
| [FLOAT4](../numeric-data-types/float4.md)                     | Float     | See [FLOAT](../numeric-data-types/float.md)     |
| [FLOAT8](../numeric-data-types/float8.md)                     | Float     | See [DOUBLE](../numeric-data-types/double.md)   |
| [NUMBER](../numeric-data-types/number.md)                     | SQL/PL    | See [DECIMAL](../numeric-data-types/decimal.md) |
| [NUMERIC](../numeric-data-types/numeric.md)                   | Fixed Num | See [DECIMAL](../numeric-data-types/decimal.md) |
| [REAL](../numeric-data-types/real.md)                         | Float     | See [DOUBLE](../numeric-data-types/double.md)   |

## String Types

| Data Type                                                                        | Class  | Description                                                                                                                 |
| -------------------------------------------------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------- |
| Data Type                                                                        | Class  | Description                                                                                                                 |
| [BINARY](binary-type/)                                                           | String | Fixed-length string for binary data with limit up to 255 bytes                                                              |
| [BLOB](../string-data-types/blob.md)                                             | String | String for variable-length binary data up to 65,535 bytes                                                                   |
| [CHAR](../string-data-types/char.md)                                             | String | Fixed-length string with limit up to 255 bytes                                                                              |
| [CHAR BYTE](../string-data-types/char-byte.md)                                   | String | See [BINARY](binary-type/)                                                                                                  |
| [CHAR VARYING](../string-data-types/char-varying.md)                             | String | See [VARCHAR](../string-data-types/varchar.md)                                                                              |
| [CHARACTER](../string-data-types/character.md)                                   | String | See [CHAR](../string-data-types/char.md)                                                                                    |
| [CHARACTER VARYING](../../../../en/character-varying/)                           | String | See [VARCHAR](../string-data-types/varchar.md)                                                                              |
| [CLOB](../string-data-types/clob.md)                                             | SQL/PL | See [LONGTEXT](../string-data-types/longtext.md)                                                                            |
| [INET6](../string-data-types/inet6.md)                                           | Binary | Stores an INET6 or mapped INET4 network address as a BINARY(16) internally while translating it into a CHAR(39) to the user |
| [JSON](json-type/)                                                               | String | An alias of LONGTEXT with a default json\_valid() CHECK (check added in MariaDB Community Server 10.4.3)                    |
| [LONG](../../../../en/long/)                                                     | String | See [MEDIUMTEXT](../string-data-types/mediumtext.md)                                                                        |
| [LONG CHAR VARYING](../string-data-types/long-char-varying.md)                   | String | See [MEDIUMTEXT](../string-data-types/mediumtext.md)                                                                        |
| [LONG CHARACTER VARYING](../string-data-types/long-character-varying.md)         | String | See [MEDIUMTEXT](../string-data-types/mediumtext.md)                                                                        |
| [LONG VARBINARY](../string-data-types/long-varbinary.md)                         | String | See [MEDIUMBLOB](../string-data-types/mediumblob.md)                                                                        |
| [LONG VARCHAR](../string-data-types/long-varchar.md)                             | String | See [MEDIUMTEXT](../string-data-types/mediumtext.md)                                                                        |
| [LONG VARCHARACTER](../string-data-types/long-varcharacter.md)                   | String | See [MEDIUMTEXT](../string-data-types/mediumtext.md)                                                                        |
| [LONGBLOB](../string-data-types/longblob.md)                                     | String | String for variable-length binary data up to 4,294,967,295 bytes                                                            |
| [LONGTEXT](../string-data-types/longtext.md)                                     | String | String for variable-length text data up to 4,294,967,295 bytes                                                              |
| [MEDIUMBLOB](../string-data-types/mediumblob.md)                                 | String | String for variable-length binary data up to 16,777,215 bytes                                                               |
| [MEDIUMTEXT](../string-data-types/mediumtext.md)                                 | String | String for variable-length text data up to 16,777,215 bytes                                                                 |
| [NATIONAL CHAR](../string-data-types/national-char.md)                           | String | Fixed-length string of specific character set with limit up to 255 bytes                                                    |
| [NATIONAL CHAR VARYING](../string-data-types/national-char-varying.md)           | String | See [NATIONAL VARCHAR](../string-data-types/national-varchar.md)                                                            |
| [NATIONAL CHARACTER](../string-data-types/national-character.md)                 | String | See [NATIONAL CHAR](../string-data-types/national-char.md)                                                                  |
| [NATIONAL CHARACTER VARYING](../string-data-types/national-character-varying.md) | String | See [NATIONAL VARCHAR](../string-data-types/national-varchar.md)                                                            |
| [NATIONAL VARCHAR](../string-data-types/national-varchar.md)                     | String | Variable-length string of specific character set with limit up to 65,535 bytes                                              |
| [NATIONAL VARCHARACTER](../string-data-types/national-varcharacter.md)           | String | See [NATIONAL VARCHAR](../string-data-types/national-varchar.md)                                                            |
| [NCHAR](../string-data-types/nchar.md)                                           | String | See [NATIONAL CHAR](../string-data-types/national-char.md)                                                                  |
| [NCHAR VARCHAR](../string-data-types/nchar-varchar.md)                           | String | See [NATIONAL VARCHAR](../string-data-types/national-varchar.md)                                                            |
| [NCHAR VARCHARACTER](../string-data-types/nchar-varcharacter.md)                 | String | See [NATIONAL VARCHAR](../string-data-types/national-varchar.md)                                                            |
| [NCHAR VARYING](../string-data-types/nchar-varying.md)                           | String | See [NATIONAL VARCHAR](../string-data-types/national-varchar.md)                                                            |
| [NVARCHAR](../../../../en/nvarchar/)                                             | String | See [NATIONAL VARCHAR](../string-data-types/national-varchar.md)                                                            |
| [RAW](../string-data-types/raw.md)                                               | SQL/PL | See [VARBINARY](../string-data-types/varbinary.md)                                                                          |
| [TEXT](../string-data-types/text.md)                                             | String | String for variable-length text data up to 65,535 bytes                                                                     |
| [TINYBLOB](../string-data-types/tinyblob.md)                                     | String | String for variable-length binary data up to 255 bytes                                                                      |
| [TINYTEXT](../string-data-types/tinytext.md)                                     | String | String for variable-length text data up to 255 bytes                                                                        |
| [VARBINARY](../string-data-types/varbinary.md)                                   | String | Variable-length string for binary data with limit up to 65,535 bytes                                                        |
| [VARCHAR](../string-data-types/varchar.md)                                       | String | Variable-length string with limit up to 65,535 bytes                                                                        |
| [VARCHAR2](../string-data-types/varchar2.md)                                     | SQL/PL | See [VARCHAR](../string-data-types/varchar.md)                                                                              |
| [VARCHARACTER](../string-data-types/varcharacter.md)                             | String | See [VARCHAR](../string-data-types/varchar.md)                                                                              |

## Date & Time Types

| Data Type                                                     | Class     | Description                                                                                                    |
| ------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------- |
| Data Type                                                     | Class     | Description                                                                                                    |
| [DATE](../date-and-time-data-types/date.md)                   | Date      | Year, month, day                                                                                               |
| [DATE (with time portion)](date-with-time-portion/)           | SQL/PL    | See [DATETIME](../date-and-time-data-types/datetime.md)                                                        |
| [DATETIME](../date-and-time-data-types/datetime.md)           | Date/Time | Year (1000-9999), month, day, hours, minutes, seconds                                                          |
| [SQL\_TSI\_YEAR](../date-and-time-data-types/sql_tsi_year.md) | Date      | See [YEAR](../../sql-functions/date-time-functions/year.md)                                                    |
| [TIME](../date-and-time-data-types/time.md)                   | Time      | Hours, minutes, seconds                                                                                        |
| [TIMESTAMP](timestamp-type/)                                  | Date/Time | Accepts a datetime value consisting of year (1970-2038), month, day, hours, minutes, seconds, and microseconds |
| [YEAR](../../sql-functions/date-time-functions/year.md)       | Date      | Two-digit or four-digit year                                                                                   |

## Geometry Types

| Data Type                                                                                                    | Class    | Description                                                       |
| ------------------------------------------------------------------------------------------------------------ | -------- | ----------------------------------------------------------------- |
| Data Type                                                                                                    | Class    | Description                                                       |
| [GEOMETRY](../../sql-structure/geometry/geometry-types.md)                                                   | Geometry | Accepts collection data; and point, line, polygon single or multi |
| [GEOMETRYCOLLECTION](../../sql-statements/geometry-constructors/geometry-constructors/geometrycollection.md) | Geometry | WKB Geometry Collection                                           |
| [LINESTRING](../../sql-statements/geometry-constructors/geometry-constructors/linestring.md)                 | Geometry | WKB LineString from WKB Point coordinate data                     |
| [MULTILINESTRING](../../sql-statements/geometry-constructors/geometry-constructors/multilinestring.md)       | Geometry | WKB MultiLineString from WKB LineString data                      |
| [MULTIPOINT](../../sql-statements/geometry-constructors/geometry-constructors/multipoint.md)                 | Geometry | WKB MultiPoint from WKB Point coordinate data                     |
| [MULTIPOLYGON](../../sql-statements/geometry-constructors/geometry-constructors/multipolygon.md)             | Geometry | WKB MultiPolygon from WKB Polygon data                            |
| [POINT](../../sql-statements/geometry-constructors/geometry-constructors/point.md)                           | Geometry | WKB Point coordinate data                                         |
| [POLYGON](../../sql-statements/geometry-constructors/geometry-constructors/polygon.md)                       | Geometry | WKB Polygon from WKB LineString data                              |

## Other Types

| Data Type                                    | Class   | Description                                                                    |
| -------------------------------------------- | ------- | ------------------------------------------------------------------------------ |
| Data Type                                    | Class   | Description                                                                    |
| [ENUM](../string-data-types/enum.md)         | Set     | A single value from up to 65,535 pre-selected options                          |
| [ROW](../string-data-types/row.md)           | SQL/PSM | This declaration is only available inside a stored procedure                   |
| [ROW TYPE OF](../row-type-of.md)             | SQL/PSM | This is special declaration only available inside a stored procedure           |
| [SET](../string-data-types/set-data-type.md) | Set     | One or more comma-separated values from a set of up to 64 pre-selected options |
| [TYPE OF](../type-of.md)                     | SQL/PSM | This is special declaration only available inside a stored procedure           |

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
