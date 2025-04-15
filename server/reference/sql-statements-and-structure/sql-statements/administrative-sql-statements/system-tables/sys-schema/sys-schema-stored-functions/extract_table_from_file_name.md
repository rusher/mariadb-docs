# extract_table_from_file_name

#

# Syntax

```
sys.extract_table_from_file_name(path)
```

#

# Description

`extract_table_from_file_name` is a [stored function](/en/stored-functions/) available with the [Sys Schema](../sys-schema-sys_config-table.md).

Given a file path, it returns the table name.

The function does not examine anything on disk. The return value, a VARCHAR(64), is determined solely from the provided path.

#

# Examples

```
SELECT sys.extract_table_from_file_name('/usr/local/mysql/data/db/t1.ibd');
+---------------------------------------------------------------------+
| sys.extract_table_from_file_name('/usr/local/mysql/data/db/t1.ibd') |
+---------------------------------------------------------------------+
| t1 |
+---------------------------------------------------------------------+
```

#

# See also

* [extract_schema_from_file_name()](extract_schema_from_file_name.md)