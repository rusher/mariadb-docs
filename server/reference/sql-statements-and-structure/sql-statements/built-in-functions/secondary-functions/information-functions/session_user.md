
# SESSION_USER

## Syntax


```
SESSION_USER()
```

## Description


Prior to [MariaDB 11.7](../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md), SESSION_USER() is a synonym for [USER()](../../../../../plugins/other-plugins/user-variables-plugin.md).


From [MariaDB 11.7](../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md), it shows the value of [CURRENT_USER()](current_user.md) when the session was created, that is, it shows a user@host pair from the [mysql.global_priv table](../../../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-global_priv-table.md), like CURRENT_USER(), but unlike CURRENT_USER() it will not change inside stored routines and views. This is SQL Standard behavior for the SESSION_USER function.


Backward-compatible behavior can be restored by setting old mode to [SESSION_USER_IS_USER](../../../../../../server-management/variables-and-modes/old-mode.md#session_user_is_user).

