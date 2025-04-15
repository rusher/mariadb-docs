
# SHOW WSREP_STATUS

`<code>SHOW WSREP_STATUS</code>` is part of the `<code>[WSREP_INFO](../../../../plugins/mariadb-replication-cluster-plugins/wsrep_info-plugin.md)</code>` plugin.


## Syntax


```
SHOW WSREP_STATUS
```

## Description


The `<code>SHOW WSREP_STATUS</code>` statement returns [Galera](../../built-in-functions/special-functions/galera-functions/README.md) node and cluster status information. It returns the same information as found in the `<code>[information_schema.WSREP_STATUS](../system-tables/information-schema/information-schema-tables/information-schema-wsrep_status-table.md)</code>` table. Only users with the `<code>[SUPER](../../account-management-sql-commands/grant.md)</code>` privilege can access this information.


## Examples


```
SHOW WSREP_STATUS;
+------------+-------------+----------------+--------------+
| Node_Index | Node_Status | Cluster_Status | Cluster_Size |
+------------+-------------+----------------+--------------+
|          0 | Synced      | Primary        |            3 |
+------------+-------------+----------------+--------------+
```
