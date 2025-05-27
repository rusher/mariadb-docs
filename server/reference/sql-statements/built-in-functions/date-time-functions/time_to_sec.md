
# TIME_TO_SEC

## Syntax


```
TIME_TO_SEC(time)
```

## Description


Returns the time argument, converted to seconds.


The value returned by `TIME_TO_SEC` is of type `[DOUBLE](../../../../data-types/data-types-numeric-data-types/double.md)`. Before [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3) (and MySQL 5.6), the type was `[INT](../../../../data-types/data-types-numeric-data-types/int.md)`. The returned value preserves microseconds of the argument. See also [Microseconds in MariaDB](microseconds-in-mariadb.md).


## Examples


```
SELECT TIME_TO_SEC('22:23:00');
+-------------------------+
| TIME_TO_SEC('22:23:00') |
+-------------------------+
|                   80580 |
+-------------------------+
```

```
SELECT TIME_TO_SEC('00:39:38');
+-------------------------+
| TIME_TO_SEC('00:39:38') |
+-------------------------+
|                    2378 |
+-------------------------+
```

```
SELECT TIME_TO_SEC('09:12:55.2355');
+------------------------------+
| TIME_TO_SEC('09:12:55.2355') |
+------------------------------+
|                   33175.2355 |
+------------------------------+
1 row in set (0.000 sec)
```


GPLv2 fill_help_tables.sql

