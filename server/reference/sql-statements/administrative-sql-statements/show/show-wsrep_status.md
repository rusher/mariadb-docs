# SHOW WSREP\_STATUS

`SHOW WSREP_STATUS` is part of the [WSREP_INFO](../../../../plugins/mariadb-replication-cluster-plugins/wsrep_info-plugin.md) plugin.

## Syntax

```
SHOW WSREP_STATUS
```

## Description

The `SHOW WSREP_STATUS` statement returns [Galera](https://github.com/mariadb-corporation/docs-server/blob/test/en/galera/README.md) node and cluster status information. It returns the same information as found in the [information_schema.WSREP_STATUS](../system-tables/information-schema/information-schema-tables/information-schema-wsrep_status-table.md) table. Only users with the [SUPER](../../account-management-sql-commands/grant.md) privilege can access this information.

## Examples

```
SHOW WSREP_STATUS;
+------------+-------------+----------------+--------------+
| Node_Index | Node_Status | Cluster_Status | Cluster_Size |
+------------+-------------+----------------+--------------+
|          0 | Synced      | Primary        |            3 |
+------------+-------------+----------------+--------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
