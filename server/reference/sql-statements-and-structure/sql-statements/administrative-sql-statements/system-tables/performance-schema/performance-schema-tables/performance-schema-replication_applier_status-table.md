
# Performance Schema replication_applier_status Table


##### MariaDB starting with [10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
The `replication_applier_status` table, along with many other new [Performance Schema tables](list-of-performance-schema-tables.md), was added in [MariaDB 10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md).


The [Performance Schema](performance-schema-table_handles-table.md) replication_applier_status table contains information about the general transaction execution status on the replica.


It contains the following fields.



| Field | Type | Null | Description |
| --- | --- | --- | --- |
| Field | Type | Null | Description |
| CHANNEL_NAME | char(64) | NO | The replication channel name. |
| SERVICE_STATE | enum('ON','OFF') | NO | Shows ON when the replication channel's applier threads are active or idle, OFF means that the applier threads are not active. |
| REMAINING_DELAY | int(10) unsigned | YES | Seconds the replica needs to wait to reach the desired delay from master. |
| COUNT_TRANSACTIONS_RETRIES | bigint(20) unsigned | NO | The number of retries that were made because the replication SQL thread failed to apply a transaction. |


