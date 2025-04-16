
# ADD_MONTHS


##### MariaDB starting with [10.6.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md)
The ADD_MONTHS function was introduced in [MariaDB 10.6.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md) to enhance Oracle compatibility. Similar functionality can be achieved with the [DATE_ADD](date_add.md) function.


## Syntax


```
ADD_MONTHS(date, months)
```


## Description


`ADD_MONTHS` adds an integer *months* to a given *date* ([DATE](../../../sql-language-structure/date-and-time-literals.md), [DATETIME](../../../../data-types/date-and-time-data-types/datetime.md) or [TIMESTAMP](timestamp-function.md)), returning the resulting date.


*months* can be positive or negative. If months is not a whole number, then it will be rounded to the nearest whole number (not truncated).


The resulting day component will remain the same as that specified in *date*, unless the resulting month has fewer days than the day component of the given date, in which case the day will be the last day of the resulting month.


Returns NULL if given an invalid date, or a NULL argument.


## Examples


```
SELECT ADD_MONTHS('2012-01-31', 2);
+-----------------------------+
| ADD_MONTHS('2012-01-31', 2) |
+-----------------------------+
| 2012-03-31                  |
+-----------------------------+

SELECT ADD_MONTHS('2012-01-31', -5);
+------------------------------+
| ADD_MONTHS('2012-01-31', -5) |
+------------------------------+
| 2011-08-31                   |
+------------------------------+

SELECT ADD_MONTHS('2011-01-31', 1);
+-----------------------------+
| ADD_MONTHS('2011-01-31', 1) |
+-----------------------------+
| 2011-02-28                  |
+-----------------------------+

SELECT ADD_MONTHS('2012-01-31', 1);
+-----------------------------+
| ADD_MONTHS('2012-01-31', 1) |
+-----------------------------+
| 2012-02-29                  |
+-----------------------------+

SELECT ADD_MONTHS('2012-01-31', 2);
+-----------------------------+
| ADD_MONTHS('2012-01-31', 2) |
+-----------------------------+
| 2012-03-31                  |
+-----------------------------+

SELECT ADD_MONTHS('2012-01-31', 3);
+-----------------------------+
| ADD_MONTHS('2012-01-31', 3) |
+-----------------------------+
| 2012-04-30                  |
+-----------------------------+

SELECT ADD_MONTHS('2011-01-15', 2.5);
+-------------------------------+
| ADD_MONTHS('2011-01-15', 2.5) |
+-------------------------------+
| 2011-04-15                    |
+-------------------------------+
1 row in set (0.001 sec)

SELECT ADD_MONTHS('2011-01-15', 2.6);
+-------------------------------+
| ADD_MONTHS('2011-01-15', 2.6) |
+-------------------------------+
| 2011-04-15                    |
+-------------------------------+
1 row in set (0.001 sec)

SELECT ADD_MONTHS('2011-01-15', 2.1);
+-------------------------------+
| ADD_MONTHS('2011-01-15', 2.1) |
+-------------------------------+
| 2011-03-15                    |
+-------------------------------+
1 row in set (0.004 sec)
```

## See Also


* [SQL_MODE=ORACLE](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)

