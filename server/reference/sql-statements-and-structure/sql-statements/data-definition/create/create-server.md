# CREATE SERVER

#

# Syntax

```
CREATE [OR REPLACE] SERVER [IF NOT EXISTS] server_name
 FOREIGN DATA WRAPPER wrapper_name
 OPTIONS (option [, option] ...)

option: <= MariaDB 11.6
 { HOST character-literal
 | DATABASE character-literal
 | USER character-literal
 | PASSWORD character-literal
 | SOCKET character-literal
 | OWNER character-literal
 | PORT numeric-literal }

option: >= MariaDB 11.7
 { HOST character-literal
 | DATABASE character-literal
 | USER character-literal
 | PASSWORD character-literal
 | SOCKET character-literal
 | OWNER character-literal
 | PORT numeric-literal
 | PORT quoted-numerical-literal
 | identifier character-literal}
```

#

# Description

This statement creates the definition of a server for use with the [Spider](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/spider-status-variables.md), [Connect](../../../../../security/user-account-management/catalogs/connecting-to-a-server-configured-for-catalogs.md), 
[FEDERATED](../../../../storage-engines/legacy-storage-engines/federated-storage-engine.md) or [FederatedX](/en/federatedx/) storage
engine. The CREATE SERVER statement creates a new row within the
[servers](/en/mysqlservers-table/) table within the mysql database. This statement
requires the [SUPER](../../account-management-sql-commands/grant.md#super) privilege or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-105-series/mariadb-1052-release-notes), the [FEDERATED ADMIN](../../account-management-sql-commands/grant.md#federated-admin) privilege.

The server_name should be a unique reference to the server. Server definitions
are global within the scope of the server, it is not possible to qualify the
server definition to a specific database. server_name has a maximum length of
64 characters (names longer than 64 characters are silently truncated), and is
case insensitive. You may specify the name as a quoted string.

The wrapper_name may be quoted with single quotes. Supported values are:

* `mysql`
* `mariadb` (in [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-103) and later)

For each option you must specify either a character literal or numeric literal.
Character literals are UTF-8, support a maximum length of 64 characters and
default to a blank (empty) string. String literals are silently truncated to 64
characters. Numeric literals must be a number between 0 and 9999, default value
is 0.

**Note**: The `OWNER` option is currently not applied, and has no effect on
the ownership or operation of the server connection that is created.

The CREATE SERVER statement creates an entry in the
[mysql.servers](/en/mysqlservers-table/) table that can later be used with the
CREATE TABLE statement when creating a [Spider](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/spider-status-variables.md), [Connect](../../../../../security/user-account-management/catalogs/connecting-to-a-server-configured-for-catalogs.md), [FederatedX](/en/federatedx/) or
[FEDERATED](../../../../storage-engines/legacy-storage-engines/federated-storage-engine.md) table. The options that you specify will
be used to populate the columns in the mysql.servers table. The table columns
are Server_name, Host, Db, Username, Password, Port and Socket.

[DROP SERVER](../drop/drop-server.md) removes a previously created server definition.

CREATE SERVER is not written to the [binary log](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md), irrespective of
the [binary log format](../../../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) being used and therefore will not replicate. From [MariaDB 10.1.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-101-series/mariadb-10113-release-notes), [Galera](../../../../../server-usage/replication-cluster-multi-master/galera-cluster/galera-use-cases.md) replicates the CREATE SERVER, [ALTER SERVER](../alter/alter-server.md) and [DROP SERVER](../drop/drop-server.md) statements.

For valid identifiers to use as server names, see [Identifier Names](../../../sql-language-structure/identifier-names.md).

#

#### MariaDB starting with [11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-117)

From [MariaDB 11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-117), the [SHOW CREATE SERVER](../../administrative-sql-statements/show/show-create-server.md) statement can be used to show the CREATE SERVER statement that created a given server definition.

#

### OR REPLACE

If the optional `OR REPLACE` clause is used, it acts as a shortcut for:

```
DROP SERVER IF EXISTS name;
CREATE SERVER server_name ...;
```

#

### IF NOT EXISTS

If the IF NOT EXISTS clause is used, MariaDB will return a warning instead of an error if the server already exists. Cannot be used together with OR REPLACE.

#

# Examples

```
CREATE SERVER s
FOREIGN DATA WRAPPER mariadb
OPTIONS (USER 'Remote', HOST '192.168.1.106', DATABASE 'test');
```

OR REPLACE and IF NOT EXISTS:

```
CREATE SERVER s 
FOREIGN DATA WRAPPER mariadb 
OPTIONS (USER 'Remote', HOST '192.168.1.106', DATABASE 'test');
ERROR 1476 (HY000): The foreign server, s, you are trying to create already exists

CREATE OR REPLACE SERVER s 
FOREIGN DATA WRAPPER mariadb 
OPTIONS (USER 'Remote', HOST '192.168.1.106', DATABASE 'test');
Query OK, 0 rows affected (0.00 sec)

CREATE SERVER IF NOT EXISTS s 
FOREIGN DATA WRAPPER mariadb 
OPTIONS (USER 'Remote', HOST '192.168.1.106', DATABASE 'test');
Query OK, 0 rows affected, 1 warning (0.00 sec)

SHOW WARNINGS;
+-------+------+----------------------------------------------------------------+
| Level | Code | Message |
+-------+------+----------------------------------------------------------------+
| Note | 1476 | The foreign server, s, you are trying to create already exists |
+-------+------+----------------------------------------------------------------+
```

#

# See Also

* [Identifier Names](../../../sql-language-structure/identifier-names.md)
* [ALTER SERVER](../alter/alter-server.md)
* [DROP SERVER](../drop/drop-server.md)
* [Spider Storage Engine](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/spider-status-variables.md)
* [Connect Storage Engine](../../../../../security/user-account-management/catalogs/connecting-to-a-server-configured-for-catalogs.md)
* [mysql.servers table](/en/mysqlservers-table/)
* [SHOW CREATE SERVER](../../administrative-sql-statements/show/show-create-server.md)