
# mysql.proc Table

The `<code>mysql.proc</code>` table contains information about [stored procedures](../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md) and [stored functions](../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md). It contains similar information to that stored in the [INFORMATION SCHEMA.ROUTINES](../information-schema/information-schema-tables/information-schema-routines-table.md) table.


This table uses the [Aria](../../../../../storage-engines/s3-storage-engine/aria_s3_copy.md) storage engine.


The `<code>mysql.proc</code>` table contains the following fields:



| Field | Type | Null | Key | Default | Description | Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| db | char(64) | NO | PRI |  | Database name. |
| name | char(64) | NO | PRI |  | Routine name. |
| type | enum('FUNCTION','PROCEDURE','PACKAGE', 'PACKAGE BODY') | NO | PRI | NULL | Whether [stored procedure](../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md), [stored function](../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) or, from [MariaDB 10.3.5](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1035-release-notes.md), a [package](../../../data-definition/create/create-package-body.md) or [package body](../../../data-definition/create/create-package-body.md). |
| specific_name | char(64) | NO |  |  |  |
| language | enum('SQL') | NO |  | SQL | Always SQL. |
| sql_data_access | enum('CONTAINS_SQL', 'NO_SQL', 'READS_SQL_DATA', 'MODIFIES_SQL_DATA') | NO |  | CONTAINS_SQL |  |
| is_deterministic | enum('YES','NO') | NO |  | NO | Whether the routine is deterministic (can produce only one result for a given list of parameters) or not. |
| security_type | enum('INVOKER','DEFINER') | NO |  | DEFINER | INVOKER or DEFINER. Indicates which user's privileges apply to this routine. |
| param_list | blob | NO |  | NULL | List of parameters. |
| returns | longblob | NO |  | NULL | What the routine returns. |
| body | longblob | NO |  | NULL | Definition of the routine. |
| definer | char(141) | NO |  |  | If the security_type is DEFINER, this value indicates which user defined this routine. |
| created | timestamp | NO |  | CURRENT_TIMESTAMP | Date and time the routine was created. |
| modified | timestamp | NO |  | 0000-00-00 00:00:00 | Date and time the routine was modified. |
| sql_mode | set('REAL_AS_FLOAT', 'PIPES_AS_CONCAT', 'ANSI_QUOTES', 'IGNORE_SPACE', 'IGNORE_BAD_TABLE_OPTIONS', 'ONLY_FULL_GROUP_BY', 'NO_UNSIGNED_SUBTRACTION', 'NO_DIR_IN_CREATE', 'POSTGRESQL', 'ORACLE', 'MSSQL', 'DB2', 'MAXDB', 'NO_KEY_OPTIONS', 'NO_TABLE_OPTIONS', 'NO_FIELD_OPTIONS', 'MYSQL323', 'MYSQL40', 'ANSI', 'NO_AUTO_VALUE_ON_ZERO', 'NO_BACKSLASH_ESCAPES', 'STRICT_TRANS_TABLES', 'STRICT_ALL_TABLES', 'NO_ZERO_IN_DATE', 'NO_ZERO_DATE', 'INVALID_DATES', 'ERROR_FOR_DIVISION_BY_ZERO', 'TRADITIONAL', 'NO_AUTO_CREATE_USER', 'HIGH_NOT_PRECEDENCE', 'NO_ENGINE_SUBSTITUTION', 'PAD_CHAR_TO_FULL_LENGTH', 'EMPTY_STRING_IS_NULL', 'SIMULTANEOUS_ASSIGNMENT') | NO |  |  | The [SQL_MODE](../../../../../../server-management/variables-and-modes/sql-mode.md) at the time the routine was created. |
| comment | text | NO |  | NULL | Comment associated with the routine. |
| character_set_client | char(32) | YES |  | NULL | The [character set](../../../../../data-types/string-data-types/character-sets/README.md) used by the client that created the routine. |
| collation_connection | char(32) | YES |  | NULL | The [collation](../../../../../data-types/string-data-types/character-sets/README.md) (and character set) used by the connection that created the routine. |
| db_collation | char(32) | YES |  | NULL | The default [collation](../../../../../data-types/string-data-types/character-sets/README.md) (and character set) for the database, at the time the routine was created. |
| body_utf8 | longblob | YES |  | NULL | Definition of the routine in utf8. |
| aggregate | enum('NONE', 'GROUP') | NO |  | NONE |
| Field | Type | Null | Key | Default | Description |



## See Also


* [Stored Procedure Internals](../../../../../mariadb-internals/mariadb-source-code-internals/stored-procedure-internals.md)
* [MySQL to MariaDB migration: handling privilege table differences when using mysqldump](https://mariadb.com/blog/mysql-mariadb-migration-handling-privilege-table-differences-when-using-mysqldump)

