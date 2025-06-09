# DROP SERVER

## Syntax

```
DROP SERVER [ IF EXISTS ] server_name
```

## Description

Drops the server definition for the server named _server\_name_. The\
corresponding row within the [mysql.servers table](../../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-servers-table.md) will be deleted. This statement requires the [SUPER](../../account-management-sql-statements/grant.md#super) privilege or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes), the [FEDERATED ADMIN](../../account-management-sql-statements/grant.md#federated-admin) privilege.

Dropping a server for a table does not affect any [FederatedX](../../../storage-engines/federatedx-storage-engine/), [FEDERATED](../../../storage-engines/legacy-storage-engines/federated-storage-engine.md), [Connect](../../../storage-engines/connect/) or [Spider](../../../storage-engines/spider/) tables that used this connection information when they were created.

DROP SERVER is not written to the [binary log](../../../../server-management/server-monitoring-logs/binary-log/), irrespective of\
the [binary log format](../../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) being used. From [MariaDB 10.1.13](broken-reference), [Galera](../../../../../kb/en/galera/) replicates the [CREATE SERVER](../create/create-server.md), [ALTER SERVER](../alter/alter-server.md) and DROP SERVER statements.

#### IF EXISTS

If the IF EXISTS clause is used, MariaDB will not return an error if the server does not exist. Unlike all other statements, DROP SERVER IF EXISTS does not issue a note if the server does not exist. See [MDEV-9400](https://jira.mariadb.org/browse/MDEV-9400).

## Examples

```
DROP SERVER s;
```

IF EXISTS:

```
DROP SERVER s;
ERROR 1477 (HY000): The foreign server name you are trying to reference 
  does not exist. Data source error:  s

DROP SERVER IF EXISTS s;
Query OK, 0 rows affected (0.00 sec)
```

## See Also

* [CREATE SERVER](../create/create-server.md)
* [ALTER SERVER](../alter/alter-server.md)
* [Spider Storage Engine](../../../storage-engines/spider/)
* [FederatedX Storage Engine](../../../storage-engines/federatedx-storage-engine/)
* [Connect Storage Engine](../../../storage-engines/connect/)
* [mysql.servers table](../../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-servers-table.md)

GPLv2 fill\_help\_tables.sql

{% @marketo/form formId="4316" %}
