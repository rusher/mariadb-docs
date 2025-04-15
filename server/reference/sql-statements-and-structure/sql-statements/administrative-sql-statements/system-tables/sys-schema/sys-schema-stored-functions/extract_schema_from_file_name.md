
# extract_schema_from_file_name

## Syntax


```
sys.extract_schema_from_file_name(path)
```

## Description


`<code>extract_schema_from_file_name</code>` is a [stored function](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) available with the [Sys Schema](../sys-schema-views/sys-schema-views-host_summary_by_statement_latency-and-xhost_summary_by_sta.md).


Given a file path, it returns the schema (database) name. The file name is assumed to be within the schema directory, and therefore the function will not return the expected result with partitions, or when tables are defined using the DATA_DIRECTORY table option.


The function does not examine anything on disk. The return value, a VARCHAR(64), is determined solely from the provided path.


## Examples


```
SELECT sys.extract_schema_from_file_name('/usr/local/mysql/data/db/t1.ibd');
+----------------------------------------------------------------------+
| sys.extract_schema_from_file_name('/usr/local/mysql/data/db/t1.ibd') |
+----------------------------------------------------------------------+
| db                                                                   |
+----------------------------------------------------------------------+
```

## See also


* [extract_table_from_file_name()](extract_table_from_file_name.md)

