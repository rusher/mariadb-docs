# PROCEDURE ANALYSE

## Syntax

```
analyse([max_elements[,max_memory]])
```

## Description

This procedure is defined in the sql/sql\_analyse.cc file. It examines\
the result from a query and returns an analysis of the results that\
suggests optimal data types for each column. To obtain this analysis,\
append PROCEDURE ANALYSE to the end of a [SELECT](../../../sql-statements/data-manipulation/selecting-data/select.md) statement:

```
SELECT ... FROM ... WHERE ... PROCEDURE ANALYSE([max_elements,[max_memory]])
```

For example:

```
SELECT col1, col2 FROM table1 PROCEDURE ANALYSE(10, 2000);
```

The results show some statistics for the values returned by the query,\
and propose an optimal data type for the columns. This can be helpful\
for checking your existing tables, or after importing new data. You\
may need to try different settings for the arguments so that PROCEDURE\
ANALYSE() does not suggest the ENUM data type when it is not\
appropriate.

The arguments are optional and are used as follows:

* max\_elements (default 256) is the maximum number of distinct values that analyse notices per column. This is used by analyse to check whether the optimal data type should be of type ENUM; if there are more than max\_elements distinct values, then ENUM is not a suggested type.
* max\_memory (default 8192) is the maximum amount of memory that analyse should allocate per column while trying to find all distinct values.

## See Also

* [PROCEDURE](../../../sql-statements/data-manipulation/selecting-data/procedure.md)
* [SELECT](../../../sql-statements/data-manipulation/selecting-data/select.md)

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
