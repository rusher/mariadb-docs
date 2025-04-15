
# Date and Time Literals


## Standard syntaxes


MariaDB supports the SQL standard and ODBC syntaxes for [DATE](date-and-time-literals.md), [TIME](../sql-statements/administrative-sql-statements/system-tables/information-schema/time_ms-column-in-information_schemaprocesslist.md) and [TIMESTAMP](../sql-statements/built-in-functions/date-time-functions/timestamp-function.md) literals.


SQL standard syntax:


* DATE 'string'
* TIME 'string'
* TIMESTAMP 'string'


ODBC syntax:


* {d 'string'}
* {t 'string'}
* {ts 'string'}


The timestamp literals are treated as [DATETIME](../../data-types/date-and-time-data-types/datetime.md) literals, because in MariaDB the range of `<code>DATETIME</code>` is closer to the `<code>TIMESTAMP</code>` range in the SQL standard.


`<code>string</code>` is a string in a proper format, as explained below.


## `<code>DATE</code>` literals


A `<code>DATE</code>` string is a string in one of the following formats: `<code>'YYYY-MM-DD'</code>` or `<code>'YY-MM-DD'</code>`. Note that any punctuation character can be used as delimiter. All delimiters must consist of 1 character. Different delimiters can be used in the same string. Delimiters are optional (but if one delimiter is used, all delimiters must be used).


A `<code>DATE</code>` literal can also be an integer, in one of the following formats: `<code>YYYYMMDD</code>` or `<code>YYMMDD</code>`.


All the following `<code>DATE</code>` literals are valid, and they all represent the same value:


```
'19940101'
'940101'
'1994-01-01'
'94/01/01'
'1994-01/01'
'94:01!01'
19940101
940101
```

## `<code>DATETIME</code>` literals


A `<code>DATETIME</code>` string is a string in one of the following formats: `<code>'YYYY-MM-DD HH:MM:SS'</code>` or `<code>'YY-MM-DD HH:MM:SS'</code>`. Note that any punctuation character can be used as delimiter for the date part and for the time part. All delimiters must consist of 1 character. Different delimiters can be used in the same string. The hours, minutes and seconds parts can consist of one character. For this reason, delimiters are mandatory for `<code>DATETIME</code>` literals.


The delimiter between the date part and the time part can be a `<code>T</code>` or any sequence of space characters (including tabs, new lines and carriage returns).


A `<code>DATETIME</code>` literal can also be a number, in one of the following formats: `<code>YYYYMMDDHHMMSS</code>`, `<code>YYMMDDHHMMSS</code>`, `<code>YYYYMMDD</code>` or `<code>YYMMDD</code>`. In this case, all the time subparts must consist of 2 digits.


All the following `<code>DATE</code>` literals are valid, and they all represent the same value:


```
'1994-01-01T12:30:03'
'1994/01/01\n\t 12+30+03'
'1994/01\\01\n\t 12+30-03'
'1994-01-01 12:30:3'
```

## `<code>TIME</code>` literals


A `<code>TIME</code>` string is a string in one of the following formats: `<code> 'D HH:MM:SS'</code>`, `<code>'HH:MM:SS</code>`, `<code>'D HH:MM'</code>`, `<code>'HH:MM'</code>`, `<code>'D HH'</code>`, or `<code>'SS'</code>`. `<code>D</code>` is a value from 0 to 34 which represents days. `<code>:</code>` is the only allowed delimiter for `<code>TIME</code>` literals. Delimiters are mandatory, with an exception: the `<code>'HHMMSS'</code>` format is allowed. When delimiters are used, each part of the literal can consist of one character.


A `<code>TIME</code>` literal can also be a number in one of the following formats: `<code>HHMMSS</code>`, `<code>MMSS</code>`, or `<code>SS</code>`.


The following literals are equivalent:


```
'09:05:00'
'9:05:0'
'9:5:0'
'090500'
```

## 2-digit years


The year part in `<code>DATE</code>` and `<code>DATETIME</code>` literals is determined as follows:


* `<code>70</code>` - `<code>99</code>` = `<code>1970</code>` - `<code>1999</code>`
* `<code>00</code>` - `<code>69</code>` = `<code>2000</code>` - `<code>2069</code>`


## Microseconds


`<code>DATETIME</code>` and `<code>TIME</code>` literals can have an optional microseconds part. For both string and numeric forms, it is expressed as a decimal part. Up to 6 decimal digits are allowed. Examples:


```
'12:30:00.123456'
123000.123456
```

See [Microseconds in MariaDB](../sql-statements/built-in-functions/date-time-functions/microseconds-in-mariadb.md) for details.


## Date and time literals and the `<code>SQL_MODE</code>`


Unless the [SQL_MODE](../../../server-management/variables-and-modes/sql-mode.md) `<code>NO_ZERO_DATE</code>` flag is set, some special values are allowed: the `<code>'0000-00-00'</code>` `<code>DATE</code>`, the `<code>'00:00:00'</code>` `<code>TIME</code>`, and the `<code>0000-00-00 00:00:00</code>` `<code>DATETIME</code>`.


If the `<code>ALLOW_INVALID_DATES</code>` flag is set, the invalid dates (for example, 30th February) are allowed. If not, if the `<code>NO_ZERO_DATE</code>` is set, an error is produced; otherwise, a zero-date is returned.


Unless the `<code>NO_ZERO_IN_DATE</code>` flag is set, each subpart of a date or time value (years, hours...) can be set to 0.


## See also


* [Date and time units](../sql-statements/built-in-functions/date-time-functions/date-and-time-units.md)

