# ALTER SERVER

#

# Syntax

```
ALTER SERVER server_name
 OPTIONS (option [, option] ...)
```

#

# Description

Alters the server information for *server_name*, adjusting the specified
options as per the [CREATE SERVER](../create/create-server.md) command. The corresponding fields in the [mysql.servers table](/en/mysqlservers-table/) are updated accordingly. This statement requires the [SUPER](../../account-management-sql-commands/grant.md#super) privilege or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1052-release-notes), the [FEDERATED ADMIN](../../account-management-sql-commands/grant.md#federated-admin) privilege.

ALTER SERVER is not written to the [binary log](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md), irrespective of
the [binary log format](../../../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) being used. From [MariaDB 10.1.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-101-series/mariadb-10113-release-notes), [Galera](../../../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-use-cases.md) replicates the [CREATE SERVER](../create/create-server.md), ALTER SERVER and [DROP SERVER](../drop/drop-server.md) statements.

#

# Examples

```
ALTER SERVER s OPTIONS (USER 'sally');
```

#

# See Also

* [CREATE SERVER](../create/create-server.md)
* [DROP SERVER](../drop/drop-server.md)
* [Spider Storage Engine](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/spider-status-variables.md)
* [mysql.servers table](/en/mysqlservers-table/)