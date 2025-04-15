
# COLUMN_ADD

## Syntax


```
COLUMN_ADD(dyncol_blob, column_nr, value [as type], [column_nr, value [as type]]...);
COLUMN_ADD(dyncol_blob, column_name, value [as type], [column_name, value [as type]]...);
```

## Description


Adds or updates [dynamic columns](../../../../nosql/dynamic-columns-api.md).


* `<code>dyncol_blob</code>` must be either a valid dynamic columns blob (for example, `<code>COLUMN_CREATE</code>` returns such blob), or an empty string.
* `<code>column_name</code>` specifies the name of the column to be added. If `<code>dyncol_blob</code>` already has a column with this name, it will be overwritten.
* `<code>value</code>` specifies the new value for the column. Passing a NULL value will cause the column to be deleted.
* `<code>as type</code>` is optional. See [#datatypes](#datatypes) section for a discussion about types.


The return value is a dynamic column blob after the modifications.


## Examples


```
UPDATE t1 SET dyncol_blob=COLUMN_ADD(dyncol_blob, "column_name", "value") WHERE id=1;
```

Note: `<code>COLUMN_ADD()</code>` is a regular function (just like
`<code>[CONCAT()](../../string-functions/concat_ws.md)</code>`), hence, in order to update the value in the table
you have to use the `<code>UPDATE ... SET dynamic_col=COLUMN_ADD(dynamic_col,
....) </code>` pattern.

