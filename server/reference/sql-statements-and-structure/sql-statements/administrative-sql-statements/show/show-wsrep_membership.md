
# SHOW WSREP_MEMBERSHIP

`<code>SHOW WSREP_MEMBERSHIP</code>` is part of the `<code>[WSREP_INFO](../../../../plugins/mariadb-replication-cluster-plugins/wsrep_info-plugin.md)</code>` plugin.


## Syntax


```
SHOW WSREP_MEMBERSHIP
```

## Description


The `<code>SHOW WSREP_MEMBERSHIP</code>` statement returns [Galera](../../built-in-functions/special-functions/galera-functions/README.md) node cluster membership information. It returns the same information as found in the `<code>[information_schema.WSREP_MEMBERSHIP](../system-tables/information-schema/information-schema-tables/information-schema-wsrep_membership-table.md)</code>` table. Only users with the `<code>[SUPER](../../account-management-sql-commands/grant.md)</code>` privilege can access this information.


## Examples


```
SHOW WSREP_MEMBERSHIP;
+-------+--------------------------------------+----------+-----------------+
| Index | Uuid                                 | Name     | Address         |
+-------+--------------------------------------+----------+-----------------+
|     0 | 19058073-8940-11e4-8570-16af7bf8fced | my_node1 | 10.0.2.15:16001 |
|     1 | 19f2b0e0-8942-11e4-9cb8-b39e8ee0b5dd | my_node3 | 10.0.2.15:16003 |
|     2 | d85e62db-8941-11e4-b1ef-4bc9980e476d | my_node2 | 10.0.2.15:16002 |
+-------+--------------------------------------+----------+-----------------+
```
