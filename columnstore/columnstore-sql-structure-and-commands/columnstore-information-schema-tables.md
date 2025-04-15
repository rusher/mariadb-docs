
# ColumnStore Information Schema Tables

 
1. [COLUMNSTORE_TABLES "COLUMNSTORE_TABLES"](#columnstore_tables)
1. [COLUMNSTORE_COLUMNS "COLUMNSTORE_COLUMNS"](#columnstore_columns)
1. [COLUMNSTORE_EXTENTS "COLUMNSTORE_EXTENTS"](#columnstore_extents)
1. [COLUMNSTORE_FILES "COLUMNSTORE_FILES"](#columnstore_files)
1. [Stored Procedures "Stored Procedures"](#stored-procedures) 

  1. [total_usage() "total_usage()"](#total_usage)
  1. [table_usage() "table_usage()"](#table_usage)
  1. [compression_ratio() "compression_ratio()"](#compression_ratio)





MariaDB ColumnStore has four Information Schema tables that expose information about the table and column storage. These tables were added in version 1.0.5 of ColumnStore and were heavily modified for 1.0.6.


## COLUMNSTORE_TABLES


The first table is the INFORMATION_SCHEMA.COLUMNSTORE_TABLES. This contains information about the tables inside ColumnStore. The table layout is as follows:



| Column | Description |
| --- | --- |
| Column | Description |
| TABLE_SCHEMA | The database schema for the table |
| TABLE_NAME | The table name |
| OBJECT_ID | The ColumnStore object ID for the table |
| CREATION_DATE | The date the table was created |
| COLUMN_COUNT | The number of columns in the table |
| AUTOINCREMENT | The start autoincrement value for the table set during CREATE TABLE |



**Note:** Tables created with ColumnStore 1.0.4 or lower will have the year field of the creation data set incorrectly by 1900 years.


## COLUMNSTORE_COLUMNS


The INFORMATION_SCHEMA.COLUMNSTORE_COLUMNS table contains information about every single column inside ColumnStore. The table layout is as follows:



| Column | Description |
| --- | --- |
| Column | Description |
| TABLE_SCHEMA | The database schema for the table |
| TABLE_NAME | The table name for the column |
| COLUMN_NAME | The column name |
| OBJECT_ID | The object ID for the column |
| DICTIONARY_OBJECT_ID | The dictionary object ID for the column (NULL if there is no dictionary object |
| LIST_OBJECT_ID | Placeholder for future information |
| TREE_OBJECT_ID | Placeholder for future information |
| DATA_TYPE | The data type for the column |
| COLUMN_LENGTH | The data length for the column |
| COLUMN_POSITION | The position of the column in the table, starting at 0 |
| COLUMN_DEFAULT | The default value for the column |
| IS_NULLABLE | Whether or not the column can be set to NULL |
| NUMERIC_PRECISION | The numeric precision for the column |
| NUMERIC_SCALE | The numeric scale for the column |
| IS_AUTOINCREMENT | Set to 1 if the column is an autoincrement column |
| COMPRESSION_TYPE | The type of compression (either "None" or "Snappy") |



## COLUMNSTORE_EXTENTS


This table displays the extent map in a user consumable form. An extent is a collection of details about a section of data related to a columnstore column. A majority of columns in ColumnStore will have multiple extents and the columns table above can be joined to this one to filter results by table or column. The table layout is as follows:



| Column | Description |
| --- | --- |
| Column | Description |
| OBJECT_ID | The object ID for the extent |
| OBJECT_TYPE | Whether this is a "Column" or "Dictionary" extent |
| LOGICAL_BLOCK_START | ColumnStore's internal start LBID for this extent |
| LOGICAL_BLOCK_END | ColumnStore's internal end LBID for this extent |
| MIN_VALUE | This minimum value stored in this extent |
| MAX_VALUE | The maximum value stored in this extent |
| WIDTH | The data width for the extent |
| DBROOT | The DBRoot number for the extent |
| PARTITION_ID | The parition ID for the extent |
| SEGMENT_ID | The segment ID for the extent |
| BLOCK_OFFSET | The block offset for the data file, each data file can contain multiple extents for a column |
| MAX_BLOCKS | The maximum number of blocks for the extent |
| HIGH_WATER_MARK | The last block committed to the extent (starting at 0) |
| STATE | The state of the extent (see below) |
| STATUS | The availability status for the column which is either "Available", "Unavailable" or "Out of service" |
| DATA_SIZE | The uncompressed data size for the extent calculated as (HWM + 1) * BLOCK_SIZE |



**Notes:**

1. The state is "Valid" for a normal state, "Invalid" if a cpimport has completed but the table has not yet been accessed (min/max values will be invalid) or "Updating" if there is a DML statement writing to the column
1. In ColumnStore the block size is 8192 bytes
1. By default ColumnStore will write create an extent file of 256*1024*WIDTH bytes for the first partition, if this is too small then for uncompressed data it will create a file of the maximum size for the extent (MAX_BLOCKS * BLOCK_SIZE). Snappy always compression adds a header block.
1. Object IDs of less than 3000 are for internal tables and will not appear in any of the information schema tables
1. Prior to 1.0.12 / 1.1.2 DATA_SIZE was incorrectly calculated
1. HWM is set to zero for the lower segments when there are multiple segments in an extent file, these can be observed when BLOCK_OFFSET > 0
1. When HWM is 0 the DATA_SIZE will show 0 instead of 8192 to avoid confusion when there is multiple segments in an extent file



## COLUMNSTORE_FILES


The columnstore_files table provides information about each file associated with extensions. Each extension can reuse a file at different block offsets so this is not a 1:1 relationship to the columnstore_extents table.



| Column | Description |
| --- | --- |
| Column | Description |
| OBJECT_ID | The object ID for the extent |
| SEGMENT_ID | The segment ID for the extent |
| PARTITION_ID | The partition ID for the extent |
| FILENAME | The full path and filename for the extent file, multiple extents for the same column can point to this file with different BLOCK_OFFSETs |
| FILE_SIZE | The disk file size for the extent |
| COMPRESSED_DATA_SIZE | The amount of the compressed file used, NULL if this is an uncompressed file |



## Stored Procedures


A few stored procedures were added in 1.0.6 to provide summaries based on the information schema tables. These can be accessed from the COLUMNSTORE_INFO schema.


### total_usage()


The total_usage() procedure gives a total disk usage summary for all the columns in ColumnStore with the exception of the columns used for internal maintenance. It is executed using the following query:


```
> call columnstore_info.total_usage();
```

### table_usage()


The table_usage() procedure gives a the total data disk usage, dictionary disk usage and grand total disk usage per-table. It can be called in several ways, the first gives a total for each table:


```
> call columnstore_info.table_usage(NULL, NULL);
```

Or for a specific table, my_table in my_schema in this example:


```
> call columnstore_info.table_usage('my_schema', 'my_table');
```

You can also request all tables for a specified schema:


```
> call columnstore_info.table_usage('my_schema', NULL);
```

**Note:** The quotes around the table name are required, an error will occur without them.


### compression_ratio()


The compression_ratio() procedure calculates the average compression ratio across all the compressed extents in ColumnStore. It is called using:


```
> call columnstore_info.compression_ratio();
```

**Note:** The compression ratio is incorrectly calculated before versions 1.0.12 / 1.1.2

