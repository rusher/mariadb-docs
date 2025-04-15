
# Information Schema WSREP_STATUS Table

The WSREP_STATUS table makes [Galera](../../../../built-in-functions/special-functions/galera-functions/README.md) node cluster status information available through the [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md). The same information can be returned using the [SHOW WSREP_STATUS](../../../show/show-wsrep_status.md) statement. Only users with the [SUPER](../../../../account-management-sql-commands/grant.md#super) privilege can access information from this table.


The `<code>WSREP_STATUS</code>` table is part of the [WSREP_INFO plugin](../../../../../../plugins/mariadb-replication-cluster-plugins/wsrep_info-plugin.md).


## Example


```
SELECT * FROM information_schema.WSREP_STATUS\G
*************************** 1. row ***************************
         NODE_INDEX: 0
        NODE_STATUS: Synced
     CLUSTER_STATUS: Primary
       CLUSTER_SIZE: 3
 CLUSTER_STATE_UUID: 00b0fbad-6e84-11e4-8a8b-376f19ce8ee7
CLUSTER_STATE_SEQNO: 2
    CLUSTER_CONF_ID: 3
                GAP: NO
   PROTOCOL_VERSION: 3
```
