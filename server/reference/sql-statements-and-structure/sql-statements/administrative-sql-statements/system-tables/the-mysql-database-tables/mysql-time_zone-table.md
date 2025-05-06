
# mysql.time_zone Table

The `mysql.time_zone` table is one of the mysql system tables that can contain [time zone](../../../../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) information. It is usually preferable for the system to handle the time zone, in which case the table will be empty (the default), but you can populate the mysql time zone tables using the [mariadb-tzinfo-to-sql](../../../../../../clients-and-utilities/mariadb-tzinfo-to-sql.md) utility. See [Time Zones](../../../../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) for details.


This table uses the [Aria](../../../../../storage-engines/aria/README.md) storage engine.


The `mysql.time_zone` table contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| Time_zone_id | int(10) unsigned | NO | PRI | NULL | ID field, auto_increments. |
| Use_leap_seconds | enum('Y','N') | NO |  | N | Whether or not leap seconds are used. |



## Example


```
SELECT * FROM mysql.time_zone;
+--------------+------------------+
| Time_zone_id | Use_leap_seconds |
+--------------+------------------+
|            1 | N                |
|            2 | N                |
|            3 | N                |
|            4 | N                |
|            5 | N                |
|            6 | N                |
|            7 | N                |
|            8 | N                |
|            9 | N                |
|           10 | N                |
...
+--------------+------------------+
```

## See Also


* [mysql.time_zone_leap_second table](mysql-time_zone_leap_second-table.md)
* [mysql.time_zone_name table](mysql-time_zone_name-table.md)
* [mysql.time_zone_transition table](mysql-time_zone_transition-table.md)
* [mysql.time_zone_transition_type table](mysql-time_zone_transition_type-table.md)


CC BY-SA / Gnu FDL

