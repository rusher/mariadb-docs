
# Information Schema PARAMETERS Table

The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>PARAMETERS</code>` table stores information about [stored procedures](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md) and [stored functions](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) parameters.


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
| DATA_TYPE | The column's [data type](../../../../../../data-types/data-types-overview/data-types-subcategory/data-types-dec.md). |
| CHARACTER_MAXIMUM_LENGTH | Maximum length. |
| CHARACTER_OCTET_LENGTH | Same as the CHARACTER_MAXIMUM_LENGTH except for multi-byte [character sets](../../../../../../data-types/string-data-types/character-sets/README.md). |
| NUMERIC_PRECISION | For numeric types, the precision (number of significant digits) for the column. NULL if not a numeric field. |
| NUMERIC_SCALE | For numeric types, the scale (significant digits to the right of the decimal point). NULL if not a numeric field. |
| DATETIME_PRECISION | Fractional-seconds precision, or NULL if not a [time data type](../../../../../../data-types/date-and-time-data-types/README.md). |
| CHARACTER_SET_NAME | [Character set](../../../../../../data-types/string-data-types/character-sets/README.md) if a non-binary [string data type](../../../../../../data-types/string-data-types/README.md), otherwise NULL. |
| COLLATION_NAME | [Collation](../../../../../../data-types/string-data-types/character-sets/README.md) if a non-binary [string data type](../../../../../../data-types/string-data-types/README.md), otherwise NULL. |
| DTD_IDENTIFIER | Description of the data type. |
| ROUTINE_TYPE | PROCEDURE or FUNCTION. |



Information from this table is similar to that found in the `<code>param_list</code>` column in the [mysql.proc](../../the-mysql-database-tables/mysql-proc-table.md) table, and the output of the `<code>[SHOW CREATE PROCEDURE](../../../show/show-create-procedure.md)</code>` and `<code>[SHOW CREATE FUNCTION](../../../show/show-create-function.md)</code>` statements.


To obtain information about the routine itself, you can query the [Information Schema ROUTINES table](information-schema-routines-table.md).


## Example


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
