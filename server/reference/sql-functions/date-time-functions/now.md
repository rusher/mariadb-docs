# NOW

## Syntax

```
NOW([precision])
CURRENT_TIMESTAMP
CURRENT_TIMESTAMP([precision])
LOCALTIME, LOCALTIME([precision])
LOCALTIMESTAMP
LOCALTIMESTAMP([precision])
```

## Description

Returns the current date and time as a value in `'YYYY-MM-DD HH:MM:SS'`\
or `YYYYMMDDHHMMSS.uuuuuu` format, depending on whether the function is\
used in a string or numeric context. The value is expressed in the\
current [time zone](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md).

**MariaDB starting with** [**11.7**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-7-rolling-releases/what-is-mariadb-117)

Starting from [MariaDB 11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-7-rolling-releases/what-is-mariadb-117), these functions return SQL standard compliant types:

* `NOW()` and `CURRENT_TIMESTAMP()` return a `TIMESTAMP` value\
  (analogous to the standard type `TIMESTAMP WITH LOCAL TIME ZONE`)\
  which corresponds to the curent point in time and is unambiguous around DST changes.
* `LOCALTIMESTAMP` still returns a `DATETIME` value as before\
  (analogous to the standard type `TIMESTAMP WITHOUT TIME ZONE`). Storing its result in a `TIMESTAMP` column can result in a data loss around DST changes.

The optional _precision_ determines the microsecond precision. See [Microseconds in MariaDB](microseconds-in-mariadb.md).

`NOW()` (or its synonyms) can be used as the default value for [TIMESTAMP](../../data-types/date-and-time-data-types/timestamp.md) columns as well as, since [MariaDB 10.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1001-release-notes), [DATETIME](../../data-types/date-and-time-data-types/datetime.md) columns. Before [MariaDB 10.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1001-release-notes), it was only possible for a single TIMESTAMP column per table to contain the CURRENT\_TIMESTAMP as its default.

When displayed in the [INFORMATION\_SCHEMA.COLUMNS](../../sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-columns-table.md) table, a default [CURRENT TIMESTAMP](current_timestamp.md) is displayed as `CURRENT_TIMESTAMP` up until [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes), and as `current_timestamp()` from [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes), due to to [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) accepting expressions in the DEFAULT clause.

Changing the [timestamp system variable](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#timestamp) with a [SET](../../sql-statements/administrative-sql-statements/set-commands/set.md) `timestamp` statement affects the value returned by NOW(), but not by [SYSDATE()](sysdate.md).

## Examples

```
SELECT NOW();
+---------------------+
| NOW()               |
+---------------------+
| 2010-03-27 13:13:25 |
+---------------------+

SELECT NOW() + 0;
+-----------------------+
| NOW() + 0             |
+-----------------------+
| 20100327131329.000000 |
+-----------------------+
```

With precision:

```
SELECT CURRENT_TIMESTAMP(2);
+------------------------+
| CURRENT_TIMESTAMP(2)   |
+------------------------+
| 2018-07-10 09:47:26.24 |
+------------------------+
```

Used as a default TIMESTAMP:

```
CREATE TABLE t (createdTS TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);
```

From [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes):

```
SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='test'
  AND COLUMN_NAME LIKE '%ts%'\G
*************************** 1. row ***************************
           TABLE_CATALOG: def
            TABLE_SCHEMA: test
              TABLE_NAME: t
             COLUMN_NAME: ts
        ORDINAL_POSITION: 1
          COLUMN_DEFAULT: current_timestamp()
...
```

<= [MariaDB 10.2.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1021-release-notes)

```
SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='test'
  AND COLUMN_NAME LIKE '%ts%'\G
*************************** 1. row ***************************
           TABLE_CATALOG: def
            TABLE_SCHEMA: test
              TABLE_NAME: t
             COLUMN_NAME: createdTS
        ORDINAL_POSITION: 1
          COLUMN_DEFAULT: CURRENT_TIMESTAMP
...
```

## See Also

* [Microseconds in MariaDB](microseconds-in-mariadb.md)
* [timestamp server system variable](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#timestamp)

GPLv2 fill\_help\_tables.sql

{% @marketo/form formId="4316" %}
