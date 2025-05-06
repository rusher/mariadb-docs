
# Information Schema INNODB_SYS_TABLES Table

The [Information Schema](../../README.md) `INNODB_SYS_TABLES` table contains information about InnoDB tables.


The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


It has the following columns:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| TABLE_ID | bigint(21) unsigned | NO |  | 0 | Unique InnoDB table identifier. |
| NAME | varchar(655) | NO |  |  | Database and table name, or the uppercase InnoDB system table name. |
| FLAG | int(11) | NO |  | 0 | See [Flag](#flag) below |
| N_COLS | int(11) unsigned (>= [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105)) int(11) (<= [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)) | NO |  | 0 | Number of columns in the table. The count includes two or three hidden InnoDB system columns, appended to the end of the column list: DB_ROW_ID (if there is no primary key or unique index on NOT NULL columns), DB_TRX_ID, DB_ROLL_PTR. |
| SPACE | int(11) unsigned (>= [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105)) int(11) (<= [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)) | NO |  | 0 | Tablespace identifier where the index resides. 0 represents the InnoDB system tablespace, while any other value represents a table created in file-per-table mode (see the [innodb_file_per_table](../../../../../../../storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) system variable). Remains unchanged after a [TRUNCATE TABLE](../../../../../table-statements/truncate-table.md) statement. |
| FILE_FORMAT | varchar(10) | YES |  | NULL | [InnoDB file format](../../../../../../../storage-engines/innodb/innodb-file-format.md) (Antelope or Barracuda). Removed in [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103). |
| ROW_FORMAT | enum('Redundant', 'Compact', 'Compressed', 'Dynamic') (>= [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105))varchar(12) (<= [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)) | YES |  | NULL | [InnoDB storage format](../../../../../../../storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md) (Compact, Redundant, Dynamic, or Compressed). |
| ZIP_PAGE_SIZE | int(11) unsigned | NO |  | 0 | For Compressed tables, the zipped page size. |
| SPACE_TYPE | enum('Single','System') (>= [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105))varchar(10) (<= [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)) | YES |  | NULL |  |



## Flag


The flag field returns the dict_table_t::flags that correspond to the data dictionary record.



| Bit | Description |
| --- | --- |
| Bit | Description |
| 0 | Set if ROW_FORMAT is not REDUNDANT. |
| 1 to 4 | 0, except for ROW_FORMAT=COMPRESSED, where they will determine the KEY_BLOCK_SIZE (the compressed page size). |
| 5 | Set for ROW_FORMAT=DYNAMIC or ROW_FORMAT=COMPRESSED. |
| 6 | Set if the DATA DIRECTORY attribute was present when the table was originally created. |
| 7 | Set if the page_compressed attribute is present. |
| 8 to 11 | Determine the page_compression_level. |
| 12 13 | Normally 00, but 11 for "no-rollback tables" ([MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103) CREATE SEQUENCE). In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1), these bits could be 01 or 10 for ATOMIC_WRITES=ON or ATOMIC_WRITES=OFF. |



Note that the table flags returned here are not the same as tablespace flags (FSP_SPACE_FLAGS).


## Example


```
SELECT * FROM information_schema.INNODB_SYS_TABLES LIMIT 2\G
*************************** 1. row ***************************
     TABLE_ID: 14
         NAME: SYS_DATAFILES
         FLAG: 0
       N_COLS: 5
        SPACE: 0
   ROW_FORMAT: Redundant
ZIP_PAGE_SIZE: 0
   SPACE_TYPE: System
*************************** 2. row ***************************
     TABLE_ID: 11
         NAME: SYS_FOREIGN
         FLAG: 0
       N_COLS: 7
        SPACE: 0
   ROW_FORMAT: Redundant
ZIP_PAGE_SIZE: 0
   SPACE_TYPE: System
2 rows in set (0.00 sec)
```

## See Also


* [InnoDB Data Dictionary Troubleshooting](../../../../../../../storage-engines/innodb/innodb-troubleshooting/innodb-data-dictionary-troubleshooting.md)


CC BY-SA / Gnu FDL

