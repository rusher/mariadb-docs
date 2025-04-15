
# mysql.time_zone_name Table

**System tables should not normally be edited directly. Use the related SQL statements instead.**



The `<code>mysql.time_zone_name</code>` table is one of the mysql system tables that can contain [time zone](../../../../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) information. It is usually preferable for the system to handle the time zone, in which case the table will be empty (the default), but you can populate the mysql time zone tables using the [mariadb-tzinfo-to-sql](../../../../../../clients-and-utilities/mariadb-tzinfo-to-sql.md) utility. See [Time Zones](../../../../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) for details.


This table uses the [Aria](../../../../../storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine.


The `<code>mysql.time_zone_name</code>` table contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| Name | char(64) | NO | PRI | NULL | Name of the time zone. |
| Time_zone_id | int(10) unsigned | NO | PRI | NULL | ID field, auto_increments. |



## Example


```
SELECT * FROM mysql.time_zone_name;
+--------------------+--------------+
| Name               | Time_zone_id |
+--------------------+--------------+
| Africa/Abidjan     |            1 |
| Africa/Accra       |            2 |
| Africa/Addis_Ababa |            3 |
| Africa/Algiers     |            4 |
| Africa/Asmara      |            5 |
| Africa/Asmera      |            6 |
| Africa/Bamako      |            7 |
| Africa/Bangui      |            8 |
| Africa/Banjul      |            9 |
| Africa/Bissau      |           10 |
...
+--------------------+--------------+
```

## See Also


* [mysql.time_zone table](mysql-time_zone-table.md)
* [mysql.time_zone_leap_second table](mysql-time_zone_leap_second-table.md)
* [mysql.time_zone_transition table](mysql-time_zone_transition-table.md)
* [mysql.time_zone_transition_type table](mysql-time_zone_transition_type-table.md)

