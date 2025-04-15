# Information Schema PARAMETERS Table

The [Information Schema](/en/information_schema/) `PARAMETERS` table stores information about [stored procedures](/en/stored-procedures/) and [stored functions](/en/stored-functions/) parameters.

It contains the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| SPECIFIC_CATALOG | Always def. |
| SPECIFIC_SCHEMA | Database name containing the stored routine parameter. |
| SPECIFIC_NAME | Stored routine name. |
| ORDINAL_POSITION | Ordinal position of the parameter, starting at 1. 0 for a function RETURNS clause. |
| PARAMETER_MODE | One of IN, OUT, INOUT or NULL for RETURNS. |
| PARAMETER_NAME | Name of the parameter, or NULL for RETURNS. |
| DATA_TYPE | The column's [data type](/en/data-types/). |
| CHARACTER_MAXIMUM_LENGTH | Maximum length. |
| CHARACTER_OCTET_LENGTH | Same as the CHARACTER_MAXIMUM_LENGTH except for multi-byte [character sets](/en/data-types-character-sets-and-collations/). |
| NUMERIC_PRECISION | For numeric types, the precision (number of significant digits) for the column. NULL if not a numeric field. |
| NUMERIC_SCALE | For numeric types, the scale (significant digits to the right of the decimal point). NULL if not a numeric field. |
| DATETIME_PRECISION | Fractional-seconds precision, or NULL if not a [time data type](/en/date-and-time-data-types/). |
| CHARACTER_SET_NAME | [Character set](/en/data-types-character-sets-and-collations/) if a non-binary [string data type](/en/string-data-types/), otherwise NULL. |
| COLLATION_NAME | [Collation](/en/data-types-character-sets-and-collations/) if a non-binary [string data type](/en/string-data-types/), otherwise NULL. |
| DTD_IDENTIFIER | Description of the data type. |
| ROUTINE_TYPE | PROCEDURE or FUNCTION. |

Information from this table is similar to that found in the `param_list` column in the [mysql.proc](/en/mysqlproc-table/) table, and the output of the `[SHOW CREATE PROCEDURE](../../../show/show-create-procedure.md)` and `[SHOW CREATE FUNCTION](../../../show/show-create-function.md)` statements.

To obtain information about the routine itself, you can query the [Information Schema ROUTINES table](information-schema-routines-table.md).

#

# Example

```
SELECT * FROM information_schema.PARAMETERS
LIMIT 1 \G
********************** 1. row **********************
 SPECIFIC_CATALOG: def
 SPECIFIC_SCHEMA: accounts
 SPECIFIC_NAME: user_counts
 ORDINAL_POSITION: 1
 PARAMETER_MODE: IN
 PARAMETER_NAME: user_order
 DATA_TYPE: varchar
CHARACTER_MAXIMUM_LENGTH: 255
 CHARACTER_OCTET_LENGTH: 765
 NUMERIC_PRECISION: NULL
 NUMERIC_SCALE: NULL
 DATETIME_PRECISION: NULL
 CHARACTER_SET_NAME: utf8
 COLLATION_NAME: utf8_general_ci
 DTD_IDENTIFIER: varchar(255)
 ROUTINE_TYPE: PROCEDURE
```