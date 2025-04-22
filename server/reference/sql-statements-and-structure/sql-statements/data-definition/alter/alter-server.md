
# ALTER SERVER

## Syntax


```
ALTER SERVER server_name
    OPTIONS (option [, option] ...)
```


## Description


Alters the server information for *server_name*, adjusting the specified
options as per the [CREATE SERVER](../create/create-server.md) command. The corresponding fields in the [mysql.servers table](../../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-servers-table.md) are updated accordingly. This statement requires the [SUPER](../../account-management-sql-commands/grant.md#super) privilege or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1052-release-notes), the [FEDERATED ADMIN](../../account-management-sql-commands/grant.md#federated-admin) privilege.


ALTER SERVER is not written to the [binary log](../../../../../server-management/server-monitoring-logs/binary-log/README.md), irrespective of
the [binary log format](../../../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) being used. From [MariaDB 10.1.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10113-release-notes), [Galera](../../../../../server-usage/replication-cluster-multi-master/galera-cluster/README.md) replicates the [CREATE SERVER](../create/create-server.md), ALTER SERVER and [DROP SERVER](../drop/drop-server.md) statements.


## Examples


```
ALTER SERVER s OPTIONS (USER 'sally');
```

## See Also


* [CREATE SERVER](../create/create-server.md)
* [DROP SERVER](../drop/drop-server.md)
* [Spider Storage Engine](../../../../storage-engines/spider/README.md)
* [mysql.servers table](../../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-servers-table.md)

