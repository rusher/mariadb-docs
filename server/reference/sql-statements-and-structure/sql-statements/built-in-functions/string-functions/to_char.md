
# TO_CHAR


##### MariaDB starting with [10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/mariadb-1061-release-notes)
The TO_CHAR function was introduced in [MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/mariadb-1061-release-notes) to enhance Oracle compatibility.


## Syntax


```
TO_CHAR(expr[, fmt])
```


## Description


The `TO_CHAR` function converts an *expr* of type [date](../../../../data-types/date-and-time-data-types/date.md), [datetime](../../../../data-types/date-and-time-data-types/datetime.md), [time](../../../../data-types/date-and-time-data-types/time.md) or [timestamp](../../../../data-types/date-and-time-data-types/timestamp.md) to a string. The optional *fmt* argument supports YYYY/YYY/YY/RRRR/RR/MM/MON/MONTH/MI/DD/DY/HH/HH12/HH24/SS and special characters. The default value is "YYYY-MM-DD HH24:MI:SS".


In Oracle, TO_CHAR can also be used to convert numbers to strings, but this is not supported in MariaDB and will give an error.


## Examples


```
SELECT TO_CHAR('1980-01-11 04:50:39', 'YYYY-MM-DD');
+----------------------------------------------+
| TO_CHAR('1980-01-11 04:50:39', 'YYYY-MM-DD') |
+----------------------------------------------+
| 1980-01-11                                   |
+----------------------------------------------+

SELECT TO_CHAR('1980-01-11 04:50:39', 'HH24-MI-SS');
+----------------------------------------------+
| TO_CHAR('1980-01-11 04:50:39', 'HH24-MI-SS') |
+----------------------------------------------+
| 04-50-39                                     |
+----------------------------------------------+

SELECT TO_CHAR('00-01-01 00:00:00', 'YY-MM-DD HH24:MI:SS');
+-----------------------------------------------------+
| TO_CHAR('00-01-01 00:00:00', 'YY-MM-DD HH24:MI:SS') |
+-----------------------------------------------------+
| 00-01-01 00:00:00                                   |
+-----------------------------------------------------+

SELECT TO_CHAR('99-12-31 23:59:59', 'YY-MM-DD HH24:MI:SS');
+-----------------------------------------------------+
| TO_CHAR('99-12-31 23:59:59', 'YY-MM-DD HH24:MI:SS') |
+-----------------------------------------------------+
| 99-12-31 23:59:59                                   |
+-----------------------------------------------------+

SELECT TO_CHAR('9999-12-31 23:59:59', 'YY-MM-DD HH24:MI:SS');
+-------------------------------------------------------+
| TO_CHAR('9999-12-31 23:59:59', 'YY-MM-DD HH24:MI:SS') |
+-------------------------------------------------------+
| 99-12-31 23:59:59                                     |
+-------------------------------------------------------+

SELECT TO_CHAR('21-01-03 08:30:00', 'Y-MONTH-DY HH:MI:SS');
+-----------------------------------------------------+
| TO_CHAR('21-01-03 08:30:00', 'Y-MONTH-DY HH:MI:SS') |
+-----------------------------------------------------+
| 1-January  -Sun 08:30:00                            |
+-----------------------------------------------------+
```

## See Also


* [SQL_MODE=ORACLE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/sql_modeoracle)

