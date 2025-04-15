
# Information Schema INNODB_TABLESPACES_SCRUBBING Table

The table was removed in [MariaDB 10.5.2](../../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md) - see [MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528).


The [Information Schema](../../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>INNODB_TABLESPACES_SCRUBBING</code>` table contains [data scrubbing](../../../../../../../storage-engines/innodb/innodb-data-scrubbing.md) information.


The `<code>PROCESS</code>` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


It has the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| SPACE | InnoDB table space id number. |
| NAME | Path to the table space file, without the extension. |
| COMPRESSED | The compressed page size, or zero if uncompressed. |
| LAST_SCRUB_COMPLETED | Date and time when the last scrub was completed, or NULL if never been performed. |
| CURRENT_SCRUB_STARTED | Date and time when the current scrub started, or NULL if never been performed. |
| CURRENT_SCRUB_ACTIVE_THREADS | Number of threads currently scrubbing the tablespace. |
| CURRENT_SCRUB_PAGE_NUMBER | Page that the scrubbing thread is currently scrubbing, or NULL if not enabled. |
| CURRENT_SCRUB_MAX_PAGE_NUMBER | When a scrubbing starts rotating a table space, the field contains its current size. NULL if not enabled. |
| ON_SSD | The field contains 1 when MariaDB detects that the table space is on a SSD based storage. 0 if not SSD or it could not be determined |



## Example


```
SELECT * FROM information_schema.INNODB_TABLESPACES_SCRUBBING LIMIT 1\G
*************************** 1. row ***************************
                        SPACE: 1
                         NAME: mysql/innodb_table_stats
                   COMPRESSED: 0
         LAST_SCRUB_COMPLETED: NULL
        CURRENT_SCRUB_STARTED: NULL
    CURRENT_SCRUB_PAGE_NUMBER: NULL
CURRENT_SCRUB_MAX_PAGE_NUMBER: 0
         ROTATING_OR_FLUSHING: 0
1 rows in set (0.00 sec)
```
