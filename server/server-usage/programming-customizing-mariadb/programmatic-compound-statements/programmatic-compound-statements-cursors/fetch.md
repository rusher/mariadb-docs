
# FETCH

## Syntax


```
FETCH cursor_name INTO var_name [, var_name] ...
```


## Description


This statement fetches the next row (if a row exists) using the
specified [open](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/qa-datasets/openstreetmap-dataset.md) [cursor](README.md), and advances the cursor pointer.


`var_name` can be a [local variable](../declare-variable.md), but *not* a [user-defined variable](../../../../reference/sql-statements-and-structure/sql-language-structure/user-defined-variables.md).


If no more rows are available, a No Data condition occurs with
`SQLSTATE` value `02000`. To detect this condition, you can set up a
handler for it (or for a `NOT FOUND` condition).


See [Cursor Overview](cursor-overview.md) for an example.


## See Also


* [Cursor Overview](cursor-overview.md)
* [DECLARE CURSOR](declare-cursor.md)
* [OPEN cursor_name](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/qa-datasets/openstreetmap-dataset.md)
* [CLOSE cursor_name](close.md)
* [Cursors in Oracle mode](../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)

<span></span>
