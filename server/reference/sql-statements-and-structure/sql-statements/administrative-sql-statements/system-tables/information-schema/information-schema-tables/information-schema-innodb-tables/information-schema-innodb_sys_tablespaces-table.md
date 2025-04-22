
# Information Schema INNODB_SYS_TABLESPACES Table

The [Information Schema](../../README.md) `INNODB_SYS_TABLESPACES` table contains information about InnoDB tablespaces. Until [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105) it was based on the internal `SYS_TABLESPACES` table. This internal table was removed in [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/mariadb-1060-release-notes), so this Information Schema table has been repurposed
to directly reflect the filesystem (fil_system.space_list).


The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


It has the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| SPACE | Unique InnoDB tablespace identifier. |
| NAME | Database and table name separated by a backslash, or the uppercase InnoDB system table name. |
| FLAG | 1 if a DATA DIRECTORY option has been specified in [CREATE TABLE](../../../../../data-definition/create/create-table.md), otherwise 0. |
| FILE_FORMAT | [InnoDB file format](../../../../../../../storage-engines/innodb/innodb-file-format.md). Removed in [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes) |
| ROW_FORMAT | [InnoDB storage format](../../../../../../../storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md) used for this tablespace. If the [Antelope](../../../../../../../storage-engines/innodb/innodb-file-format.md#antelope) file format is used, this value is always Compact or Redundant. When a table's [checksum algorithm](../../../../../../../storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm) is full_crc32 (the default from [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105)), the value can only be Compressed or NULL. |
| PAGE_SIZE | Page size in bytes for this tablespace. Until [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1050-release-notes), this was the value of the [innodb_page_size](../../../../../../../storage-engines/innodb/innodb-system-variables.md#innodb_page_size) variable. From [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/mariadb-1060-release-notes), contains the physical page size of a page (previously ZIP_PAGE_SIZE). |
| ZIP_PAGE_SIZE | Zip page size for this tablespace. Removed in [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/mariadb-1060-release-notes). |
| SPACE_TYPE | Tablespace type. Can be General for general tablespaces or Single for file-per-table tablespaces. Introduced [MariaDB 10.2.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1021-release-notes). Removed [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1050-release-notes). |
| FS_BLOCK_SIZE | File system block size. Introduced [MariaDB 10.2.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1021-release-notes). |
| FILE_SIZE | Maximum size of the file, uncompressed. Introduced [MariaDB 10.2.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1021-release-notes). |
| ALLOCATED_SIZE | Actual size of the file as per space allocated on disk. Introduced [MariaDB 10.2.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1021-release-notes). |
| FILENAME | Tablespace datafile path, previously part of the [INNODB_SYS_DATAFILES table](information-schema-innodb_sys_datafiles-table.md). Added in [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/mariadb-1060-release-notes). |



## Examples


[MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104):


```
DESC information_schema.innodb_sys_tablespaces;
+----------------+---------------------+------+-----+---------+-------+
| Field          | Type                | Null | Key | Default | Extra |
+----------------+---------------------+------+-----+---------+-------+
| SPACE          | int(11) unsigned    | NO   |     | 0       |       |
| NAME           | varchar(655)        | NO   |     |         |       |
| FLAG           | int(11) unsigned    | NO   |     | 0       |       |
| ROW_FORMAT     | varchar(22)         | YES  |     | NULL    |       |
| PAGE_SIZE      | int(11) unsigned    | NO   |     | 0       |       |
| ZIP_PAGE_SIZE  | int(11) unsigned    | NO   |     | 0       |       |
| SPACE_TYPE     | varchar(10)         | YES  |     | NULL    |       |
| FS_BLOCK_SIZE  | int(11) unsigned    | NO   |     | 0       |       |
| FILE_SIZE      | bigint(21) unsigned | NO   |     | 0       |       |
| ALLOCATED_SIZE | bigint(21) unsigned | NO   |     | 0       |       |
+----------------+---------------------+------+-----+---------+-------+
```

From [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104):


```
SELECT * FROM information_schema.INNODB_SYS_TABLESPACES LIMIT 2\G
*************************** 1. row ***************************
         SPACE: 2
          NAME: mysql/innodb_table_stats
          FLAG: 33
    ROW_FORMAT: Dynamic
     PAGE_SIZE: 16384
 ZIP_PAGE_SIZE: 0
    SPACE_TYPE: Single
 FS_BLOCK_SIZE: 4096
     FILE_SIZE: 98304
ALLOCATED_SIZE: 98304
*************************** 2. row ***************************
         SPACE: 3
          NAME: mysql/innodb_index_stats
          FLAG: 33
    ROW_FORMAT: Dynamic
     PAGE_SIZE: 16384
 ZIP_PAGE_SIZE: 0
    SPACE_TYPE: Single
 FS_BLOCK_SIZE: 4096
     FILE_SIZE: 98304
ALLOCATED_SIZE: 98304
```
