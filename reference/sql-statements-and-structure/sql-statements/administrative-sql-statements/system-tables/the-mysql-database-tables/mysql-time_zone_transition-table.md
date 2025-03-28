# mysql.time_zone_transition Table

**System tables should not normally be edited directly. Use the related SQL statements instead.**

The `mysql.time_zone_transition` table is one of the `mysql` system tables that can contain [time zone](../../../../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) information. It is usually preferable for the system to handle the time zone, in which case the table will be empty (the default), but you can populate the `mysql` time zone tables using the [mariadb-tzinfo-to-sql](../../../../../../clients-and-utilities/mariadb-tzinfo-to-sql.md) utility. See [Time Zones](../../../../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) for details.

This table uses the [Aria](../../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/aria-encryption/aria-enabling-encryption.md) storage engine.

The `mysql.time_zone_transition` table contains the following fields:

| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| Time_zone_id | int(10) unsigned | NO | PRI | NULL | |
| Transition_time | bigint(20) | NO | PRI | NULL | |
| Transition_type_id | int(10) unsigned | NO | | NULL | |

#

# Example

```
SELECT * FROM mysql.time_zone_transition;
+--------------+-----------------+--------------------+
| Time_zone_id | Transition_time | Transition_type_id |
+--------------+-----------------+--------------------+
| 1 | -1830383032 | 1 |
| 2 | -1640995148 | 2 |
| 2 | -1556841600 | 1 |
| 2 | -1546388400 | 2 |
| 2 | -1525305600 | 1 |
| 2 | -1514852400 | 2 |
| 2 | -1493769600 | 1 |
| 2 | -1483316400 | 2 |
| 2 | -1462233600 | 1 |
| 2 | -1451780400 | 2 |
...
+--------------+-----------------+--------------------+
```

#

# See Also

* [mysql.time_zone table](/en/mysqltime_zone-table/)
* [mysql.time_zone_leap_second table](/en/mysqltime_zone_leap_second-table/)
* [mysql.time_zone_name table](/en/mysqltime_zone_name-table/)
* [mysql.time_zone_transition_type table](/en/mysqltime_zone_transition_type-table/)