# UNIX\_TIMESTAMP

## Syntax

```
UNIX_TIMESTAMP()
UNIX_TIMESTAMP(date)
```

## Description

If called with no argument, returns a Unix timestamp (seconds since\
'1970-01-01 00:00:00' [UTC](../../../data-types/string-data-types/character-sets/internationalization-and-localization/coordinated-universal-time.md)) as an unsigned integer. If `UNIX_TIMESTAMP()`\
is called with a date argument, it returns the value of the argument as seconds\
since '1970-01-01 00:00:00' UTC. date may be a `[DATE](../../../../data-types/date-and-time-data-types/date.md)` string, a`[DATETIME](../../../../data-types/date-and-time-data-types/datetime.md)` string, a `[TIMESTAMP](../../../../data-types/date-and-time-data-types/timestamp.md)`, or a number in\
the format YYMMDD or YYYYMMDD. The server interprets date as a value in the\
current [time zone](../../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) and converts it to an internal value in [UTC](../../../data-types/string-data-types/character-sets/internationalization-and-localization/coordinated-universal-time.md). Clients can set\
their time zone as described in [time zones](../../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md).

The inverse function of `UNIX_TIMESTAMP()` is `[FROM_UNIXTIME()](from_unixtime.md)`

`UNIX_TIMESTAMP()` supports [microseconds](microseconds-in-mariadb.md).

Timestamps in MariaDB have a maximum value of 4294967295, equivalent to 2106-02-07 06:28:15. This is due to the underlying 32-bit limitation. Using the function on a timestamp beyond this will result in NULL being returned. Use [DATETIME](../../../data-types/date-and-time-data-types/datetime.md) as a storage type if you require dates beyond this.

**MariaDB until** [**11.5**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115)

Before [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115), the maximum value was 2147483647, equivalent to 2038-01-19 05:14:07.

### Error Handling

Returns NULL for wrong arguments to `UNIX_TIMESTAMP()`. In MySQL and MariaDB before 5.3 wrong arguments to `UNIX_TIMESTAMP()` returned 0.

### Compatibility

As you can see in the examples above, UNIX\_TIMESTAMP(constant-date-string) returns a timestamp with 6 decimals while [MariaDB 5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2) and before returns it without decimals. This can cause a problem if you are using UNIX\_TIMESTAMP() as a partitioning function. You can fix this by using [FLOOR](../numeric-functions/floor.md)(UNIX\_TIMESTAMP(..)) or changing the date string to a date number, like 20080101000000.

## Examples

```
SELECT UNIX_TIMESTAMP();
+------------------+
| UNIX_TIMESTAMP() |
+------------------+
|       1269711082 |
+------------------+

SELECT UNIX_TIMESTAMP('2007-11-30 10:30:19');
+---------------------------------------+
| UNIX_TIMESTAMP('2007-11-30 10:30:19') |
+---------------------------------------+
|                     1196436619.000000 |
+---------------------------------------+

SELECT UNIX_TIMESTAMP("2007-11-30 10:30:19.123456");
+----------------------------------------------+
| unix_timestamp("2007-11-30 10:30:19.123456") |
+----------------------------------------------+
|                            1196411419.123456 |
+----------------------------------------------+

SELECT FROM_UNIXTIME(UNIX_TIMESTAMP('2007-11-30 10:30:19'));
+------------------------------------------------------+
| FROM_UNIXTIME(UNIX_TIMESTAMP('2007-11-30 10:30:19')) |
+------------------------------------------------------+
| 2007-11-30 10:30:19.000000                           |
+------------------------------------------------------+

SELECT FROM_UNIXTIME(FLOOR(UNIX_TIMESTAMP('2007-11-30 10:30:19')));
+-------------------------------------------------------------+
| FROM_UNIXTIME(FLOOR(UNIX_TIMESTAMP('2007-11-30 10:30:19'))) |
+-------------------------------------------------------------+
| 2007-11-30 10:30:19                                         |
+-------------------------------------------------------------+
```

## See Also

* [FROM\_UNIXTIME()](from_unixtime.md)

GPLv2 fill\_help\_tables.sql
