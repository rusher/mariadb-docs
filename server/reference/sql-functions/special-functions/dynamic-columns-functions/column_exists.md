# COLUMN\_EXISTS

## Syntax

```
COLUMN_EXISTS(dyncol_blob, column_nr);
COLUMN_EXISTS(dyncol_blob, column_name);
```

## Description

Checks if a column with name `column_name` exists in `dyncol_blob`. If yes, return `1`, otherwise return `0`. See [dynamic columns](../../../sql-structure/nosql/dynamic-columns.md) for more information.

CC BY-SA / Gnu FDL
