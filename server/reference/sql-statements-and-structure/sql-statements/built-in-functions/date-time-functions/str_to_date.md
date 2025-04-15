
# STR_TO_DATE

## Syntax


```
STR_TO_DATE(str,format)
```


## Description


This is the inverse of the [DATE_FORMAT](date_format.md)() function. It takes
a string `<code>str</code>` and a format string `<code>format</code>`. `<code>STR_TO_DATE()</code>` returns a
`<code>DATETIME</code>` value if the format string contains both date and time parts, or a
`<code>DATE</code>` or `<code>TIME</code>` value if the string contains only date or time parts.


The date, time, or datetime values contained in `<code>str</code>` should be given in the format indicated by format. If str contains an illegal date, time, or datetime value, `<code>STR_TO_DATE()</code>` returns `<code>NULL</code>`. An illegal value also produces a warning.


Under specific [SQL_MODE](../../../../../server-management/variables-and-modes/sql-mode.md) settings an error may also be generated if the `<code>str</code>` isn't a valid date:


* [ALLOW_INVALID_DATES](../../../../../server-management/variables-and-modes/sql-mode.md#allow_invalid_dates)
* [NO_ZERO_DATE](../../../../../server-management/variables-and-modes/sql-mode.md#no_zero_date)
* [NO_ZERO_IN_DATE](../../../../../server-management/variables-and-modes/sql-mode.md#no_zero_in_date)


The options that can be used by STR_TO_DATE(), as well as its inverse [DATE_FORMAT()](date_format.md) and the [FROM_UNIXTIME()](from_unixtime.md) function, are:



| Option | Description |
| --- | --- |
| Option | Description |
| %a | Short weekday name in current locale (Variable [lc_time_names](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lc_time_names)). |
| %b | Short form month name in current locale. For locale en_US this is one of: Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov or Dec. |
| %c | Month with 1 or 2 digits. |
| %D | Day with English suffix 'th', 'nd', 'st' or 'rd''. (1st, 2nd, 3rd...). |
| %d | Day with 2 digits. |
| %e | Day with 1 or 2 digits. |
| %f | [Microseconds](microseconds-in-mariadb.md) 6 digits. |
| %H | Hour with 2 digits between 00-23. |
| %h | Hour with 2 digits between 01-12. |
| %I | Hour with 2 digits between 01-12. |
| %i | Minute with 2 digits. |
| %j | Day of the year (001-366) |
| %k | Hour with 1 digits between 0-23. |
| %l | Hour with 1 digits between 1-12. |
| %M | Full month name in current locale (Variable [lc_time_names](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lc_time_names)). |
| %m | Month with 2 digits. |
| %p | AM/PM according to current locale (Variable [lc_time_names](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lc_time_names)). |
| %r | Time in 12 hour format, followed by AM/PM. Short for '%I:%i:%S %p'. |
| %S | Seconds with 2 digits. |
| %s | Seconds with 2 digits. |
| %T | Time in 24 hour format. Short for '%H:%i:%S'. |
| %U | Week number (00-53), when first day of the week is Sunday. |
| %u | Week number (00-53), when first day of the week is Monday. |
| %V | Week number (01-53), when first day of the week is Sunday. Used with %X. |
| %v | Week number (01-53), when first day of the week is Monday. Used with %x. |
| %W | Full weekday name in current locale (Variable [lc_time_names](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#lc_time_names)). |
| %w | Day of the week. 0 = Sunday, 6 = Saturday. |
| %X | Year with 4 digits when first day of the week is Sunday. Used with %V. |
| %x | Year with 4 digits when first day of the week is Monday. Used with %v. |
| %Y | Year with 4 digits. |
| %y | Year with 2 digits. |
| %# | For [str_to_date](str_to_date.md)(), skip all numbers. |
| %. | For [str_to_date](str_to_date.md)(), skip all punctation characters. |
| %@ | For [str_to_date](str_to_date.md)(), skip all alpha characters. |
| %% | A literal % character. |



## Examples


```
SELECT STR_TO_DATE('Wednesday, June 2, 2014', '%W, %M %e, %Y');
+---------------------------------------------------------+
| STR_TO_DATE('Wednesday, June 2, 2014', '%W, %M %e, %Y') |
+---------------------------------------------------------+
| 2014-06-02                                              |
+---------------------------------------------------------+


SELECT STR_TO_DATE('Wednesday23423, June 2, 2014', '%W, %M %e, %Y');
+--------------------------------------------------------------+
| STR_TO_DATE('Wednesday23423, June 2, 2014', '%W, %M %e, %Y') |
+--------------------------------------------------------------+
| NULL                                                         |
+--------------------------------------------------------------+
1 row in set, 1 warning (0.00 sec)

SHOW WARNINGS;
+---------+------+-----------------------------------------------------------------------------------+
| Level   | Code | Message                                                                           |
+---------+------+-----------------------------------------------------------------------------------+
| Warning | 1411 | Incorrect datetime value: 'Wednesday23423, June 2, 2014' for function str_to_date |
+---------+------+-----------------------------------------------------------------------------------+

SELECT STR_TO_DATE('Wednesday23423, June 2, 2014', '%W%#, %M %e, %Y');
+----------------------------------------------------------------+
| STR_TO_DATE('Wednesday23423, June 2, 2014', '%W%#, %M %e, %Y') |
+----------------------------------------------------------------+
| 2014-06-02                                                     |
+----------------------------------------------------------------+
```

## See Also


* [DATE_FORMAT()](date_format.md)
* [FROM_UNIXTIME()](from_unixtime.md)

