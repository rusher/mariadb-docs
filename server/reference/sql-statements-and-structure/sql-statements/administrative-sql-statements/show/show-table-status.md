
# SHOW TABLE STATUS

## Syntax


```
SHOW TABLE STATUS [{FROM | IN} db_name]
    [LIKE 'pattern' | WHERE expr]
```


## Description


`SHOW TABLE STATUS` works like [SHOW TABLES](show-tables.md), but provides more extensive information about each table (until [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes), only non-TEMPORARY tables are shown).


The `LIKE` clause, if present on its own, indicates which table names to
match. The `WHERE` and `LIKE` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).


The following information is returned:



| Column | Description |
| --- | --- |
| Column | Description |
| Name | Table name. |
| Engine | Table [storage engine](../../../../storage-engines/README.md). |
| Version | Version number from the table's .frm file. |
| Row_format | Row format (see [InnoDB](../../../../storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md), [Aria](../../../../storage-engines/aria/aria-storage-formats.md) and [MyISAM](../../../../storage-engines/myisam-storage-engine/myisam-storage-formats.md) row formats). |
| Rows | Number of rows in the table. Some engines, such as [InnoDB](../../../../storage-engines/innodb/README.md) may store an estimate. |
| Avg_row_length | Average row length in the table. |
| Data_length | For [InnoDB](../../../../storage-engines/innodb/README.md), the index size, in pages, multiplied by the page size. For [Aria](../../../../storage-engines/aria/README.md) and [MyISAM](../../../../storage-engines/myisam-storage-engine/README.md), length of the data file, in bytes. For [MEMORY](../../../../storage-engines/memory-storage-engine.md), the approximate allocated memory. |
| Max_data_length | Maximum length of the data file, ie the total number of bytes that could be stored in the table. Not used in [InnoDB](../../../../storage-engines/innodb/README.md). |
| Index_length | Length of the index file. |
| Data_free | Bytes allocated but unused. For InnoDB tables in a shared tablespace, the free space of the shared tablespace with small safety margin. An estimate in the case of partitioned tables - see the [PARTITIONS](../system-tables/information-schema/information-schema-tables/information-schema-partitions-table.md) table. |
| Auto_increment | Next [AUTO_INCREMENT](../../../../data-types/auto_increment.md) value. |
| Create_time | Time the table was created. Some engines just return the ctime information from the file system layer here, in that case the value is not necessarily the table creation time but rather the time the file system metadata for it had last changed. |
| Update_time | Time the table was last updated. On Windows, the timestamp is not updated on update, so MyISAM values will be inaccurate. In [InnoDB](../../../../storage-engines/innodb/README.md), if shared tablespaces are used, will be NULL, while buffering can also delay the update, so the value will differ from the actual time of the last UPDATE, INSERT or DELETE. |
| Check_time | Time the table was last checked. Not kept by all storage engines, in which case will be NULL. |
| Collation | [Character set and collation](../../../../data-types/string-data-types/character-sets/README.md). |
| Checksum | Live checksum value, if any. |
| Create_options | Extra [CREATE TABLE](../../data-definition/create/create-table.md) options. |
| Comment | Table comment provided when MariaDB created the table. |
| Max_index_length | Maximum index length (supported by MyISAM and Aria tables). |
| Temporary | Until [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes), placeholder to signal that a table is a temporary table and always "N", except "Y" for generated information_schema tables and NULL for views. From [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes), will also be set to "Y" for local temporary tables. |



Similar information can be found in the [information_schema.TABLES](../system-tables/information-schema/information-schema-tables/information-schema-tables-table.md) table as well as by using [mariadb-show](../../../../../clients-and-utilities/mariadb-show.md):


```
mariadb-show --status db_name
```

## Views


For views, all columns in `SHOW TABLE STATUS` are `NULL` except 'Name' and 'Comment'


## Example


```
show table status\G
*************************** 1. row ***************************
           Name: bus_routes
         Engine: InnoDB
        Version: 10
     Row_format: Dynamic
           Rows: 5
 Avg_row_length: 3276
    Data_length: 16384
Max_data_length: 0
   Index_length: 0
      Data_free: 0
 Auto_increment: NULL
    Create_time: 2017-05-24 11:17:46
    Update_time: NULL
     Check_time: NULL
      Collation: latin1_swedish_ci
       Checksum: NULL
 Create_options: 
        Comment:
```
