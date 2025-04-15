
# DDL statements that differ for ColumnStore

In most cases, a ColumnStore table works just as any other MariaDB table. There are however a few differences.


The following table lists the data definition statements (DDL) that differ from normal MariaDB [DDL](../../../server/reference/sql-statements-and-structure/sql-statements/data-definition/README.md) when used on ColumnStore tables.



| DDL | Difference |
| --- | --- |
| DDL | Difference |
| [DROP TABLE](../../../server/reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-tablespace.md) | Columnstore supports [DROP TABLE ...RESTRICT](columnstore-drop-table.md) which only drops the table in the front end. |
| [RENAME TABLE](../../../server/reference/sql-statements-and-structure/sql-statements/data-definition/rename-table.md) | ColumnStore doesn't allow one to rename a table between databases. |
| [CREATE TABLE](../../../server/reference/sql-statements-and-structure/vectors/create-table-with-vectors.md) | ColumnStore doesn't need indexes, partitions and many other table and column options. See here for [ColumnStore Specific Syntax](columnstore-create-table.md) |
| [CREATE INDEX](../../../server/reference/sql-statements-and-structure/sql-statements/data-definition/create/create-index.md) | ColumnStore doesn't need indexes. Hence an index many not be created on a table that is defined with engine=columnstore |


