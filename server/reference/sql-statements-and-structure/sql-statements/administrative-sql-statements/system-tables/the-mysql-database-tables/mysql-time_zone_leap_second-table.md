
# mysql.time_zone_leap_second Table

**System tables should not normally be edited directly. Use the related SQL statements instead.**



The `mysql.time_zone_leap_second` table is one of the mysql system tables that can contain [time zone](../../../../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) information. It is usually preferable for the system to handle the time zone, in which case the table will be empty (the default), but you can populate the mysql time zone tables using the [mariadb-tzinfo-to-sql](../../../../../../clients-and-utilities/mariadb-tzinfo-to-sql.md) utility. See [Time Zones](../../../../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) for details.


This table uses the [Aria](../../../../../storage-engines/aria/README.md) storage engine.


The `mysql.time_zone_leap_second` table contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| Transition_time | bigint(20) | NO | PRI | NULL |  |
| Correction | int(11) | NO |  | NULL |  |



## See Also


* [mysql.time_zone table](mysql-time_zone-table.md)
* [mysql.time_zone_name table](mysql-time_zone_name-table.md)
* [mysql.time_zone_transition table](mysql-time_zone_transition-table.md)
* [mysql.time_zone_transition_type table](mysql-time_zone_transition_type-table.md)


CC BY-SA / Gnu FDL

