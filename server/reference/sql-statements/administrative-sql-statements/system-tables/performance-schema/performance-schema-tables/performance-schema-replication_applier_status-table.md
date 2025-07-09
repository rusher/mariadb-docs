# Performance Schema replication\_applier\_status Table

**MariaDB starting with** [**10.5.2**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes)

The `replication_applier_status` table, along with many other new [Performance Schema tables](list-of-performance-schema-tables.md), was added in [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes).

The [Performance Schema](../) replication\_applier\_status table contains information about the general transaction execution status on the replica.

It contains the following fields.

| Field                        | Type                | Null | Description                                                                                                                    |
| ---------------------------- | ------------------- | ---- | ------------------------------------------------------------------------------------------------------------------------------ |
| CHANNEL\_NAME                | char(64)            | NO   | The replication channel name.                                                                                                  |
| SERVICE\_STATE               | enum('ON','OFF')    | NO   | Shows ON when the replication channel's applier threads are active or idle, OFF means that the applier threads are not active. |
| REMAINING\_DELAY             | int(10) unsigned    | YES  | Seconds the replica needs to wait to reach the desired delay from master.                                                      |
| COUNT\_TRANSACTIONS\_RETRIES | bigint(20) unsigned | NO   | The number of retries that were made because the replication SQL thread failed to apply a transaction.                         |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
