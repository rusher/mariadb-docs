# CONNECTION_ID

#

# Syntax

```
CONNECTION_ID()
```

#

# Description

Returns the connection ID for the connection. Every connection (including events) has an ID that is unique among the set of currently connected clients.

Until [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), returns MYSQL_TYPE_LONGLONG, or bigint(10). From [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), returns MYSQL_TYPE_LONG, or int(10).

#

# Examples

```
SELECT CONNECTION_ID();
+-----------------+
| CONNECTION_ID() |
+-----------------+
| 3 |
+-----------------+
```

#

# See Also

* [SHOW PROCESSLIST](../../../administrative-sql-statements/show/show-processlist.md)
* [INFORMATION_SCHEMA.PROCESSLIST](../../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md)