
# DATE_ADD

## Syntax


```
DATE_ADD(date,INTERVAL expr unit)
```


## Description


Performs date arithmetic. The *date* argument specifies the
starting date or datetime value. *expr* is an expression specifying the
interval value to be added to the starting date. *expr* is a
string; it may start with a "`-`" for negative intervals. *unit* is a
keyword indicating the units in which the expression should be interpreted. See [Date and Time Units](date-and-time-units.md) for a complete list of permitted units.


The result type of `DATE_ADD()` is determined as follows:


* if the first argument is of the type `DATETIME`, the function returns `DATETIME`
* if the first argument is `DATE` and the interval uses `HOUR` or smaller units, the function returns `DATETIME`
* if the first argument is `DATE` and the interval uses `DAY` or larger units, the function returns `DATE`
* similarly, if the first argument is `TIME` and the interval uses `DAY` or smaller units the function returns `TIME`, if the interval uses anything larger, the function returns `DATETIME`
* if the first argument isn't a temporal type, the function returns a string


## Examples


```
SELECT '2008-12-31 23:59:59' + INTERVAL 1 SECOND;
+-------------------------------------------+
| '2008-12-31 23:59:59' + INTERVAL 1 SECOND |
+-------------------------------------------+
| 2009-01-01 00:00:00                       |
+-------------------------------------------+
```

```
SELECT INTERVAL 1 DAY + '2008-12-31';
+-------------------------------+
| INTERVAL 1 DAY + '2008-12-31' |
+-------------------------------+
| 2009-01-01                    |
+-------------------------------+
```

```
SELECT '2005-01-01' - INTERVAL 1 SECOND;
+----------------------------------+
| '2005-01-01' - INTERVAL 1 SECOND |
+----------------------------------+
| 2004-12-31 23:59:59              |
+----------------------------------+
```

```
SELECT DATE_ADD('2000-12-31 23:59:59', INTERVAL 1 SECOND);
+----------------------------------------------------+
| DATE_ADD('2000-12-31 23:59:59', INTERVAL 1 SECOND) |
+----------------------------------------------------+
| 2001-01-01 00:00:00                                |
+----------------------------------------------------+
```

```
SELECT DATE_ADD('2010-12-31 23:59:59', INTERVAL 1 DAY);
+-------------------------------------------------+
| DATE_ADD('2010-12-31 23:59:59', INTERVAL 1 DAY) |
+-------------------------------------------------+
| 2011-01-01 23:59:59                             |
+-------------------------------------------------+
```

```
SELECT DATE_ADD('2100-12-31 23:59:59', INTERVAL '1:1' MINUTE_SECOND);
+---------------------------------------------------------------+
| DATE_ADD('2100-12-31 23:59:59', INTERVAL '1:1' MINUTE_SECOND) |
+---------------------------------------------------------------+
| 2101-01-01 00:01:00                                           |
+---------------------------------------------------------------+
```

```
SELECT DATE_ADD('1900-01-01 00:00:00', INTERVAL '-1 10' DAY_HOUR);
+------------------------------------------------------------+
| DATE_ADD('1900-01-01 00:00:00', INTERVAL '-1 10' DAY_HOUR) |
+------------------------------------------------------------+
| 1899-12-30 14:00:00                                        |
+------------------------------------------------------------+
```

```
SELECT DATE_ADD('1992-12-31 23:59:59.000002', INTERVAL '1.999999' SECOND_MICROSECOND);
+--------------------------------------------------------------------------------+
| DATE_ADD('1992-12-31 23:59:59.000002', INTERVAL '1.999999' SECOND_MICROSECOND) |
+--------------------------------------------------------------------------------+
| 1993-01-01 00:00:01.000001                                                     |
+--------------------------------------------------------------------------------+
```

## See Also


* [DATE_SUB](date_sub.md)
* [ADD_MONTHS](add_months.md)


GPLv2 fill_help_tables.sql

