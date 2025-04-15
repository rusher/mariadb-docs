
# HOUR

## Syntax


```
HOUR(time)
```

## Description


Returns the hour for time. The range of the return value is 0 to 23
for time-of-day values. However, the range of `<code>TIME</code>` values actually is
much larger, so HOUR can return values greater than 23.


The return value is always positive, even if a negative `<code>TIME</code>` value is provided.


## Examples


```
SELECT HOUR('10:05:03');
+------------------+
| HOUR('10:05:03') |
+------------------+
|               10 |
+------------------+

SELECT HOUR('272:59:59');
+-------------------+
| HOUR('272:59:59') |
+-------------------+
|               272 |
+-------------------+
```

Difference between `<code>[EXTRACT (HOUR FROM ...)](../../administrative-sql-statements/system-tables/sys-schema/sys-schema-stored-functions/extract_schema_from_file_name.md)</code>` (>= [MariaDB 10.0.7](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1007-release-notes.md) and [MariaDB 5.5.35](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5535-release-notes.md)) and `<code>HOUR</code>`:


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
* [EXTRACT()](../../administrative-sql-statements/system-tables/sys-schema/sys-schema-stored-functions/extract_schema_from_file_name.md)

