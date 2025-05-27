# COLUMN\_ADD

## Syntax

```
COLUMN_ADD(dyncol_blob, column_nr, value [as type], [column_nr, value [as type]]...);
COLUMN_ADD(dyncol_blob, column_name, value [as type], [column_name, value [as type]]...);
```

## Description

Adds or updates [dynamic columns](../../../../sql-statements-and-structure/nosql/dynamic-columns.md).

* `dyncol_blob` must be either a valid dynamic columns blob (for example, `COLUMN_CREATE` returns such blob), or an empty string.
* `column_name` specifies the name of the column to be added. If `dyncol_blob` already has a column with this name, it will be overwritten.
* `value` specifies the new value for the column. Passing a NULL value will cause the column to be deleted.
* `as type` is optional. See [#datatypes](column_add.md#datatypes) section for a discussion about types.

The return value is a dynamic column blob after the modifications.

## Examples

```
UPDATE t1 SET dyncol_blob=COLUMN_ADD(dyncol_blob, "column_name", "value") WHERE id=1;
```

Note: `COLUMN_ADD()` is a regular function (just like`[CONCAT()](../../string-functions/concat.md)`), hence, in order to update the value in the table\
you have to use the `UPDATE ... SET dynamic_col=COLUMN_ADD(dynamic_col, ....)` pattern.

CC BY-SA / Gnu FDL
