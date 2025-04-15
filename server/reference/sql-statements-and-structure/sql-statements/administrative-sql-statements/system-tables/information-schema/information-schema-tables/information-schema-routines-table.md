
# Information Schema ROUTINES Table

The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>ROUTINES</code>` table stores information about [stored procedures](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md) and [stored functions](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md).


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| SPECIFIC_NAME |  |
| ROUTINE_CATALOG | Always def. |
| ROUTINE_SCHEMA | Database name associated with the routine. |
| ROUTINE_NAME | Name of the routine. |
| ROUTINE_TYPE | Whether the routine is a PROCEDURE or a FUNCTION. |
| DATA_TYPE | The return value's [data type](../../../../../../data-types/data-types-overview/data-types-subcategory/data-types-dec.md) (for stored functions). |
| CHARACTER_MAXIMUM_LENGTH | Maximum length. |
| CHARACTER_OCTET_LENGTH | Same as the CHARACTER_MAXIMUM_LENGTH except for multi-byte [character sets](../../../../../../data-types/string-data-types/character-sets/README.md). |
| NUMERIC_PRECISION | For numeric types, the precision (number of significant digits) for the column. NULL if not a numeric field. |
| NUMERIC_SCALE | For numeric types, the scale (significant digits to the right of the decimal point). NULL if not a numeric field. |
| DATETIME_PRECISION | Fractional-seconds precision, or NULL if not a [time data type](../../../../../../data-types/date-and-time-data-types/README.md). |
| CHARACTER_SET_NAME | [Character set](../../../../../../data-types/string-data-types/character-sets/README.md) if a non-binary [string data type](../../../../../../data-types/string-data-types/README.md), otherwise NULL. |
| COLLATION_NAME | [Collation](../../../../../../data-types/string-data-types/character-sets/README.md) if a non-binary [string data type](../../../../../../data-types/string-data-types/README.md), otherwise NULL. |
| DATA_TYPE | The column's [data type](../../../../../../data-types/data-types-overview/data-types-subcategory/data-types-dec.md). |
| ROUTINE_BODY | Always SQL. |
| ROUTINE_DEFINITION | Definition of the routine. |
| EXTERNAL_NAME | Always NULL. |
| EXTERNAL_LANGUAGE | Always SQL. |
| PARAMETER_STYLE | Always SQL. |
| IS_DETERMINISTIC | Whether the routine is deterministic (can produce only one result for a given list of parameters) or not. |
| SQL_DATA_ACCESS | One of READS SQL DATA, MODIFIES SQL DATA, CONTAINS SQL, or NO SQL. |
| SQL_PATH | Always NULL. |
| SECURITY_TYPE | INVOKER or DEFINER. Indicates which user's privileges apply to this routine. |
| CREATED | Date and time the routine was created. |
| LAST_ALTERED | Date and time the routine was last changed. |
| SQL_MODE | The [SQL_MODE](../../../../../../../server-management/variables-and-modes/sql-mode.md) at the time the routine was created. |
| ROUTINE_COMMENT | Comment associated with the routine. |
| DEFINER | If the SECURITY_TYPE is DEFINER, this value indicates which user defined this routine. |
| CHARACTER_SET_CLIENT | The [character set](../../../../../../data-types/string-data-types/character-sets/README.md) used by the client that created the routine. |
| COLLATION_CONNECTION | The [collation](../../../../../../data-types/string-data-types/character-sets/README.md) (and character set) used by the connection that created the routine. |
| DATABASE_COLLATION | The default [collation](../../../../../../data-types/string-data-types/character-sets/README.md) (and character set) for the database, at the time the routine was created. |



It provides information similar to, but more complete, than the `<code>[SHOW PROCEDURE STATUS](../../../show/show-procedure-status.md)</code>` and `<code>[SHOW FUNCTION STATUS](../../../show/show-function-status.md)</code>` statements.


For information about the parameters accepted by the routine, you can query the `<code>[information_schema.PARAMETERS](information-schema-parameters-table.md)</code>` table.


## See also


* [Stored Function Overview](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/stored-function-overview.md)
* [Stored Procedure Overview](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/stored-procedure-overview.md)

