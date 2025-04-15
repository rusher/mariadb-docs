
# COLUMN_EXISTS

## Syntax


```
COLUMN_EXISTS(dyncol_blob, column_nr);
COLUMN_EXISTS(dyncol_blob, column_name);
```

## Description


Checks if a column with name `<code>column_name</code>` exists in `<code>dyncol_blob</code>`. If yes, return `<code>1</code>`, otherwise return `<code>0</code>`. See [dynamic columns](../../../../nosql/dynamic-columns-api.md) for more information.

