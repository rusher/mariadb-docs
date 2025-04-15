
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


Returns the current date and time as a value in `<code>'YYYY-MM-DD HH:MM:SS'</code>`
or `<code>YYYYMMDDHHMMSS.uuuuuu</code>` format, depending on whether the function is
used in a string or numeric context. The value is expressed in the
current [time zone](../../../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md).



##### MariaDB starting with [11.7](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md)
Starting from [MariaDB 11.7](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md), these functions return SQL standard compliant types:

* `<code>NOW()</code>` and `<code>CURRENT_TIMESTAMP()</code>` return a `<code>TIMESTAMP</code>` value
(analogous to the standard type `<code>TIMESTAMP WITH LOCAL TIME ZONE</code>`)
which corresponds to the curent point in time and is unambiguous around DST changes.
* `<code>LOCALTIMESTAMP</code>` still returns a `<code>DATETIME</code>` value as before
(analogous to the standard type `<code>TIMESTAMP WITHOUT TIME ZONE</code>`). Storing its result in a `<code>TIMESTAMP</code>` column can result in a data loss around DST changes.



The optional *precision* determines the microsecond precision. See [Microseconds in MariaDB](microseconds-in-mariadb.md).


`<code>NOW()</code>` (or its synonyms) can be used as the default value for [TIMESTAMP](timestamp-function.md) columns as well as, since [MariaDB 10.0.1](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1001-release-notes.md), [DATETIME](../../../../data-types/date-and-time-data-types/datetime.md) columns. Before [MariaDB 10.0.1](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1001-release-notes.md), it was only possible for a single TIMESTAMP column per table to contain the CURRENT_TIMESTAMP as its default.


When displayed in the [INFORMATION_SCHEMA.COLUMNS](../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-columns-table.md) table, a default [CURRENT TIMESTAMP](current_timestamp.md) is displayed as `<code>CURRENT_TIMESTAMP</code>` up until [MariaDB 10.2.2](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md), and as `<code>current_timestamp()</code>` from [MariaDB 10.2.3](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md), due to to [MariaDB 10.2](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md) accepting expressions in the DEFAULT clause.


Changing the [timestamp system variable](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#timestamp) with a [SET](../../../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md) `<code>timestamp</code>` statement affects the value returned by NOW(), but not by [SYSDATE()](sysdate.md).


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

From [MariaDB 10.2.2](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md):


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

<= [MariaDB 10.2.1](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1021-release-notes.md)


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
* [timestamp server system variable](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#timestamp)

