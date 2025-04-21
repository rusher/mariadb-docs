
# mysql.event Table

The `mysql.event` table contains information about MariaDB [events](../../../../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/README.md). Similar information can be obtained by viewing the [INFORMATION_SCHEMA.EVENTS](../information-schema/information-schema-tables/information-schema-events-table.md) table, or with the [SHOW EVENTS](https://mariadb.com/kb/en/show-event) and [SHOW CREATE EVENT](../../show/show-create-event.md) statements.


The table is upgraded live, and there is no need to restart the server if the table has changed.


This table uses the [Aria](../../../../../storage-engines/aria/README.md) storage engine.


The `mysql.event` table contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| db | char(64) | NO | PRI |  |  |
| name | char(64) | NO | PRI |  |  |
| body | longblob | NO |  | NULL |  |
| definer | char(141) | NO |  |  |  |
| execute_at | datetime | YES |  | NULL |  |
| interval_value | int(11) | YES |  | NULL |  |
| interval_field | enum('YEAR', 'QUARTER', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'WEEK', 'SECOND', 'MICROSECOND', 'YEAR_MONTH', 'DAY_HOUR', 'DAY_MINUTE', 'DAY_SECOND', 'HOUR_MINUTE', 'HOUR_SECOND', 'MINUTE_SECOND', 'DAY_MICROSECOND', 'HOUR_MICROSECOND', 'MINUTE_MICROSECOND', 'SECOND_MICROSECOND') | YES |  | NULL |  |
| created | timestamp | NO |  | CURRENT_TIMESTAMP |  |
| modified | timestamp | NO |  | 0000-00-00 00:00:00 |  |
| last_executed | datetime | YES |  | NULL |  |
| starts | datetime | YES |  | NULL |  |
| ends | datetime | YES |  | NULL |  |
| status | enum('ENABLED', 'DISABLED', 'SLAVESIDE_DISABLED') | NO |  | ENABLED | Current status of the event, one of enabled, disabled, or disabled on the slaveside. |
| on_completion | enum('DROP','PRESERVE') | NO |  | DROP |  |
| sql_mode | set('REAL_AS_FLOAT', 'PIPES_AS_CONCAT', 'ANSI_QUOTES', 'IGNORE_SPACE', 'IGNORE_BAD_TABLE_OPTIONS', 'ONLY_FULL_GROUP_BY', 'NO_UNSIGNED_SUBTRACTION', 'NO_DIR_IN_CREATE', 'POSTGRESQL', 'ORACLE', 'MSSQL', 'DB2', 'MAXDB', 'NO_KEY_OPTIONS', 'NO_TABLE_OPTIONS', 'NO_FIELD_OPTIONS', 'MYSQL323', 'MYSQL40', 'ANSI', 'NO_AUTO_VALUE_ON_ZERO', 'NO_BACKSLASH_ESCAPES', 'STRICT_TRANS_TABLES', 'STRICT_ALL_TABLES', 'NO_ZERO_IN_DATE', 'NO_ZERO_DATE', 'INVALID_DATES', 'ERROR_FOR_DIVISION_BY_ZERO', 'TRADITIONAL', 'NO_AUTO_CREATE_USER', 'HIGH_NOT_PRECEDENCE', 'NO_ENGINE_SUBSTITUTION', 'PAD_CHAR_TO_FULL_LENGTH') | NO |  |  | The [SQL_MODE](../../../../../../server-management/variables-and-modes/sql-mode.md) at the time the event was created. |
| comment | char(64) | NO |  |  |  |
| originator | int(10) unsigned | NO |  | NULL |  |
| time_zone | char(64) | NO |  | SYSTEM |  |
| character_set_client | char(32) | YES |  | NULL |  |
| collation_connection | char(32) | YES |  | NULL |  |
| db_collation | char(32) | YES |  | NULL |  |
| body_utf8 | longblob | YES |  | NULL |  |


