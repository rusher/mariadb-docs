# DROP SERVER

#

# Syntax

```
DROP SERVER [ IF EXISTS ] server_name
```

#

# Description

Drops the server definition for the server named *server_name*. The
corresponding row within the [mysql.servers table](/en/mysqlservers-table/) will be deleted. This statement requires the [SUPER](../../account-management-sql-commands/grant.md#super) privilege or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1052-release-notes), the [FEDERATED ADMIN](../../account-management-sql-commands/grant.md#federated-admin) privilege.

Dropping a server for a table does not affect any [FederatedX](/en/federatedx/), [FEDERATED](../../../../storage-engines/legacy-storage-engines/federated-storage-engine.md), [Connect](../../../../../security/user-account-management/catalogs/connecting-to-a-server-configured-for-catalogs.md) or [Spider](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/spider-status-variables.md) tables that used this connection information when they were created.

DROP SERVER is not written to the [binary log](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md), irrespective of
the [binary log format](../../../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) being used. From [MariaDB 10.1.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-101-series/mariadb-10113-release-notes), [Galera](../../../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-use-cases.md) replicates the [CREATE SERVER](../create/create-server.md), [ALTER SERVER](../alter/alter-server.md) and DROP SERVER statements.

#

### IF EXISTS

If the IF EXISTS clause is used, MariaDB will not return an error if the server does not exist. Unlike all other statements, DROP SERVER IF EXISTS does not issue a note if the server does not exist. See [MDEV-9400](https://jira.mariadb.org/browse/MDEV-9400).

#

# Examples

```
DROP SERVER s;
```

IF EXISTS:

```
DROP SERVER s;
ERROR 1477 (HY000): The foreign server name you are trying to reference 
 does not exist. Data source error: s

DROP SERVER IF EXISTS s;
Query OK, 0 rows affected (0.00 sec)
```

#

# See Also

* [CREATE SERVER](../create/create-server.md)
* [ALTER SERVER](../alter/alter-server.md)
* [Spider Storage Engine](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/spider-status-variables.md)
* [FederatedX Storage Engine](/en/federatedx/)
* [Connect Storage Engine](../../../../../security/user-account-management/catalogs/connecting-to-a-server-configured-for-catalogs.md)
* [mysql.servers table](/en/mysqlservers-table/)