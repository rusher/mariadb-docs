
# Information Schema USER_VARIABLES Table


## Description


The `<code>USER_VARIABLES</code>` table is created when the [user_variables](../../../../../../plugins/other-plugins/user-variables-plugin.md) plugin is enabled, and contains information about [user-defined variables](../../../../../sql-language-structure/user-defined-variables.md).


The table contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| VARIABLE_NAME | Variable name. |
| VARIABLE_VALUE | Variable value. |
| VARIABLE_TYPE | Variable [type](../../../../../../data-types/data-types-overview/data-types-subcategory/data-types-dec.md). |
| CHARACTER_SET_NAME | [Character set](../../../../../../data-types/string-data-types/character-sets/README.md). |



User variables are reset and the table emptied with the [FLUSH USER_VARIABLES](../../../flush-commands/flush-tables-for-export.md) statement. `<code>SHOW USER_VARIABLES</code>` displays a subset of the data.


## Example


```
SET @v1 = 0;
SET @v2 = 'abc';
SET @v3 = CAST(123 AS CHAR(5));

SELECT * FROM information_schema.USER_VARIABLES ORDER BY VARIABLE_NAME;
+---------------+----------------+---------------+--------------------+
| VARIABLE_NAME | VARIABLE_VALUE | VARIABLE_TYPE | CHARACTER_SET_NAME |
+---------------+----------------+---------------+--------------------+
| v1            | 0              | INT           | latin1             |
| v2            | abc            | VARCHAR       | utf8               |
| v3            | 123            | VARCHAR       | utf8               |
+---------------+----------------+---------------+--------------------+

SHOW USER_VARIABLES;
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| v3            | 123   |
| v2            | abc   |
| v1            | 0     |
+---------------+-------+
```

## See Also


* [User-defined variables](../../../../../sql-language-structure/user-defined-variables.md)
* [Performance Schema user_variables_by_thread Table](../../performance-schema/performance-schema-tables/performance-schema-user_variables_by_thread-table.md)

