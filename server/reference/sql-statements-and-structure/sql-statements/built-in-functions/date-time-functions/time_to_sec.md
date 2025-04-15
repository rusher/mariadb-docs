
# TIME_TO_SEC

## Syntax


```
TIME_TO_SEC(time)
```

## Description


Returns the time argument, converted to seconds.


The value returned by `<code>TIME_TO_SEC</code>` is of type `<code>[DOUBLE](../../../../data-types/data-types-numeric-data-types/double.md)</code>`. Before [MariaDB 5.3](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) (and MySQL 5.6), the type was `<code>[INT](../../../../../../general-resources/learning-and-training/video-presentations-and-screencasts/interviews-related-to-mariadb.md)</code>`. The returned value preserves microseconds of the argument. See also [Microseconds in MariaDB](microseconds-in-mariadb.md).


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
