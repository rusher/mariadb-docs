# CONNECTION\_ID

## Syntax

```
CONNECTION_ID()
```

## Description

Returns the connection ID for the connection. Every connection (including events) has an ID that is unique among the set of currently connected clients.

Until [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), returns MYSQL\_TYPE\_LONGLONG, or bigint(10). From [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), returns MYSQL\_TYPE\_LONG, or int(10).

## Examples

```
SELECT CONNECTION_ID();
+-----------------+
| CONNECTION_ID() |
+-----------------+
|               3 |
+-----------------+
```

## See Also

* [SHOW PROCESSLIST](../../../sql-statements/administrative-sql-statements/show/show-processlist.md)
* [INFORMATION\_SCHEMA.PROCESSLIST](../../../sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md)

GPLv2 fill\_help\_tables.sql
