# INSERT SELECT

## Syntax

```
INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
    [INTO] tbl_name [(col_name,...)]
    SELECT ...
    [ ON DUPLICATE KEY UPDATE col_name=expr, ... ]
```

## Description

With `INSERT ... SELECT`, you can quickly insert many rows\
into a table from one or more other tables. For example:

```
INSERT INTO tbl_temp2 (fld_id)
  SELECT tbl_temp1.fld_order_id
  FROM tbl_temp1 WHERE tbl_temp1.fld_order_id > 100;
```

`tbl_name` can also be specified in the form `db_name`.`tbl_name` (see [Identifier Qualifiers](../../../sql-structure/sql-language-structure/identifier-qualifiers.md)). This allows to copy rows between different databases.

If the new table has a primary key or UNIQUE indexes, you can use [IGNORE](ignore.md) to handle duplicate key errors during the query. The newer values will not be inserted if an identical value already exists.

`[REPLACE](../changing-deleting-data/replace.md)` can be used instead of `INSERT` to prevent duplicates on `UNIQUE` indexes by deleting old values. In that case, `ON DUPLICATE KEY UPDATE` cannot be used.

`INSERT ... SELECT` works for tables which already exist. To create a table for a given resultset, you can use [CREATE TABLE ... SELECT](../../data-definition/create/create-table.md).

## See Also

* [INSERT](insert.md)
* [INSERT DELAYED](insert-delayed.md)
* [HIGH\_PRIORITY and LOW\_PRIORITY](../changing-deleting-data/high_priority-and-low_priority.md)
* [Concurrent Inserts](concurrent-inserts.md)
* [INSERT - Default & Duplicate Values](insert-default-duplicate-values.md)
* [INSERT IGNORE](insert-ignore.md)
* [INSERT ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md)

GPLv2 fill\_help\_tables.sql

{% @marketo/form formId="4316" %}
