
# INSERT SELECT

## Syntax


```
INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
    [INTO] tbl_name [(col_name,...)]
    SELECT ...
    [ ON DUPLICATE KEY UPDATE col_name=expr, ... ]
```


## Description


With `<code class="highlight fixed" style="white-space:pre-wrap">INSERT ... SELECT</code>`, you can quickly insert many rows
into a table from one or more other tables. For example:


```
INSERT INTO tbl_temp2 (fld_id)
  SELECT tbl_temp1.fld_order_id
  FROM tbl_temp1 WHERE tbl_temp1.fld_order_id > 100;
```

`<code>tbl_name</code>` can also be specified in the form `<code>db_name</code>`.`<code>tbl_name</code>` (see [Identifier Qualifiers](../../../sql-language-structure/identifier-qualifiers.md)). This allows to copy rows between different databases.


If the new table has a primary key or UNIQUE indexes, you can use [IGNORE](ignore.md) to handle duplicate key errors during the query. The newer values will not be inserted if an identical value already exists.


`<code>[REPLACE](../../built-in-functions/string-functions/replace-function.md)</code>` can be used instead of `<code>INSERT</code>` to prevent duplicates on `<code>UNIQUE</code>` indexes by deleting old values. In that case, `<code>ON DUPLICATE KEY UPDATE</code>` cannot be used.


`<code>INSERT ... SELECT</code>` works for tables which already exist. To create a table for a given resultset, you can use [CREATE TABLE ... SELECT](../../../vectors/create-table-with-vectors.md).


## See Also


* [INSERT](../../built-in-functions/string-functions/insert-function.md)
* [INSERT DELAYED](insert-delayed.md)
* [HIGH_PRIORITY and LOW_PRIORITY](../changing-deleting-data/high_priority-and-low_priority.md)
* [Concurrent Inserts](concurrent-inserts.md)
* [INSERT - Default & Duplicate Values](insert-default-duplicate-values.md)
* [INSERT IGNORE](insert-ignore.md)
* [INSERT ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md)

