
# Information Schema INNODB_UNDO_LOGS Table


##### MariaDB [5.5.27](../../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5527-release-notes.md) - [10.0](../../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)
The `<code>INNODB_UNDO_LOGS</code>` are a Percona enhancement, introduced in version [MariaDB 5.5.27](../../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5527-release-notes.md) and removed in 10.0.


The [Information Schema](../../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>INNODB_UNDO_LOGS</code>` table is a Percona enchancement, and is only available for XtraDB, not InnoDB (see [XtraDB and InnoDB](../../../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md)). It contains information about the the InnoDB [undo log](../../../../../../../storage-engines/innodb/innodb-undo-log.md), with each record being an undo log segment. It was removed in [MariaDB 10.0](../../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md).


It has the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| TRX_ID | Unique transaction ID number, matching the value from the [information_schema.INNODB_TRX](../information-schema-innodb-tables/information-schema-innodb_trx-table.md) table. |
| RSEG_ID | Rollback segment ID, matching the value from the information_schema.INNODB_RSEG table. |
| USEG_ID | Undo segment ID. |
| SEGMENT_TYPE | Indicates the operation type, for example INSERT or UPDATE. |
| STATE | Segment state; one of ACTIVE (contains active transaction undo log), CACHED, TO_FREE (insert undo segment can be freed), TO_PURGE (update undo segment won't be re-used and can be purged when all undo data is removed) or PREPARED (segment of a prepared transaction). |
| SIZE | Size in pages of the segment. |


