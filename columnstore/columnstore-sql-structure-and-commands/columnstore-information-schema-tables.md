# ColumnStore Information Schema Tables

1. [COLUMNSTORE\_TABLES "COLUMNSTORE\_TABLES"](columnstore-information-schema-tables.md#columnstore_tables)
2. [COLUMNSTORE\_COLUMNS "COLUMNSTORE\_COLUMNS"](columnstore-information-schema-tables.md#columnstore_columns)
3. [COLUMNSTORE\_EXTENTS "COLUMNSTORE\_EXTENTS"](columnstore-information-schema-tables.md#columnstore_extents)
4. [COLUMNSTORE\_FILES "COLUMNSTORE\_FILES"](columnstore-information-schema-tables.md#columnstore_files)
5. [Stored Procedures "Stored Procedures"](columnstore-information-schema-tables.md#stored-procedures)
6. [total\_usage() "total\_usage()"](columnstore-information-schema-tables.md#total_usage)
7. [table\_usage() "table\_usage()"](columnstore-information-schema-tables.md#table_usage)
8. [compression\_ratio() "compression\_ratio()"](columnstore-information-schema-tables.md#compression_ratio)

MariaDB ColumnStore has four Information Schema tables that expose information about the table and column storage. The tables were added in version 1.0.5 of ColumnStore and were heavily modified for 1.0.6.

## COLUMNSTORE\_TABLES

The first table is the INFORMATION\_SCHEMA.COLUMNSTORE\_TABLES. It contains information about the tables inside ColumnStore. The table layout is as follows:

<table><thead><tr><th>Column</th><th width="249">Description</th></tr></thead><tbody><tr><td>Column</td><td>Description</td></tr><tr><td>TABLE_SCHEMA</td><td>The database schema for the table</td></tr><tr><td>TABLE_NAME</td><td>The table name</td></tr><tr><td>OBJECT_ID</td><td>The ColumnStore object ID for the table</td></tr><tr><td>CREATION_DATE</td><td>The date the table was created</td></tr><tr><td>COLUMN_COUNT</td><td>The number of columns in the table</td></tr><tr><td>AUTOINCREMENT</td><td>The start autoincrement value for the table is set during CREATE TABLE</td></tr></tbody></table>

**Note:** Tables created with ColumnStore 1.0.4 or lower will have the year field of the creation data set incorrectly by 1900 years.

## COLUMNSTORE\_COLUMNS

The INFORMATION\_SCHEMA.COLUMNSTORE\_COLUMNS table contains information about every single column inside ColumnStore.&#x20;

## COLUMNSTORE\_EXTENTS

This table displays the extent map in a user-consumable form. An extent is a collection of details about a section of data related to a columnstore column. A majority of columns in ColumnStore will have multiple extents, and the columns table above can be joined to this one to filter results by table or column. The table layout is as follows:

| Column                | Description                                                                                           |
| --------------------- | ----------------------------------------------------------------------------------------------------- |
| Column                | Description                                                                                           |
| OBJECT\_ID            | The object ID for the extent                                                                          |
| OBJECT\_TYPE          | Whether this is a "Column" or "Dictionary" extent                                                     |
| LOGICAL\_BLOCK\_START | ColumnStore's internal start LBID for this extent                                                     |
| LOGICAL\_BLOCK\_END   | ColumnStore's internal end LBID for this extent                                                       |
| MIN\_VALUE            | This minimum value stored in this extent                                                              |
| MAX\_VALUE            | The maximum value stored in this extent                                                               |
| WIDTH                 | The data width for the extent                                                                         |
| DBROOT                | The DBRoot number for the extent                                                                      |
| PARTITION\_ID         | The parition ID for the extent                                                                        |
| SEGMENT\_ID           | The segment ID for the extent                                                                         |
| BLOCK\_OFFSET         | The block offset for the data file, each data file can contain multiple extents for a column          |
| MAX\_BLOCKS           | The maximum number of blocks for the extent                                                           |
| HIGH\_WATER\_MARK     | The last block committed to the extent (starting at 0)                                                |
| STATE                 | The state of the extent (see below)                                                                   |
| STATUS                | The availability status for the column which is either "Available", "Unavailable" or "Out of service" |
| DATA\_SIZE            | The uncompressed data size for the extent calculated as (HWM + 1) \* BLOCK\_SIZE                      |

**Notes:**

1. The state is "Valid" for a normal state, "Invalid" if a cpimport has completed but the table has not yet been accessed (min/max values will be invalid) or "Updating" if there is a DML statement writing to the column
2. In ColumnStore the block size is 8192 bytes
3. By default ColumnStore will write create an extent file of 25&#x36;_&#x31;02&#x34;_&#x57;IDTH bytes for the first partition, if this is too small then for uncompressed data it will create a file of the maximum size for the extent (MAX\_BLOCKS \* BLOCK\_SIZE). Snappy always compression adds a header block.
4. Object IDs of less than 3000 are for internal tables and will not appear in any of the information schema tables
5. HWM is set to zero for the lower segments when there are multiple segments in an extent file, these can be observed when BLOCK\_OFFSET > 0
6. When HWM is 0 the DATA\_SIZE will show 0 instead of 8192 to avoid confusion when there is multiple segments in an extent file

## COLUMNSTORE\_FILES

The columnstore\_files table provides information about each file associated with extensions. Each extension can reuse a file at different block offsets so this is not a 1:1 relationship to the columnstore\_extents table.

| Column                 | Description                                                                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Column                 | Description                                                                                                                               |
| OBJECT\_ID             | The object ID for the extent                                                                                                              |
| SEGMENT\_ID            | The segment ID for the extent                                                                                                             |
| PARTITION\_ID          | The partition ID for the extent                                                                                                           |
| FILENAME               | The full path and filename for the extent file, multiple extents for the same column can point to this file with different BLOCK\_OFFSETs |
| FILE\_SIZE             | The disk file size for the extent                                                                                                         |
| COMPRESSED\_DATA\_SIZE | The amount of the compressed file used, NULL if this is an uncompressed file                                                              |

## Stored Procedures

The total\_usage() procedure gives a total disk usage summary for all the columns in ColumnStore except the columns used for internal maintenance. It is executed using the following query:

```
> call columnstore_info.total_usage();
```

### table\_usage()

The table\_usage() procedure gives a the total data disk usage, dictionary disk usage and grand total disk usage per-table. It can be called in several ways, the first gives a total for each table:

```
> call columnstore_info.table_usage(NULL, NULL);
```

Or for a specific table, my\_table in my\_schema in this example:

```
> call columnstore_info.table_usage('my_schema', 'my_table');
```

You can also request all tables for a specified schema:

```
> call columnstore_info.table_usage('my_schema', NULL);
```

**Note:** The quotes around the table name are required; an error will occur without them.

### compression\_ratio()

The compression\_ratio() procedure calculates the average compression ratio across all the compressed extents in ColumnStore. It is called using

```
> call columnstore_info.compression_ratio();
```

CC BY-SA / Gnu FDL
