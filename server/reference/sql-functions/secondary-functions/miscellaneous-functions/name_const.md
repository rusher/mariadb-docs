
# NAME_CONST

## Syntax


```
NAME_CONST(name,value)
```

## Description


Returns the given value. When used to produce a result set column,
 `NAME_CONST()` causes the column to have the given name. The
arguments should be constants.


This function is used internally when replicating stored procedures. It makes little sense to use it explicitly in SQL statements, and it was not supposed to be used like that.


```
SELECT NAME_CONST('myname', 14);
+--------+
| myname |
+--------+
|     14 |
+--------+
```


<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>


{% @marketo/form formId="4316" %}
