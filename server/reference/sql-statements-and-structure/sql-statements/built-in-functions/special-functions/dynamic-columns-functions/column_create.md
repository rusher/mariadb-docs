
# COLUMN_CREATE

## Syntax


```
COLUMN_CREATE(column_nr, value [as type], [column_nr, value [as type]]...);
COLUMN_CREATE(column_name, value [as type], [column_name, value [as type]]...);
```

## Description


Returns a [dynamic columns](../../../../nosql/dynamic-columns-api.md) blob that stores the specified columns with values.


The return value is suitable for


* storing in a table
* further modification with other dynamic columns functions


The **`<code>as type</code>`** part allows one to specify the value type. In most cases,
this is redundant because MariaDB will be able to deduce the type of the
value. Explicit type specification may be needed when the type of the value is
not apparent. For example, a literal `<code>'2012-12-01'</code>` has a CHAR type by
default, one will need to specify `<code>'2012-12-01' AS DATE</code>` to have it stored as
a date. See [Dynamic Columns:Datatypes](../../../../nosql/dynamic-columns-api.md#datatypes) for further details.


## Examples


```
INSERT INTO tbl SET dyncol_blob=COLUMN_CREATE("column_name", "value");
```
