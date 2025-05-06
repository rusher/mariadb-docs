
# LOAD INDEX

## Syntax


```
LOAD INDEX INTO CACHE
  tbl_index_list [, tbl_index_list] ...

tbl_index_list:
  tbl_name
    [[INDEX|KEY] (index_name[, index_name] ...)]
    [IGNORE LEAVES]
```

## Description


The `LOAD INDEX INTO CACHE` statement preloads a table index into the key
cache to which it has been assigned by an explicit [CACHE INDEX](../../../administrative-sql-statements/cache-index.md)
statement, or into the default key cache otherwise. 
`LOAD INDEX INTO CACHE` is used only for [MyISAM](../../../../../storage-engines/myisam-storage-engine/README.md) or [Aria](../../../../../storage-engines/aria/README.md) tables.


The `IGNORE LEAVES` modifier causes only blocks for the nonleaf nodes of
the index to be preloaded.


GPLv2 fill_help_tables.sql

