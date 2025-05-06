
# ColumnStore Drop Table

 
1. [Syntax "Syntax"](#syntax)
1. [See also "See also"](#see-also)





The [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-table) statement deletes a table from ColumnStore.


## Syntax


```
DROP  TABLE [IF EXISTS] 
    tbl_name 
    [RESTRICT ]
```

The RESTRICT clause limits the table to being dropped in the front end only. This could be useful when the table has been dropped on one user module, and needs to be synced to others.


images here


The following statement drops the *orders* table on the front end only:


```
DROP TABLE orders RESTRICT;
```

## See also


* [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-table)


CC BY-SA / Gnu FDL

