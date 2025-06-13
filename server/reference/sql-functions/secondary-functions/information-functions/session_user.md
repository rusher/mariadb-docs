# SESSION\_USER

## Syntax

```
SESSION_USER()
```

## Description

Prior to [MariaDB 11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/mariadb-11-7-rolling-releases/what-is-mariadb-117), SESSION\_USER() is a synonym for [USER()](user.md).

From [MariaDB 11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/mariadb-11-7-rolling-releases/what-is-mariadb-117), it shows the value of [CURRENT\_USER()](current_user.md) when the session was created, that is, it shows a user@host pair from the [mysql.global\_priv table](../../../sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-global_priv-table.md), like CURRENT\_USER(), but unlike CURRENT\_USER() it will not change inside stored routines and views. This is SQL Standard behavior for the SESSION\_USER function.

Backward-compatible behavior can be restored by setting old mode to [SESSION\_USER\_IS\_USER](../../../../server-management/variables-and-modes/old-mode.md#session_user_is_user).

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
