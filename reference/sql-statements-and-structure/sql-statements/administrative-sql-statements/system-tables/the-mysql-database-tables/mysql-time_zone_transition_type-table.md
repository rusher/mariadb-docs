# mysql.time_zone_transition_type Table

**System tables should not normally be edited directly. Use the related SQL statements instead.**

The `mysql.time_zone_transition_type` table is one of the `mysql` system tables that can contain [time zone](../../../../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) information. It is usually preferable for the system to handle the time zone, in which case the table will be empty (the default), but you can populate the `mysql` time zone tables using the [mariadb-tzinfo-to-sql](../../../../../../clients-and-utilities/mariadb-tzinfo-to-sql.md) utility. See [Time Zones](../../../../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) for details.

This table uses the [Aria](../../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/aria-encryption/aria-enabling-encryption.md) storage engine.

The `mysql.time_zone_transition_type` table contains the following fields:

| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| Time_zone_id | int(10) unsigned | NO | PRI | NULL | |
| Transition_type_id | int(10) unsigned | NO | PRI | NULL | |
| Offset | int(11) | NO | | 0 | |
| Is_DST | tinyint(3) unsigned | NO | | 0 | |
| Abbreviation | char(8) | NO | | | |

#

# Example

```
SELECT * FROM mysql.time_zone_transition_type;
+--------------+--------------------+--------+--------+--------------+
| Time_zone_id | Transition_type_id | Offset | Is_DST | Abbreviation |
+--------------+--------------------+--------+--------+--------------+
| 1 | 0 | -968 | 0 | LMT |
| 1 | 1 | 0 | 0 | GMT |
| 2 | 0 | -52 | 0 | LMT |
| 2 | 1 | 1200 | 1 | GHST |
| 2 | 2 | 0 | 0 | GMT |
| 3 | 0 | 8836 | 0 | LMT |
| 3 | 1 | 10800 | 0 | EAT |
| 3 | 2 | 9000 | 0 | BEAT |
| 3 | 3 | 9900 | 0 | BEAUT |
| 3 | 4 | 10800 | 0 | EAT |
...
+--------------+--------------------+--------+--------+--------------+
```

#

# See Also

* [mysql.time_zone table](/en/mysqltime_zone-table/)
* [mysql.time_zone_leap_second table](/en/mysqltime_zone_leap_second-table/)
* [mysql.time_zone_name table](/en/mysqltime_zone_name-table/)
* [mysql.time_zone_transition table](/en/mysqltime_zone_transition-table/)