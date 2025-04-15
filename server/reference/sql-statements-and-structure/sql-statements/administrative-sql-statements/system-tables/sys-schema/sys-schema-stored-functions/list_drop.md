# list_drop

#

# Syntax

```
sys.list_drop(list,value)
```

#

# Description

`list_drop` is a [stored function](/en/stored-functions/) available with the [Sys Schema](../sys-schema-sys_config-table.md).

It takes a *list* to be be modified and a *value* to be dropped from the list, returning the resulting value. This can be used, for example, to remove a value from a system variable taking a comma-delimited list of options, such as [sql_mode](../../../../../../../server-management/variables-and-modes/sql-mode.md).

The related function [list_add](list_add.md) can be used to add a value to a list.

#

# Examples

```
SELECT @@sql_mode;
+-----------------------------------------------------------------------+
| @@sql_mode |
+-----------------------------------------------------------------------+
| STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,
NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+-----------------------------------------------------------------------+

SET @@sql_mode = sys.list_drop(@@sql_mode, 'NO_ENGINE_SUBSTITUTION');

SELECT @@sql_mode;
+-----------------------------------------------------------------------+
| @@sql_mode |
+-----------------------------------------------------------------------+
| STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,
NO_AUTO_CREATE_USER |
+-----------------------------------------------------------------------+
```

#

# See Also

* [list_add](list_add.md)