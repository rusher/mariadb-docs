# mysql.proxies_priv Table

**System tables should not normally be edited directly. Use the related SQL statements instead.**

The `mysql.proxies_priv` table contains information about proxy privileges. The table can be queried and although it is possible to directly update it, it is best to use [GRANT](../../../account-management-sql-commands/grant.md) for setting privileges.

This table uses the [Aria](../../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/aria-encryption/aria-enabling-encryption.md) storage engine.

The `mysql.proxies_priv` table contains the following fields:

| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| Host | char(60) | NO | PRI | | |
| User | char(80) | NO | PRI | | |
| Proxied_host | char(60) | NO | PRI | | |
| Proxied_user | char(80) | NO | PRI | | |
| With_grant | tinyint(1) | NO | | 0 | |
| Grantor | char(141) | NO | MUL | | |
| Timestamp | timestamp | NO | | CURRENT_TIMESTAMP | |

The [Acl_proxy_users](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#acl_proxy_users) status variable indicates how many rows the `mysql.proxies_priv` table contains.