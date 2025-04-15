# mysql.spider_table_crd Table

The `mysql.spider_table_crd` table is installed by the [Spider storage engine](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/spider-status-variables.md).

This table uses the [Aria](../../../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/aria-encryption/aria-enabling-encryption.md) storage engine.

It contains the following fields:

| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| db_name | char(64) | NO | PRI | | |
| table_name | char(199) | NO | PRI | | |
| key_seq | int(10) unsigned | NO | PRI | 0 | |
| cardinality | bigint(20) | NO | | 0 | |