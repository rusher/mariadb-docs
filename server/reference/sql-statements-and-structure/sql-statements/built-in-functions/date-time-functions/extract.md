
# EXTRACT

## Syntax


```
EXTRACT(unit FROM date)
```


## Description


The EXTRACT() function extracts the required unit from the date. See [Date and Time Units](date-and-time-units.md) for a complete list of permitted units.


In [MariaDB 10.0.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1007-release-notes) and [MariaDB 5.5.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/mariadb-5535-release-notes), `EXTRACT (HOUR FROM ...)` was changed to return a value from 0 to 23, adhering to the SQL standard. Until [MariaDB 10.0.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1006-release-notes) and [MariaDB 5.5.34](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/mariadb-5534-release-notes), and in all versions of MySQL at least as of MySQL 5.7, it could return a value > 23. [HOUR()](hour.md) is not a standard function, so continues to adhere to the old behaviour inherited from MySQL.


## Examples


```
SELECT EXTRACT(YEAR FROM '2009-07-02');
+---------------------------------+
| EXTRACT(YEAR FROM '2009-07-02') |
+---------------------------------+
|                            2009 |
+---------------------------------+

SELECT EXTRACT(YEAR_MONTH FROM '2009-07-02 01:02:03');
+------------------------------------------------+
| EXTRACT(YEAR_MONTH FROM '2009-07-02 01:02:03') |
+------------------------------------------------+
|                                         200907 |
+------------------------------------------------+

SELECT EXTRACT(DAY_MINUTE FROM '2009-07-02 01:02:03');
+------------------------------------------------+
| EXTRACT(DAY_MINUTE FROM '2009-07-02 01:02:03') |
+------------------------------------------------+
|                                          20102 |
+------------------------------------------------+

SELECT EXTRACT(MICROSECOND FROM '2003-01-02 10:30:00.000123');
+--------------------------------------------------------+
| EXTRACT(MICROSECOND FROM '2003-01-02 10:30:00.000123') |
+--------------------------------------------------------+
|                                                    123 |
+--------------------------------------------------------+
```

From [MariaDB 10.0.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1007-release-notes) and [MariaDB 5.5.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/mariadb-5535-release-notes), `EXTRACT (HOUR FROM...)` returns a value from 0 to 23, as per the SQL standard. `HOUR` is not a standard function, so continues to adhere to the old behaviour inherited from MySQL.


```
SELECT EXTRACT(HOUR FROM '26:30:00'), HOUR('26:30:00');
+-------------------------------+------------------+
| EXTRACT(HOUR FROM '26:30:00') | HOUR('26:30:00') |
+-------------------------------+------------------+
|                             2 |               26 |
+-------------------------------+------------------+
```

## See Also


* [Date and Time Units](date-and-time-units.md)
* [Date and Time Literals](../../../sql-language-structure/date-and-time-literals.md)
* [HOUR()](hour.md)

