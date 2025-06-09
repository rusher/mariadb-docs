# mysql.transaction\_registry Table

**System tables should not normally be edited directly. Use the related SQL statements instead.**

The `mysql.transaction_registry` table was introduced in [MariaDB 10.3.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1034-release-notes) as part of [system-versioned tables](../../../../sql-structure/temporal-tables/system-versioned-tables.md). It is used for [transaction-precise versioning](../../../../sql-structure/temporal-tables/system-versioned-tables.md#transaction-precise-history-in-innodb), and contains the following fields:

| Field            | Type                                                                       | Null | Key      | Default                    | Description                                                                                                                   |
| ---------------- | -------------------------------------------------------------------------- | ---- | -------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Field            | Type                                                                       | Null | Key      | Default                    | Description                                                                                                                   |
| transaction\_id  | bigint(20) unsigned                                                        | NO   | Primary  | NULL                       |                                                                                                                               |
| commit\_id       | bigint(20) unsigned                                                        | NO   | Unique   | NULL                       |                                                                                                                               |
| begin\_timestamp | timestamp(6)                                                               | NO   | Multiple | 0000-00-00 00:00:00.000000 | Timestamp when the transaction began (BEGIN statement), however see [MDEV-16024](https://jira.mariadb.org/browse/MDEV-16024). |
| commit           | timestamp(6)                                                               | NO   | Multiple | 0000-00-00 00:00:00.000000 | Timestamp when the transaction was committed.                                                                                 |
| isolation\_level | enum('READ-UNCOMMITTED','READ-COMMITTED','REPEATABLE-READ','SERIALIZABLE') | NO   |          | NULL                       | Transaction [isolation level](../../../transactions/set-transaction.md#isolation-levels).                                     |

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
