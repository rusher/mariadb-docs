# COLUMN_DELETE

#

# Syntax

```
COLUMN_DELETE(dyncol_blob, column_nr, column_nr...);
COLUMN_DELETE(dyncol_blob, column_name, column_name...);
```

#

# Description

Deletes a [dynamic column](../../../../nosql/dynamic-columns-api.md) with the specified name. Multiple names can be given. The return value is a dynamic column blob after the modification.