
# Information Schema INNODB_SYS_INDEXES Table

The [Information Schema](../../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `INNODB_SYS_INDEXES` table contains information about InnoDB indexes.


The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


It has the following columns:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| INDEX_ID | bigint(21) unsigned | NO |  | 0 | A unique index identifier. |
| NAME | varchar(64) | NO |  |  | Index name, lowercase for all user-created indexes, or uppercase for implicitly-created indexes; PRIMARY (primary key), GEN_CLUST_INDEX (index representing primary key where there isn't one), ID_IND, FOR_IND (validating foreign key constraint) , REF_IND. |
| TABLE_ID | bigint(21) unsigned | NO |  | 0 | Table identifier, matching the value from [INNODB_SYS_TABLES.TABLE_ID](information-schema-innodb_sys_tables-table.md). |
| TYPE | int(11) | NO |  | 0 | Numeric type identifier; one of 0 (secondary index), 1 (clustered index), 2 (unique index), 3 (primary index), 32 ([full-text index](../../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md)). |
| N_FIELDS | int(11) | NO |  | 0 | Number of columns in the index. GEN_CLUST_INDEX's have a value of 0 as the index is not based on an actual column in the table. |
| PAGE_NO | int(11) | NO |  | 0 | Index B-tree's root page number. -1 (unused) for full-text indexes, as they are laid out over several auxiliary tables. |
| SPACE | int(11) | NO |  | 0 | Tablespace identifier where the index resides. 0 represents the InnoDB system tablespace, while any other value represents a table created in file-per-table mode (see the [innodb_file_per_table](../../../../../../../storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) system variable). Remains unchanged after a [TRUNCATE TABLE](../../../../../table-statements/truncate-table.md) statement, and not necessarily unique. |
| MERGE_THRESHOLD | int(11) | NO |  | 0 |  |



## Example


```
SELECT * FROM information_schema.INNODB_SYS_INDEXES LIMIT 3\G
*************************** 1. row ***************************
       INDEX_ID: 11
           NAME: ID_IND
       TABLE_ID: 11
           TYPE: 3
       N_FIELDS: 1
        PAGE_NO: 302
          SPACE: 0
MERGE_THRESHOLD: 50
*************************** 2. row ***************************
       INDEX_ID: 12
           NAME: FOR_IND
       TABLE_ID: 11
           TYPE: 0
       N_FIELDS: 1
        PAGE_NO: 303
          SPACE: 0
MERGE_THRESHOLD: 50
*************************** 3. row ***************************
       INDEX_ID: 13
           NAME: REF_IND
       TABLE_ID: 11
           TYPE: 3
       N_FIELDS: 1
        PAGE_NO: 304
          SPACE: 0
MERGE_THRESHOLD: 50
3 rows in set (0.00 sec)
```
