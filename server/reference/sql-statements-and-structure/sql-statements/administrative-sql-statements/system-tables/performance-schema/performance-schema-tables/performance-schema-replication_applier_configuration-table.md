
# Performance Schema replication_applier_configuration Table


##### MariaDB starting with [10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes)
The `replication_applier_configuration` table, along with many other new [Performance Schema tables](list-of-performance-schema-tables.md), was added in [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes).


The [Performance Schema](../README.md) replication_applier_configuration table contains configuration settings affecting replica transactions.


It contains the following fields.



| Field | Type | Null | Description |
| --- | --- | --- | --- |
| Field | Type | Null | Description |
| CHANNEL_NAME | char(64) | NO | Replication channel name. |
| DESIRED_DELAY | int(11) | NO | Target number of seconds the replica should be delayed to the master. |


