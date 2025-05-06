
# UTC_TIME

## Syntax


```
UTC_TIME
UTC_TIME([precision])
```

## Description


Returns the current [UTC time](../../../../data-types/string-data-types/character-sets/internationalization-and-localization/coordinated-universal-time.md) as a value in 'HH:MM:SS' or HHMMSS.uuuuuu format, depending on whether the function is used in a string or numeric context.


The optional *precision* determines the microsecond precision. See [Microseconds in MariaDB](microseconds-in-mariadb.md).


## Examples


```
SELECT UTC_TIME(), UTC_TIME() + 0;
+------------+----------------+
| UTC_TIME() | UTC_TIME() + 0 |
+------------+----------------+
| 17:32:34   |  173234.000000 |
+------------+----------------+
```

With precision:


```
SELECT UTC_TIME(5);
+----------------+
| UTC_TIME(5)    |
+----------------+
| 07:52:50.78369 |
+----------------+
```

## See Also


* [Microseconds in MariaDB](microseconds-in-mariadb.md)


GPLv2 fill_help_tables.sql

