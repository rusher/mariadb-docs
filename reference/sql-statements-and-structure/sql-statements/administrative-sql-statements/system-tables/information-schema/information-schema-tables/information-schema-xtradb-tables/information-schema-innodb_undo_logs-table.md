# Information Schema INNODB_UNDO_LOGS Table

#

#### MariaDB [5.5.27](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-55-series/mariadb-5527-release-notes) - [10.0](/en/what-is-mariadb-100/)

The `INNODB_UNDO_LOGS` are a Percona enhancement, introduced in version [MariaDB 5.5.27](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-55-series/mariadb-5527-release-notes) and removed in 10.0.

The [Information Schema](/en/information_schema/) `INNODB_UNDO_LOGS` table is a Percona enchancement, and is only available for XtraDB, not InnoDB (see [XtraDB and InnoDB](/en/xtradb-and-innodb/)). It contains information about the the InnoDB [undo log](/en/undo-log/), with each record being an undo log segment. It was removed in [MariaDB 10.0](/en/what-is-mariadb-100/).

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