
# DATE_ADD

## Syntax


```
DATE_ADD(date,INTERVAL expr unit)
```


## Description


Performs date arithmetic. The *date* argument specifies the
starting date or datetime value. *expr* is an expression specifying the
interval value to be added to the starting date. *expr* is a
string; it may start with a "`<code>-</code>`" for negative intervals. *unit* is a
keyword indicating the units in which the expression should be interpreted. See [Date and Time Units](date-and-time-units.md) for a complete list of permitted units.


The result type of `<code>DATE_ADD()</code>` is determined as follows:


* if the first argument is of the type `<code>DATETIME</code>`, the function returns `<code>DATETIME</code>`
* if the first argument is `<code>DATE</code>` and the interval uses `<code>HOUR</code>` or smaller units, the function returns `<code>DATETIME</code>`
* if the first argument is `<code>DATE</code>` and the interval uses `<code>DAY</code>` or larger units, the function returns `<code>DATE</code>`
* similarly, if the first argument is `<code>TIME</code>` and the interval uses `<code>DAY</code>` or smaller units the function returns `<code>TIME</code>`, if the interval uses anything larger, the function returns `<code>DATETIME</code>`
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

